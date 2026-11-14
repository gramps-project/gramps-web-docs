# Sauvegarder et restaurer

Les propriétaires d'arbres peuvent créer, télécharger et restaurer des sauvegardes de l'arbre dans la section **Sauvegardes** des [paramètres d'administration](settings.md).

Une sauvegarde contient les données de l'arbre généalogique, y compris les dossiers privés, les paramètres de l'arbre et les utilisateurs de l'arbre. Les fichiers multimédias ne sont pas inclus ; voir [Sauvegarder vos fichiers multimédias](export.md#back-up-your-media-files).

## Sauvegardes stockées

Si l'administrateur du serveur a défini un répertoire de sauvegarde (`BACKUP_DIR`, voir [Configuration du serveur](../install_setup/configuration.md)), les sauvegardes peuvent être stockées sur le serveur. Sinon, la section affiche un avis indiquant que le stockage des sauvegardes n'est pas configuré, et seule la restauration à partir d'un fichier téléchargé est disponible.

Cliquez sur **Créer une sauvegarde...** pour créer une sauvegarde. Elle est créée en tant que tâche en arrière-plan et apparaît ensuite dans la liste des sauvegardes stockées, avec sa date, le nombre de personnes et sa taille. Le serveur conserve uniquement les sauvegardes les plus récentes (cinq par défaut) et supprime automatiquement les anciennes. Le nombre de sauvegardes pouvant être créées par jour est également limité.

Pour chaque sauvegarde stockée, vous pouvez :

- **Télécharger** la sauvegarde sous forme de fichier `.tar`, par exemple pour en conserver une copie ailleurs.
- **Restaurer** la sauvegarde, comme décrit ci-dessous.
- **Supprimer** la sauvegarde, après confirmation.

Une sauvegarde effectuée avec une version plus récente de Gramps Web que celle en cours d'exécution sur le serveur est marquée d'une icône d'avertissement et ne peut pas être restaurée.

## Restaurer à partir d'une sauvegarde

Restaure l'arbre à partir d'une sauvegarde stockée ou d'un fichier téléchargé. Pour restaurer une sauvegarde stockée, cliquez sur le bouton de restauration à côté de celle-ci. Pour restaurer à partir d'un fichier, sélectionnez une sauvegarde Gramps Web (`.tar`) ou un fichier XML Gramps (`.gramps`) et cliquez sur **Restaurer**.

!!! danger
    La restauration des données est un remplacement destructeur, pas une fusion. Tout objet existant non présent dans la sauvegarde est supprimé.

Pour une sauvegarde Gramps Web, une boîte de dialogue s'affiche indiquant quand la sauvegarde a été effectuée, pour quel arbre et avec quelle version, et vous permet de choisir quelles parties restaurer :

- **Données** – les objets de l'arbre généalogique
- **Paramètres de l'arbre** – les paramètres de la page d'administration, tels que les couleurs de thème, le titre de l'application et la note de la page d'accueil
- **Utilisateurs** – les utilisateurs de l'arbre

Cliquez sur **Aperçu** pour voir ce que la restauration changerait. Un fichier XML Gramps ne contient que des données, donc pour un tel fichier, l'aperçu commence immédiatement. Vous serez invité à vous ré-authentifier si votre session n'est pas suffisamment récente. L'aperçu s'exécute en tant que tâche en arrière-plan et, une fois terminé, ouvre une boîte de dialogue résumant les changements par type d'objet (personnes, familles, événements, lieux, citations, sources, dépôts, objets multimédias, notes, étiquettes), et pour les paramètres de l'arbre et les utilisateurs si sélectionnés :

- **Ajouter** – objets présents dans la sauvegarde mais manquants dans l'arbre actuel
- **Mettre à jour** – objets présents dans les deux qui diffèrent
- **Supprimer** – objets dans l'arbre actuel qui sont absents de la sauvegarde
- **Inchangé** – objets identiques dans les deux

Si des objets doivent être supprimés, la boîte de dialogue avertit combien. Passez en revue le résumé, puis cliquez sur **Restaurer** pour appliquer les changements, ou **Annuler** pour abandonner.

Après la restauration, les utilisateurs ajoutés à partir de la sauvegarde sont listés. Ils reçoivent un mot de passe aléatoire, donc ils doivent réinitialiser leur mot de passe avant de pouvoir se connecter. Les utilisateurs qui existent déjà sur le serveur ne sont jamais modifiés. Les objets multimédias dont les fichiers sont manquants sur le serveur sont également listés ; téléchargez-les via [Importer des fichiers multimédias](import-media.md).

!!! note
    La restauration des données ne restaure que les données des objets et les références multimédias. Les fichiers multimédias binaires eux-mêmes et les métadonnées de l'arbre (personne par défaut, signets, groupes de noms) ne sont pas affectés.

!!! astuce
    Utilisez ceci pour revenir à un arbre à une sauvegarde connue, par exemple après une mauvaise importation ou une modification en masse indésirable.

## Gramps XML comme sauvegarde

Si le stockage des sauvegardes n'est pas disponible, ou si vous souhaitez simplement conserver une copie des données de l'arbre généalogique, [exportez](export.md) l'arbre au format XML Gramps. Un tel fichier peut également être restauré via [Restaurer à partir d'une sauvegarde](#restore-from-backup).

Notez que si votre utilisateur Gramps Web n'a pas la permission de voir les dossiers privés, l'exportation ne sera pas une sauvegarde complète, car elle ne contiendra aucun dossier privé.
