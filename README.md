# Mes recettes Monsieur Cuisine Connect

Recettes personnelles pour le Monsieur Cuisine Connect, au format JSON de Toque.

## Première recette

[Prélavage doux du bol — sans chauffe](recipes/nettoyage-doux-du-bol.json) : 500 ml d’eau froide ou tiède, une petite goutte de liquide vaisselle doux et un cycle de 30 secondes à vitesse 5, sans chauffe. Il s’agit d’un prélavage maison pour des résidus légers, à compléter par un rinçage et un nettoyage normal.

Cette adaptation est sourcée dans la fiche et reste à tester physiquement sur le robot. Le premier test prévu porte sur le téléchargement et l’affichage. Les sécurités de la machine doivent être validées avant d’exécuter le programme. Une synchronisation ne démarre jamais les lames ou la chauffe.

## Modifier ou ajouter une recette

1. Modifier un fichier dans `recipes/`, ou y ajouter un fichier JSON.
2. Conserver son identifiant `perso-…` lors des corrections ; utiliser un nouvel identifiant pour une nouvelle recette.
3. Enregistrer la modification sur `main`. L’action « Vérifier et publier les recettes » valide les fichiers puis régénère `catalog.json`.

Les réglages machine importés portent `needsReview: true` pour demander une vérification dans Toque. La validation automatique des fichiers ne remplace pas un essai de la recette ou des sécurités du robot.

## Catalogue pour le robot

Le catalogue est [catalog.json](catalog.json). Il utilise `toque-recettes-1` et une révision déterministe calculée à partir des recettes.

Accès public sans jeton : `https://api.github.com/repos/maximehuran/monsieur-cuisine-recipes/contents/catalog.json`, avec l’en-tête `Accept: application/vnd.github.raw+json`.

Toque officiel 0.5.1 ne sait pas encore lire ce dépôt. La version adaptée [Toque 0.5.2.1](https://github.com/maximehuran/monsieur-cuisine-recipes/releases/tag/v0.5.2.1) est compilée à partir d’une révision précise des sources et du petit correctif contenu dans `integration/toque-github-recipes.patch`. Aucune copie complète du projet Toque n’est conservée ici. Ce correctif reste une adaptation à entretenir lors d’un changement de version de base.

Une installation initiale de cet APK par-dessus Toque est nécessaire. Ensuite : **Réglages → Mes recettes GitHub → Synchroniser maintenant**, puis rechercher « Prélavage ». Le robot vérifie aussi le dépôt au démarrage et chaque jour tant que Toque est ouvert, connecté et au repos, hors recette guidée en cours. Les réglages de cuisson restent déclenchés par l’utilisateur.

Les erreurs de téléchargement ou de format laissent les recettes précédentes disponibles. Les synchronisations Lidl préservent les identifiants personnels `perso-…`. Le catalogue est limité à 500 recettes et 2 Mio. Cette première intégration ne télécharge pas les photos des recettes personnelles.

Les mises à jour de recettes ne mettent pas l’application à jour. Le bouton de mise à jour de cette version adaptée consulte uniquement les versions publiées dans ce dépôt. Les sources Toque conservent leur licence MIT, reproduite dans [LICENSE.Toque](LICENSE.Toque) et [LICENSE.Monsieur-Cuisine-SDK](LICENSE.Monsieur-Cuisine-SDK).

## Sources de la fiche de nettoyage

- [Test du Connect par Technplay](https://technplay.com/test-monsieur-cuisine-lidl/) : prélavage avec 500 ml d’eau et vitesse 5.
- [Guide Cuisine Pratique](https://cuisine-pratique.com/blogs/robot-cuisine-et-air-fryer/comment-nettoyer-monsieur-cuisine-connect) : cycle court d’environ 30 secondes, puis rinçage.
- [Notice SilverCrest SKMC 1200 B2, section 17](https://mode-emploi.info/wp-content/uploads/2022/06/Notice-dutilisation-SKMC-1200-B2-1.pdf) : entretien, précautions pour les lames et séchage.

La combinaison proposée est une adaptation de ces sources, pas un programme de nettoyage officiel du fabricant.
