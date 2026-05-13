# Carte

La page Carte affiche tous les lieux de votre arbre généalogique sous forme de marqueurs interactifs sur une carte géographique. Elle est accessible depuis la barre latérale.

## Marqueurs de lieu

Seuls les lieux ayant des coordonnées GPS stockées dans la base de données Gramps sont affichés sur la carte. Les lieux sans coordonnées sont silencieusement omis. Les coordonnées GPS peuvent être définies sur la page de détail du lieu (modifiez le lieu et remplissez les champs de latitude et de longitude).

!!! astuce
    Si de nombreux lieux manquent sur la carte, ouvrez une page de détail d'un lieu et vérifiez si la latitude et la longitude sont définies. Vous pouvez ajouter ou corriger les coordonnées directement depuis la vue d'édition du lieu.

Chaque lieu avec des coordonnées est affiché sous forme de marqueur. Cliquer sur un marqueur ouvre une carte de résumé affichant le nom du lieu et ses événements et personnes associés. Cliquez sur le nom du lieu dans la carte pour ouvrir la page de détail complète du lieu.

## Recherche

La zone de recherche dans le coin supérieur gauche de la carte vous permet de sauter à n'importe quel emplacement dans le monde par son nom. Cela ne filtre pas les lieux de l'arbre – cela déplace simplement et zoom la carte vers l'emplacement recherché.

## Curseur temporel

Le curseur temporel en bas de la page filtre quels marqueurs de lieu sont affichés en fonction de l'année de leurs événements associés :

- Faites glisser le curseur pour sélectionner une année.
- Seuls les lieux liés à des événements qui tombent dans la fenêtre temporelle sélectionnée sont affichés.
- Utilisez ceci pour retracer où vos ancêtres ont vécu à un moment donné de l'histoire.

## Couches de carte

Un bouton de changement de couche (icône de couches empilées, en bas à gauche) vous permet de choisir entre deux cartes de base :

### Carte de base

La couche par défaut, alimentée par [OpenFreeMap](https://openfreemap.org) (style Liberty pour le mode clair, style sombre pour le mode sombre). C'est une carte moderne polyvalente adaptée pour localiser des lieux.

### Carte historique

Change la carte de base pour [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), un projet communautaire qui cartographie le monde tel qu'il existait à différents moments dans le temps – pensez-y comme à un homologue historique d'OpenStreetMap.

Lorsque la couche de Carte historique est active, le curseur temporel filtre également les tuiles de la carte elles-mêmes : OHM rend la carte telle qu'elle apparaissait dans l'année sélectionnée, donc les frontières historiques, les noms de lieux et les caractéristiques sont affichés au lieu des modernes. Cela permet de voir à la fois l'emplacement de votre ancêtre et le contexte géographique et politique contemporain dans une seule vue.

!!! note
    La couverture d'OpenHistoricalMap varie selon la région et la période. Les zones ou époques avec peu de contributions peuvent montrer des détails historiques limités. Si vous remarquez des données historiques manquantes ou inexactes, envisagez de [contribuer à OpenHistoricalMap](https://www.openhistoricalmap.org) – c'est un projet communautaire ouvert que tout le monde peut éditer.
