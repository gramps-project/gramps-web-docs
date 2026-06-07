# Paramètres d'administration

La page **Paramètres > Administration** est accessible via l'icône utilisateur dans la barre d'application en haut. Elle n'est disponible que pour les utilisateurs ayant le rôle de Propriétaire ou d'Administrateur et fournit des outils pour gérer la base de données de l'arbre généalogique.

La page est organisée en sections repliables. Cliquez sur un en-tête de section pour l'agrandir.

## Données

Couvre les quotas d'utilisation, l'importation de données et la gestion des fichiers multimédias.

### Quotas d'utilisation

Le haut de la section montre l'utilisation actuelle par rapport à toutes les limites configurées :

- **Personnes** – le nombre d'objets personne dans l'arbre par rapport au maximum configuré (∞ si illimité)
- **Stockage multimédia** – taille totale des fichiers multimédias téléchargés par rapport au quota de stockage configuré (∞ si illimité)

Les quotas sont définis par l'administrateur du serveur ; voir [Configuration du serveur](../install_setup/configuration.md) pour plus de détails.

### Importer des données

La section d'importation vous permet de télécharger un fichier d'arbre généalogique ou une archive multimédia. Voir [Importer des données](import.md) pour des instructions complètes.

### Statut des fichiers multimédias

Cette section montre :

- Le nombre total d'objets multimédias dans l'arbre et si certains manquent d'une somme de contrôle
- Le nombre d'objets multimédias dont le fichier associé est manquant sur le serveur

Une coche verte indique que tout est en ordre. Si des problèmes sont détectés, des liens vers les objets affectés sont affichés. Les sommes de contrôle manquantes se produisent généralement lorsque des données ont été importées à partir d'un format tel que GEDCOM qui inclut des références multimédias mais pas les fichiers réels. Les fichiers manquants peuvent être téléchargés via la fonction d'importation d'archive multimédia.

### Importer une archive multimédia

Permet de télécharger un fichier ZIP de fichiers multimédias pour compléter les fichiers manquants. Voir [Importer des données](import.md) pour des instructions complètes.

## Index de recherche

### Gérer l'index de recherche

Gramps Web maintient un index de recherche en texte intégral qui est normalement mis à jour automatiquement chaque fois que des données changent. L'indicateur de statut montre combien d'objets sont actuellement indexés par rapport au nombre total d'objets.

Cliquez sur **Mettre à jour l'index de recherche** pour déclencher une reconstruction complète. Un indicateur de progression est affiché pendant que la tâche s'exécute en arrière-plan. Cela est généralement nécessaire uniquement après une mise à niveau du serveur.

### Index de recherche sémantique

