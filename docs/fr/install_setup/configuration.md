# Configuration du serveur

En utilisant l'image Docker par défaut, toute la configuration nécessaire peut être effectuée depuis le navigateur. Cependant, selon le déploiement, il peut être nécessaire de personnaliser la configuration du serveur.

Cette page répertorie toutes les méthodes pour modifier la configuration et toutes les options de configuration existantes.

## Fichier de configuration vs. variables d'environnement

Pour les paramètres, vous pouvez utiliser soit un fichier de configuration, soit des variables d'environnement.

Lorsque vous utilisez la [configuration basée sur Docker Compose](deployment.md), vous pouvez inclure un fichier de configuration en ajoutant l'élément de liste suivant sous la clé `volumes:` dans le bloc `grampsweb:` :

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
où `/path/to/config.cfg` est le chemin vers le fichier de configuration dans le système de fichiers de votre serveur (le côté droit fait référence au chemin dans le conteneur et ne doit pas être modifié).

Lors de l'utilisation de variables d'environnement,

- préfixez chaque nom de paramètre avec `GRAMPSWEB_` pour obtenir le nom de la variable d'environnement
- Utilisez des doubles underscores pour les paramètres de dictionnaire imbriqués, par exemple `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` définira la valeur de l'option de configuration `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Notez que les options de configuration définies via l'environnement ont la priorité sur celles du fichier de configuration. Si les deux sont présentes, la variable d'environnement "gagne".

## Paramètres de configuration existants
Les options de configuration suivantes existent.

### Paramètres requis

Clé | Description
----|-------------
`TREE` | Le nom de la base de données de l'arbre généalogique à utiliser. Affichez les arbres disponibles avec `gramps -l`. Si un arbre avec ce nom n'existe pas, un nouvel arbre vide sera créé.
`SECRET_KEY` | La clé secrète pour flask. Le secret ne doit pas être partagé publiquement. Le changer invalidera tous les jetons d'accès.
`USER_DB_URI` | L'URL de la base de données des utilisateurs. Toute URL compatible avec SQLAlchemy est autorisée.

!!! info
    Vous pouvez générer une clé secrète sécurisée par exemple avec la commande

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Paramètres optionnels

Clé | Description
----|-------------
`MEDIA_BASE_DIR` | Chemin à utiliser comme répertoire de base pour les fichiers multimédias, remplaçant le répertoire de base multimédia défini dans Gramps. Lors de l'utilisation de [S3](s3.md), doit avoir la forme `s3://<bucket_name>`
`SEARCH_INDEX_DB_URI` | URL de la base de données pour l'index de recherche. Seuls `sqlite` ou `postgresql` sont autorisés comme backends. Par défaut, c'est `sqlite:///indexdir/search_index.db`, créant un fichier SQLite dans le dossier `indexdir` par rapport au chemin où le script est exécuté
`STATIC_PATH` | Chemin pour servir des fichiers statiques (par exemple, un frontend web statique)
`BASE_URL` | URL de base où l'API peut être atteinte (par exemple, `https://mygramps.mydomain.com/`). Ceci est nécessaire par exemple pour construire des liens de réinitialisation de mot de passe corrects
`CORS_ORIGINS` | Origines d'où les requêtes CORS sont autorisées. Par défaut, toutes sont interdites. Utilisez `"*"` pour autoriser les requêtes de n'importe quel domaine.
`EMAIL_HOST` | Hôte du serveur SMTP (par exemple, pour l'envoi d'e-mails de réinitialisation de mot de passe)
`EMAIL_PORT` | Port du serveur SMTP. Par défaut, c'est 465
`EMAIL_HOST_USER` | Nom d'utilisateur du serveur SMTP
`EMAIL_HOST_PASSWORD` | Mot de passe du serveur SMTP
`EMAIL_USE_TLS` | Booléen, s'il faut utiliser TLS pour l'envoi d'e-mails. Par défaut, c'est `True`. Lors de l'utilisation de STARTTLS, définissez ceci sur `False` et utilisez un port différent de 25.
`DEFAULT_FROM_EMAIL` | Adresse "De" pour les e-mails automatisés
`THUMBNAIL_CACHE_CONFIG` | Dictionnaire avec les paramètres pour le cache des vignettes. Voir [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) pour les paramètres possibles.
`REQUEST_CACHE_CONFIG` | Dictionnaire avec les paramètres pour le cache des requêtes. Voir [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) pour les paramètres possibles.
`PERSISTENT_CACHE_CONFIG` | Dictionnaire avec les paramètres pour le cache persistant, utilisé par exemple pour la télémétrie. Voir [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) pour les paramètres possibles.
`CELERY_CONFIG` | Paramètres pour la file d'attente de tâches en arrière-plan Celery. Voir [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) pour les paramètres possibles.
`REPORT_DIR` | Répertoire temporaire où la sortie des rapports Gramps sera stockée
`EXPORT_DIR` | Répertoire temporaire où la sortie de l'exportation de la base de données Gramps sera stockée
`REGISTRATION_DISABLED` | Si `True`, interdire l'enregistrement de nouveaux utilisateurs (par défaut `False`)
`DISABLE_TELEMETRY` | Si `True`, désactiver la télémétrie des statistiques (par défaut `False`). Voir [télémétrie](telemetry.md) pour plus de détails.

!!! info
    Lors de l'utilisation de variables d'environnement pour la configuration, les options booléennes comme `EMAIL_USE_TLS` doivent être soit la chaîne `true` soit `false` (sensible à la casse !).

### Paramètres uniquement pour la base de données backend PostgreSQL

Ceci est requis si vous avez configuré votre base de données Gramps pour fonctionner avec l'[addon PostgreSQL](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL).

