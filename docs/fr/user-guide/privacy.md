# Enregistrements privés

Tout enregistrement dans l'arbre peut être marqué comme privé. Avec les [rôles utilisateurs](../install_setup/users.md#user-roles), cela détermine qui voit quoi.

## Qui peut voir quoi

Gramps Web n'est jamais ouvert au public : seuls les utilisateurs ayant un compte peuvent voir quoi que ce soit. "Public" dans Gramps signifie simplement "non privé", c'est-à-dire visible par chaque utilisateur connecté de l'arbre.

| Rôle | Enregistrements publics | Enregistrements privés |
|---|---|---|
| Invité | voir | – |
| Membre | voir | voir |
| Contributeur | voir, ajouter | voir, ajouter |
| Éditeur, Propriétaire, Administrateur | voir, ajouter, éditer, supprimer | voir, ajouter, éditer, supprimer |

Pour les invités, les enregistrements privés n'existent pas : ils sont exclus des pages, des listes, des résultats de recherche, des graphiques, des rapports, des exports et des réponses de l'assistant IA. Cela est appliqué là où le serveur lit la base de données, et non en cachant des éléments dans l'application, donc un invité ne peut pas accéder aux données privées d'une autre manière non plus.

Les comptes qui n'ont pas encore été approuvés (après [auto-inscription](registration.md)) ne peuvent pas se connecter du tout.

Donc, si des proches ou d'autres personnes avec un compte invité ne doivent pas voir certaines informations, marquez-les comme privées. Si tous les utilisateurs d'un arbre peuvent voir tout, donnez-leur le rôle de membre (ou supérieur) et il n'est pas nécessaire de marquer quoi que ce soit comme privé.

## Les personnes vivantes ne sont pas privées automatiquement

Rien n'est rendu privé automatiquement – pas même les personnes qui sont encore en vie. Les données des personnes vivantes sont visibles par les invités jusqu'à ce que vous les marquiez comme privées. Cela s'applique également aux arbres importés.

Pour rendre privées les personnes qui sont probablement vivantes dans Gramps Web :

1. Dans la liste des personnes, ouvrez le [filtre avancé](lists.md#advanced-filter) et ajoutez la condition "Personnes probablement vivantes" (laissez la date vide pour aujourd'hui). Appliquez le filtre.
2. Cliquez sur **Sélectionner**, cochez la case dans l'en-tête, et choisissez **Tout sélectionner**.
3. Choisissez l'action **Confidentialité** et marquez les enregistrements comme privés.

"Probablement vivants" est estimé à partir des dates de la personne et de ses proches. Les personnes sans dates utilisables sont considérées comme vivantes. Vérifiez le résultat, et gardez à l'esprit que l'estimation peut changer à mesure que vous ajoutez des données.

Marquer une personne comme privée cache la personne, mais pas ses événements, notes, médias ou familles – voir ci-dessous. Gramps Desktop dispose de plus d'outils pour définir la confidentialité de nombreux enregistrements liés à la fois, que vous pouvez utiliser avec l'[addon de synchronisation](../administration/sync.md).

Les personnes qui meurent plus tard ne deviennent pas publiques automatiquement non plus. Que vous le souhaitiez ou non dépend de vous – de nombreux chercheurs préfèrent garder les informations collectées privées pendant un certain temps.

## Lecture des icônes de verrouillage

Les utilisateurs qui peuvent voir des données privées voient un verrou à côté des éléments privés. Il existe deux types :

- **Verrou rempli** – l'enregistrement lui-même est privé. Sur la page d'une personne, par exemple, un verrou rempli à côté d'un événement signifie que l'événement est privé, et à côté d'un enfant que l'enfant est privé.
- **Verrou en contour** – seul le *lien* est privé, pas l'enregistrement auquel il mène. Par exemple, le lien d'une personne vers un événement peut être privé tandis que l'événement lui-même est public. L'événement est alors caché de la page de cette personne mais reste visible ailleurs, comme sur les pages des autres participants ou dans la liste des événements.

Si à la fois l'enregistrement et son lien sont privés, le verrou rempli est affiché.

La même distinction s'applique aux enfants (l'enfant ou le lien de l'enfant vers la famille), aux associations, aux liens de dépôt d'une source, et aux médias dans une galerie. Les noms, attributs, adresses et URLs appartiennent à leur enregistrement et n'ont que le verrou rempli.

## Rendre quelque chose privé

Vous avez besoin de permissions d'édition pour changer la confidentialité.

- **Un enregistrement entier** : ouvrez sa page, entrez en mode édition, et cliquez sur le bouton de verrou dans la barre d'outils.
- **Une partie d'un enregistrement** – un nom alternatif, un attribut, une adresse, une URL, une association, un lien d'enfant ou un lien de dépôt : ouvrez la boîte de dialogue d'édition de cet élément et activez l'interrupteur **Privé**. Le nom principal n'a pas d'interrupteur, car la personne apparaîtrait sinon comme "Privée".
- **Un événement de la page d'une personne ou d'une famille** : la boîte de dialogue d'édition de l'événement a un interrupteur de confidentialité pour l'événement lui-même. Si l'événement est partagé avec d'autres personnes, il ne devient modifiable qu'après **Modifier pour tout le monde**, car il est privé pour tous.
- **Le lien d'une personne vers un événement** : sur la page de l'événement, ouvrez la ligne du participant en mode édition. L'interrupteur de confidentialité là s'applique uniquement au lien de ce participant, donc l'événement reste visible pour les autres participants.
- **Un objet média dans une galerie** : en mode édition, cliquez sur le verrou dans le coin de la tuile.
- **De nombreux enregistrements à la fois** : sélectionnez-les dans une liste et utilisez l'action **Confidentialité**, voir [Listes](lists.md#tags-and-privacy).

Pour vérifier quels enregistrements dans une liste sont privés, activez la colonne **Confidentialité** dans le sélecteur de colonnes de la liste.

## Choses à garder à l'esprit

- Rendre un enregistrement privé ne rend pas privés les enregistrements auxquels il est lié. Si une personne est privée, ses événements, les familles auxquelles elle appartient, et les notes qui y sont attachées restent visibles à moins qu'elles ne soient privées elles-mêmes. Utilisez le filtre avancé ou la colonne **Confidentialité** pour vérifier les enregistrements liés.
- Rendre une famille ou un événement privé le cache, mais pas les personnes qui y sont.
- [Les correspondances ADN et les données Y-ADN](dna-matches.md#private-matches) ont leur propre interrupteur **Privé** dans leurs boîtes de dialogue.
- Les exports et archives de médias réalisés par un utilisateur qui ne peut pas voir les données privées ne contiennent aucun enregistrement ou fichier privé.
- La confidentialité est une fonctionnalité de Gramps, donc les enregistrements marqués comme privés dans Gramps Desktop sont privés dans Gramps Web également, et vice versa.
