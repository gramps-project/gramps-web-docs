# Utilisation de Gramps Web pour l'analyse Y-DNA

!!! note "Note"
    Cette fonctionnalité nécessite la version 3.3.0 ou ultérieure de l'API Gramps Web et la version 25.9.0 ou ultérieure du frontend Gramps Web.

La vue Y-DNA dans Gramps Web peut utiliser des données brutes de polymorphisme de nucléotides simples (SNP) du chromosome Y pour déterminer le haplogroupe Y-DNA le plus probable d'une personne et afficher les ancêtres dérivés dans l'arbre du chromosome Y humain avec des estimations de temps.

## Comment obtenir et stocker les données SNP Y-DNA

Pour obtenir les données SNP Y-DNA, vous devez faire effectuer un test Y-DNA par un service de test génétique. Le résultat est représenté sous forme d'un ensemble de mutations (SNP), chacune identifiée par une chaîne (par exemple, `R-BY44535`) et un signe `+` ou `-` indiquant si la mutation est présente ou absente. Gramps Web s'attend à ce que la chaîne de tous les SNP testés soit au format `SNP1+, SNP2-, SNP3+,...` et soit stockée dans un attribut de personne de type personnalisé `Y-DNA` (sensible à la casse). Vous pouvez soit créer manuellement cet attribut dans Gramps Web ou Gramps Desktop, soit naviguer vers la vue Y-DNA dans Gramps Web et cliquer sur le bouton bleu "Ajouter", sélectionner la personne à laquelle ajouter les données, et coller la chaîne SNP. Dans tous les cas, les données seront stockées comme un attribut de personne dans votre base de données Gramps.

[Voir ci-dessous](#instructions-pour-obtenir-des-données-snp-des-services-de-test) pour des instructions sur la façon d'obtenir les données SNP auprès de divers services de test.

## Comment cela fonctionne

Une fois qu'une personne a un attribut `Y-DNA` contenant les données SNP, Gramps Web utilisera la bibliothèque Python open-source [yclade](https://github.com/DavidMStraub/yclade) pour déterminer la position la plus probable de la personne sur l'arbre du chromosome Y humain. L'arbre a été créé par le projet [YFull](https://www.yfull.com/) basé sur des dizaines de milliers de tests Y-DNA. Notez que Gramps Web utilise une copie locale de l'arbre YFull, donc aucune donnée n'est envoyée à un tiers.

L'arbre est parcouru de la racine aux feuilles, et à chaque nœud, les SNP associés à ce nœud sont comparés aux SNP testés positivement et négativement de la personne, et la branche appropriée est suivie.

Le résultat final est une succession de clades depuis la racine de l'arbre (l'[« Adam » chromosomique Y](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) jusqu'au clade le plus dérivé qui est cohérent avec les données SNP de la personne. Chaque clade a une âge estimé basé sur les âges des échantillons dans la base de données YFull qui appartiennent à ce clade.

Puisque les chromosomes Y sont hérités du père au fils, cette succession correspond à un extrait de l'ascendance patrilinéaire de la personne.

## Comment interpréter les résultats

L'information la plus importante est le haplogroupe le plus probable de la personne, affiché en haut de la page. Le nom est lié à la page correspondante sur le site [YFull](https://www.yfull.com/), qui contient plus d'informations, telles que le pays d'origine des échantillons testés appartenant à ce haplogroupe.

Dans l'arbre des ancêtres patrilinéaires montré dans Gramps Web, la case directement au-dessus de la personne testée est l'ancêtre commun le plus récent (MRCA) de tous les échantillons testés appartenant au haplogroupe de la personne. La date affichée pour cet ancêtre est sa date de naissance approximative estimée. L'ancêtre au-dessus de lui est l'ancêtre où la mutation définissant ce haplogroupe est apparue pour la première fois.

En raison du taux de mutation lent des chromosomes Y, le MRCA peut dater de plusieurs centaines d'années dans le passé. Pour les haplogroupes rares (c'est-à-dire les haplogroupes où peu de personnes ont été testées jusqu'à présent), cela peut même être des milliers d'années.

## Instructions pour obtenir des données SNP des services de test

### [YSEQ](https://www.yseq.net/)

Une fois connecté à "Mon Compte", allez à "Mes Résultats / Voir mes Allèles" et naviguez vers le bas de la page. Le champ de texte "Liste des allèles compacte" a été ajouté spécifiquement pour Gramps Web et est dans exactement le bon format pour être collé dans l'attribut `Y-DNA`.
