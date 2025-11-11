# Utilisation de Gramps Web pour la généalogie ADN

Il existe trois branches de la généalogie ADN en fonction du type d'ADN utilisé :

- Les chromosomes autosomiques (numérotés de 1 à 22) sont hérités du père et de la mère, donc la probabilité d'hériter d'un morceau d'ADN d'un ancêtre donné diminue de manière exponentielle avec le nombre de générations. Cela les rend utiles pour trouver des degrés de séparation avec des proches lorsqu'il y a un ancêtre commun relativement récent (quelques générations).
- Le chromosome Y est uniquement transmis du père au fils, il peut donc être utilisé pour retracer la lignée paternelle.
- L'ADN mitochondrial est transmis de la mère à la fille, il peut donc être utilisé pour retracer la lignée maternelle.

À l'heure actuelle, Gramps Web fournit des outils pour travailler avec [les correspondances des tests ADN autosomiques](dna-matches.md). Pour obtenir ces données, vous devez avoir accès à un test ADN qui est téléchargé dans une base de données de correspondance permettant de visualiser les données de correspondance des segments d'ADN (par exemple, MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web ne réalise pas lui-même les correspondances, car il n'a accès qu'aux données que vous téléchargez.
