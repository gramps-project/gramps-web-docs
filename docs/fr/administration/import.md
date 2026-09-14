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

GEDCOM est le format d'échange commun que presque tous les programmes de généalogie et services en ligne peuvent exporter. Recherchez une option "Exporter" ou "Télécharger" dans votre programme ou sur le site Web, et choisissez GEDCOM si plusieurs formats vous sont proposés. La page Wiki de Gramps [Importer depuis un autre programme de généalogie](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) contient des notes sur des programmes spécifiques.

Si vous utilisez Gramps Desktop, choisissez Gramps XML (`.gramps`) plutôt que GEDCOM. Il contient toutes les données de Gramps sans perte, et vos arbres en ligne et hors ligne conservent les mêmes identifiants, afin qu'ils puissent être [synchronisés](sync.md). Voir [Provenant de Gramps Desktop](#coming-from-gramps-desktop) ci-dessous.

## Importer un fichier d'arbre généalogique

1. Ouvrez la section **Données** des paramètres d'administration.
2. Sous "Importer un arbre généalogique", choisissez votre fichier et cliquez sur **Importer**.
3. Le fichier est d'abord analysé, et une boîte de dialogue "Confirmer l'importation" indique combien d'objets il contient (personnes, familles, événements, lieux, etc.). Rien n'a encore été ajouté à votre arbre. Vérifiez que les comptes semblent plausibles, puis cliquez sur **Importer** pour continuer, ou **Annuler** pour abandonner sans rien changer.
4. L'importation s'exécute en arrière-plan et un indicateur de progression est affiché. Une fois les données importées, l'index de recherche est mis à jour, ce qui peut prendre un certain temps pour un grand arbre.

Lorsque l'importation est terminée, vérifiez le résultat : comparez le nombre de personnes dans le panneau **Statistiques** de la page d'accueil avec le nombre dans votre ancien programme, et ouvrez une famille que vous connaissez bien pour voir que les parents, enfants, dates et lieux ont été transférés comme prévu.

