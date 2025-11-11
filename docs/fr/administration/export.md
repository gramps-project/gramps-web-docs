## Sauvegardez votre arbre généalogique

Pour créer une sauvegarde de votre arbre généalogique, ouvrez la page d'exportation dans Gramps Web et sélectionnez le format XML Gramps.

En cliquant sur "exporter", le fichier sera généré et le téléchargement commencera une fois qu'il sera prêt.

Notez que si votre utilisateur Gramps Web n'a pas la permission de voir les enregistrements privés, l'exportation ne sera pas une sauvegarde complète, car elle ne contiendra aucun enregistrement privé.

## Partagez votre arbre généalogique avec des utilisateurs d'autres programmes de généalogie

Lorsque le partage de données généalogiques au format XML Gramps n'est pas une option, vous pouvez également exporter un fichier GEDCOM. Notez que cela n'est pas adapté en tant que sauvegarde de votre arbre Gramps Web.

## Sauvegardez vos fichiers multimédias

Pour sauvegarder vos fichiers multimédias, vous pouvez créer et télécharger une archive ZIP de tous les fichiers multimédias sur la page d'exportation.

Notez que, surtout pour les grands arbres, cela peut être une opération coûteuse pour le serveur et ne devrait être effectué que si cela est absolument nécessaire.

Une meilleure option pour sauvegarder régulièrement vos fichiers multimédias est d'utiliser le [module complémentaire Gramps Web Sync](sync.md) (qui n'est pas en soi une solution de sauvegarde) et de créer des sauvegardes incrémentielles sur votre ordinateur local.

Dans les deux cas, si votre utilisateur Gramps Web n'a pas la permission de voir les enregistrements privés, l'exportation ne contiendra pas de fichiers d'objets multimédias privés.

## Passez à une autre instance de Gramps Web

Gramps Web ne vous enferme pas avec un fournisseur spécifique et vous pouvez toujours passer à une autre instance de Gramps Web sans perdre de données, et sans avoir un accès direct à l'un ou l'autre des serveurs.

Pour réaliser une migration complète, suivez ces étapes (en supposant que vous avez les permissions de propriétaire de l'arbre) :

1. Allez sur la page d'exportation et exportez votre arbre en tant que fichier XML Gramps (`.gramps`). Si vous utilisez le [module complémentaire Sync](sync.md), vous pouvez également générer l'exportation dans Gramps desktop.
2. Sur la page d'exportation, générez et téléchargez une archive multimédia. Si vous utilisez le [module complémentaire Sync](sync.md), vous pouvez également simplement ZIP votre dossier multimédia Gramps local.
3. Allez dans Paramètres > Administration > Gérer les utilisateurs et cliquez sur le bouton "Exporter les détails de l'utilisateur". Cela téléchargera un fichier JSON.
4. Dans la nouvelle instance de Gramps Web, ouvrez la page d'importation. Importez le fichier `.gramps` exporté à l'étape 1.
5. Sur la page d'importation de la nouvelle instance de Gramps Web, téléchargez l'archive multimédia (ZIP).
6. Allez dans Paramètres > Administration > Gérer les utilisateurs de la nouvelle instance de Gramps Web. Cliquez sur le bouton "Importer les comptes utilisateurs" et téléchargez le fichier JSON téléchargé à l'étape 3.

Notez que, bien que vos comptes utilisateurs soient migrés, tous vos utilisateurs devront définir de nouveaux mots de passe en utilisant le lien "mot de passe oublié", car les mots de passe sont stockés sous forme cryptée et ne peuvent pas être exportés.
