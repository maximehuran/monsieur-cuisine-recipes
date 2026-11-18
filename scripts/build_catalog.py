#!/usr/bin/env python3
"""Valider les recettes puis générer un catalogue Toque déterministe, sans dépendance."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPERATURES = {0, 37, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130}


def integer(value, minimum, maximum, label):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{label} : entier attendu entre {minimum} et {maximum}")


def validate(recipe):
    if not isinstance(recipe, dict):
        raise ValueError("Une recette doit être un objet JSON")
    recipe_id = recipe.get("id", "")
    if not isinstance(recipe_id, str) or not recipe_id.startswith("perso-") or len(recipe_id) < 7:
        raise ValueError("L’identifiant stable doit commencer par perso-")
    if not isinstance(recipe.get("title"), str) or not recipe["title"].strip():
        raise ValueError("Titre manquant")
    if recipe.get("source") != "user":
        raise ValueError("La source d’une recette personnelle doit être user")
    if not isinstance(recipe.get("ingredients"), list) or not isinstance(recipe.get("steps"), list) or not recipe["steps"]:
        raise ValueError("Ingrédients et étapes requis")
    for step in recipe["steps"]:
        if not isinstance(step, dict) or not isinstance(step.get("text"), str) or not step["text"].strip():
            raise ValueError("Chaque étape doit contenir un texte")
        if "weigh" in step:
            integer(step["weigh"].get("grams"), 1, 5000, "Pesée")
        machine = step.get("machine")
        if machine is None:
            continue
        if not isinstance(machine, dict) or machine.get("program") not in {"manuel", "petrir", "vapeur", "rissoler", "turbo"}:
            raise ValueError("Programme machine inconnu")
        speed, temperature = machine.get("speed"), machine.get("tempC")
        integer(speed, 0, 10, "Vitesse")
        integer(temperature, 0, 130, "Température")
        if temperature not in TEMPERATURES:
            raise ValueError("Température absente de la table du Connect")
        if type(machine.get("reverse", False)) is not bool:
            raise ValueError("reverse doit être un booléen")
        if machine.get("accessory", "blade") not in {"blade", "whisk"}:
            raise ValueError("Accessoire inconnu")
        if machine.get("accessory") == "whisk" and speed > 4:
            raise ValueError("Fouet : vitesse 4 maximum")
        if machine["program"] == "manuel":
            if speed < 1 or (temperature and speed > 3) or (machine.get("reverse") and speed > 3):
                raise ValueError("Réglage manuel incompatible avec les limites du Connect")
            integer(machine.get("seconds"), 1, 900 if speed > 6 else 5940, "Durée")
        else:
            maximum = {"petrir": 120, "vapeur": 5940, "rissoler": 840, "turbo": 3}[machine["program"]]
            integer(machine.get("seconds"), 1, maximum, "Durée")
        if step.get("needsReview") is not True:
            raise ValueError("Chaque réglage importé doit porter needsReview: true")


def build(directory=ROOT / "recipes"):
    recipes, seen = [], set()
    for path in sorted(directory.glob("*.json")):
        recipe = json.loads(path.read_text(encoding="utf-8"))
        validate(recipe)
        if recipe["id"] in seen:
            raise ValueError(f"Identifiant dupliqué : {recipe['id']}")
        seen.add(recipe["id"])
        recipes.append(recipe)
    canonical = json.dumps(recipes, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return {"format": "toque-recettes-1", "revision": hashlib.sha256(canonical).hexdigest(), "recipes": recipes}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Vérifier le catalogue existant sans l’écrire")
    args = parser.parse_args()
    output = json.dumps(build(), ensure_ascii=False, indent=2) + "\n"
    target = ROOT / "catalog.json"
    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != output:
            raise SystemExit("catalog.json doit être régénéré")
    else:
        target.write_text(output, encoding="utf-8")
    print(f"OK : {len(json.loads(output)['recipes'])} recette(s), catalogue valide")
