# Utilisation du chat IA

!!! info
    Le chat IA nécessite la version 2.5.0 ou supérieure de l'API Gramps Web et la version 24.10.0 ou supérieure de Gramps Web. La version 3.6.0 de l'API Gramps Web a introduit des capacités d'appel d'outils pour des interactions plus intelligentes.

La vue de chat dans Gramps Web (si disponible dans votre installation) donne accès à un assistant IA qui peut répondre à des questions sur votre arbre généalogique.

!!! warning
    Étant donné qu'il s'agit encore d'une fonctionnalité nouvelle et en évolution, certains types de questions fonctionnent bien tandis que d'autres ne le font pas. De plus, comme avec tout assistant IA, il peut donner des réponses factuellement incorrectes, alors assurez-vous de toujours vérifier.

## Comment ça fonctionne

Pour comprendre quels types de questions l'assistant peut répondre, il est utile de comprendre comment cela fonctionne en coulisses :

1. L'utilisateur pose une question.
2. L'assistant IA peut utiliser plusieurs approches pour trouver des réponses :
   - **Recherche sémantique** : Gramps Web identifie les objets dans votre arbre généalogique qui sont les plus susceptibles de contenir des informations pertinentes. Par exemple, si vous demandez "Quels sont les noms des enfants de John Doe ?", les familles avec John Doe comme père seront parmi les meilleurs résultats.
   - **Appel d'outils (API Gramps Web v3.6.0+)** : L'assistant peut interroger directement votre base de données en utilisant des outils spécialisés pour rechercher, filtrer des personnes/événements/familles/lieux selon des critères spécifiques, calculer des relations entre des individus et récupérer des informations détaillées.
3. Gramps Web transmet la question ainsi que les informations récupérées à un grand modèle de langage pour formuler une réponse.
4. La réponse vous est affichée.

## Ce que vous pouvez demander

Avec les capacités d'appel d'outils introduites dans la version 3.6.0 de l'API Gramps Web, l'assistant IA peut désormais gérer des questions plus complexes :

- **Relations familiales** : "Qui sont les grands-parents de Jane Smith ?" ou "Comment John Doe est-il lié à Mary Johnson ?"
- **Recherches filtrées** : "Montrez-moi toutes les personnes nées à Londres après 1850" ou "Quels événements se sont produits à Paris ?"
- **Requêtes basées sur des dates** : "Qui est mort avant 1900 ?" ou "Listez les mariages qui ont eu lieu entre 1920 et 1950"
- **Informations sur les lieux** : "Quels lieux se trouvent en France ?" ou "Parlez-moi de l'église de St. Mary"
- **Questions générales** : "Quels sont les noms des enfants de John Doe ?" ou "Quand est née Mary Smith ?"

## Conseils pour poser des questions

Pour obtenir les meilleurs résultats de l'assistant IA :

- **Soyez spécifique** : Formulez votre question avec autant de détails que possible pour éviter les ambiguïtés. Par exemple, "Quand John Smith, né en 1850 à Boston, s'est-il marié ?" est mieux que "Quand John Smith s'est-il marié ?"
- **Utilisez des noms propres** : Mentionnez des noms, des lieux et des dates spécifiques lorsque cela est pertinent.
- **Posez une chose à la fois** : Décomposez les questions complexes en parties plus simples pour de meilleurs résultats.
- **Utilisez votre langue** : Les grands modèles de langage sont multilingues, donc vous pouvez poser des questions dans votre propre langue et recevoir des réponses dans la même langue.

!!! tip
    Veuillez partager votre expérience sur ce qui fonctionne et ce qui ne fonctionne pas avec la communauté.
