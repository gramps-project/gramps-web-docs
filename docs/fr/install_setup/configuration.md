# Configuration du serveur

Avec l’image Docker par défaut, toute la configuration nécessaire peut être effectuée depuis le navigateur. Toutefois, selon le déploiement, il peut être nécessaire de personnaliser la configuration du serveur.

Cette page répertorie toutes les méthodes permettant de modifier la configuration ainsi que toutes les options de configuration existantes.


## Fichier de configuration ou variables d’environnement

Pour les paramètres, vous pouvez utiliser soit un fichier de configuration, soit des variables d’environnement.

Lorsque vous utilisez la [configuration basée sur Docker Compose](deployment.md), vous pouvez inclure un fichier de configuration en ajoutant l’élément suivant sous la clé `volumes:` dans le bloc `grampsweb:` :

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
où `/path/to/config.cfg` correspond au chemin du fichier de configuration dans le système de fichiers de votre serveur (le côté droit fait référence au chemin dans le conteneur et ne doit pas être modifié).

Lorsque vous utilisez des variables d’environnement,

- préfixez chaque nom de paramètre par `GRAMPSWEB_` pour obtenir le nom de la variable d’environnement ;
- utilisez deux caractères de soulignement pour les paramètres de dictionnaires imbriqués, par exemple `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` définira la valeur de l’option de configuration `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`.

Notez que les options de configuration définies via l’environnement sont prioritaires sur celles du fichier de configuration. Si les deux sont présentes, la variable d’environnement « gagne ».

!!! warning "Les variables d’environnement sans préfixe sont obsolètes"
    Pour des raisons historiques, quelques paramètres — `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` et `STATIC_PATH` — peuvent encore être définis via une variable d’environnement *sans* le préfixe `GRAMPSWEB_`. Cette méthode est obsolète, génère un avertissement au démarrage et cessera de fonctionner dans une prochaine version. Utilisez toujours la forme préfixée, par exemple `GRAMPSWEB_TREE` au lieu de `TREE`.

    Notez que cela concerne uniquement les variables d’environnement. Dans un fichier de configuration, les noms des paramètres sont toujours utilisés sans préfixe.

!!! tip "Vérification des options obsolètes"
    Les options de configuration obsolètes dont votre serveur dépend encore — telles que les variables d’environnement sans préfixe, `SEARCH_INDEX_DIR` ou `EMAIL_USE_TLS` — sont consignées sous forme d’avertissements au démarrage. Depuis Gramps Web API 3.22, elles sont également répertoriées, avec leur remplacement et la version dans laquelle leur prise en charge sera supprimée, en haut de la page **Informations système** (accessible via l’icône utilisateur dans la barre d’application supérieure) lorsque vous êtes connecté en tant qu’administrateur.

    Les paramètres de messagerie et l’URL de base enregistrés dans la base de données par l’assistant de première exécution des anciennes versions y sont également répertoriés. Définissez-les dans votre configuration avec les valeurs enregistrées ; l’avertissement disparaît dès qu’elles correspondent.

## Paramètres de configuration existants
Les options de configuration suivantes existent.

### Paramètres obligatoires

Clé | Description
----|-------------
`TREE` | Nom de la base de données de l’arbre généalogique à utiliser. Affichez les arbres disponibles avec `gramps -l`. Si aucun arbre portant ce nom n’existe, un nouvel arbre vide sera créé.
`SECRET_KEY` | Clé secrète de Flask. Le secret ne doit pas être partagé publiquement. Sa modification invalidera tous les jetons d’accès.
`USER_DB_URI` | URL de la base de données des utilisateurs. Toute URL compatible avec SQLAlchemy est autorisée.

!!! info
    Vous pouvez générer une clé secrète sécurisée, par exemple avec la commande

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Paramètres facultatifs

