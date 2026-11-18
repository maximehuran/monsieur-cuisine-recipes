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

Toque officiel 0.5.1 ne sait pas encore lire ce dépôt. La [PR nº 16 sur Wuki60/MrCuisineVibeConnect](https://github.com/Wuki60/MrCuisineVibeConnect/pull/16) propose des sources JSON configurables et utilise ce dépôt comme exemple. Elle est en brouillon, avec tests et compilation réussis ; l’interface reste à vérifier sur le robot. Cette fonctionnalité n’est pas encore intégrée à une version officielle.

Si cette contribution est intégrée puis publiée, il suffira de mettre à jour Toque et d’ajouter l’adresse ci-dessus dans **Réglages → Sources de recettes JSON**. Les recettes pourront ensuite se synchroniser au démarrage et chaque jour quand l’application est ouverte, connectée et au repos, hors recette guidée en cours. Modifier les recettes dans ce dépôt ne nécessitera alors aucune recompilation de Toque.

Les erreurs de téléchargement ou de format conserveront le catalogue précédent. Chaque source disposera d’un espace distinct : la synchronisation Lidl ne supprimera pas les recettes de ce dépôt. Les favoris seront conservés lorsqu’une recette disparaît de la source. Le format proposé est limité à 500 recettes et 2 Mio ; les photos personnalisées ne sont pas téléchargées.

### Prototype personnel en pause

L’ancienne [version adaptée 0.5.2.1](https://github.com/maximehuran/monsieur-cuisine-recipes/releases/tag/v0.5.2.1) et le correctif `integration/toque-github-recipes.patch` sont conservés pour référence. Leur compilation automatique est désactivée. Ce prototype n’a pas été installé sur le robot pendant cette préparation et ne constitue plus le parcours proposé : la priorité est la contribution au projet officiel. L’action de validation et de publication de `catalog.json` reste active.

Les mises à jour des recettes sont distinctes des mises à jour de l’application. La contribution conserve le mécanisme officiel de mise à jour de Toque. Les sources Toque conservent leur licence MIT, reproduite dans [LICENSE.Toque](LICENSE.Toque) et [LICENSE.Monsieur-Cuisine-SDK](LICENSE.Monsieur-Cuisine-SDK).

## Sources de la fiche de nettoyage

- [Test du Connect par Technplay](https://technplay.com/test-monsieur-cuisine-lidl/) : prélavage avec 500 ml d’eau et vitesse 5.
- [Guide Cuisine Pratique](https://cuisine-pratique.com/blogs/robot-cuisine-et-air-fryer/comment-nettoyer-monsieur-cuisine-connect) : cycle court d’environ 30 secondes, puis rinçage.
- [Notice SilverCrest SKMC 1200 B2, section 17](https://mode-emploi.info/wp-content/uploads/2022/06/Notice-dutilisation-SKMC-1200-B2-1.pdf) : entretien, précautions pour les lames et séchage.

La combinaison proposée est une adaptation de ces sources, pas un programme de nettoyage officiel du fabricant.
