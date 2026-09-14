# Comment Gramps organise les données

Gramps Web stocke un arbre généalogique non pas sous forme de graphique, mais sous forme d'objets séparés – personnes, familles, événements, lieux, sources, etc. – qui sont liés les uns aux autres. Une fois que vous comprenez comment ces objets s'imbriquent, la saisie des données devient prévisible : tout ce que vous souhaitez lier doit d'abord exister.

Gramps Web utilise le même modèle de données que Gramps Desktop, donc tout ce qui est mentionné sur cette page s'applique aux deux.

## Les éléments de base

| Objet | Ce qu'il représente | Exemples |
|---|---|---|
| Personne | Un individu | Vous, votre grand-mère |
| Famille | Un couple, leurs enfants, ou les deux | Vos parents et leurs enfants |
| Événement | Quelque chose qui s'est produit, avec une date et un lieu | Naissance, mariage, recensement, émigration |
| Lieu | Une localisation géographique | Un village, une paroisse, un pays |
| Source | Un document ou une collection d'informations | Un registre paroissial, un recensement, un livre |
| Citation | Une référence spécifique dans une source | Page 12, entrée 3 du registre paroissial |
| Répertoire | L'endroit où une source est conservée | Un archive, une bibliothèque, un site web |
| Note | Texte libre | Une transcription, des remarques de recherche |
| Objet multimédia | Un fichier | Une photo, un certificat scanné |

Chaque type d'objet a sa propre liste dans Gramps Web, voir [Listes](lists.md).

## Personnes et familles

Les parents et les enfants ne sont pas liés directement, mais par l'intermédiaire d'une **famille**. Une famille a jusqu'à deux partenaires et un nombre quelconque d'enfants :

- Vos parents et vous êtes liés par la famille dans laquelle vous êtes un enfant.
- Vos frères et sœurs sont les autres enfants de la même famille.
- Vous et votre conjoint formez une autre famille, dans laquelle vous êtes un partenaire, avec vos enfants.

Une personne peut être un enfant dans une famille et un partenaire dans plusieurs. Chaque enfant a une relation avec chacun des parents, telle que naissance, adoption ou beau-fils, et chaque famille a un type de relation, tel que marié ou union civile.

