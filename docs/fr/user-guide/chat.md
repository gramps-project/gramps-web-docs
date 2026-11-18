# Utilisation de l'assistant IA

La vue **Assistant** dans Gramps Web (si activée dans votre installation) donne accès à un assistant IA qui répond aux questions sur votre arbre généalogique.

!!! warning
    Comme avec tout assistant IA, les réponses peuvent être incorrectes. Utilisez les liens dans la réponse pour vérifier les dossiers sur lesquels elles sont basées.

## Comment ça fonctionne

L'assistant ne connaît pas votre arbre à l'avance. Pour répondre à une question, un modèle de langage large recherche les dossiers nécessaires, tout comme vous le feriez vous-même :

- il recherche dans l'arbre avec la [recherche en texte intégral](search.md),
- il filtre les personnes, événements et familles par des critères tels que les noms, dates, lieux ou le nombre d'enfants,
- il trouve les ancêtres, descendants et autres parents d'une personne, avec leur relation,
- il lit des dossiers complets de personnes, familles, événements, lieux et notes.

Il répond ensuite en se basant sur les dossiers qu'il a trouvés, avec des liens vers ceux-ci. Pendant qu'il travaille, les outils qu'il utilise sont affichés, afin que vous puissiez suivre. Les questions qui prennent plus de temps s'exécutent en arrière-plan – vous pouvez naviguer ailleurs et revenir.

L'assistant répond uniquement à partir de votre arbre, pas à partir des connaissances générales du modèle de langage – même sur des personnes bien connues. Si l'arbre ne contient pas une information, il le dit, mentionnant les informations connexes qu'il a trouvées, par exemple dans une note. Il ne voit que ce que vous êtes autorisé à voir : les liens vers les dossiers privés sont affichés en texte brut pour les utilisateurs qui ne peuvent pas les consulter.

Les questions de suivi conservent le contexte des questions précédentes dans la même conversation, vous pouvez donc demander "Et quand est-il mort ?" après avoir posé une question sur une personne.

## Ce que vous pouvez demander

- **Faits sur les personnes** : "Quand est née Mary Smith ?" ou "Quels sont les noms des enfants de John Doe ?"
- **Parents** : "Qui sont les grands-parents de Jane Smith ?" ou "Quels descendants de Johann Meyer ont émigré en Amérique ?"
- **Recherches avec critères** : "Qui est né à Londres après 1850 ?", "Liste des mariages entre 1920 et 1950", ou "Quels couples ont eu cinq enfants ou plus ?"
- **Lieux** : "Quels événements se sont produits à Paris ?" ou "Qui est né au Danemark ?" – les lieux au sein d'un lieu plus grand sont inclus.
- **Notes** : "Que disent les notes sur la ferme de la famille Meyer ?"

Les questions qui nécessitent l'ensemble de l'arbre à la fois, comme "Quel est le prénom le plus courant ?", fonctionnent moins bien, car l'assistant ne voit qu'un nombre limité de dossiers par recherche.

## Demander des images

Si l'administrateur du serveur l'a activé, l'invite dispose d'un bouton pour joindre des images. Vous pouvez également coller une image ou déposer des fichiers image sur l'invite. Jusqu'à quatre images peuvent être jointes à une question, par exemple un scan d'un acte d'église pour demander "Qui est mentionné dans cette entrée, et est-il dans mon arbre ?"

Les images ne sont envoyées qu'avec la question à laquelle elles sont jointes. Les questions de suivi peuvent faire référence à ce que l'assistant a dit à leur sujet, mais pas aux images elles-mêmes, donc attachez-les à nouveau si nécessaire. Si votre arbre a une limite d'utilisation de l'IA, chaque image compte comme une question supplémentaire.

## Permettre à l'assistant de modifier votre arbre

Si l'administrateur du serveur l'a activé, les éditeurs, propriétaires et administrateurs peuvent demander à l'assistant de modifier l'arbre, par exemple "Ajouter un baptême le 3 mai 1802 à St. Mary's pour Johann Meyer" ou "Corriger l'année de naissance d'Anna Smith, elle devrait être 1871".

L'assistant ne change jamais rien de son propre chef. Il répond avec une carte **Modifications proposées** qui liste chaque dossier qu'il ajouterait, modifierait ou supprimerait, avec les anciennes valeurs barrées et les nouvelles valeurs mises en évidence. Rien ne se passe tant que vous n'avez pas cliqué sur **Appliquer**. Les modifications sont alors effectuées en une seule étape, que vous pouvez annuler comme toute autre modification, à partir du message qui apparaît ou dans l'[historique des révisions](revisions.md).

Vérifiez attentivement une proposition avant de l'appliquer – en particulier que l'assistant a choisi la bonne personne, et qu'il n'a pas ajouté un nouveau dossier (tel qu'un lieu ou une source) qui existe déjà dans votre arbre sous un nom légèrement différent. Si une proposition n'est pas tout à fait correcte, indiquez ce qu'il faut changer, et l'assistant proposera à nouveau.

Une fois qu'une proposition a été appliquée, les propositions plus anciennes dans la même conversation ne peuvent plus être appliquées, car elles ont été faites pour l'arbre tel qu'il était auparavant. Il en va de même si l'un des dossiers affectés a été modifié entre-temps.

## Conseils pour poser des questions

- **Nommez les personnes.** L'assistant ne sait pas qui vous êtes ni qui est votre personne de référence, donc au lieu de "ma grand-mère", demandez à propos de "la grand-mère d'Anna Smith (née en 1950)". Vous pouvez également utiliser des identifiants Gramps, par exemple "les enfants de I0042".
- **Soyez spécifique** lorsque les noms sont courants : "Quand le John Smith né en 1850 à Boston s'est-il marié ?" est mieux que "Quand John Smith s'est-il marié ?"
- **Utilisez votre langue.** Vous pouvez poser des questions dans votre propre langue et recevoir des réponses dans la même langue.
- **Demandez à nouveau différemment** si une réponse semble incomplète – par exemple en nommant le lieu ou la période de temps qui vous intéresse.

!!! tip
    Veuillez partager votre expérience sur ce qui fonctionne et ce qui ne fonctionne pas avec la communauté.
