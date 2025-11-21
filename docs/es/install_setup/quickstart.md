Para probar Gramps Web en tu computadora local (Linux, Mac o Windows) sin interferir con tu instalación de Gramps Desktop, puedes usar Docker con el siguiente comando:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Esto hará que una nueva instancia vacía de Gramps Web sea accesible en [http://localhost:5055](http://localhost:5055), donde puedes crear un usuario administrador e importar un archivo XML de Gramps.

!!! info
    Dado que esta configuración simple no permite ejecutar tareas largas en un proceso separado, importar un archivo XML de Gramps grande podría fallar debido a un tiempo de espera en el asistente de primer uso.

Para usar archivos multimedia de tu computadora, puedes montar la carpeta de medios de Gramps en el contenedor con

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Ten en cuenta que esto no persistirá los cambios que realices en la base de datos cuando reinicies el contenedor. Para configurar correctamente Gramps Web, continúa leyendo sobre [Despliegue](deployment.md).
