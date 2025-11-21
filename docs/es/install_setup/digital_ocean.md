# Gramps Web DigitalOcean 1-Click App

En lugar de [configurar Gramps Web tú mismo](deployment.md), también puedes utilizar la [Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean aloja la versión de demostración de Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="Insignia de Referencia de DigitalOcean" /></a>

Como parte del procedimiento de configuración, deberás registrarte para obtener una cuenta con DigitalOcean y seleccionar un plan de pago para el "droplet" (máquina virtual) a utilizar.

Se podría argumentar que esta es actualmente la forma más sencilla de desplegar tu propia instancia de Gramps Web autoalojada, asegurada con SSL, sin utilizar tu propio hardware.

!!! info
    Ten en cuenta que estarás pagando a DigitalOcean por los servicios de alojamiento. El proyecto de código abierto Gramps no proporciona soporte pago.

## Paso 1: Crear una cuenta en DigitalOcean

Crea una cuenta en [DigitalOcean](https://www.digitalocean.com/) si aún no tienes una.

## Paso 2: Crear el droplet

- Ve a [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) y haz clic en "Crear Droplet de Gramps Web".
- Elige un plan con al menos 2 GB de RAM.
- Configura la autenticación para tu droplet.
- Haz clic en "Crear Droplet".

!!! info
    Puede que necesites esperar hasta diez minutos para que la 1-Click App instale la última versión de `docker-compose`.
    Usar la última versión de `docker-compose` puede mitigar errores que hacen referencia a `firstlogin.sh`. 

## Paso 3: Configurar un nombre de dominio

Necesitarás un nombre de dominio (o subdominio). Si posees un dominio, apúntalo a la dirección IP de tu droplet. De lo contrario, podrías utilizar un servicio gratuito como [DuckDNS](https://www.duckdns.org/).

## Paso 4: Iniciar sesión en tu droplet

Conéctate por SSH a tu droplet. Deberías ver el mensaje "¡Bienvenido a la configuración de la aplicación Gramps Web DigitalOcean 1-click!". Si este no es el caso, espera unos minutos y vuelve a intentarlo (la instalación aún no ha terminado).

El script de configuración te pedirá el nombre de dominio (por ejemplo, `mygrampswebinstance.duckdns.org`) y una dirección de correo electrónico (necesaria para el certificado de Let's Encrypt).

Cuando esto esté hecho, espera a que la configuración se complete en segundo plano.

## Paso 5: Lanzar Gramps Web

Tu instancia de Gramps Web ahora debería ser accesible en la raíz de tu dominio, con un certificado SSL válido, y debería mostrar el asistente de primer uso.
