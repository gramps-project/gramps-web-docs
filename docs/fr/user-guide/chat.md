# Utilisation du chat IA

!!! info
    Le chat IA nécessite la version 2.5.0 ou supérieure de l'API Gramps Web et la version 24.10.0 ou supérieure de Gramps Web.


La vue de chat dans Gramps Web (si disponible dans votre installation) donne accès à un assistant IA qui peut répondre aux questions concernant votre arbre généalogique.

!!! warning
    Étant donné qu'il s'agit encore d'une fonctionnalité nouvelle et en évolution, certains types de questions fonctionnent bien tandis que d'autres ne le font pas. De plus, comme avec tout assistant IA, il peut donner des réponses factuellement incorrectes, donc assurez-vous de toujours vérifier.

## Comment ça fonctionne

Pour comprendre quels types de questions l'assistant peut répondre, il est utile de comprendre comment cela fonctionne en coulisses :

1. L'utilisateur pose une question.
2. Gramps Web identifie un certain nombre d'objets Gramps (par exemple, dix) qui sont les plus susceptibles de contenir les informations répondant à la question. À cette fin, il utilise une technique appelée "recherche sémantique". Par exemple, si vous demandez "Quel est le nom des enfants de John Doe ?", si une famille existe avec John Doe comme père, il est probable qu'elle figure parmi les meilleurs résultats.
3. Gramps Web transmet la question de l'utilisateur ainsi que les informations contextuelles récupérées à un grand modèle de langage ("chatbot") et lui demande d'extraire la bonne réponse.
4. La réponse est affichée à l'utilisateur.

## Comment poser une question

En raison de la façon dont le chat fonctionne, il n'est (actuellement) pas possible pour l'assistant IA de répondre à des questions sur des relations spécifiques autres que les parents ou les enfants, à moins que cette information ne soit contenue sous forme de texte dans une note.

Puisque chaque réponse est basée sur un nombre limité de meilleurs résultats de recherche sémantique, il ne peut également pas répondre à des questions sur des statistiques ("combien de personnes dans ma base de données ...").

Pour éviter les ambiguïtés et les malentendus, il est utile de formuler la question de manière aussi détaillée que possible.

Notez que les grands modèles de langage sont multilingues, donc vous pouvez lui parler dans votre propre langue et il répondra dans la même langue.

!!! tip
    Merci de partager votre expérience sur ce qui fonctionne et ce qui ne fonctionne pas avec la communauté.
