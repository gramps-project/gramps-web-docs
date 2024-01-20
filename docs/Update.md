# Update Gramps Web

If you are using one of the installation methods based on Docker Compose, updating Gramps Web to the latest version is simple. In the folder where your `docker-compose.yml` is located, run the following commands

```bash
docker-compose pull
docker-compose up -d
```

For minor version jumps of [Gramps Web API](https://github.com/gramps-project/gramps-web-api), this is all that is needed. Do follow the [release notes of Gramps Web API](https://github.com/gramps-project/gramps-web-api/releases) though, as there could be breaking changes that require additional attention or configuration changes.

Note that the default `grampsweb:latest` docker image always combines the latest version of the API with the latest version of the frontend. If you want to upgrade the two components separately - which is possible - a more involved setup than described here is necessary.
