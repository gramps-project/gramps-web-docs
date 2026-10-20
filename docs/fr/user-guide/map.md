# Carte

La page Carte affiche tous les lieux de votre arbre généalogique sous forme de marqueurs interactifs sur une carte géographique. Elle est accessible depuis la barre latérale.

## Marqueurs de lieu

Seuls les lieux ayant des coordonnées GPS stockées dans la base de données Gramps sont affichés sur la carte. Les lieux sans coordonnées sont silencieusement omis. Les coordonnées GPS peuvent être définies sur la page de détail du lieu (modifiez le lieu et remplissez les champs de latitude et de longitude).

!!! astuce
    Si de nombreux lieux manquent sur la carte, ouvrez une page de détail de lieu et vérifiez si la latitude et la longitude sont définies. Vous pouvez ajouter ou corriger les coordonnées directement depuis la vue d'édition du lieu.

Chaque lieu avec des coordonnées est affiché comme un marqueur. Cliquer sur un marqueur ouvre une carte de résumé montrant le nom du lieu et ses événements et personnes liés. Cliquez sur le nom du lieu dans la carte pour ouvrir la page de détail complète du lieu.

## Recherche

La zone de recherche dans le coin supérieur gauche de la carte recherche au fur et à mesure que vous tapez et regroupe les résultats sous trois rubriques :

