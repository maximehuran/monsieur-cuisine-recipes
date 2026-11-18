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

Toque officiel 0.5.1 ne sait pas encore lire ce dépôt. L’intégration en préparation est un petit correctif appliqué à une révision précise des sources de Toque, sans créer ici une copie complète du projet. Une installation initiale de cette version adaptée sera nécessaire ; ensuite, seules les recettes se synchroniseront automatiquement. Les étapes restent déclenchées par l’utilisateur sur le robot.

## Sources de la fiche de nettoyage

- [Test du Connect par Technplay](https://technplay.com/test-monsieur-cuisine-lidl/) : prélavage avec 500 ml d’eau et vitesse 5.
- [Guide Cuisine Pratique](https://cuisine-pratique.com/blogs/robot-cuisine-et-air-fryer/comment-nettoyer-monsieur-cuisine-connect) : cycle court d’environ 30 secondes, puis rinçage.
- [Notice SilverCrest SKMC 1200 B2, section 17](https://mode-emploi.info/wp-content/uploads/2022/06/Notice-dutilisation-SKMC-1200-B2-1.pdf) : entretien, précautions pour les lames et séchage.

La combinaison proposée est une adaptation de ces sources, pas un programme de nettoyage officiel du fabricant.
