# Carte

La page Carte affiche tous les lieux de votre arbre généalogique sous forme de marqueurs interactifs sur une carte géographique. Elle est accessible depuis la barre latérale.

## Marqueurs de lieu

Seuls les lieux ayant des coordonnées GPS enregistrées dans la base de données Gramps sont affichés sur la carte. Les lieux sans coordonnées sont silencieusement omis. Les coordonnées GPS peuvent être définies sur la page de détails du lieu (modifiez le lieu et remplissez les champs de latitude et de longitude).

!!! astuce
    Si de nombreux lieux manquent sur la carte, ouvrez une page de détails de lieu et vérifiez si la latitude et la longitude sont définies. Vous pouvez ajouter ou corriger les coordonnées directement depuis la vue d'édition du lieu.

Chaque lieu avec des coordonnées est affiché sous forme de marqueur. Cliquer sur un marqueur ouvre une carte de résumé affichant le nom du lieu et ses événements et personnes associés. Cliquez sur le nom du lieu dans la carte pour ouvrir la page de détails complète du lieu.

## Recherche

La zone de recherche dans le coin supérieur gauche de la carte recherche au fur et à mesure que vous tapez et regroupe les résultats sous trois rubriques :

- **Lieux** – lieux dans votre arbre généalogique. En sélectionnant un lieu, la carte se déplace vers celui-ci et met en surbrillance son marqueur.
- **Personnes** – personnes dans votre arbre généalogique. En sélectionnant une personne, la carte passe en vue de la personne décrite [ci-dessous](#suivre-une-personne-sur-la-carte).
- **Externe** – emplacements provenant de [OpenStreetMap](https://www.openstreetmap.org/), pour n'importe quel endroit dans le monde. En sélectionnant un emplacement, la carte se déplace et zoome simplement vers cet endroit ; cela ne filtre pas ou ne change pas les lieux de votre arbre.

Les résultats externes sont également utiles lors de l'ajout de coordonnées à un lieu : vous pouvez rechercher l'emplacement ici pour voir où il se trouve avant d'entrer sa latitude et sa longitude.

## Suivre une personne sur la carte

Sélectionner une personne – depuis la zone de recherche de la carte, ou avec le bouton **Ouvrir dans la carte** sur la page de détails d'une personne – montre les lieux connectés aux événements de cette personne, reliés par des lignes dans l'ordre chronologique. De petites flèches le long de chaque ligne indiquent la direction du voyage, vous permettant de suivre la vie d'une personne de la naissance à la mort sur la carte.

Les lieux sur une page de détails de lieu ont également un bouton **Ouvrir dans la carte**, qui ouvre la carte centrée sur ce lieu.

## Curseur temporel

Le curseur temporel en bas de la page filtre les marqueurs de lieu affichés en fonction de l'année de leurs événements associés :

- Faites glisser le curseur pour sélectionner une année.
- Seuls les lieux liés à des événements qui tombent dans la fenêtre temporelle sélectionnée sont affichés.
- Utilisez ceci pour retracer où vos ancêtres ont vécu à un moment donné de l'histoire.

## Couches de carte

Un bouton de commutation de couche (icône de couches empilées, en bas à gauche) vous permet de choisir entre deux cartes de base :

### Carte de base

La couche par défaut, alimentée par [OpenFreeMap](https://openfreemap.org) (style Liberty pour le mode clair, style sombre pour le mode sombre). Il s'agit d'une carte moderne polyvalente adaptée pour localiser des lieux.

### Carte historique

Change la carte de base pour [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), un projet communautaire qui cartographie le monde tel qu'il existait à différents moments dans le temps – pensez-y comme un équivalent historique à OpenStreetMap.

Lorsque la couche de carte historique est active, le curseur temporel filtre également les tuiles de la carte elles-mêmes : OHM rend la carte telle qu'elle apparaissait à l'année sélectionnée, donc les frontières historiques, les noms de lieux et les caractéristiques sont affichés au lieu des modernes. Cela permet de voir à la fois l'emplacement de votre ancêtre et le contexte géographique et politique contemporain dans une seule vue.

!!! note
    La couverture d'OpenHistoricalMap varie selon la région et la période. Les zones ou époques avec des contributions rares peuvent montrer des détails historiques limités. Si vous remarquez des données historiques manquantes ou inexactes, envisagez de [contribuer à OpenHistoricalMap](https://www.openhistoricalmap.org) – c'est un projet communautaire ouvert que tout le monde peut éditer.

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

### Affichage des superpositions sur la page Carte

Une fois qu'un objet média a été géoréférencé de cette manière, il devient automatiquement disponible en tant que couche activable sur la page Carte. Ouvrez le commutateur de couche (icône de couches empilées, en bas à gauche) pour afficher ou masquer chaque superposition indépendamment de la carte de base. Les superpositions sont listées par le titre de l'objet média.
