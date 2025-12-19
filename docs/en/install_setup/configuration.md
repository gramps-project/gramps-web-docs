# Server Configuration

Using the default Docker image, all necessary configuration can be made from the browser. However, depending on the deployment, it can be necessary to customize the server configuration.

This page lists all methods to change the configuration and all existing configuration options.


## Configuration file vs. environment variables

For the settings, you can either use a configuration file or environment variables.

When you use the [Docker Compose based setup](deployment.md), you can include a configuration file by adding the following list item under the `volumes:` key in the `grampsweb:` block:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
where `/path/to/config.cfg` is the path to the config file in your server's file system (the right-hand side refers to the path in the container and must not be changed).

When using environment variables,

- prefix every setting name with `GRAMPSWEB_` to obtain the name of the environment variable
- Use double underscores for nested dictionary settings, e.g `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` will set the value of the `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` config option

Note that configuration options set via the environment take precedence over the ones in the configuration file. If both are present, the environment variable "wins".

## Existing configuration settings
The following configuration options exist.

### Required settings

Key | Description
----|-------------
`TREE` | The name of the family tree database to use. Show available trees with `gramps -l`. If a tree with this name does not exist, a new empty one will be created.
`SECRET_KEY` | The secret key for flask. The secret must not be shared publicly. Changing it will invalidate all access tokens.
`USER_DB_URI` | The database URL of the user database. Any URL compatible with SQLAlchemy is allowed.

!!! info
    You can generate a secure secret key e.g. with the command

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Optional settings

