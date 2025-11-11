# Travailler avec les correspondances ADN

Les correspondances ADN sont des segments d'ADN qui concordent entre deux individus, identifiés par la présence de marqueurs, appelés SNP (l'acronyme pour polymorphismes nucléotidiques uniques, prononcé « snips »).

Pour obtenir ces données, vous devez avoir accès à un test ADN qui est téléchargé dans une base de données de correspondance permettant de visualiser les données de correspondance des segments ADN (par exemple, MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web ne réalise pas la correspondance elle-même, car elle n'a accès qu'aux données que vous téléchargez.

## Saisie des données de correspondance ADN

Pour entrer des données de correspondance ADN, vous avez besoin de [permissions d'édition](../install_setup/users.md) car les données sont stockées sous forme de note dans la base de données Gramps. La vue ADN, accessible depuis le menu principal, fournit un moyen pratique d'entrer ces données au bon format.

Pour entrer une nouvelle correspondance, cliquez sur le bouton + dans le coin inférieur droit. Dans la boîte de dialogue qui s'ouvre, sélectionnez les deux individus. Notez que la « Première personne » et la « Deuxième personne » sont traitées différemment : la correspondance est stockée comme une association de la première à la deuxième personne. Seule la première personne sera sélectionnable pour la vue de correspondance ADN et le navigateur de chromosomes. En général, la première personne est celle dont vous avez accès au test ADN et la deuxième personne est un parent plus éloigné.

Si la deuxième personne n'est pas dans la base de données, vous devez d'abord la créer en utilisant le bouton « Créer une personne » dans le coin supérieur droit de l'interface utilisateur. Une fois que vous avez créé la personne, vous pouvez revenir à la vue de correspondance ADN et sélectionner la personne nouvellement créée.

Ensuite, collez les données brutes dans le champ de texte. Les données doivent être un tableau séparé par des virgules ou des tabulations de correspondances, contenant généralement le numéro de chromosome, la position de départ et de fin de la correspondance, le nombre de SNP dans la correspondance et la longueur de la correspondance en unités de centimorgans (cM). Vous pouvez également faire glisser et déposer un fichier contenant les données de correspondance dans le champ de texte.

Un exemple minimal d'un tel tableau est :

```csv
Chromosome,Start Location,End Location,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Si le format est valide, un aperçu est affiché sous le champ de texte sous forme de tableau.

Enfin, cliquez sur le bouton « Enregistrer » pour stocker la correspondance dans la base de données.

## Visualisation des données de correspondance ADN

La vue de correspondance ADN dispose d'un menu déroulant qui permet de sélectionner chaque personne dans la base de données ayant une correspondance ADN associée. Une fois qu'une personne est sélectionnée, les données de correspondance ADN sont affichées dans un tableau sous le menu déroulant. Il montre le nom de la personne avec laquelle la correspondance est associée, la relation avec la personne sélectionnée dans le menu déroulant (déterminée automatiquement à partir de la base de données Gramps), la longueur totale de l'ADN partagé en centimorgans (cM), le nombre de segments partagés et la longueur du plus grand de ces segments.

Lorsque vous cliquez sur une correspondance individuelle, cela ouvre une page de détails montrant tous les segments et si la correspondance est du côté maternel ou paternel. Cette information peut être soit saisie manuellement (en fournissant un `P` pour paternel ou `M` pour maternel dans une colonne nommée `Côté` dans les données brutes) soit déterminée automatiquement par Gramps en fonction de l'ancêtre commun le plus récent.

## Modification d'une correspondance

Vous pouvez modifier une correspondance en cliquant sur le bouton crayon dans le coin inférieur droit de la vue de détails de la correspondance. Cela ouvre une boîte de dialogue similaire à celle de la création d'une nouvelle correspondance, mais avec les données pré-remplies. Notez que vous pouvez changer les données brutes, mais pas les individus associés à la correspondance – vous devez supprimer la correspondance et en créer une nouvelle si vous souhaitez changer les individus.

## Travailler avec les données de correspondance dans Gramps Desktop

Les données de correspondance ADN sont stockées sous forme de note dans la base de données Gramps. Le format est compatible avec le 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
disponible pour Gramps Desktop. Sa page wiki contient plus de détails sur la façon d'obtenir les données, comment les interpréter et comment entrer les données dans Gramps.

!!! info
    L'API Gramps Web v2.8.0 a introduit des changements pour accepter une gamme plus large de données brutes de correspondance ADN, qui ne sont pas encore disponibles dans l'Addon Gramps Desktop. L'Addon Gramps Desktop sera mis à jour à l'avenir pour prendre en charge les mêmes formats également.
