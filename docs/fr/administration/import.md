# Importer des données

Vous pouvez importer un arbre généalogique existant dans Gramps Web en téléchargeant un fichier exporté depuis un autre programme de généalogie, un service en ligne ou depuis Gramps Desktop.

L'importation se trouve dans la section **Données** des [paramètres d'administration](settings.md) (icône utilisateur dans la barre d'application en haut ▸ Administration), qui est accessible aux propriétaires d'arbres et aux administrateurs. Tant que l'arbre est encore vide, le bouton **Importer un arbre généalogique** sur la carte "Commencer" de la page d'accueil y mène également.

## Quel fichier utiliser

| Provenant de | Exportez votre arbre sous | Extension de fichier |
|---|---|---|
| Un autre programme de généalogie ou service en ligne | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Un tableur | Gramps CSV | `.csv` |
| Un carnet d'adresses | vCard | `.vcf` |

Le GEDCOM est le format d'échange commun que presque tous les programmes de généalogie et services en ligne peuvent exporter. Recherchez une option "Exporter" ou "Télécharger" dans votre programme ou sur le site web, et choisissez GEDCOM si plusieurs formats vous sont proposés. La page Wiki de Gramps [Importer depuis un autre programme de généalogie](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) contient des notes sur des programmes spécifiques.

Si vous utilisez Gramps Desktop, choisissez Gramps XML (`.gramps`) plutôt que GEDCOM. Il contient toutes les données de Gramps sans perte, et vos arbres en ligne et hors ligne conservent les mêmes identifiants, de sorte qu'ils peuvent être [synchronisés](sync.md). Voir [Provenant de Gramps Desktop](#provenant-de-gramps-desktop) ci-dessous.

## Importer un fichier d'arbre généalogique

1. Ouvrez la section **Données** des paramètres d'administration.
2. Sous "Importer un arbre généalogique", choisissez votre fichier et cliquez sur **Importer**.
3. Le fichier est d'abord analysé, et une boîte de dialogue "Confirmer l'importation" montre combien d'objets il contient (personnes, familles, événements, lieux, etc.). Rien n'a encore été ajouté à votre arbre. Vérifiez que les comptes semblent plausibles, puis cliquez sur **Importer** pour continuer, ou **Annuler** pour abandonner sans rien changer.
4. L'importation s'exécute en arrière-plan et un indicateur de progression est affiché. Une fois les données importées, l'index de recherche est mis à jour, ce qui peut prendre un certain temps pour un grand arbre. Si l'importation échoue, la raison est affichée.

Lorsque l'importation est terminée, vérifiez le résultat : comparez le nombre de personnes dans le panneau **Statistiques** sur la page d'accueil avec le nombre dans votre ancien programme, et ouvrez une famille que vous connaissez bien pour voir que les parents, enfants, dates et lieux ont été transférés comme prévu.

!!! warning
    Une importation régulière est purement additive : elle crée toujours de nouveaux objets et ne met jamais à jour ou ne supprime les objets existants, même pour les objets qui existent déjà dans votre arbre sous le même ID ou identifiant Gramps. Importer le même fichier deux fois – ou importer un fichier qui chevauche des données déjà présentes dans l'arbre – dupliquera chaque objet correspondant plutôt que de les fusionner ou de les ignorer.

    Si vous devez apporter des modifications effectuées ailleurs à un arbre qui a déjà été importé, utilisez [Restaurer à partir d'une sauvegarde](backups.md#restore-from-backup) à la place, ce qui remplace l'arbre pour correspondre au fichier téléchargé plutôt que d'y ajouter. Cela nécessite un fichier Gramps XML ou une sauvegarde Gramps Web.

## Quotas d'utilisation

L'administrateur du serveur peut définir des limites pour votre arbre (voir [Configuration du serveur](../install_setup/configuration.md)). Le haut de la section **Données** montre l'utilisation actuelle par rapport à ces limites :

- **Personnes** – le nombre d'objets personne dans l'arbre par rapport au maximum configuré (∞ si illimité)
- **Stockage multimédia** – taille totale des fichiers multimédias téléchargés par rapport au quota de stockage configuré (∞ si illimité)

Une importation qui dépasserait la limite du nombre de personnes est refusée dans son ensemble.

## Fichiers GEDCOM

Les fichiers GEDCOM 5.5.1 et GEDCOM 7 peuvent être importés. Il y a quelques points à prendre en compte.

### Encodage des caractères

Un fichier GEDCOM 5.5.1 déclare son encodage de caractères dans son en-tête. Les encodages UTF-8, UTF-16, ANSEL et Windows (ANSI) sont pris en charge. Si les noms avec des accents ou d'autres caractères spéciaux semblent déformés après l'importation (par exemple `MÃ¼ller` au lieu de `Müller`), le fichier a probablement été exporté avec un encodage différent de celui qu'il déclare. Exportez à nouveau le fichier depuis votre ancien programme, en choisissant UTF-8 s'il offre un choix, et [recommencez](#recommencer).

Les fichiers GEDCOM 7 doivent toujours être encodés en UTF-8 ; les autres fichiers sont rejetés avec une erreur "Fichier GEDCOM invalide".

### Données spécifiques au programme

De nombreux programmes ajoutent leurs propres extensions au GEDCOM que d'autres programmes ne comprennent pas. Gramps ne supprime pas silencieusement ces données : les lignes qu'il ne peut pas interpréter sont collectées dans une note de type "importation GEDCOM", attachée à la personne, à la famille ou à tout autre objet auquel elles appartiennent. Consultez ces notes pour voir si quelque chose d'important n'a pas été transféré.

### Fichiers multimédias

Un fichier GEDCOM contient des références à des fichiers multimédias (tels que des photos ou des documents numérisés), mais pas les fichiers eux-mêmes. Après l'importation, les objets multimédias existent dans votre arbre, mais leurs fichiers sont manquants, ce qui est indiqué sous [État des fichiers multimédias](import-media.md#media-file-status). Pour ajouter les fichiers, voir [Importer des fichiers multimédias](import-media.md).

## Provenant de Gramps Desktop

Si vous utilisez Gramps Desktop, il y a deux étapes pour préparer votre base de données afin de vous assurer que tout fonctionnera correctement par la suite.

1. Vérifiez et réparez la base de données
    - Optionnel : créez une sauvegarde de la base de données en exportant vers Gramps XML
    - Exécutez l'[outil de vérification et de réparation de la base de données](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Cela corrige certaines incohérences internes qui pourraient entraîner des problèmes dans Gramps Web.
2. Convertir les chemins multimédias en relatifs
    - Utilisez le Gestionnaire multimédia de Gramps pour [convertir tous les chemins multimédias d'absolus à relatifs](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Notez que même avec des chemins relatifs, tout fichier multimédia en dehors de votre répertoire multimédia Gramps ne fonctionnera pas correctement lorsqu'il sera synchronisé avec Gramps Web.

Ensuite, exportez votre arbre vers Gramps XML (`.gramps`), importez-le comme décrit ci-dessus, et [téléchargez vos fichiers multimédias](import-media.md). Pour continuer à travailler sur le même arbre sur votre ordinateur et sur le web, utilisez l'[addon de synchronisation Gramps Web](sync.md).

### Pourquoi pas de support pour le package Gramps XML ?

Bien que Gramps XML (`.gramps`) soit le format préféré pour l'importation de données, le package Gramps XML (`.gpkg`) n'est pas pris en charge par Gramps Web. Cela est dû au fait que les routines d'importation et d'exportation pour les fichiers multimédias ne sont pas adaptées à une utilisation sur un serveur web.

## Problèmes courants

**"Format non pris en charge".** Seules les extensions de fichiers listées [ci-dessus](#quel-fichier-utiliser) peuvent être importées. Si votre programme ou service en ligne vous a donné une archive ZIP, décompressez-la et téléchargez le fichier `.ged` à l'intérieur.

**Tout apparaît deux fois.** Le même fichier a été importé deux fois. Comme les importations ne fusionnent jamais, [recommencez](#recommencer).

**Caractères spéciaux déformés.** Voir [Encodage des caractères](#encodage-des-caractères).

**Photos manquantes.** Voir [Importer des fichiers multimédias](import-media.md).

### Recommencer

Si une importation s'est mal passée, ou si vous souhaitez corriger quelque chose dans votre ancien programme et importer à nouveau, videz d'abord l'arbre en utilisant [Supprimer tous les objets](#supprimer-tous-les-objets), puis importez le fichier corrigé. Notez que cela supprime également toutes les modifications que vous avez apportées dans Gramps Web depuis l'importation.

### Supprimer tous les objets

!!! danger
    La suppression d'objets est **irréversible**. Faites une [sauvegarde](backups.md) avant de continuer.

**Supprimer tous les objets** se trouve dans la section **Zone de danger** des [paramètres d'administration](settings.md). En cliquant sur **Supprimer**, une boîte de dialogue s'ouvre où vous pouvez choisir de supprimer :

- **Tous les objets** – vide complètement l'arbre
- **Types d'objets spécifiques** – par exemple, uniquement des événements ou uniquement des objets multimédias

Vous serez invité à vous ré-authentifier (vous reconnecter) pour confirmer l'action. La suppression s'exécute en tâche de fond et un indicateur de progression est affiché.

!!! warning
    La suppression d'un sous-ensemble seulement de types d'objets (plutôt que de tous les objets à la fois) peut prendre beaucoup de temps pour de grands arbres, car le serveur doit vérifier et mettre à jour toutes les relations entre les objets.
