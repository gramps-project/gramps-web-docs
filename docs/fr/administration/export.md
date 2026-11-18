# Exporter des données

La page d'exportation vous permet de télécharger les données de l'arbre généalogique dans divers formats, ainsi qu'une archive de tous les fichiers multimédias.

## Exporter l'arbre généalogique au format Gramps XML

Pour obtenir une copie des données de l'arbre généalogique, ouvrez la page d'exportation dans Gramps Web et sélectionnez le format Gramps XML. Cliquez sur **Générer** pour créer le fichier, et **Télécharger** une fois qu'il est prêt. Pour un grand arbre, la génération du fichier peut prendre un certain temps ; vous pouvez quitter la page entre-temps et télécharger le fichier plus tard depuis son entrée dans les [notifications](../user-guide/notifications.md).

Notez que si votre utilisateur Gramps Web n'a pas la permission de voir les enregistrements privés, l'exportation ne contiendra aucun enregistrement privé.

## Sauvegarder votre arbre généalogique

Pour des sauvegardes complètes de l'arbre – y compris ses paramètres et utilisateurs – voir [Sauvegarder et restaurer](backups.md). Une exportation au format Gramps XML peut servir de sauvegarde des données de l'arbre généalogique uniquement et peut être restaurée via [Restaurer à partir de la sauvegarde](backups.md#restore-from-backup).

## Partager votre arbre généalogique avec des utilisateurs d'autres programmes de généalogie

Lorsque le partage de données généalogiques au format Gramps XML n'est pas une option, vous pouvez également exporter un fichier GEDCOM. Notez que cela n'est pas adapté comme sauvegarde de votre arbre Gramps Web.

## Sauvegarder vos fichiers multimédias

Pour sauvegarder vos fichiers multimédias, vous pouvez créer et télécharger une archive ZIP de tous les fichiers multimédias sur la page d'exportation.

Notez que, surtout pour les grands arbres, cela peut être une opération coûteuse pour le serveur et ne doit être effectuée que si cela est absolument nécessaire. Pour cette raison, le nombre d'archives multimédias pouvant être créées est limité (par défaut à une par heure). Si vous atteignez la limite, le message d'erreur l'indique.

Une meilleure option pour sauvegarder vos fichiers multimédias de manière régulière est d'utiliser le [module complémentaire Gramps Web Sync](sync.md) (qui n'est pas en soi une solution de sauvegarde) et de créer des sauvegardes incrémentielles sur votre ordinateur local.

Dans les deux cas, si votre utilisateur Gramps Web n'a pas la permission de voir les enregistrements privés, l'exportation ne contiendra pas de fichiers d'objets multimédias privés.

## Passer à une autre instance de Gramps Web

Gramps Web ne vous enferme pas avec un fournisseur spécifique et vous pouvez toujours passer à une autre instance de Gramps Web sans perdre de données, et sans avoir un accès direct à l'un ou l'autre des serveurs.

Pour réaliser une migration complète, suivez ces étapes (en supposant que vous avez les permissions de propriétaire de l'arbre) :

1. Allez sur la page d'exportation et exportez votre arbre au format Gramps XML (`.gramps`). Si vous utilisez le [module complémentaire Sync](sync.md), vous pouvez également générer l'exportation dans Gramps desktop.
2. Sur la page d'exportation, générez et téléchargez une archive multimédia. Si vous utilisez le [module complémentaire Sync](sync.md), vous pouvez également simplement ZIP votre dossier multimédia Gramps local.
3. Allez dans Paramètres > Administration > Gérer les utilisateurs et cliquez sur le bouton "Exporter les détails de l'utilisateur". Cela téléchargera un fichier JSON.
4. Dans la nouvelle instance de Gramps Web, ouvrez la [page d'importation](import.md). Importez le fichier `.gramps` exporté à l'étape 1.
5. Sur la page d'importation de la nouvelle instance de Gramps Web, téléchargez l'archive multimédia (ZIP) sous [Importer des fichiers multimédias](import-media.md).
6. Allez dans Paramètres > Administration > Gérer les utilisateurs de la nouvelle instance de Gramps Web. Cliquez sur le bouton "Importer des comptes utilisateurs" et téléchargez le fichier JSON téléchargé à l'étape 3.

Notez que, bien que vos comptes utilisateurs soient migrés, tous vos utilisateurs devront définir de nouveaux mots de passe en utilisant le lien "mot de passe oublié", car les mots de passe sont stockés sous forme cryptée et ne peuvent pas être exportés.
