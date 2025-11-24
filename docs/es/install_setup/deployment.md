# Desplegando Gramps Web con Docker

La opción más conveniente para alojar Gramps Web en tu propio servidor (o servidor virtual) es con Docker Compose.

Asumiremos que Docker y Docker Compose ya están instalados en tu sistema. Puedes usar Windows, Mac OS o Linux como sistema anfitrión. Las arquitecturas soportadas incluyen no solo x86-64 (sistemas de escritorio), sino también sistemas ARM como una Raspberry Pi, que puede servir como un servidor web de bajo costo, pero lo suficientemente potente.

!!! note
    No necesitas instalar Gramps en el servidor ya que está contenido en la imagen de Docker.


## Paso 1: Configuración de Docker

Crea un nuevo archivo en el servidor llamado `docker-compose.yml` e inserta el siguiente contenido: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

Esto generará seis volúmenes nombrados para asegurarse de que todos los datos relevantes persistan al reiniciar el contenedor.

!!! warning
    Lo anterior hará que la API esté disponible en el puerto 80 de la máquina anfitriona **sin protección SSL/TLS**. Puedes usar esto para pruebas locales, pero no lo expongas directamente a Internet, ¡es completamente inseguro!

## Paso 2: Asegurar el acceso con SSL/TLS

La API web **debe** ser servida al internet público a través de HTTPS. Hay varias opciones, por ejemplo:

- Usar un hosting de Docker que incluya SSL/TLS automáticamente
- Usar un Proxy Inverso Nginx con un certificado de Let's Encrypt

Consulta [Docker con Let's Encrypt](lets_encrypt.md) para saber cómo configurar lo primero.

Si planeas usar Gramps Web solo en tu red local, puedes omitir este paso.

## Paso 3: Iniciar el servidor

Ejecuta

```
docker compose up -d
```

En la primera ejecución, la aplicación mostrará un asistente de primer uso que te permitirá

- Crear una cuenta para el usuario propietario (admin)
- Establecer algunas opciones de configuración necesarias
- Importar un árbol genealógico en formato XML de Gramps (`.gramps`)

## Paso 4: Subir archivos multimedia

Hay varias opciones para subir archivos multimedia.

- Al usar archivos almacenados en el mismo servidor que Gramps Web, puedes montar un directorio en el contenedor de Docker en lugar de usar un volumen nombrado, es decir, `/home/server_user/gramps_media/:/app/media` en lugar de `gramps_media:/app/media`, y subir tus archivos multimedia allí.
- Al usar archivos multimedia [alojados en S3](s3.md), puedes usar el complemento S3 Media Uploader.
- La opción posiblemente más conveniente es usar [Gramps Web Sync](../administration/sync.md).