Clé | Description
----|-------------
`POSTGRES_USER` | Le nom d'utilisateur pour la connexion à la base de données
`POSTGRES_PASSWORD` | Le mot de passe pour l'utilisateur de la base de données

### Paramètres pertinents pour l'hébergement de plusieurs arbres

Les paramètres suivants sont pertinents lors de [l'hébergement de plusieurs arbres](multi-tree.md).

Clé | Description
----|-------------
`MEDIA_PREFIX_TREE` | Booléen, s'il faut ou non utiliser un sous-dossier séparé pour les fichiers multimédias de chaque arbre. Par défaut, c'est `False`, mais il est fortement recommandé d'utiliser `True` dans une configuration multi-arbres
`NEW_DB_BACKEND` | Le backend de base de données à utiliser pour les nouveaux arbres généalogiques créés. Doit être l'un de `sqlite`, `postgresql` ou `sharedpostgresql`. Par défaut, c'est `sqlite`.
`POSTGRES_HOST` | Le nom d'hôte du serveur PostgreSQL utilisé pour créer de nouveaux arbres lors de l'utilisation d'une configuration multi-arbres avec le backend SharedPostgreSQL
`POSTGRES_PORT` | Le port du serveur PostgreSQL utilisé pour créer de nouveaux arbres lors de l'utilisation d'une configuration multi-arbres avec le backend SharedPostgreSQL

### Paramètres pour l'authentification OIDC

Ces paramètres sont nécessaires si vous souhaitez utiliser l'authentification OpenID Connect (OIDC) avec des fournisseurs externes. Pour des instructions de configuration détaillées et des exemples, voir [Authentification OIDC](oidc.md).

Clé | Description
----|-------------
`OIDC_ENABLED` | Booléen, s'il faut activer l'authentification OIDC. Par défaut, c'est `False`.
`OIDC_ISSUER` | URL de l'émetteur du fournisseur OIDC (pour des fournisseurs OIDC personnalisés)
`OIDC_CLIENT_ID` | ID client OAuth (pour des fournisseurs OIDC personnalisés)
`OIDC_CLIENT_SECRET` | Secret client OAuth (pour des fournisseurs OIDC personnalisés)
`OIDC_NAME` | Nom d'affichage personnalisé pour le fournisseur. Par défaut, c'est "OIDC"
`OIDC_SCOPES` | Portées OAuth. Par défaut, c'est "openid email profile"
`OIDC_USERNAME_CLAIM` | La revendication à utiliser pour le nom d'utilisateur. Par défaut, c'est "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Optionnel : URL vers le point de terminaison de configuration OpenID Connect (si vous n'utilisez pas le standard `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Booléen, s'il faut désactiver l'authentification locale par nom d'utilisateur/mot de passe. Par défaut, c'est `False`
`OIDC_AUTO_REDIRECT` | Booléen, s'il faut rediriger automatiquement vers OIDC lorsqu'un seul fournisseur est configuré. Par défaut, c'est `False`

#### Fournisseurs OIDC intégrés

Pour les fournisseurs intégrés (Google, Microsoft, GitHub), utilisez ces paramètres :

Clé | Description
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID client pour Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Secret client pour Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID client pour Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Secret client pour Microsoft OAuth
`OIDC_GITHUB_CLIENT_ID` | ID client pour GitHub OAuth
`OIDC_GITHUB_CLIENT_SECRET` | Secret client pour GitHub OAuth

#### Mappage des rôles OIDC

Ces paramètres vous permettent de mapper les groupes/rôles OIDC de votre fournisseur d'identité aux rôles d'utilisateur Gramps Web :

Clé | Description
----|-------------
`OIDC_ROLE_CLAIM` | Le nom de la revendication dans le jeton OIDC qui contient les groupes/rôles de l'utilisateur. Par défaut, c'est "groups"
`OIDC_GROUP_ADMIN` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Admin" de Gramps
`OIDC_GROUP_OWNER` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Owner" de Gramps
`OIDC_GROUP_EDITOR` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Editor" de Gramps
`OIDC_GROUP_CONTRIBUTOR` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Contributor" de Gramps
`OIDC_GROUP_MEMBER` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Member" de Gramps
`OIDC_GROUP_GUEST` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Guest" de Gramps

### Paramètres uniquement pour les fonctionnalités d'IA

Ces paramètres sont nécessaires si vous souhaitez utiliser des fonctionnalités alimentées par l'IA comme le chat ou la recherche sémantique.

Clé | Description
----|-------------
`LLM_BASE_URL` | URL de base pour l'API de chat compatible OpenAI. Par défaut, c'est `None`, ce qui utilise l'API OpenAI.
`LLM_MODEL` | Le modèle à utiliser pour l'API de chat compatible OpenAI. Si non défini (par défaut), le chat est désactivé.
`VECTOR_EMBEDDING_MODEL` | Le modèle [Sentence Transformers](https://sbert.net/) à utiliser pour les embeddings vectoriels de recherche sémantique. Si non défini (par défaut), la recherche sémantique et le chat sont désactivés.
`LLM_MAX_CONTEXT_LENGTH` | Limite de caractères pour le contexte de l'arbre généalogique fourni au LLM. Par défaut, c'est 50000.

## Exemple de fichier de configuration

Un fichier de configuration minimal pour la production pourrait ressembler à ceci :
```python
TREE="Mon Arbre Généalogique"
BASE_URL="https://monarbre.exemple.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.exemple.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@exemple.com"
EMAIL_HOST_PASSWORD="..." # votre mot de passe SMTP
DEFAULT_FROM_EMAIL="gramps@exemple.com"