!!! avertissement
    Une importation régulière est purement additive : elle crée toujours de nouveaux objets et ne met jamais à jour ou ne supprime les objets existants, même pour les objets qui existent déjà dans votre arbre sous le même ID ou identifiant Gramps. Importer le même fichier deux fois – ou importer un fichier qui chevauche des données déjà présentes dans l'arbre – dupliquera chaque objet correspondant plutôt que de les fusionner ou de les ignorer.

    Si vous devez apporter des modifications effectuées ailleurs à un arbre qui a déjà été importé, utilisez plutôt [Restaurer à partir de la sauvegarde](settings.md#restore-from-backup), qui remplace l'arbre pour correspondre au fichier téléchargé plutôt que d'y ajouter. Cela nécessite un fichier Gramps XML.

Si une limite sur le nombre de personnes a été fixée pour votre arbre (voir [Quotas d'utilisation](settings.md#usage-quotas)), une importation qui la dépasserait est refusée dans son ensemble.

## Fichiers GEDCOM

Les fichiers GEDCOM 5.5.1 et GEDCOM 7 peuvent être importés. Il y a quelques points à prendre en compte.

### Encodage des caractères

Un fichier GEDCOM 5.5.1 déclare son encodage de caractères dans son en-tête. Les encodages UTF-8, UTF-16, ANSEL et Windows (ANSI) sont pris en charge. Si les noms avec des accents ou d'autres caractères spéciaux apparaissent déformés après l'importation (par exemple `MÃ¼ller` au lieu de `Müller`), le fichier a probablement été exporté avec un encodage différent de celui qu'il déclare. Exportez à nouveau le fichier depuis votre ancien programme, en choisissant UTF-8 s'il vous offre un choix, et [recommencez](#starting-over).

Les fichiers GEDCOM 7 doivent toujours être encodés en UTF-8 ; les autres fichiers sont rejetés avec une erreur "Fichier GEDCOM invalide".

### Données spécifiques au programme

De nombreux programmes ajoutent leurs propres extensions au GEDCOM que d'autres programmes ne comprennent pas. Gramps ne supprime pas silencieusement ces données : les lignes qu'il ne peut pas interpréter sont collectées dans une note de type "importation GEDCOM", attachée à la personne, à la famille ou à tout autre objet auquel elles appartiennent. Consultez ces notes pour voir si quelque chose d'important n'a pas été transféré.

### Fichiers multimédias

Un fichier GEDCOM contient des références à des fichiers multimédias (tels que des photos ou des documents numérisés), mais pas les fichiers eux-mêmes. Après l'importation, les objets multimédias existent dans votre arbre, mais leurs fichiers sont manquants, ce qui est indiqué sous [État des fichiers multimédias](settings.md#media-file-status). Pour ajouter les fichiers, voir [Importer des fichiers multimédias](#import-media-files) ci-dessous.

## Provenant de Gramps Desktop

Si vous utilisez Gramps Desktop, il y a deux étapes pour préparer votre base de données afin de vous assurer que tout fonctionnera correctement par la suite.

1. Vérifiez et réparez la base de données
    - Optionnel : créez une sauvegarde de la base de données en exportant vers Gramps XML
    - Exécutez l'[outil de vérification et de réparation de la base de données](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Cela corrige certaines incohérences internes qui pourraient entraîner des problèmes dans Gramps Web.
2. Convertir les chemins multimédias en relatifs
    - Utilisez le Gestionnaire multimédia de Gramps pour [convertir tous les chemins multimédias d'absolus à relatifs](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Notez qu même avec des chemins relatifs, tous les fichiers multimédias en dehors de votre répertoire multimédia Gramps ne fonctionneront pas correctement lorsqu'ils seront synchronisés avec Gramps Web.

Ensuite, exportez votre arbre vers Gramps XML (`.gramps`), importez-le comme décrit ci-dessus, et téléchargez vos fichiers multimédias comme décrit dans la section suivante. Pour continuer à travailler sur le même arbre sur votre ordinateur et sur le web, utilisez le [module complémentaire Gramps Web Sync](sync.md).

### Pourquoi pas de support pour le package Gramps XML ?

Bien que Gramps XML (`.gramps`) soit le format préféré pour l'importation de données, le *package* Gramps XML (`.gpkg`) n'est pas pris en charge par Gramps Web. Cela est dû au fait que les routines d'importation et d'exportation pour les fichiers multimédias ne sont pas adaptées à une utilisation sur un serveur web.

## Importer des fichiers multimédias

Si vous avez importé un arbre généalogique et devez télécharger les fichiers multimédias correspondants, utilisez **Importer des fichiers multimédias** dans la section Données des paramètres d'administration. Il attend un fichier ZIP contenant les fichiers multimédias manquants. Les fichiers sont associés aux objets multimédias dans votre arbre de l'une des deux manières suivantes :

- **Par somme de contrôle.** Pour les objets multimédias qui ont une somme de contrôle – comme c'est le cas pour les arbres importés depuis Gramps Desktop – le fichier avec la somme de contrôle correspondante est utilisé, quel que soit son nom ou la structure de dossier dans le fichier ZIP. Cela ne fonctionne que si les sommes de contrôle dans la base de données Gramps sont correctes, ce que garantit l'exécution de l'outil de vérification et de réparation.
- **Par chemin.** Les objets multimédias sans somme de contrôle – comme c'est typique après une importation GEDCOM – sont associés par leur chemin : le fichier ZIP doit contenir le fichier sous exactement le chemin relatif enregistré dans l'objet multimédia.

Si les chemins enregistrés dans votre fichier GEDCOM sont absolus (par exemple `C:\Users\...\photo.jpg`), l'association par chemin ne fonctionnera pas. Dans ce cas, il est recommandé d'abord d'importer tout dans Gramps Desktop, qui a plus d'options pour associer des fichiers multimédias existants avec un arbre importé, puis de passer à Gramps Web comme décrit dans [Provenant de Gramps Desktop](#coming-from-gramps-desktop).

## Problèmes courants

**"Format non pris en charge".** Seules les extensions de fichier énumérées [ci-dessus](#which-file-to-use) peuvent être importées. Si votre programme ou service en ligne vous a donné une archive ZIP, décompressez-la et téléchargez le fichier `.ged` à l'intérieur.

**Tout apparaît deux fois.** Le même fichier a été importé deux fois. Étant donné que les importations ne fusionnent jamais, [recommencez](#starting-over).

**Caractères spéciaux déformés.** Voir [Encodage des caractères](#character-encoding).

**Les photos sont manquantes.** Voir [Importer des fichiers multimédias](#import-media-files).

### Recommencer

Si une importation a mal tourné, ou si vous souhaitez corriger quelque chose dans votre ancien programme et importer à nouveau, videz d'abord l'arbre en utilisant [Supprimer tous les objets](settings.md#delete-all-objects) dans la zone de danger des paramètres d'administration, puis importez le fichier corrigé. Notez que cela supprime également toutes les modifications que vous avez apportées dans Gramps Web depuis l'importation.
