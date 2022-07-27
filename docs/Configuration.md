# Server Configuration

Using the default Docker image, all necessary configuration can be made from the browser. However, depending on the deployment, it can be necessary to customize the server configuration.

This page lists all methods to change the configuration and all existing configuration options.

## Configuration file

A configuration file is not mandatory as most settings can also be provided as environment variables. The basic setup shown in the [Deployment](Deployment.md) docs works without one. 

When you use the [Docker Compose based setup](Deployment.md), you can include a configuration file by adding the following list item under the `volumes:` key in the `grampsweb:` block:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
where `/path/to/config.cfg` is the path to the config file in your server's file system (the right-hand side refers to the path in the container and must not be changed).

## Existing configuration settings
The following configuration options exist. The last column indicates whether the option can be set from an environment variable.

### Required settings

Key | Description | Set from environment
----|-------------|---------------------
`TREE` | The name of the family tree database to use. Show available trees with `gramps -l` | yes
`SECRET_KEY` | The secret key for flask. This must be set for use in production. The secret must not be shared publicly. Changing it will invalidate all access tokens | yes

!!! info
    You can generate a secure secret key e.g. with the command

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Optional settings

Key | Description | Set from environment
----|-------------|---------------------
`MEDIA_BASE_DIR` | Path to use as base directory for media files, overriding the media base directory set in Gramps | yes
`SEARCH_INDEX_DIR` | Path for the full-text search index. Defaults to `indexdir` relative to the path where the script is run | yes
`STATIC_PATH` | Path to serve static files from (e.g. a static web frontend) | yes
`BASE_URL` | Base URL where the API can be reached (e.g. `https://mygramps.mydomain.com/`). This is necessary e.g. to build correct passwort reset links | yes
`CORS_ORIGINS` | Origins where CORS requests are allowed from. By default, all are disallowed. Use `"*"` to allow requests from any domain. | no
`EMAIL_HOST` | SMTP server host (e.g. for sending password reset e-mails) | yes
`EMAIL_PORT` | SMTP server port. defaults to 465 | yes
`EMAIL_HOST_USER` | SMTP server username | yes
`EMAIL_HOST_PASSWORD` | SMTP server password | yes
`EMAIL_USE_TLS` | Boolean, whether to use TLS for sending e-mails. Defaults to true  | no
`DEFAULT_FROM_EMAIL` | "From" address for automated e-mails | yes
`THUMBNAIL_CACHE_CONFIG` | Dictionary with settings for the thumbnail cache. See [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for possible settings. | no

### Settings only for PostgreSQL backend database

This is required if you've configured your Gramps database to work with the [PostgreSQL addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL).

Key | Description | Set from environment
----|-------------|---------------------
`POSTGRES_USER` | The user name for the database connection | yes
`POSTGRES_PASSWORD` | The password for the database user | yes

### Settings only during development

Key | Description | Set from environment
----|-------------|---------------------
`DISABLE_AUTH` | If `True`, disable the authentication system. **Warning: never** use this in a production environment, as it will allow read and write access from the public! | no

## Example configuration file

A minimal configuration file for production could look like this:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # your SMPT password
DEFAULT_FROM_EMAIL="gramps@example.com"
```