Si le serveur a [la recherche sémantique (alimentée par l'IA) activée](../install_setup/configuration.md), une section supplémentaire apparaît avec deux actions :

- **Régénérer l'index de recherche sémantique** – reconstruit l'ensemble de l'index sémantique à partir de zéro. Cela est coûteux en ressources et peut prendre beaucoup de temps.
- **Mettre à jour l'index de recherche sémantique** – effectue une mise à jour incrémentielle, ajoutant uniquement des objets non encore indexés. Plus rapide qu'une reconstruction complète.

## Paramètres de l'arbre

### Nom de l'arbre généalogique

!!! note
    Renommer l'arbre ne fonctionne que dans une [configuration multi-arbres](../install_setup/multi-tree.md) ou lorsque `TREE_ID` est explicitement défini dans la [configuration du serveur](../install_setup/configuration.md). Sur une installation par défaut à arbre unique sans `TREE_ID` défini, cela générera une erreur.

Cela permet de changer le nom de la base de données d'arbre généalogique Gramps sous-jacente. Entrez un nouveau nom et cliquez sur **Renommer** pour appliquer.

!!! tip
    Si vous souhaitez seulement changer le nom affiché dans la barre d'application sans renommer la base de données, utilisez plutôt le paramètre [Titre de l'application](#app-title).

### Informations sur le chercheur

Définissez le nom, l'adresse et les coordonnées du chercheur principal. Ces informations sont intégrées dans les exports (par exemple, les fichiers GEDCOM).

## Personnalisation

### Couleurs du thème

Définissez une **couleur principale** et une **couleur d'accent** personnalisées pour l'interface Gramps Web. Ces couleurs sont appliquées à tous les utilisateurs de cet arbre et prennent effet immédiatement après l'enregistrement.

Utilisez les sélecteurs de couleurs pour choisir des couleurs, puis cliquez sur **Enregistrer**. Cliquez sur **Réinitialiser** pour revenir aux valeurs par défaut.

### Titre de l'application

Définissez un titre personnalisé pour l'application. S'il est défini, cela remplace le nom de l'arbre généalogique dans la barre de titre du navigateur et la barre d'application en haut.

Entrez un titre et cliquez sur **Enregistrer**. Laissez vide pour utiliser la valeur par défaut (le nom de l'arbre généalogique).

### Note de la page d'accueil

Sélectionnez un objet **Note** Gramps à afficher sur la page d'accueil du tableau de bord. Le contenu de la note est rendu sous les colonnes principales du tableau de bord et est visible par tous les utilisateurs ayant accès à l'arbre.

Utilisez le sélecteur d'objets pour rechercher et choisir une note, puis enregistrez. Cliquez sur **Supprimer** pour effacer la note actuelle de la page d'accueil.

### Image de la page d'accueil

Sélectionnez un objet **Média** Gramps à afficher sous forme d'image sur la page d'accueil du tableau de bord. Lorsqu'il est combiné avec une note de page d'accueil, l'image apparaît à côté du texte de la note. Sans note, seule l'image est affichée.

Utilisez le sélecteur d'objets pour rechercher et choisir un objet multimédia, puis enregistrez. Cliquez sur **Supprimer** pour effacer l'image actuelle de la page d'accueil.

### Paramètres d'exportation/importation

Les paramètres au niveau de l'arbre (titre de l'application, couleurs du thème, note/image de la page d'accueil, etc.) peuvent être exportés sous forme de fichier JSON pour sauvegarde ou pour être copiés vers une autre instance de Gramps Web.

- Cliquez sur **Exporter les paramètres** pour télécharger les paramètres actuels sous forme de fichier JSON.
- Cliquez sur **Importer les paramètres de l'arbre** pour télécharger un fichier JSON précédemment exporté et appliquer les paramètres.

## Traitement de l'arbre généalogique

### Vérifier et réparer la base de données

Cet outil vérifie la base de données Gramps pour des incohérences internes et corrige celles qu'il peut – analogue à l'[outil Vérifier et réparer la base de données](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) dans Gramps Desktop.

Cliquez sur **Vérifier et réparer** et attendez que l'indicateur de progression se termine. Le résultat est affiché sous le bouton :

- Si aucune erreur n'a été trouvée, un message de confirmation est affiché.
- Si des erreurs ont été trouvées, un résumé des corrections appliquées est affiché.

Exécutez cet outil si vous rencontrez des erreurs ou des comportements inattendus qui pourraient être causés par des incohérences dans la base de données, comme des relations manquantes entre les objets.

## Étiquettes

### Gérer les étiquettes

Créez, renommez, recolorez et supprimez des [étiquettes](../user-guide/tags.md) pour l'arbre généalogique. Les étiquettes sont stockées dans la base de données Gramps, partagées entre tous les utilisateurs et entièrement compatibles avec Gramps Desktop.

Cliquez sur **Nouvelle étiquette** pour créer une étiquette. Utilisez les contrôles à côté d'une étiquette existante pour la renommer (icône de crayon), changer sa couleur (sélecteur de couleur) ou la supprimer (icône de suppression).

!!! note
    Supprimer une étiquette la retire de tous les objets auxquels elle a été appliquée.

Voir [Étiquettes](../user-guide/tags.md) pour savoir comment les étiquettes sont utilisées dans tout Gramps Web, y compris les étiquettes spéciales `Blog` et `ToDo`.

## Zone de danger

!!! danger
    Les actions dans la Zone de danger sont **irréversibles**. Faites une sauvegarde avant de continuer.

### Supprimer tous les objets

Supprime les objets de l'arbre généalogique. Cliquer sur **Supprimer** ouvre une boîte de dialogue où vous pouvez choisir de supprimer :

- **Tous les objets** – vide complètement l'arbre
- **Types d'objets spécifiques** – par exemple, uniquement des événements ou uniquement des objets multimédias

Vous serez invité à vous ré-authentifier (vous reconnecter) pour confirmer l'action. La suppression s'exécute en tant que tâche en arrière-plan et un indicateur de progression est affiché.

!!! warning
    Supprimer uniquement un sous-ensemble de types d'objets (plutôt que tous les objets à la fois) peut prendre beaucoup de temps pour de grands arbres, car le serveur doit vérifier et mettre à jour toutes les relations entre les objets.

!!! tip
    Utilisez cela pour repartir à zéro avant d'importer un nouvel arbre, ou pour supprimer des types d'objets spécifiques qui ont été importés incorrectement.
