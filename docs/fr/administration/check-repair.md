# Vérifier et valider les données

La section **Traitement de l'arbre généalogique** des [paramètres d'administration](settings.md) contient deux outils qui vérifient l'arbre généalogique : un pour les problèmes techniques dans la base de données et un pour les données implausibles.

## Vérifier et réparer la base de données

Cet outil vérifie la base de données Gramps pour des incohérences internes et corrige celles qu'il peut – analogue à l'outil [Vérifier et réparer la base de données](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) dans Gramps Desktop.

Cliquez sur **Vérifier et réparer** et attendez que l'indicateur de progression se termine. Le résultat est affiché sous le bouton :

- Si aucune erreur n'a été trouvée, un message de confirmation est affiché.
- Si des erreurs ont été trouvées, un résumé des corrections appliquées est affiché.

Exécutez cet outil si vous rencontrez des erreurs ou un comportement inattendu qui pourrait être causé par des incohérences dans la base de données, telles que des relations manquantes entre les objets.

## Vérifier les données

Alors que [Vérifier et réparer la base de données](#check-and-repair-database) recherche des incohérences *techniques*, cet outil recherche des données *implausibles* – analogue à l'outil [Vérifier les données](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) dans Gramps Desktop. Il signale des choses qui ne sont pas impossibles mais qui sont suffisamment improbables pour mériter un second regard, comme une mère âgée de 12 ans ou une personne ayant vécu jusqu'à 130 ans.

Sous **Options**, vous pouvez ajuster les seuils utilisés par les tests – âge maximum, âge minimum et maximum pour se marier ou avoir des enfants, nombre maximum d'enfants, etc. – ainsi que si vous souhaitez estimer les dates manquantes ou inexactes et si vous souhaitez signaler des dates invalides telles que le 31 février. Les options que vous modifiez sont mémorisées dans votre navigateur pour la prochaine exécution ; **Réinitialiser** restaure les valeurs par défaut.

Cliquez sur **Vérifier les données** pour commencer. La vérification s'exécute en tant que tâche en arrière-plan, et les résultats sont ensuite listés sous **Résultats de la vérification des données**. Rien n'est modifié par cet outil : il ne fait que rapporter ce qu'il trouve.

!!! note
    Un résultat n'est pas une preuve d'une erreur. De longues vies et de grands écarts d'âge se produisent, donc considérez les résultats comme une liste de choses à vérifier plutôt qu'une liste de choses à corriger.
