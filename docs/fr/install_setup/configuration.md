# Configuration du serveur

En utilisant l'image Docker par défaut, toute la configuration nécessaire peut être effectuée depuis le navigateur. Cependant, en fonction du déploiement, il peut être nécessaire de personnaliser la configuration du serveur.

Cette page répertorie toutes les méthodes pour modifier la configuration et toutes les options de configuration existantes.


## Fichier de configuration vs. variables d'environnement

Pour les paramètres, vous pouvez soit utiliser un fichier de configuration, soit des variables d'environnement.

Lorsque vous utilisez la [configuration basée sur Docker Compose](deployment.md), vous pouvez inclure un fichier de configuration en ajoutant l'élément de liste suivant sous la clé `volumes:` dans le bloc `grampsweb:` :

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
où `/path/to/config.cfg` est le chemin vers le fichier de configuration dans le système de fichiers de votre serveur (le côté droit fait référence au chemin dans le conteneur et ne doit pas être modifié).

Lors de l'utilisation de variables d'environnement,

- préfixez chaque nom de paramètre avec `GRAMPSWEB_` pour obtenir le nom de la variable d'environnement
- Utilisez des doubles underscores pour les paramètres de dictionnaire imbriqués, par exemple `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` définira la valeur de l'option de configuration `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Notez que les options de configuration définies via l'environnement ont la priorité sur celles du fichier de configuration. Si les deux sont présentes, la variable d'environnement "gagne".