C'est pourquoi "ajouter des parents" à une personne signifie ajouter la personne en tant qu'enfant à une famille – ce que le [graphique de l'arbre](tree-edit.md) fait pour vous en une seule étape.

## Événements

Une naissance, un décès ou un mariage n'est pas un champ d'une personne, mais un **événement** à part entière, avec un type, une date, un lieu et une description. Les personnes sont liées à un événement par un **rôle** : la personne dont il s'agit a le rôle "Principal", tandis qu'une autre personne peut être liée au même événement en tant que témoin.

Les événements qui concernent un couple, comme un mariage, appartiennent à la famille plutôt qu'à l'un ou l'autre partenaire. Un événement peut également être partagé par plusieurs personnes – par exemple, un enregistrement de recensement répertoriant tout un ménage – au lieu d'être saisi une fois par personne.

## Objets partagés : lieux et sources

Les lieux, sources, citations, répertoires, notes et objets multimédias existent en tant que tels, et un nombre quelconque d'autres objets peut faire référence au même. Cela a quelques conséquences :

- **Créer une fois, sélectionner plusieurs fois.** Le village où dix de vos ancêtres sont nés est un lieu, sélectionné dans dix événements de naissance. Si vous corrigez son nom ou ses coordonnées, la correction s'applique partout.
- **Créez-le avant de le sélectionner.** Les formulaires dans Gramps Web sélectionnent des lieux et des sources qui existent déjà. Créez d'abord un nouveau lieu ou une nouvelle source en utilisant le bouton **+** (Ajouter) dans la barre d'application en haut.
- **Les lieux sont imbriqués.** Un lieu peut être englobé par un plus grand – un village par un comté, le comté par un pays – donc vous n'avez pas à répéter toute la hiérarchie pour chaque village.
- **Les sources et les citations sont séparées.** Une source est le registre paroissial dans son ensemble ; une citation est l'entrée spécifique qui soutient un fait, avec sa page, sa date, et votre confiance en elle. De nombreuses citations peuvent pointer vers la même source.

Si vous avez accidentellement créé le même lieu ou la même source deux fois, vous pouvez [fusionner les doublons](lists.md#merge).

## La Personne Domicile

La Personne Domicile est la personne à partir de laquelle les graphiques de l'arbre généalogique commencent et le point de départ par défaut pour les rapports. Voir [Première connexion](first-login.md) pour savoir comment la définir.

!!! note "Différent de Gramps Desktop"
    Dans Gramps Desktop, la Personne Domicile est stockée dans la base de données de l'arbre généalogique, donc elle est la même pour tous ceux qui ouvrent cette base de données. Gramps Web ne l'utilise pas. Au lieu de cela, la Personne Domicile est stockée dans votre navigateur, séparément pour chaque arbre : elle n'est pas partagée avec d'autres utilisateurs, et elle ne vous suit pas sur un autre navigateur ou appareil. Après avoir importé un arbre depuis Gramps Desktop, ou lorsque vous utilisez Gramps Web sur un autre appareil, vous devez la définir à nouveau.

## Un ordre recommandé

Lors de la saisie d'une nouvelle famille à la main, cet ordre évite de sauter d'un formulaire à l'autre :

1. **Lieux et sources.** Créez les lieux dont vous avez besoin et, si vous enregistrez des sources, la source à partir de laquelle vous travaillez.
2. **Personnes.** Ajoutez les personnes avec leurs dates et lieux de naissance et de décès. C'est le plus rapide en mode édition du graphique de l'arbre généalogique, qui crée les familles pour vous – voir [Démarrer un nouvel arbre](start-tree.md) et [Édition de l'arbre généalogique](tree-edit.md).
3. **Événements supplémentaires.** Ouvrez une famille (par exemple depuis l'onglet Relations d'une personne) pour ajouter le mariage, et la page d'une personne pour ajouter d'autres événements.
4. **Citations.** Dans l'onglet Citations de Source de la personne, de l'événement ou d'un autre objet qu'une source soutient, ajoutez une nouvelle citation, sélectionnez la source, et entrez la page.
5. **Notes et médias.** Joignez des transcriptions, des photos et des scans – voir [Ajouter des fichiers multimédias](media.md).

## Saisie des dates

Une date est saisie sous forme de champs séparés pour l'année, le mois et le jour, qui peuvent également être remplis à l'aide d'un sélecteur de date. Laissez de côté les parties que vous ne connaissez pas : une année seule est une date valide.

Au lieu de deviner un jour exact, décrivez ce que vous savez réellement avec le **Type** de la date :

| Ce que vous savez | Type | Exemple |
|---|---|---|
| La date exacte, ou une partie de celle-ci | Régulière | 12 mars 1850, ou juste 1850 |
| Une date approximative | environ | environ 1850 |
| Une limite | avant, après | avant 1900 |
| La date se situe quelque part dans une période | Plage | entre 1850 et 1855 |
| Quelque chose a duré pendant une période | Durée | de 1850 à 1855 |
| Seulement le début ou la fin d'une période | de, à | de 1850 |

Le champ **Qualité** enregistre comment vous êtes arrivé à une date : "Estimée" pour une estimation éclairée, "Calculée" pour une date dérivée d'autres informations, comme une année de naissance calculée à partir d'un âge au décès.

!!! warning "Les dates environ et estimées couvrent 50 ans dans les deux sens"
    Lorsque Gramps compare des dates, il traite une date de type "environ" – et toute date avec la qualité "Estimée" – comme une plage allant de 50 ans avant à 50 ans après la date donnée. Par exemple, filtrer la liste des personnes pour celles nées entre 1840 et 1860 trouve également une personne née "environ 1880", car cette date est considérée comme couvrant 1830 à 1930. De la même manière, "avant" et "après" sont considérés comme allant jusqu'à 50 ans avant ou après la date.

    Cela peut conduire à des résultats surprenants, donc utilisez "environ" et "Estimée" uniquement lorsque vous ne pouvez pas affiner la date. Si vous connaissez une période plus courte, une Plage telle que "entre 1878 et 1882" est plus précise.

Le champ **Calendrier** vous permet d'entrer une date dans le calendrier utilisé dans l'enregistrement original, tel que le calendrier julien, au lieu de le convertir vous-même.