Clé | Description
----|-------------
`MEDIA_BASE_DIR` | Chemin à utiliser comme répertoire de base des fichiers multimédias, remplaçant le répertoire de base des fichiers multimédias défini dans Gramps. Lorsque vous utilisez [S3](s3.md), doit être de la forme `s3://<bucket_name>`
`TREE_ID` | Nom du répertoire de la base de données de l’arbre généalogique à utiliser en mode arbre unique (lorsque `TREE` n’est pas défini sur `*`). Lorsqu’il est défini, le serveur identifie l’arbre par le nom de son répertoire plutôt que par son nom d’affichage, ce qui est plus robuste en cas de changement de nom. Obligatoire si vous souhaitez renommer l’arbre via l’API. Le nom du répertoire peut être trouvé via `GET /api/trees/-` (champ `id`).
`SEARCH_INDEX_DB_URI` | URL de la base de données pour l’index de recherche. Seuls `sqlite` et `postgresql` sont autorisés comme moteurs principaux. La valeur par défaut est `sqlite:///indexdir/search_index.db`, ce qui crée un fichier SQLite dans le dossier `indexdir`, relatif au chemin depuis lequel le script est exécuté.
`SEARCH_INDEX_DIR` | **Obsolète** (utilisez `SEARCH_INDEX_DB_URI` à la place). Répertoire contenant l’index de recherche. S’il est défini alors que `SEARCH_INDEX_DB_URI` ne l’est pas, l’URL de l’index de recherche est dérivée sous la forme `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Chemin depuis lequel les fichiers statiques doivent être servis (par exemple, une interface web statique).
`BASE_URL` | URL de base à laquelle l’API est accessible (par exemple `https://mygramps.mydomain.com/`). Elle est nécessaire, par exemple, pour générer correctement les liens de réinitialisation du mot de passe. Web Push nécessite également une URL HTTPS accessible publiquement ; la valeur par défaut `http://localhost/` désactive Web Push. Lorsque vous configurez ce paramètre via l’environnement, utilisez `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Origines depuis lesquelles les requêtes CORS sont autorisées. Par défaut, toutes les origines sont interdites. Utilisez `"*"` pour autoriser les requêtes provenant de n’importe quel domaine.
`EMAIL_HOST` | Hôte du serveur SMTP (par exemple pour l’envoi d’e-mails de réinitialisation du mot de passe).
`EMAIL_PORT` | Port du serveur SMTP. La valeur par défaut est 465.
`EMAIL_HOST_USER` | Nom d’utilisateur du serveur SMTP.
`EMAIL_HOST_PASSWORD` | Mot de passe du serveur SMTP.
`EMAIL_USE_TLS` | **Obsolète** (utilisez `EMAIL_USE_SSL` ou `EMAIL_USE_STARTTLS` à la place). Valeur booléenne indiquant s’il faut utiliser TLS pour l’envoi d’e-mails. La valeur par défaut est `True`. Lors de l’utilisation de STARTTLS, définissez ce paramètre sur `False` et utilisez un port différent de 25.
`EMAIL_USE_SSL` | Valeur booléenne indiquant s’il faut utiliser SSL/TLS implicite pour SMTP (v3.6.0+). La valeur par défaut est `True` si `EMAIL_USE_TLS` n’est pas explicitement défini. Généralement utilisé avec le port 465.
`EMAIL_USE_STARTTLS` | Valeur booléenne indiquant s’il faut utiliser STARTTLS explicite pour SMTP (v3.6.0+). La valeur par défaut est `False`. Généralement utilisé avec le port 587 ou 25.
`DEFAULT_FROM_EMAIL` | Adresse « De » des e-mails automatisés.
`THUMBNAIL_CACHE_CONFIG` | Dictionnaire contenant les paramètres du cache des miniatures. Consultez [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) pour connaître les paramètres possibles.
`REQUEST_CACHE_CONFIG` | Dictionnaire contenant les paramètres du cache des requêtes. Consultez [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) pour connaître les paramètres possibles.
`PERSISTENT_CACHE_CONFIG` | Dictionnaire contenant les paramètres du cache persistant, utilisé notamment pour la télémétrie. Consultez [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) pour connaître les paramètres possibles.
`CELERY_CONFIG` | Paramètres de la file de tâches d’arrière-plan Celery. Consultez [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) pour connaître les paramètres possibles.
`REPORT_DIR` | Répertoire temporaire dans lequel sera enregistrée la sortie des rapports Gramps exécutés.
`EXPORT_DIR` | Répertoire temporaire dans lequel sera enregistrée la sortie de l’exportation de la base de données Gramps.
`BACKUP_DIR` | Répertoire dans lequel les [sauvegardes](../administration/backups.md) sont stockées, dans un sous-répertoire par arbre (v3.24.0+). Si ce paramètre n’est pas défini (valeur par défaut), les sauvegardes ne peuvent pas être stockées sur le serveur, mais peuvent toujours être restaurées depuis un fichier téléversé. Utilisez un emplacement persistant, par exemple un volume Docker, et de préférence un emplacement lui-même sauvegardé ou synchronisé ailleurs.
`BACKUP_KEEP` | Nombre de sauvegardes conservées par arbre ; les plus anciennes sont supprimées lorsqu’une nouvelle sauvegarde est créée (v3.24.0+). La valeur par défaut est `5`.
`RATE_LIMIT_BACKUP` | Limite de fréquence pour la création de sauvegardes, par arbre (v3.24.0+). La valeur par défaut est `"10 per day"`.
`RATE_LIMIT_MEDIA_ARCHIVE` | Limite de fréquence pour la création d’archives multimédias sur la page Exportation. La valeur par défaut est `"1 per hour"`.
`REGISTRATION_DISABLED` | Si `True`, interdit l’inscription de nouveaux utilisateurs (valeur par défaut `False`). Depuis Gramps Web API 3.26, la page de connexion masque également son lien d’inscription.
`PROXY_FIX_X_FOR` | Nombre de reverse proxies de confiance placés devant Gramps Web (v3.26.0+). Définissez ce paramètre sur `1` derrière un reverse proxy unique afin que les limites de fréquence s’appliquent par client plutôt qu’à tous les utilisateurs collectivement. La valeur par défaut est `0`. Ne définissez ce paramètre que si le serveur est accessible exclusivement via ces proxies.
`DISABLE_TELEMETRY` | Si `True`, désactive la télémétrie statistique (valeur par défaut `False`). Consultez la page sur la [télémétrie](telemetry.md) pour plus de détails.
`PILLOW_MAX_IMAGE_PIXELS` | Définit le paramètre `PIL.Image.MAX_IMAGE_PIXELS`, qui indique le nombre de pixels que peut contenir l’image traitée. Consultez la [documentation](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) pour plus de détails.
`MAX_THUMBNAIL_FILE_BYTES` | Définit une taille maximale stricte pour les fichiers de miniatures. La valeur par défaut est `50 * 1024 * 1024` (50 Mo). L’augmenter peut accroître considérablement l’utilisation de la mémoire et provoquer des plantages dus à un manque de mémoire ou une perte de données si de gros fichiers sont décompressés en mémoire.


