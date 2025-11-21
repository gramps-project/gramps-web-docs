# Configuración de TrueNAS

Esta guía explica cómo configurar Gramps Web en TrueNAS Community Edition 25.04.

!!! warning
    Esta guía está destinada a TrueNAS Community Edition 25.04 o posterior, que introdujo un nuevo sistema de aplicaciones basado en Docker Compose. No se aplica a versiones anteriores de TrueNAS.

## Requisitos previos

- TrueNAS Community Edition 25.04 o posterior
- Familiaridad básica con la interfaz web de TrueNAS
- Un conjunto de datos para almacenar los datos de Gramps Web

## Descripción general

TrueNAS Community Edition 25.04 introdujo un nuevo sistema de aplicaciones basado en Docker Compose que reemplaza el enfoque anterior basado en Helm chart. Esta guía te guiará a través de la creación de una aplicación personalizada para Gramps Web utilizando Docker Compose.

## Paso 1: Preparar el almacenamiento

1. Navega a **Conjuntos de datos** en la interfaz web de TrueNAS
2. Crea un nuevo conjunto de datos para Gramps Web (por ejemplo, `grampsweb`). Toma nota de la ruta completa a este conjunto de datos, por ejemplo, `/mnt/storage/grampsweb`, ya que la necesitarás más adelante.

Crea subdirectorios para los diversos componentes:
- `users` - Base de datos de usuarios
- `database` - Archivo(s) de base de datos de Gramps
- `media` - Archivos multimedia

## Paso 2: Crear la aplicación Docker Compose

1. Navega a **Aplicaciones** en la interfaz web de TrueNAS
2. Haz clic en **Descubrir Aplicaciones**
3. Busca "Gramps Web" y haz clic en él
4. Haz clic en "Instalar"

Esto te llevará a la página de configuración de la aplicación.

## Paso 3: Configurar la aplicación

### Configuración de Gramps Web

- **Zona horaria:** Establece tu zona horaria local (por ejemplo, `Europe/Berlin`)
- **Contraseña de Redis:** Establece una contraseña para Redis. Esto solo será utilizado internamente por la aplicación.
- **Deshabilitar telemetría:** por favor, deja esta casilla sin marcar – consulta [aquí para más detalles](telemetry.md).
- **Clave secreta:** es crucial que establezcas esto en un valor fuerte y único. Consulta [configuración del servidor](configuration.md#existing-configuration-settings) para obtener instrucciones sobre cómo generar una clave aleatoria.
- **Variables de entorno adicionales:** Necesitarás establecer todas las [opciones de configuración](configuration.md) adicionales como variables de entorno precedidas por `GRAMPSWEB_`. Por favor, revisa la [documentación de configuración](configuration.md) en detalle – por ejemplo, el hecho de que los valores booleanos deben establecerse como `true` o `false` (todo en minúsculas) en el caso de las variables de entorno, un error común.

Por favor, **al menos** establece el `GRAMPSWEB_BASE_URL` a la URL a la que tu instancia de Gramps Web será accesible – esto es necesario para un funcionamiento adecuado.

También podrías querer configurar la configuración de correo electrónico en esta etapa. Si lo haces, puedes omitir el paso de configuración de correo electrónico en el asistente de incorporación. Las variables de entorno relevantes son:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Todas las configuraciones se pueden cambiar más tarde haciendo clic en "Editar" en la interfaz de Aplicaciones de TrueNAS.

### Configuración de almacenamiento

- **Almacenamiento de usuarios:** Selecciona la ruta al directorio `users` que creaste anteriormente.
- **Almacenamiento de índice:** Puedes dejar la configuración predeterminada "ixVolume (Conjunto de datos creado automáticamente por el sistema)"
- **Almacenamiento de caché de miniaturas:** Puedes dejar la configuración predeterminada "ixVolume (Conjunto de datos creado automáticamente por el sistema)"
- **Almacenamiento de caché:** Puedes dejar la configuración predeterminada "ixVolume (Conjunto de datos creado automáticamente por el sistema)"
- **Almacenamiento multimedia:** Selecciona la ruta al directorio `media` que creaste anteriormente.
- **Almacenamiento de base de datos de Gramps:** Selecciona la ruta al directorio `database` que creaste anteriormente.

### Configuración de recursos

Te recomendamos que asignes al menos 2 CPUs y 4096 MB de RAM para asegurar un funcionamiento fluido.

## Paso 4: Acceder a Gramps Web

Una vez que la aplicación esté desplegada, puedes acceder a Gramps Web haciendo clic en el botón "Interfaz Web" en la interfaz de Aplicaciones de TrueNAS. Deberías ver el asistente de incorporación "Bienvenido a Gramps Web".

Si deseas permitir que los usuarios accedan a tu interfaz de Gramps Web, **no** expongas la aplicación directamente a Internet, sino procede al siguiente paso.

## Paso 5: Configurar un proxy inverso

Para exponer de forma segura tu instancia de Gramps Web a los usuarios, se recomienda configurar un proxy inverso. Esto te permite gestionar certificados SSL/TLS y controlar el acceso.

La opción más fácil es utilizar la aplicación oficial TrueNAS Nginx Proxy Manager. Busca la aplicación en la interfaz de Aplicaciones de TrueNAS e instálala. Puedes dejar todas las configuraciones en sus valores predeterminados, pero te recomendamos que establezcas una variable de entorno adicional: `DISABLE_IPV6` con el valor `true` para evitar posibles problemas relacionados con IPv6.

Una vez desplegado, abre la interfaz web de Nginx Proxy Manager y crea un nuevo host proxy con la siguiente configuración:

- Esquema: `http`
- Nombre de host / IP de reenvío: el nombre de host de tu servidor TrueNAS (por ejemplo, `truenas`)
- Puerto de reenvío: el puerto asignado a tu aplicación Gramps Web (consulta la interfaz de Aplicaciones de TrueNAS para el puerto exacto)
- En la pestaña "SSL", marca "Forzar SSL"
- En "Certificados SSL", selecciona "Agregar certificado SSL" > "Let's Encrypt" para crear un nuevo certificado Let's Encrypt para tu dominio.

Consulta la [documentación de Nginx Proxy Manager](https://nginxproxymanager.com/guide/) para más detalles sobre cómo configurar tu enrutador y obtener certificados SSL.