!!! warning "Les variables d'environnement sans préfixe sont obsolètes"
    Pour des raisons historiques, une poignée de paramètres – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL`, et `STATIC_PATH` – peuvent encore être définis via une variable d'environnement *sans* le préfixe `GRAMPSWEB_`. Cela est obsolète, génère un avertissement au démarrage et cessera de fonctionner dans une future version. Utilisez toujours la forme préfixée, par exemple `GRAMPSWEB_TREE` au lieu de `TREE`.

    Notez que cela ne concerne que les variables d'environnement. Dans un fichier de configuration, les noms des paramètres sont toujours utilisés sans préfixe.

!!! tip "Vérification des options obsolètes"
    Les options de configuration obsolètes dont votre serveur dépend encore – telles que les variables d'environnement sans préfixe, `SEARCH_INDEX_DIR`, ou `EMAIL_USE_TLS` – sont enregistrées comme avertissements au démarrage. Depuis Gramps Web API 3.22, elles sont également listées, avec leur remplacement et la version dans laquelle le support sera supprimé, en haut de la page **Informations système** (accessible via l'icône utilisateur dans la barre d'application en haut) lorsque vous êtes connecté en tant qu'administrateur.

    Les paramètres de messagerie et l'URL de base que l'assistant de première exécution des anciennes versions a stockés dans la base de données y sont également listés. Définissez-les dans votre configuration aux valeurs stockées ; l'avertissement disparaît une fois qu'elles correspondent.

## Paramètres de configuration existants
Les options de configuration suivantes existent.

### Paramètres requis

Clé | Description
----|-------------
`TREE` | Le nom de la base de données de l'arbre généalogique à utiliser. Affichez les arbres disponibles avec `gramps -l`. Si un arbre avec ce nom n'existe pas, un nouvel arbre vide sera créé.
`SECRET_KEY` | La clé secrète pour flask. Le secret ne doit pas être partagé publiquement. Le changement invalidera tous les jetons d'accès.
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
`TREE_ID` | Le nom du répertoire de la base de données de l'arbre généalogique à utiliser en mode arbre unique (lorsque `TREE` n'est pas défini sur `*`). Lorsqu'il est défini, le serveur identifie l'arbre par son nom de répertoire plutôt que par son nom d'affichage, ce qui est plus robuste aux renommages. Requis si vous souhaitez renommer l'arbre via l'API. Le nom du répertoire peut être trouvé via `GET /api/trees/-` (le champ `id`).
`SEARCH_INDEX_DB_URI` | URL de la base de données pour l'index de recherche. Seuls `sqlite` ou `postgresql` sont autorisés comme backends. Par défaut, il est défini sur `sqlite:///indexdir/search_index.db`, créant un fichier SQLite dans le dossier `indexdir` par rapport au chemin où le script est exécuté.
`SEARCH_INDEX_DIR` | **Obsolète** (utilisez `SEARCH_INDEX_DB_URI` à la place). Répertoire contenant l'index de recherche. S'il est défini alors que `SEARCH_INDEX_DB_URI` est non défini, l'URL de l'index de recherche est dérivée comme `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Chemin pour servir des fichiers statiques (par exemple, un frontend web statique)
`BASE_URL` | URL de base où l'API peut être atteinte (par exemple, `https://mygramps.mydomain.com/`). Ceci est nécessaire par exemple pour construire des liens de réinitialisation de mot de passe corrects. Web Push nécessite également une URL HTTPS accessible publiquement ; le défaut `http://localhost/` désactive Web Push. Lors de la configuration de ce paramètre via l'environnement, utilisez `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Origines d'où les requêtes CORS sont autorisées. Par défaut, toutes sont interdites. Utilisez `"*"` pour autoriser les requêtes de n'importe quel domaine.
`EMAIL_HOST` | Hôte du serveur SMTP (par exemple, pour l'envoi d'e-mails de réinitialisation de mot de passe)
`EMAIL_PORT` | Port du serveur SMTP. par défaut 465
`EMAIL_HOST_USER` | Nom d'utilisateur du serveur SMTP
`EMAIL_HOST_PASSWORD` | Mot de passe du serveur SMTP
`EMAIL_USE_TLS` | **Obsolète** (utilisez `EMAIL_USE_SSL` ou `EMAIL_USE_STARTTLS` à la place). Booléen, si TLS doit être utilisé pour l'envoi d'e-mails. Par défaut, c'est `True`. Lors de l'utilisation de STARTTLS, définissez ceci sur `False` et utilisez un port différent de 25.
`EMAIL_USE_SSL` | Booléen, si SSL/TLS implicite doit être utilisé pour SMTP (v3.6.0+). Par défaut, c'est `True` si `EMAIL_USE_TLS` n'est pas explicitement défini. Utilisé typiquement avec le port 465.
`EMAIL_USE_STARTTLS` | Booléen, si STARTTLS explicite doit être utilisé pour SMTP (v3.6.0+). Par défaut, c'est `False`. Utilisé typiquement avec le port 587 ou 25.
`DEFAULT_FROM_EMAIL` | Adresse "De" pour les e-mails automatisés
`THUMBNAIL_CACHE_CONFIG` | Dictionnaire avec les paramètres pour le cache des vignettes. Voir [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) pour les paramètres possibles.
`REQUEST_CACHE_CONFIG` | Dictionnaire avec les paramètres pour le cache des requêtes. Voir [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) pour les paramètres possibles.
`PERSISTENT_CACHE_CONFIG` | Dictionnaire avec les paramètres pour le cache persistant, utilisé par exemple pour la télémétrie. Voir [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) pour les paramètres possibles.
`CELERY_CONFIG` | Paramètres pour la file d'attente de tâches en arrière-plan Celery. Voir [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) pour les paramètres possibles.
`REPORT_DIR` | Répertoire temporaire où la sortie des rapports Gramps sera stockée
`EXPORT_DIR` | Répertoire temporaire où la sortie de l'exportation de la base de données Gramps sera stockée
`BACKUP_DIR` | Répertoire où les [sauvegardes](../administration/backups.md) sont stockées, dans un sous-répertoire par arbre (v3.24.0+). Si non défini (par défaut), les sauvegardes ne peuvent pas être stockées sur le serveur, mais peuvent toujours être restaurées à partir d'un fichier téléchargé. Utilisez un emplacement persistant, par exemple un volume Docker, et de préférence un qui est lui-même sauvegardé ou synchronisé ailleurs.
`BACKUP_KEEP` | Nombre de sauvegardes stockées conservées par arbre ; les plus anciennes sont supprimées lorsqu'une nouvelle sauvegarde est créée (v3.24.0+). Par défaut, c'est `5`
`RATE_LIMIT_BACKUP` | Limite de taux pour la création de sauvegardes, par arbre (v3.24.0+). Par défaut, c'est `"10 par jour"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Limite de taux pour la création d'archives multimédias sur la page d'exportation. Par défaut, c'est `"1 par heure"`
`REGISTRATION_DISABLED` | Si `True`, interdire l'enregistrement de nouveaux utilisateurs (par défaut `False`)
`DISABLE_TELEMETRY` | Si `True`, désactiver la télémétrie des statistiques (par défaut `False`). Voir [télémétrie](telemetry.md) pour plus de détails.
`PILLOW_MAX_IMAGE_PIXELS` | Définit le paramètre PIL.Image.MAX_IMAGE_PIXELS, qui indique le nombre de pixels que l'image traitée peut contenir. Voir [docs](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) pour plus de détails.
`MAX_THUMBNAIL_FILE_BYTES` | Définit une taille de fichier maximale stricte pour les vignettes. Par défaut, c'est `50 * 1024 * 1024` (50 Mo). L'augmentation de cette valeur peut considérablement augmenter l'utilisation de la mémoire et peut entraîner des plantages par manque de mémoire ou une perte de données si de gros fichiers sont décompressés en mémoire.


