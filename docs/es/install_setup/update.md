# Actualizar Gramps Web

Si estás utilizando uno de los métodos de instalación basados en Docker Compose, actualizar Gramps Web a la última versión es simple. En la carpeta donde se encuentra tu `docker-compose.yml`, ejecuta los siguientes comandos

```bash
docker compose pull
docker compose up -d
```

Para saltos de versión menores de [Gramps Web API](https://github.com/gramps-project/gramps-web-api), esto es todo lo que se necesita. Sin embargo, sigue las [notas de la versión de Gramps Web API](https://github.com/gramps-project/gramps-web-api/releases), ya que podría haber cambios incompatibles que requieran atención adicional o cambios de configuración.

Ten en cuenta que la imagen docker por defecto `grampsweb:latest` siempre combina la última versión de la API con la última versión del frontend. Si deseas actualizar los dos componentes por separado - lo cual es posible - se necesita una configuración más compleja de la que se describe aquí.