!!! info
    Lorsque vous utilisez des variables d’environnement pour la configuration, les options booléennes telles que `EMAIL_USE_SSL` doivent être soit la chaîne `true`, soit la chaîne `false` (en respectant la casse !).


### Paramètres pour les bases de données PostgreSQL

Ces paramètres sont obligatoires si vos arbres généalogiques sont hébergés dans une [base de données PostgreSQL](postgres.md) à l’aide de l’extension SharedPostgreSQL.

Clé | Description
----|-------------
`POSTGRES_USER` | Nom d’utilisateur pour la connexion à la base de données.
`POSTGRES_PASSWORD` | Mot de passe de l’utilisateur de la base de données.


### Paramètres pertinents pour l’hébergement de plusieurs arbres

Les paramètres suivants sont pertinents lorsque vous [hébergez plusieurs arbres](multi-tree.md).


Clé | Description
----|-------------
`MEDIA_PREFIX_TREE` | Valeur booléenne indiquant s’il faut utiliser ou non un sous-dossier distinct pour les fichiers multimédias de chaque arbre. La valeur par défaut est `False`, mais il est fortement recommandé d’utiliser `True` dans une configuration multi-arbres.
`NEW_DB_BACKEND` | Moteur de base de données à utiliser pour les arbres généalogiques nouvellement créés. Doit être `sqlite` ou `sharedpostgresql`. La valeur par défaut est `sqlite`. La valeur `postgresql` est toujours acceptée, mais elle est obsolète, car le moteur PostgreSQL sera supprimé dans Gramps Web API 4.0.
`POSTGRES_HOST` | Nom d’hôte du serveur PostgreSQL utilisé pour créer de nouveaux arbres lors de l’utilisation d’une configuration multi-arbres avec le moteur SharedPostgreSQL.
`POSTGRES_PORT` | Port du serveur PostgreSQL utilisé pour créer de nouveaux arbres lors de l’utilisation d’une configuration multi-arbres avec le moteur SharedPostgreSQL.