!!! info
    Lors de l'utilisation de variables d'environnement pour la configuration, les options booléennes comme `EMAIL_USE_SSL` doivent être soit la chaîne `true` soit `false` (sensible à la casse !).


### Paramètres pour les bases de données PostgreSQL

Ces paramètres sont requis si vos arbres généalogiques sont hébergés dans une [base de données PostgreSQL](postgres.md) utilisant l'addon SharedPostgreSQL.

Clé | Description
----|-------------
`POSTGRES_USER` | Le nom d'utilisateur pour la connexion à la base de données
`POSTGRES_PASSWORD` | Le mot de passe pour l'utilisateur de la base de données


### Paramètres pertinents pour l'hébergement de plusieurs arbres

Les paramètres suivants sont pertinents lors de [l'hébergement de plusieurs arbres](multi-tree.md).


Clé | Description
----|-------------
`MEDIA_PREFIX_TREE` | Booléen, si oui ou non utiliser un sous-dossier séparé pour les fichiers multimédias de chaque arbre. Par défaut, c'est `False`, mais il est fortement recommandé d'utiliser `True` dans une configuration multi-arbres
`NEW_DB_BACKEND` | Le backend de base de données à utiliser pour les arbres généalogiques nouvellement créés. Doit être l'un de `sqlite` ou `sharedpostgresql`. Par défaut, c'est `sqlite`. La valeur `postgresql` est toujours acceptée mais obsolète, car le backend PostgreSQL sera supprimé dans Gramps Web API 4.0.
`POSTGRES_HOST` | Le nom d'hôte du serveur PostgreSQL utilisé pour créer de nouveaux arbres lors de l'utilisation d'une configuration multi-arbres avec le backend SharedPostgreSQL
`POSTGRES_PORT` | Le port du serveur PostgreSQL utilisé pour créer de nouveaux arbres lors de l'utilisation d'une configuration multi-arbres avec le backend SharedPostgreSQL


### Paramètres pour l'authentification OIDC

Ces paramètres sont nécessaires si vous souhaitez utiliser l'authentification OpenID Connect (OIDC) avec des fournisseurs externes. Pour des instructions de configuration détaillées et des exemples, voir [Authentification OIDC](oidc.md).

Clé | Description
----|-------------
`OIDC_ENABLED` | Booléen, si l'authentification OIDC doit être activée. Par défaut, c'est `False`.
`OIDC_ISSUER` | URL de l'émetteur du fournisseur OIDC (pour les fournisseurs OIDC personnalisés)
`OIDC_CLIENT_ID` | ID client OAuth (pour les fournisseurs OIDC personnalisés)
`OIDC_CLIENT_SECRET` | Secret client OAuth (pour les fournisseurs OIDC personnalisés)
`OIDC_NAME` | Nom d'affichage personnalisé pour le fournisseur. Par défaut, c'est "OIDC"
`OIDC_SCOPES` | Scopes OAuth. Par défaut, c'est "openid email profile"
`OIDC_USERNAME_CLAIM` | La revendication à utiliser pour le nom d'utilisateur. Par défaut, c'est "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Optionnel : URL vers le point de configuration OpenID Connect (si vous n'utilisez pas le standard `/.well-known/openid-configuration`)
`OIDC_PKCE` | Booléen, si PKCE doit être utilisé. S'il n'est pas défini, PKCE est utilisé lorsque le document de découverte du fournisseur liste `S256`. Voir [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Booléen, si l'authentification locale par nom d'utilisateur/mot de passe doit être désactivée. Par défaut, c'est `False`
`OIDC_AUTO_REDIRECT` | Booléen, si la redirection automatique vers OIDC doit se faire lorsque seul un fournisseur est configuré. Par défaut, c'est `False`

#### Fournisseurs OIDC intégrés

Pour les fournisseurs intégrés (Google, Microsoft), utilisez ces paramètres :

Clé | Description
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID client pour Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Secret client pour Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID client pour Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Secret client pour Microsoft OAuth
`OIDC_GOOGLE_PKCE` | Booléen, paramètre PKCE pour Google, voir [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Booléen, paramètre PKCE pour Microsoft, voir [PKCE](oidc.md#pkce)

#### Mappage des rôles OIDC

Ces paramètres vous permettent de mapper les groupes/rôles OIDC de votre fournisseur d'identité aux rôles utilisateurs de Gramps Web :

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

Ces paramètres sont nécessaires si vous souhaitez utiliser le chat IA. Voir [Configuration du chat IA](chat.md) pour plus de détails.

!!! note
    Les paramètres `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` et `VECTOR_EMBEDDING_API_KEY` pour la recherche sémantique sont ignorés depuis Gramps Web API 3.25, qui a supprimé la recherche sémantique. Le chat IA nécessite uniquement `LLM_MODEL`.

Clé | Description
----|-------------
`LLM_BASE_URL` | URL de base pour l'API de chat compatible OpenAI. Par défaut, c'est `None`, ce qui utilise l'API OpenAI.
`LLM_MODEL` | Le modèle à utiliser pour l'API de chat compatible OpenAI. S'il n'est pas défini (par défaut), le chat est désactivé. À partir de v3.6.0, l'assistant IA utilise Pydantic AI avec des capacités d'appel d'outils.
`LLM_MAX_OUTPUT_TOKENS` | Nombre maximum de tokens que le modèle peut générer dans une seule réponse. Non défini par défaut, laissant la limite au serveur du modèle. Utile pour les serveurs de modèles sans limite propre, où une réponse pourrait autrement se prolonger indéfiniment.
`LLM_MAX_CONTEXT_LENGTH` | Limite de caractères pour le contexte de l'arbre généalogique fourni au LLM. Par défaut, c'est 50000.
`LLM_SYSTEM_PROMPT` | Invite système personnalisée pour l'assistant de chat LLM (v3.6.0+). S'il n'est pas défini, utilise l'invite par défaut optimisée pour la généalogie.


## Exemple de fichier de configuration

Un fichier de configuration minimal pour la production pourrait ressembler à ceci :
```python
TREE="Mon arbre généalogique"
BASE_URL="https://monarbre.exemple.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.exemple.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Utiliser SSL implicite pour le port 465
EMAIL_HOST_USER="gramps@exemple.com"
EMAIL_HOST_PASSWORD="..." # votre mot de passe SMTP
DEFAULT_FROM_EMAIL="gramps@exemple.com"
