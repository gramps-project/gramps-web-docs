# Server Configuration

Using the default Docker image, all necessary configuration can be made from the browser. However, depending on the deployment, it can be necessary to customize the server configuration.

This page lists all methods to change the configuration and all existing configuration options.

## Configuration file vs. environment variables

For the settings, you can either use a configuration file or environment variables.

When you use the [Docker Compose based setup](Deployment.md), you can include a configuration file by adding the following list item under the `volumes:` key in the `grampsweb:` block:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
where `/path/to/config.cfg` is the path to the config file in your server's file system (the right-hand side refers to the path in the container and must not be changed).

When using environment variables,

- prefix every setting name with `GRAMPSWEB_` to obtain the name of the environment variable
- Use double underscores for nested dictionary settings, e.g `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` will set the value of the `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` config option

## Existing configuration settings
The following configuration options exist.

### Required settings

Key | Description 
----|-------------
`TREE` | The name of the family tree database to use. Show available trees with `gramps -l`. If a tree with this name does not exist, a new empty one will be created.
`SECRET_KEY` | The secret key for flask. The secret must not be shared publicly. Changing it will invalidate all access tokens

!!! info
    You can generate a secure secret key e.g. with the command

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Optional settings

Key | Description 
----|-------------
`MEDIA_BASE_DIR` | Path to use as base directory for media files, overriding the media base directory set in Gramps. When using [S3](s3.md), must have the form `s3://<bucket_name>`
`SEARCH_INDEX_DIR` | Path for the full-text search index. Defaults to `indexdir` relative to the path where the script is run
`STATIC_PATH` | Path to serve static files from (e.g. a static web frontend)
`BASE_URL` | Base URL where the API can be reached (e.g. `https://mygramps.mydomain.com/`). This is necessary e.g. to build correct passwort reset links
`CORS_ORIGINS` | Origins where CORS requests are allowed from. By default, all are disallowed. Use `"*"` to allow requests from any domain.
`EMAIL_HOST` | SMTP server host (e.g. for sending password reset e-mails)
`EMAIL_PORT` | SMTP server port. defaults to 465
`EMAIL_HOST_USER` | SMTP server username
`EMAIL_HOST_PASSWORD` | SMTP server password
`EMAIL_USE_TLS` | Boolean, whether to use TLS for sending e-mails. Defaults to true 
`DEFAULT_FROM_EMAIL` | "From" address for automated e-mails
`THUMBNAIL_CACHE_CONFIG` | Dictionary with settings for the thumbnail cache. See [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) for possible settings.
`CELERY_CONFIG` | Settings for the Celery background task queue. See [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) for possible settings.

### Settings only for PostgreSQL backend database

This is required if you've configured your Gramps database to work with the [PostgreSQL addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL).

Key | Description 
----|-------------
`POSTGRES_USER` | The user name for the database connection
`POSTGRES_PASSWORD` | The password for the database user


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
EMAIL_HOST_PASSWORD="..." # your SMTP password
DEFAULT_FROM_EMAIL="gramps@example.com"
```
