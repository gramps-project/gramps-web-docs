# Configuration pour l'hébergement de plusieurs arbres

Par défaut, Gramps Web ne permet d'accéder qu'à une seule base de données d'arbres familiaux (« arbre »), spécifiée dans le fichier de configuration.

Cependant, à partir de la version 0.7.0 de l'API backend de Gramps Web, il est également possible de servir plusieurs arbres à partir d'une seule installation. Cependant, chaque utilisateur est (actuellement) lié à un seul arbre, donc cette configuration n'est pas adaptée au partage d'arbres entre utilisateurs, mais à l'hébergement de plusieurs instances isolées de Gramps Web.

## Activer le support multi-arbres

Pour activer le support multi-arbres, l'option de configuration `TREE` doit être définie sur un astérisque unique `*`, par exemple dans un fichier de configuration :

```python
TREE = "*"
```

Cela rendra tous les arbres dans le répertoire de la base de données Gramps du serveur accessibles (sous réserve de permissions utilisateur suffisantes). L'ID de l'arbre est le nom du sous-répertoire. Vous pouvez lister les arbres existants (noms et IDs) avec la commande

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

De plus, vous devez définir l'option de configuration `MEDIA_PREFIX_TREE` sur `True` pour garantir que les fichiers multimédias sont stockés dans des sous-dossiers séparés. Sinon, les utilisateurs peuvent accéder à des fichiers multimédias qui appartiennent à un arbre pour lequel ils n'ont pas de permission !

## Ajouter un compte utilisateur à un arbre spécifique

Pour ajouter un utilisateur à un arbre spécifique, il suffit d'ajouter l'option de ligne de commande `--tree TREEID` à la commande d'ajout d'utilisateur. Vous pouvez également faire un POST sur le point de terminaison `/users/` avec la propriété `tree` définie dans la charge utile JSON.

Les noms d'utilisateur et les adresses e-mail doivent être uniques à travers *tous* les arbres.

## Créer un nouvel arbre

Pour créer un nouvel arbre, il est recommandé de faire un POST sur le point de terminaison `/trees/` plutôt que d'utiliser l'interface de ligne de commande Gramps. Cela utilisera un UUIDv4 comme ID d'arbre, ce qui entraîne une sécurité supplémentaire car le nom ne peut pas être deviné. Actuellement, seul SQLite est pris en charge pour les arbres nouvellement créés.

## Autoriser

Pour autoriser (récupérer un jeton), seuls le nom d'utilisateur et le mot de passe sont nécessaires, comme en mode à arbre unique, puisque l'ID de l'arbre est connu pour chaque utilisateur, il n'est donc pas nécessaire de le fournir.

## Migrer les fichiers multimédias existants

Si vous souhaitez migrer une instance Gramps Web existante vers le support multi-arbres et que vous utilisez des fichiers multimédias locaux, vous pouvez simplement les déplacer vers un sous-dossier de l'emplacement d'origine avec l'ID de l'arbre comme nom.

Si vous utilisez des fichiers multimédias hébergés sur S3, vous pouvez utiliser le script fourni dans le répertoire `scripts` du dépôt `gramps-web-api` :

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Cela suppose que les clés d'accès pertinentes sont déjà définies en tant que variables d'environnement.

## Migrer la base de données utilisateur existante

Si vous souhaitez activer le support multi-arbres et réutiliser des utilisateurs existants, vous devez les assigner à un arbre spécifique. Vous pouvez utiliser la commande suivante fournie à cet effet,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Personnaliser le frontend

La page d'inscription accessible depuis la page de connexion ne fonctionne pas dans une configuration multi-arbres, car un arbre doit être spécifié pour l'inscription. Il est donc conseillé de définir `hideRegisterLink` sur `true` dans la [configuration du frontend](frontend-config.md).
