# Carte

La page Carte affiche tous les lieux de votre arbre généalogique sous forme de marqueurs interactifs sur une carte géographique. Elle est accessible depuis la barre latérale.

## Marqueurs de lieu

Seuls les lieux ayant des coordonnées GPS stockées dans la base de données Gramps sont affichés sur la carte. Les lieux sans coordonnées sont omis silencieusement. Les coordonnées GPS peuvent être définies sur la page de détail du lieu (modifiez le lieu et remplissez les champs de latitude et de longitude).

!!! astuce
    Si de nombreux lieux manquent sur la carte, ouvrez une page de détail du lieu et vérifiez si la latitude et la longitude sont définies. Vous pouvez ajouter ou corriger les coordonnées directement depuis la vue d'édition du lieu.

Chaque lieu avec des coordonnées est affiché comme un marqueur. Cliquer sur un marqueur ouvre une carte de résumé affichant le nom du lieu et ses événements et personnes associés. Cliquez sur le nom du lieu dans la carte pour ouvrir la page de détail complète du lieu.

## Recherche

La zone de recherche dans le coin supérieur gauche de la carte vous permet de sauter à n'importe quel emplacement dans le monde par son nom. Cela ne filtre pas les lieux de l'arbre – cela déplace simplement et zoome la carte vers l'emplacement recherché.

## Curseur temporel

Le curseur temporel en bas de la page filtre les marqueurs de lieu affichés en fonction de l'année de leurs événements associés :

- Faites glisser le curseur pour sélectionner une année.
- Seuls les lieux liés à des événements qui tombent dans la fenêtre temporelle sélectionnée sont affichés.
- Utilisez ceci pour retracer où vos ancêtres ont vécu à un moment particulier de l'histoire.

## Couches de carte

Un bouton de commutation de couches (icône de couches empilées, en bas à gauche) vous permet de choisir entre deux cartes de base :

### Carte de base

La couche par défaut, alimentée par [OpenFreeMap](https://openfreemap.org) (style Liberty pour le mode clair, style sombre pour le mode sombre). C'est une carte moderne à usage général adaptée pour localiser des lieux.

### Carte historique

Change la carte de base pour [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), un projet communautaire qui cartographie le monde tel qu'il existait à différents moments dans le temps – pensez-y comme un pendant historique à OpenStreetMap.

Lorsque la couche Carte historique est active, le curseur temporel filtre également les tuiles de la carte elles-mêmes : OHM rend la carte telle qu'elle apparaissait dans l'année sélectionnée, donc les frontières historiques, les noms de lieux et les caractéristiques sont affichés au lieu des modernes. Cela permet de voir à la fois l'emplacement de votre ancêtre et le contexte géographique et politique contemporain dans une seule vue.

!!! note
    La couverture d'OpenHistoricalMap varie selon la région et la période. Les zones ou époques avec peu de contributions peuvent montrer des détails historiques limités. Si vous remarquez des données historiques manquantes ou inexactes, envisagez de [contribuer à OpenHistoricalMap](https://www.openhistoricalmap.org) – c'est un projet communautaire ouvert que tout le monde peut éditer.

## Superpositions de carte personnalisées

En plus des couches de base intégrées, vous pouvez transformer n'importe quelle image de carte historique numérisée – stockée dans Gramps en tant qu'objet **Média** – en une superposition personnalisée positionnée sur la carte en direct. Cela est utile pour les scans de vieux plans de ville, cartes paroissiales ou cartes de propriété que vous souhaitez comparer directement avec la géographie moderne ou historique.

### Géoréférencer une image

1. Ouvrez l'objet média pour l'image de la carte numérisée et passez en mode édition.
2. Ouvrez l'onglet "Carte" et cliquez sur **Modifier les coordonnées**. Cela ouvre une boîte de dialogue de géoréférencement avec l'image à côté d'une carte.
3. Cliquez sur **Sélectionner un point sur la carte**, puis cliquez sur l'emplacement sur la carte auquel un point de l'image doit correspondre. L'image est placée sur la carte pour la première fois dès qu'un point est sélectionné.
4. Utilisez le curseur **Échelle** pour redimensionner l'image et le curseur **Opacité** pour voir la carte de base à travers elle pendant le positionnement.
5. Cliquez sur **Aligner l'image** et cliquez à nouveau sur la carte pour déplacer l'image afin que le point épinglé soit parfaitement aligné.
6. Répétez les étapes d'échelle, d'opacité et d'alignement jusqu'à ce que l'image corresponde à la géographie sous-jacente, puis enregistrez.

En arrière-plan, cela stocke les coordonnées des coins de l'image dans un attribut `map:bounds` sur l'objet média.

### Affichage des superpositions sur la page Carte

Une fois qu'un objet média a été géoréférencé de cette manière, il devient automatiquement disponible en tant que couche activable sur la page Carte. Ouvrez le commutateur de couches (icône de couches empilées, en bas à gauche) pour afficher ou masquer chaque superposition indépendamment de la carte de base. Les superpositions sont listées par le titre de l'objet média.
