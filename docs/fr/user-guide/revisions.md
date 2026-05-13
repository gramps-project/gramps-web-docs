# Historique des révisions

La vue de l'historique des révisions montre toutes les modifications qui ont été apportées à l'arbre généalogique.

La vue de liste affiche les modifications regroupées par "transactions". Une transaction est un groupe d'une ou plusieurs additions, suppressions ou modifications d'objets Gramps. Par exemple, l'ajout d'une nouvelle famille avec deux personnes existantes comme père et mère génère une transaction avec un objet famille ajouté et deux objets personne modifiés (car ils contiennent le lien vers le nouvel objet famille).

Cliquer sur une transaction ouvre la vue des détails de la transaction. Elle contient la liste des ajouts, suppressions et mises à jour individuelles par objet Gramps.

Sélectionner un changement individuel ouvre une vue de la représentation JSON brute de l'objet Gramps avec les ajouts et suppressions mis en surbrillance en vert et en rouge, respectivement.

## Annuler une révision

Sur la page des détails de la transaction, un bouton **Annuler** vous permet d'inverser cette transaction. En cliquant dessus, il est vérifié si l'annulation peut être effectuée proprement.

**Annulation propre** – si aucun des objets affectés par la transaction n'a été modifié depuis, l'annulation peut se poursuivre sans risque. Une boîte de dialogue de confirmation s'affiche et en cliquant sur **Annuler**, la transaction est inversée.

**Force requise** – si un ou plusieurs objets affectés ont été modifiés par une transaction ultérieure, une annulation propre n'est pas possible. La boîte de dialogue avertit que forcer l'annulation peut entraîner des incohérences de données, puisque les modifications ultérieures qui dépendent des objets en question seront préservées telles quelles, même si les objets sous-jacents sont rétablis. Vous pouvez alors soit annuler, soit cliquer sur **Forcer l'annulation** pour continuer quand même.

Dans les deux cas, l'annulation s'exécute en tant que tâche en arrière-plan et un indicateur de progression est affiché.
