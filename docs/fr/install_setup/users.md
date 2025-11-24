# Système d'utilisateur

Gramps Web n'est pas destiné à être exposé à Internet pour un accès public, mais uniquement par des utilisateurs authentifiés. Les comptes utilisateurs peuvent être créés par le propriétaire du site via la ligne de commande ou l'interface web, ou par auto-inscription suivie d'une approbation par le propriétaire du site.

## Rôles des utilisateurs

Les rôles d'utilisateur suivants sont actuellement définis.

Rôle | ID de rôle | Permissions
-----|------------|------------
Invité | 0 | Voir des objets non privés
Membre | 1 | Invité + voir des objets privés
Contributeur* | 2 | Membre + ajouter des objets
Éditeur | 3 | Contributeur + éditer et supprimer des objets
Propriétaire | 4 | Éditeur + gérer les utilisateurs
Administrateur | 5 | Propriétaire + éditer d'autres arbres dans une configuration multi-arbres

\* Notez que le rôle de "Contributeur" est actuellement seulement partiellement supporté ; par exemple, les objets familiaux ne peuvent pas être ajoutés car ils impliquent une modification des objets de personne Gramps sous-jacents des membres de la famille. Il est recommandé d'utiliser les autres rôles chaque fois que possible.

## Configuration de qui peut utiliser le chat AI

Si vous avez [configuré le chat AI](chat.md), vous verrez une option ici pour choisir quels groupes d'utilisateurs sont autorisés à utiliser la fonctionnalité de chat.

## Gestion des utilisateurs

Il existe deux façons de gérer les utilisateurs :

- Avec les permissions de propriétaire en utilisant l'interface web
- En ligne de commande sur le serveur

Le compte propriétaire requis pour accéder d'abord à l'application web peut être ajouté dans l'assistant d'intégration qui est automatiquement lancé lors de l'accès à Gramps Web avec une base de données utilisateur vide.

### Gestion des utilisateurs en ligne de commande

Lors de l'utilisation de [Docker Compose](deployment.md), la commande de base est

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

Le `COMMAND` peut être `add` ou `delete`. Utilisez `--help` pour `[ARGS]` afin d'afficher la syntaxe et les options de configuration possibles.

### Approbation des utilisateurs auto-inscrits

Lorsqu'un utilisateur s'auto-inscrit, il n'obtient pas un accès immédiat. Un email est envoyé au propriétaire de l'arbre concernant la nouvelle inscription de l'utilisateur et un email est envoyé à l'utilisateur pour confirmer son adresse email. La confirmation réussie de son adresse email change son rôle de `non confirmé` à `désactivé`. Tant que le compte utilisateur est dans l'un de ces deux rôles, l'utilisateur ne peut pas se connecter. Le propriétaire de l'arbre doit examiner la demande de l'utilisateur et lui attribuer un rôle approprié avant qu'il ne soit autorisé à se connecter.
