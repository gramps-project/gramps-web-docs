# Travailler avec les correspondances ADN

Les correspondances ADN sont des segments d'ADN qui concordent entre deux individus, identifiés par la présence de marqueurs, appelés SNP (l'acronyme pour polymorphismes nucléotidiques uniques, prononcé « snips »).

Pour obtenir ces données, vous devez avoir accès à un test ADN qui est téléchargé dans une base de données de correspondance permettant de visualiser les données de correspondance des segments ADN (par exemple, MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web ne réalise pas la correspondance lui-même, car il n'a accès qu'aux données que vous téléchargez.

## Saisie des données de correspondance ADN

Pour entrer des données de correspondance ADN, vous avez besoin de [permissions d'édition](../install_setup/users.md) car les données sont stockées sous forme de note dans la base de données Gramps. La vue ADN, accessible depuis le menu principal, fournit un moyen pratique d'entrer ces données dans le bon format.

Pour entrer une nouvelle correspondance, cliquez sur le bouton + dans le coin inférieur droit. Dans la boîte de dialogue qui s'ouvre, sélectionnez les deux individus. Notez que la « Première personne » et la « Deuxième personne » sont traitées différemment : la correspondance est stockée comme une association de la première à la deuxième personne. Seule la première personne sera sélectionnable pour la vue de correspondance ADN et le navigateur de chromosomes. En général, la première personne est celle dont vous avez accès au test ADN et la deuxième personne est un parent plus éloigné.

Si la deuxième personne n'est pas dans la base de données, vous devez d'abord la créer en utilisant le bouton « Créer une personne » dans le coin supérieur droit de l'interface utilisateur. Une fois que vous avez créé la personne, vous pouvez revenir à la vue de correspondance ADN et sélectionner la personne nouvellement créée.

Ensuite, collez les données brutes dans le champ de texte. Les données doivent être un tableau de correspondances séparées par des virgules ou des tabulations, contenant généralement le numéro de chromosome, la position de début et de fin de la correspondance, le nombre de SNP dans la correspondance et la longueur de la correspondance en unités de centimorgans (cM). Vous pouvez également faire glisser et déposer un fichier contenant les données de correspondance dans le champ de texte.

Un exemple minimal de ce tableau est :

```csv
Chromosome,Start Location,End Location,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Si le format est valide, un aperçu est affiché sous le champ de texte sous forme de tableau.

Enfin, cliquez sur le bouton « Enregistrer » pour stocker la correspondance dans la base de données.

## Affichage des données de correspondance ADN

La vue de correspondance ADN a un menu déroulant qui permet de sélectionner chaque personne dans la base de données qui a une correspondance ADN associée. Une fois qu'une personne est sélectionnée, ses correspondances sont listées dans un tableau : le nom de la correspondance, leur relation avec la personne sélectionnée, la longueur totale de l'ADN partagé en centimorgans (cM), le nombre de segments partagés et la longueur du plus grand de ces segments.

Pour les correspondances déjà placées dans l'arbre, la colonne de relation montre la relation enregistrée dans l'arbre (déterminée automatiquement à partir de la base de données Gramps). Pour les correspondances qui ne sont pas liées à la personne sélectionnée dans l'arbre, elle montre la relation estimée à partir de l'ADN partagé, marquée par "≈".

Cliquer sur une correspondance ouvre sa page, avec un résumé de l'ADN partagé, l'[estimation de la relation](#relationship-estimate), un graphique de la relation dans l'arbre, et la liste des segments. Chaque segment indique s'il est du côté paternel ou maternel. Le côté peut être saisi manuellement (en fournissant un `P` pour paternel ou `M` pour maternel dans une colonne nommée `Side` dans les données brutes) ou déterminé automatiquement à partir de l'ancêtre commun le plus récent. Le bouton de téléchargement à côté des segments les enregistre sous forme de fichier CSV dans le format accepté par la boîte de dialogue de correspondance.

## Estimation de la relation

L'ADN partagé n'est pas une preuve d'une relation spécifique : la quantité d'ADN que deux parents partagent varie beaucoup, et différentes relations se chevauchent. Gramps Web montre donc une gamme de relations possibles avec leurs probabilités, calculées à partir du nombre et des longueurs des segments partagés (nécessite Gramps Web API 3.26 ou version ultérieure).

Les relations sont regroupées par leur *degré* :

- **Parent ou enfant** et **Frère ou sœur** sont affichés séparément.
- **Parent de degré 2** comprend les demi-frères et sœurs, les grands-parents et petits-enfants, ainsi que les tantes, oncles, nièces et neveux.
- **Parent de degré 3** comprend les cousins germains, les arrière-grands-parents, les grandes-tantes et grands-oncles, ainsi que les demi-tantes et demi-oncles.
- Chaque degré supplémentaire est d'environ une génération de plus, par exemple, les cousins germains éloignés sont de degré 4 et les cousins issus de germains sont de degré 5. Le degré 9 et au-delà sont regroupés sous "9+".

Les relations ayant le même degré partagent en moyenne à peu près la même quantité d'ADN, donc l'ADN seul ne peut pas les distinguer. Utilisez les âges des personnes pour décider entre elles – un parent de degré 2 de 30 ans d'un individu de 60 ans est plus probablement une nièce qu'un grand-parent.

L'estimation est la plus fiable pour les proches parents. Pour les relations éloignées, les correspondances partagent seulement quelques segments, et les probabilités se répartissent sur plusieurs degrés.

### Vérification de l'arbre par rapport à l'ADN

Si la correspondance est placée dans l'arbre, Gramps Web vérifie si l'ADN partagé correspond à la relation enregistrée. Si l'ADN est très peu probable pour cette relation, une icône d'avertissement est affichée dans le tableau des correspondances et un avertissement sur la page de correspondance. Le nombre entre parenthèses, par exemple "1 : 500", compare la probabilité que l'ADN corresponde à la relation enregistrée avec la probabilité qu'il corresponde à la relation la plus probable.

Un avertissement est une raison d'examiner de plus près, pas une preuve d'une erreur. Les causes courantes sont :

- une erreur dans l'arbre, comme un parent incorrect,
- une parenté mal attribuée, par exemple une adoption inconnue ou un père biologique différent,
- des données de correspondance incomplètes, par exemple si seuls les segments au-dessus d'un seuil élevé ont été copiés depuis le service de test,
- des relations par plus d'une lignée, par exemple des personnes liées par leur mère et leur père ("effondrement de pedigree"), qui partagent plus d'ADN que prévu.

Les relations qui ne sont pas par naissance, comme par adoption, ne sont pas vérifiées.

## Édition d'une correspondance

Pour éditer une correspondance, ouvrez sa page et cliquez sur le bouton d'édition, ou appuyez sur `e`. Notez que vous pouvez changer les données brutes, mais pas les individus associés à la correspondance – vous devez supprimer la correspondance et en créer une nouvelle si vous souhaitez changer les individus.

## Correspondances privées

Les boîtes de dialogue pour ajouter et éditer une correspondance ont un interrupteur **Privé**. Une correspondance privée, y compris ses segments, est cachée aux utilisateurs qui ne peuvent pas voir les enregistrements privés. Les correspondances privées sont marquées par un cadenas pour tous les autres. Voir [Enregistrements privés](privacy.md) pour en savoir plus sur la confidentialité.

## Travailler avec les données de correspondance dans Gramps Desktop

Les données de correspondance ADN sont stockées sous forme de note dans la base de données Gramps. Le format est compatible avec le 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
disponible pour Gramps Desktop. Sa page wiki contient plus de détails sur la façon d'obtenir les données, comment les interpréter et comment entrer les données dans Gramps.

!!! info
    Gramps Web API v2.8.0 a introduit des changements pour accepter une gamme plus large de données brutes de correspondance ADN, qui ne sont pas encore disponibles dans l'Addon Gramps Desktop. L'Addon Gramps Desktop sera mis à jour à l'avenir pour prendre en charge les mêmes formats également.