- **Lieux** – lieux dans votre arbre généalogique. En en sélectionnant un, la carte se déplace vers celui-ci et met en surbrillance son marqueur.
- **Personnes** – personnes dans votre arbre généalogique. En en sélectionnant une, la carte passe en vue de la personne décrite [ci-dessous](#suivre-une-personne-sur-la-carte).
- **Externe** – emplacements provenant d'[OpenStreetMap](https://www.openstreetmap.org/), pour n'importe où dans le monde. En en sélectionnant un, la carte se déplace et zoome simplement sur cet emplacement ; cela ne filtre ni ne change les lieux de votre arbre.

Les résultats externes sont également utiles lors de l'ajout de coordonnées à un lieu : vous pouvez rechercher l'emplacement ici pour voir où il se trouve avant d'entrer sa latitude et sa longitude.

## Suivre une personne sur la carte

Sélectionner une personne – depuis la zone de recherche de la carte, ou avec le bouton **Ouvrir dans la carte** sur la page de détail d'une personne – montre les lieux connectés aux événements de cette personne, reliés par des lignes dans l'ordre chronologique. De petites flèches le long de chaque ligne indiquent la direction du voyage, vous permettant de suivre la vie d'une personne depuis sa naissance jusqu'à sa mort sur la carte.

Les lieux sur une page de détail de lieu ont également un bouton **Ouvrir dans la carte**, qui ouvre la carte centrée sur ce lieu.

## Curseur temporel

Le curseur temporel en bas de la page filtre les marqueurs de lieu affichés en fonction de l'année de leurs événements associés :

- Faites glisser le curseur pour sélectionner une année.
- Seuls les lieux liés à des événements qui tombent dans la fenêtre temporelle sélectionnée sont affichés.
- Utilisez ceci pour retracer où vos ancêtres ont vécu à un moment donné de l'histoire.

## Couches de carte

Un bouton de commutateur de couche (icône de couches empilées, en bas à gauche) vous permet de choisir entre deux cartes de base. En dessous, il répertorie vos propres couches de carte sous "Vos cartes" (voir [Superpositions de carte personnalisées](#superpositions-de-carte-personnalisees) et [Fichiers de carte de lieux](#fichiers-de-carte-de-lieux)) et la couche [bâtiments Wikidata](#batiments-wikidata) sous "Externe", chacune pouvant être activée ou désactivée.

Les étiquettes des deux cartes de base sont affichées dans la langue que vous avez sélectionnée dans Gramps Web, où les données de la carte ont un nom dans cette langue, et dans le nom local sinon.

### Carte de base

La couche par défaut, alimentée par [OpenFreeMap](https://openfreemap.org) (style Liberty pour le mode clair, style sombre pour le mode sombre). Il s'agit d'une carte moderne polyvalente adaptée pour localiser des lieux.

### Carte historique

Change la carte de base pour [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), un projet communautaire qui cartographie le monde tel qu'il existait à différents moments dans le temps – pensez-y comme un pendant historique à OpenStreetMap.

Lorsque la couche de Carte historique est active, le curseur temporel filtre également les tuiles de la carte elles-mêmes : OHM rend la carte telle qu'elle apparaissait dans l'année sélectionnée, de sorte que les frontières historiques, les noms de lieux et les caractéristiques sont affichés au lieu des modernes. Cela permet de voir à la fois l'emplacement de votre ancêtre et le contexte géographique et politique contemporain dans une seule vue.

!!! note
    La couverture d'OpenHistoricalMap varie selon la région et la période. Les zones ou époques avec peu de contributions peuvent montrer des détails historiques limités. Si vous remarquez des données historiques manquantes ou inexactes, envisagez de [contribuer à OpenHistoricalMap](https://www.openhistoricalmap.org) – c'est un projet communautaire ouvert que tout le monde peut éditer.

## Superpositions de carte personnalisées

En plus des couches de base intégrées, vous pouvez transformer n'importe quelle image de carte historique numérisée – stockée dans Gramps en tant qu'objet **Média** – en une superposition personnalisée positionnée sur la carte en direct. Cela est utile pour les scans de vieux plans de ville, de cartes paroissiales ou de cartes de propriété que vous souhaitez comparer directement avec la géographie moderne ou historique.

### Géoréférencer une image

1. Ouvrez l'objet média pour l'image de la carte numérisée et passez en mode édition.
2. Ouvrez l'onglet "Carte" et cliquez sur **Modifier les coordonnées**. Cela ouvre une boîte de dialogue de géoréférencement avec l'image à côté d'une carte.
3. Cliquez sur **Sélectionner un point sur la carte**, puis cliquez sur l'emplacement sur la carte auquel un point sur l'image doit correspondre. L'image est placée sur la carte pour la première fois dès qu'un point est sélectionné.
4. Utilisez le curseur **Échelle** pour redimensionner l'image et le curseur **Opacité** pour voir la carte de base à travers elle pendant le positionnement.
5. Cliquez sur **Aligner l'image** et cliquez à nouveau sur la carte pour déplacer l'image afin que le point épinglé s'aligne précisément.
6. Répétez les étapes d'échelle, d'opacité et d'alignement jusqu'à ce que l'image corresponde à la géographie sous-jacente, puis enregistrez.

En arrière-plan, cela stocke les coordonnées des coins de l'image dans un attribut `map:bounds` sur l'objet média.

### Afficher les superpositions sur la page Carte

Une fois qu'un objet média a été géoréférencé de cette manière, il devient automatiquement disponible en tant que couche activable sur la page Carte. Ouvrez le commutateur de couche (icône de couches empilées, en bas à gauche) pour afficher ou masquer chaque superposition indépendamment de la carte de base. Les superpositions sont répertoriées par le titre de l'objet média.

## Fichiers de carte de lieux

Les lieux peuvent avoir des fichiers de carte attachés en tant qu'objets média – par exemple, les limites d'une paroisse, d'un district ou d'un domaine, ou un itinéraire. Les fichiers pris en charge sont KML (`.kml`), GeoJSON (`.geojson`) et GPX (`.gpx`).

Lorsque vous sélectionnez un lieu sur la carte, ses fichiers de carte sont dessinés au-dessus de la carte, en utilisant les couleurs stockées dans le fichier lorsqu'elles sont disponibles. Cela fonctionne également pour les lieux sans coordonnées : la carte zoome alors sur la zone couverte par les fichiers. Tant que le lieu est sélectionné, ses fichiers sont répertoriés dans le commutateur de couche sous "Vos cartes", où vous pouvez désactiver chacun d'eux.

Pour ajouter un fichier de carte à un lieu, ajoutez-le à la galerie du lieu comme tout autre [fichier média](media.md).

## Bâtiments Wikidata

La couche "bâtiments Wikidata" montre les bâtiments enregistrés dans [Wikidata](https://www.wikidata.org/), tels que des églises, des fermes ou des maisons de ville. Elle est désactivée par défaut et peut être activée dans le commutateur de couche sous "Externe". Les bâtiments ne sont affichés que lorsque la carte est suffisamment zoomée. Lorsque le curseur temporel est actif, seuls les bâtiments qui existaient à l'époque sélectionnée sont affichés.

Cliquez sur un bâtiment pour voir ses détails provenant de Wikidata, tels que sa date de construction ou de démolition, ses adresses, occupants et propriétaires.

### Enregistrer un bâtiment en tant que lieu

Les utilisateurs qui peuvent ajouter des objets voient un bouton **Enregistrer en tant que lieu** dans les détails du bâtiment. Cela ouvre le formulaire pour un nouveau lieu, prérempli avec le nom du bâtiment dans votre langue, un type de lieu (`Ferme` pour les fermes, sinon `Bâtiment`), ses coordonnées et un lien vers l'élément Wikidata. Complétez le formulaire, par exemple en sélectionnant le lieu englobant, et enregistrez-le.

Si un lieu dans votre arbre est au même emplacement que le bâtiment, le bouton indique **Ouvrir le lieu enregistré** à la place et montre ce lieu.

!!! info
    L'administrateur du serveur peut supprimer la couche de bâtiments Wikidata avec l'option `mapWikidata` de la [configuration du frontend](../install_setup/frontend-config.md).
