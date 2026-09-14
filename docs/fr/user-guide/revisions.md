# Historique des révisions

La vue de l'historique des révisions montre toutes les modifications qui ont été apportées à l'arbre généalogique.

La vue en liste affiche les modifications regroupées par "transactions". Une transaction est un groupe d'une ou plusieurs ajouts, suppressions ou modifications d'objets Gramps. Par exemple, l'ajout d'une nouvelle famille avec deux personnes existantes en tant que père et mère génère une transaction avec un objet de famille ajouté et deux objets de personne modifiés (car ils contiennent le lien vers le nouvel objet de famille).

Cliquer sur une transaction ouvre la vue détaillée de la transaction. Elle contient la liste des ajouts, suppressions et mises à jour individuelles par objet Gramps.

Sélectionner un changement individuel ouvre une vue de la représentation JSON brute de l'objet Gramps avec les ajouts et suppressions mis en évidence en vert et en rouge, respectivement. Un bouton au-dessus de la différence vous dirige directement vers la page de l'objet.

## Révisions d'un seul objet

Pour voir l'historique d'une personne, d'une famille, d'un événement ou d'un autre objet particulier, ouvrez sa page et passez à l'onglet **Révisions**. Il liste chaque changement apporté à cet objet, du plus récent au plus ancien, avec le type de changement (ajouté, mis à jour ou supprimé), l'utilisateur qui l'a effectué et quand. Cliquer sur une entrée ouvre la transaction à laquelle elle appartient, où vous pouvez inspecter la différence ou l'annuler.

Cliquez sur **Afficher plus** pour charger des entrées plus anciennes ; pour les objets ayant un historique très long, seules les révisions les plus récentes sont affichées. Pour les objets modifiés avant que l'historique des révisions ne soit enregistré, l'onglet n'affiche que le moment de la dernière modification.

!!! note
    L'onglet Révisions est visible pour les membres et au-dessus et nécessite la version 3.22 ou ultérieure de l'API Web Gramps.

## Annuler une révision

Sur la page de détail de la transaction, un bouton **Annuler** vous permet de revenir sur cette transaction. En cliquant dessus, il est vérifié si l'annulation peut être effectuée proprement.

**Annulation propre** – si aucun des objets affectés par la transaction n'a été modifié depuis, l'annulation peut se poursuivre sans risque. Une boîte de dialogue de confirmation s'affiche et en cliquant sur **Annuler**, la transaction est inversée.

**Force requise** – si un ou plusieurs objets affectés ont été modifiés par une transaction ultérieure, une annulation propre n'est pas possible. La boîte de dialogue avertit que forcer l'annulation peut entraîner des incohérences de données, puisque les modifications ultérieures qui dépendent des objets en question seront préservées telles quelles même si les objets sous-jacents sont rétablis. Vous pouvez alors soit annuler, soit cliquer sur **Forcer l'annulation** pour continuer malgré tout.

Dans les deux cas, l'annulation s'exécute en tant que tâche en arrière-plan et un indicateur de progression est affiché.
