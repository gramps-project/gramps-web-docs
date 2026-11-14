# Personnaliser l'arbre

Les propriétaires et administrateurs d'arbre peuvent adapter le nom et l'apparence de l'arbre, ainsi que sa page d'accueil, pour tous les utilisateurs. Ces paramètres se trouvent dans les sections **Paramètres de l'arbre** et **Personnalisation** des [Paramètres d'administration](settings.md).

## Nom de l'arbre généalogique

!!! note
    Renommer l'arbre ne fonctionne que dans une [configuration multi-arbre](../install_setup/multi-tree.md) ou lorsque `TREE_ID` est explicitement défini dans la [configuration du serveur](../install_setup/configuration.md). Dans une installation par défaut à arbre unique sans `TREE_ID` défini, cela générera une erreur.

Cela permet de changer le nom de la base de données d'arbre généalogique Gramps sous-jacente. Entrez un nouveau nom et cliquez sur **Renommer** pour appliquer.

!!! tip
    Si vous souhaitez uniquement changer le nom affiché dans la barre de l'application sans renommer la base de données, utilisez plutôt le paramètre [Titre de l'application](#app-title).

## Informations sur le chercheur

Définissez le nom, l'adresse et les coordonnées du chercheur principal. Ces informations sont intégrées dans les exports (par exemple, les fichiers GEDCOM).

## Couleurs du thème

Définissez une **couleur principale** et une **couleur d'accent** personnalisées pour l'interface Web de Gramps. Ces couleurs sont appliquées à tous les utilisateurs de cet arbre et prennent effet immédiatement après l'enregistrement.

Utilisez les sélecteurs de couleurs pour choisir des couleurs, puis cliquez sur **Enregistrer**. Cliquez sur **Réinitialiser** pour revenir aux valeurs par défaut.

## Titre de l'application

Définissez un titre personnalisé pour l'application. S'il est défini, cela remplace le nom de l'arbre généalogique dans la barre de titre du navigateur et la barre d'application en haut.

Entrez un titre et cliquez sur **Enregistrer**. Laissez vide pour utiliser la valeur par défaut (le nom de l'arbre généalogique).

## Note de la page d'accueil

Sélectionnez un objet **Note** Gramps à afficher sur la page d'accueil du tableau de bord. Le contenu de la note est rendu en dessous des colonnes principales du tableau de bord et est visible par tous les utilisateurs ayant accès à l'arbre.

Utilisez le sélecteur d'objet pour rechercher et choisir une note, puis enregistrez. Cliquez sur **Supprimer** pour effacer la note actuelle de la page d'accueil.

## Image de la page d'accueil

Sélectionnez un objet **Média** Gramps à afficher en tant qu'image sur la page d'accueil du tableau de bord. Lorsqu'il est combiné avec une note de page d'accueil, l'image apparaît à côté du texte de la note. Sans note, seule l'image est affichée.

Utilisez le sélecteur d'objet pour rechercher et choisir un objet média, puis enregistrez. Cliquez sur **Supprimer** pour effacer l'image actuelle de la page d'accueil.

## Paramètres d'exportation/importation

Les paramètres au niveau de l'arbre (titre de l'application, couleurs du thème, note/image de la page d'accueil, etc.) peuvent être exportés sous forme de fichier JSON pour sauvegarde ou pour être copiés vers une autre instance de Gramps Web.

- Cliquez sur **Exporter les paramètres** pour télécharger les paramètres actuels sous forme de fichier JSON.
- Cliquez sur **Importer les paramètres de l'arbre** pour télécharger un fichier JSON précédemment exporté et appliquer les paramètres.
