Version adaptée de Toque 0.5.1, pour un Monsieur Cuisine Connect sous Android 6.

- Réglages → Mes recettes GitHub : catalogue de maximehuran/monsieur-cuisine-recipes.
- Synchronisation au démarrage puis quotidienne lorsque le robot est connecté et au repos, hors recette guidée en cours.
- Synchronisation manuelle disponible ; les mises à jour de l’application restent manuelles.
- Conservation des recettes personnelles pendant les imports et synchronisations Lidl.
- Catalogue invalide refusé en entier ; remplacement du catalogue personnel en transaction, favoris conservés.
- Réglages machine importés soumis à une vérification sur le robot avant lancement.

Le catalogue peut se mettre à jour automatiquement ; aucun programme moteur ou de chauffe n’est lancé par une synchronisation. La première recette de prélavage est une adaptation à valider physiquement. Cette version ne corrige pas le capteur du bol inversé : les sécurités du robot restent à valider avant utilisation réelle.

Sources : flexbox/MrCuisineVibeConnect, commit a26d9d7b7da24cd5d1abba014ef914bb1bdf6cbd (application issue de Wuki60/MrCuisineVibeConnect), licence MIT. Le dépôt contient seulement le correctif ; la compilation récupère la source puis l’applique. L’APK utilise la signature publique du projet d’origine pour permettre l’installation par-dessus Toque sans désinstallation.