Key | Description
----|-------------
`MEDIA_BASE_DIR` | Path to use as base directory for media files, overriding the media base directory set in Gramps. When using [S3](s3.md), must have the form `s3://<bucket_name>`
`SEARCH_INDEX_DB_URI` | Database URL for the search index. Only `sqlite` or `postgresql` are allowed as backends. Defaults to `sqlite:///indexdir/search_index.db`, creating an SQLite file in the folder `indexdir` relative to the path where the script is run
`STATIC_PATH` | Path to serve static files from (e.g. a static web frontend)
`BASE_URL` | Base URL where the API can be reached (e.g. `https://mygramps.mydomain.com/`). This is necessary e.g. to build correct password reset links
`CORS_ORIGINS` | Origins where CORS requests are allowed from. By default, all are disallowed. Use `"*"` to allow requests from any domain.
`EMAIL_HOST` | SMTP server host (e.g. for sending password reset e-mails)
`EMAIL_PORT` | SMTP server port. defaults to 465
`EMAIL_HOST_USER` | SMTP server username
`EMAIL_HOST_PASSWORD` | SMTP server password
`EMAIL_USE_TLS` | **Deprecated** (use `EMAIL_USE_SSL` or `EMAIL_USE_STARTTLS` instead). Boolean, whether to use TLS for sending e-mails. Defaults to `True`. When using STARTTLS, set this to `False` and use a port different from 25.
`EMAIL_USE_SSL` | Boolean, whether to use implicit SSL/TLS for SMTP (v3.6.0+). Defaults to `True` if `EMAIL_USE_TLS` is not explicitly set. Typically used with port 465.
`EMAIL_USE_STARTTLS` | Boolean, whether to use explicit STARTTLS for SMTP (v3.6.0+). Defaults to `False`. Typically used with port 587 or 25.
`DEFAULT_FROM_EMAIL` | "From" address for automated e-mails
`THUMBNAIL_CACHE_CONFIG` | Dictionary with settings for the thumbnail cache. See [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for possible settings.
`REQUEST_CACHE_CONFIG` | Dictionary with settings for the request cache. See [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for possible settings.
`PERSISTENT_CACHE_CONFIG` | Dictionary with settings for the persistent cache, used e.g. for telemetry. See [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for possible settings.
`CELERY_CONFIG` | Settings for the Celery background task queue. See [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) for possible settings.
`REPORT_DIR` | Temporary directory where the output of running Gramps reports will be stored
`EXPORT_DIR` | Temporary directory where the output of exporting the Gramps database will be stored
`REGISTRATION_DISABLED` | If `True`, disallow new user registration (default `False`)
`DISABLE_TELEMETRY` | If `True`, disable statistics telemetry (default `False`). See [telemetry](telemetry.md) for details.


!!! info
    When using environment variables for configuration, boolean options like `EMAIL_USE_TLS` must be either the string `true` or `false` (case sensitive!).


### Settings only for PostgreSQL backend database

This is required if you've configured your Gramps database to work with the [PostgreSQL addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL).

Key | Description
----|-------------
`POSTGRES_USER` | The user name for the database connection
`POSTGRES_PASSWORD` | The password for the database user


### Settings relevant for hosting multiple trees

The following settings are relevant when [hosting multiple trees](multi-tree.md).


Key | Description
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, whether or not to use a separate subfolder for the media files of each tree. Defaults to `False`, but strongly recommend to use `True` in a multi-tree setup
`NEW_DB_BACKEND` | The database backend to use for newly created family trees. Must be one of `sqlite`, `postgresql`, or `sharedpostgresql`. Defaults to `sqlite`.
`POSTGRES_HOST` | The host name of the PostgreSQL server used for creating new trees when using a multi-tree setup with the SharedPostgreSQL backend
`POSTGRES_PORT` | The port of the PostgreSQL server used for creating new trees when using a multi-tree setup with the SharedPostgreSQL backend


### Settings for OIDC authentication

These settings are needed if you want to use OpenID Connect (OIDC) authentication with external providers. For detailed setup instructions and examples, see [OIDC Authentication](oidc.md).

Key | Description
----|-------------
`OIDC_ENABLED` | Boolean, whether to enable OIDC authentication. Defaults to `False`.
`OIDC_ISSUER` | OIDC provider issuer URL (for custom OIDC providers)
`OIDC_CLIENT_ID` | OAuth client ID (for custom OIDC providers)
`OIDC_CLIENT_SECRET` | OAuth client secret (for custom OIDC providers)
`OIDC_NAME` | Custom display name for the provider. Defaults to "OIDC"
`OIDC_SCOPES` | OAuth scopes. Defaults to "openid email profile"
`OIDC_USERNAME_CLAIM` | The claim to use for the username. Defaults to "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Optional: URL to the OpenID Connect configuration endpoint (if not using standard `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, whether to disable local username/password authentication. Defaults to `False`
`OIDC_AUTO_REDIRECT` | Boolean, whether to automatically redirect to OIDC when only one provider is configured. Defaults to `False`

#### Built-in OIDC providers

For built-in providers (Google, Microsoft, GitHub), use these settings:

Key | Description
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Client ID for Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Client secret for Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | Client ID for Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Client secret for Microsoft OAuth
`OIDC_GITHUB_CLIENT_ID` | Client ID for GitHub OAuth
`OIDC_GITHUB_CLIENT_SECRET` | Client secret for GitHub OAuth

#### OIDC Role Mapping

These settings allow you to map OIDC groups/roles from your identity provider to Gramps Web user roles:

Key | Description
----|-------------
`OIDC_ROLE_CLAIM` | The claim name in the OIDC token that contains the user's groups/roles. Defaults to "groups"
`OIDC_GROUP_ADMIN` | The group/role name from your OIDC provider that maps to the Gramps "Admin" role
`OIDC_GROUP_OWNER` | The group/role name from your OIDC provider that maps to the Gramps "Owner" role
`OIDC_GROUP_EDITOR` | The group/role name from your OIDC provider that maps to the Gramps "Editor" role
`OIDC_GROUP_CONTRIBUTOR` | The group/role name from your OIDC provider that maps to the Gramps "Contributor" role
`OIDC_GROUP_MEMBER` | The group/role name from your OIDC provider that maps to the Gramps "Member" role
`OIDC_GROUP_GUEST` | The group/role name from your OIDC provider that maps to the Gramps "Guest" role

### Settings only for AI features

These settings are needed if you want to use AI-powered features like chat or semantic search.

Key | Description
----|-------------
`LLM_BASE_URL` | Base URL for the OpenAI-compatible chat API. Defaults to `None`, which uses the OpenAI API.
`LLM_MODEL` | The model to use for the OpenAI-compatible chat API. If unset (the default), chat is disabled. As of v3.6.0, the AI assistant uses Pydantic AI with tool calling capabilities.
`VECTOR_EMBEDDING_MODEL` | The [Sentence Transformers](https://sbert.net/) model to use for semantic search vector embeddings. If unset (the default), semantic search and chat are disabled.
`LLM_MAX_CONTEXT_LENGTH` | Character limit for the family tree context provided to the LLM. Defaults to 50000.
`LLM_SYSTEM_PROMPT` | Custom system prompt for the LLM chat assistant (v3.6.0+). If unset, uses the default genealogy-optimized prompt.


## Example configuration file

A minimal configuration file for production could look like this:
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
