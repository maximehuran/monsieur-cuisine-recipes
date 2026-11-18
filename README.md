# Mes recettes Monsieur Cuisine Connect

Recettes personnelles pour le Monsieur Cuisine Connect, au format JSON de Toque.

## Nettoyage du bol

[Nettoyage du bol — prélavage, lavage et aide au séchage](recipes/nettoyage-doux-du-bol.json) : trois cycles de 500 ml, avec vidange entre les cycles. Prélavage à l’eau claire, lavage avec une petite goutte de liquide vaisselle, puis rinçage : 30 secondes à vitesse 5, sans chauffe, pour chaque cycle.

La fiche inclut une étape personnalisée après vidange : **2 minutes à 37 °C, vitesse 1**, avec confirmation dans Toque. Ce fonctionnement à vide est hors recommandations du fabricant, non validé physiquement et non recommandé par les sources citées. Il peut être passé pour suivre la notice. Aucun contrôle du bol ou du couvercle n’est modifié. Cette étape ne garantit pas un séchage complet et ne remplace pas le nettoyage du couteau et des joints. Terminer par la finition selon la notice et laisser les pièces sécher à l’air libre.

Les sources et les choix d’adaptation sont distingués dans la provenance de la fiche. La durée de 10 minutes est indicative, hors finition et séchage complet. L’identifiant de la recette est conservé lors de cette évolution.

## Modifier ou ajouter une recette

1. Modifier un fichier dans `recipes/`, ou y ajouter un fichier JSON.
2. Conserver son identifiant `perso-…` lors des corrections ; utiliser un nouvel identifiant pour une nouvelle recette.
3. Enregistrer la modification sur `main`. L’action « Vérifier et publier les recettes » valide les fichiers puis régénère `catalog.json`.

Les réglages machine importés portent `needsReview: true` pour demander une vérification dans Toque. La validation automatique des fichiers ne remplace pas un essai de la recette ou des sécurités du robot.

## Catalogue pour le robot

Le catalogue est [catalog.json](catalog.json). Il utilise `toque-recettes-1` et une révision déterministe calculée à partir des recettes.

Accès public sans jeton : `https://api.github.com/repos/maximehuran/monsieur-cuisine-recipes/contents/catalog.json`, avec l’en-tête `Accept: application/vnd.github.raw+json`.

L’application du robot est maintenue séparément dans le [fork de Toque](https://github.com/maximehuran/MrCuisineVibeConnect). Ses [releases](https://github.com/maximehuran/MrCuisineVibeConnect/releases) incluent les sources JSON configurables ; Toque officiel 0.5.1 ne les inclut pas encore. La [PR nº 16 chez Wuki60](https://github.com/Wuki60/MrCuisineVibeConnect/pull/16) propose cette fonctionnalité au projet principal, indépendamment des réglages propres au fork.

Après l’installation initiale du fork, ajouter l’adresse ci-dessus dans **Réglages → Sources de recettes JSON → Gérer les catalogues personnels**, puis synchroniser. Rechercher « Prélavage » pour ouvrir la fiche. Les recettes se synchronisent ensuite au démarrage et chaque jour quand l’application est ouverte, connectée et au repos, hors recette guidée en cours. Modifier les recettes dans ce dépôt ne nécessite aucune recompilation de Toque.

Le fork récupère uniquement les releases officielles publiées de Wuki60, conserve ses fonctionnalités et ne publie un nouvel APK qu’après fusion et tests. Sur le robot, **Rechercher une mise à jour** et la confirmation **Installer** restent manuels et consultent le fork. La synchronisation des recettes reste indépendante. Le [guide du fork](https://github.com/maximehuran/MrCuisineVibeConnect/blob/main/docs/FORK_WORKFLOW.fr.md) décrit le fonctionnement, les limites et la sauvegarde préalable.

Les erreurs de téléchargement ou de format conserveront le catalogue précédent. Chaque source disposera d’un espace distinct : la synchronisation Lidl ne supprimera pas les recettes de ce dépôt. Les favoris seront conservés lorsqu’une recette disparaît de la source. Le format proposé est limité à 500 recettes et 2 Mio ; les photos personnalisées ne sont pas téléchargées.

### Prototype personnel en pause

L’ancienne [version adaptée 0.5.2.1](https://github.com/maximehuran/monsieur-cuisine-recipes/releases/tag/v0.5.2.1) et le correctif `integration/toque-github-recipes.patch` sont conservés pour référence. Leur compilation automatique est désactivée. Ce prototype n’a pas été installé sur le robot pendant cette préparation et ne constitue plus le parcours proposé : le parcours actuel utilise le fork applicatif séparé, tout en poursuivant la contribution au projet officiel. L’action de validation et de publication de `catalog.json` reste active.

Les mises à jour des recettes sont distinctes des mises à jour de l’application. Le fork conserve la confirmation manuelle de mise à jour et utilise ses propres releases. Les sources Toque conservent leur licence MIT, reproduite dans [LICENSE.Toque](LICENSE.Toque) et [LICENSE.Monsieur-Cuisine-SDK](LICENSE.Monsieur-Cuisine-SDK).

## Sources de la fiche de nettoyage

- [Test du Connect par Technplay](https://technplay.com/test-monsieur-cuisine-lidl/) : prélavage avec 500 ml d’eau et vitesse 5.
- [Guide Cuisine Pratique](https://cuisine-pratique.com/blogs/robot-cuisine-et-air-fryer/comment-nettoyer-monsieur-cuisine-connect) : cycle court d’environ 30 secondes, puis rinçage.
- [Notice SilverCrest SKMC 1200 B2, section 17](https://mode-emploi.info/wp-content/uploads/2022/06/Notice-dutilisation-SKMC-1200-B2-1.pdf) : entretien, précautions pour les lames et séchage.

La routine proposée est une adaptation de ces sources, pas un programme de nettoyage officiel du fabricant. L’étape d’aide au séchage après vidange est une personnalisation distincte, hors notice ; aucune de ces sources ne la valide.