### Paramètres pour l’authentification OIDC

Ces paramètres sont nécessaires si vous souhaitez utiliser l’authentification OpenID Connect (OIDC) avec des fournisseurs externes. Pour obtenir des instructions détaillées de configuration et des exemples, consultez [Authentification OIDC](oidc.md).

Clé | Description
----|-------------
`OIDC_ENABLED` | Valeur booléenne indiquant s’il faut activer l’authentification OIDC. La valeur par défaut est `False`.
`OIDC_ISSUER` | URL de l’émetteur du fournisseur OIDC (pour les fournisseurs OIDC personnalisés).
`OIDC_CLIENT_ID` | ID client OAuth (pour les fournisseurs OIDC personnalisés).
`OIDC_CLIENT_SECRET` | Secret client OAuth (pour les fournisseurs OIDC personnalisés).
`OIDC_NAME` | Nom d’affichage personnalisé du fournisseur. La valeur par défaut est « OIDC ».
`OIDC_SCOPES` | Portées OAuth. La valeur par défaut est « openid email profile ».
`OIDC_USERNAME_CLAIM` | Claim à utiliser pour le nom d’utilisateur. La valeur par défaut est « preferred_username ».
`OIDC_OPENID_CONFIG_URL` | Facultatif : URL du point de terminaison de configuration OpenID Connect (si vous n’utilisez pas `/.well-known/openid-configuration`).
`OIDC_PKCE` | Valeur booléenne indiquant s’il faut utiliser PKCE. Si elle n’est pas définie, PKCE est utilisé lorsque le document de découverte du fournisseur répertorie `S256`. Consultez [PKCE](oidc.md#pkce).
`OIDC_DISABLE_LOCAL_AUTH` | Valeur booléenne indiquant s’il faut désactiver l’authentification locale par nom d’utilisateur et mot de passe. La valeur par défaut est `False`.
`OIDC_AUTO_REDIRECT` | Valeur booléenne indiquant s’il faut rediriger automatiquement vers OIDC lorsqu’un seul fournisseur est configuré. La valeur par défaut est `False`.
`OIDC_ALLOWED_REDIRECT_URIS` | Liste d’URI `https` auxquels les applications natives peuvent transmettre le résultat de la connexion (v3.26.0+), définie comme une liste JSON dans une variable d’environnement. Vide par défaut. Nécessaire uniquement si la documentation d’une application native le demande. Consultez [Applications natives](oidc.md#native-apps).

#### Fournisseurs OIDC intégrés

Pour les fournisseurs intégrés (Google, Microsoft), utilisez les paramètres suivants :

Clé | Description
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID client pour Google OAuth.
`OIDC_GOOGLE_CLIENT_SECRET` | Secret client pour Google OAuth.
`OIDC_MICROSOFT_CLIENT_ID` | ID client pour Microsoft OAuth.
`OIDC_MICROSOFT_CLIENT_SECRET` | Secret client pour Microsoft OAuth.
`OIDC_GOOGLE_PKCE` | Valeur booléenne, paramètre PKCE pour Google ; consultez [PKCE](oidc.md#pkce).
`OIDC_MICROSOFT_PKCE` | Valeur booléenne, paramètre PKCE pour Microsoft ; consultez [PKCE](oidc.md#pkce).

#### Mappage des rôles OIDC

Ces paramètres vous permettent de mapper les groupes/rôles OIDC de votre fournisseur d’identité aux rôles des utilisateurs de Gramps Web :

Clé | Description
----|-------------
`OIDC_ROLE_CLAIM` | Nom du claim dans le jeton OIDC contenant les groupes/rôles de l’utilisateur. La valeur par défaut est « groups ».
`OIDC_GROUP_ADMIN` | Nom du groupe/rôle de votre fournisseur OIDC correspondant au rôle Gramps « Admin ».
`OIDC_GROUP_OWNER` | Nom du groupe/rôle de votre fournisseur OIDC correspondant au rôle Gramps « Owner ».
`OIDC_GROUP_EDITOR` | Nom du groupe/rôle de votre fournisseur OIDC correspondant au rôle Gramps « Editor ».
`OIDC_GROUP_CONTRIBUTOR` | Nom du groupe/rôle de votre fournisseur OIDC correspondant au rôle Gramps « Contributor ».
`OIDC_GROUP_MEMBER` | Nom du groupe/rôle de votre fournisseur OIDC correspondant au rôle Gramps « Member ».
`OIDC_GROUP_GUEST` | Nom du groupe/rôle de votre fournisseur OIDC correspondant au rôle Gramps « Guest ».

### Paramètres réservés aux fonctionnalités d’IA

Ces paramètres sont nécessaires si vous souhaitez utiliser le chat IA. Consultez [Configuration du chat IA](chat.md) pour plus de détails.

!!! note
    Les paramètres `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` et `VECTOR_EMBEDDING_API_KEY` pour la recherche sémantique sont ignorés depuis Gramps Web API 3.25, qui a supprimé la recherche sémantique. Le chat IA nécessite uniquement `LLM_MODEL`.

Clé | Description
----|-------------
`LLM_BASE_URL` | URL de base de l’API de chat compatible avec OpenAI. La valeur par défaut est `None`, ce qui utilise l’API OpenAI.
`LLM_MODEL` | Modèle à utiliser pour l’API de chat compatible avec OpenAI. S’il n’est pas défini (valeur par défaut), le chat est désactivé. Depuis la version v3.6.0, l’assistant IA utilise Pydantic AI avec des fonctionnalités d’appel d’outils.
`LLM_MAX_OUTPUT_TOKENS` | Nombre maximal de jetons que le modèle peut générer dans une seule réponse. Non défini par défaut, la limite étant alors laissée au serveur du modèle. Utile pour les serveurs de modèles qui ne disposent pas de leur propre limite et dont une réponse pourrait sinon se poursuivre indéfiniment.
`LLM_MAX_CONTEXT_LENGTH` | Limite en caractères du contexte de l’arbre généalogique fourni au LLM. La valeur par défaut est 50000.
`LLM_SYSTEM_PROMPT` | Prompt système personnalisé pour l’assistant de chat LLM (v3.6.0+). S’il n’est pas défini, le prompt par défaut optimisé pour la généalogie est utilisé.
`LLM_VISION` | Valeur booléenne indiquant si les utilisateurs peuvent joindre des images à leurs questions (v3.26.0+). Activez cette option uniquement si le modèle accepte les images. La valeur par défaut est `False`. Consultez [Images dans les questions](chat.md#images-in-questions).
`LLM_ALLOW_WRITE_PROPOSALS` | Valeur booléenne indiquant si l’assistant peut proposer des modifications de l’arbre que les utilisateurs pourront examiner et appliquer (v3.26.0+). La valeur par défaut est `False`. Consultez [Autoriser l’assistant à proposer des modifications](chat.md#letting-the-assistant-propose-changes).


## Exemple de fichier de configuration

Un fichier de configuration minimal pour la production pourrait ressembler à ceci :
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Use implicit SSL for port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # your SMTP password
DEFAULT_FROM_EMAIL="gramps@example.com"
```
