# Aplicación Gramps Web de DigitalOcean con instalación en un clic

En lugar de [configurar Gramps Web tú mismo](deployment.md), también puedes usar la [aplicación Gramps Web de DigitalOcean con instalación en un clic](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). DigitalOcean aloja la versión de demostración de Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="Insignia de referencia de DigitalOcean" /></a>

Como parte del procedimiento de configuración, tendrás que crear una cuenta en DigitalOcean y seleccionar un plan de pago para el «droplet» (máquina virtual) que utilizarás.

Podría decirse que esta es actualmente la forma más sencilla de implementar tu propia instancia de Gramps Web, autoalojada y protegida con SSL, sin utilizar tu propio hardware.

!!! info
    Ten en cuenta que pagarás a DigitalOcean por los servicios de alojamiento. El proyecto de código abierto Gramps no ofrece soporte de pago.

## Paso 1: Crea una cuenta de DigitalOcean

Crea una cuenta en [DigitalOcean](https://www.digitalocean.com/) si todavía no tienes una.

## Paso 2: Crea el droplet

- Ve a [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) y haz clic en «Create Gramps Web Droplet».
- Elige un plan con al menos 2 GB de RAM.
- Configura la autenticación en tu droplet
- Haz clic en «Create Droplet»

## Paso 3: Configura un nombre de dominio

Necesitarás un nombre de dominio (o subdominio). Si eres propietario de un dominio, apúntalo a la dirección IP de tu droplet. De lo contrario, puedes usar un servicio gratuito como [DuckDNS](https://www.duckdns.org/).

## Paso 4: Inicia sesión en tu droplet

Conéctate a tu droplet mediante SSH. Deberías ver el mensaje «Welcome to the Gramps Web DigitalOcean 1-click app setup!». Si no es así, espera unos minutos e inténtalo de nuevo (la instalación todavía no ha terminado).

El script de configuración te pedirá el nombre de dominio (por ejemplo, `mygrampswebinstance.duckdns.org`) y una dirección de correo electrónico (necesaria para el certificado de Let's Encrypt). De forma opcional, también te pedirá la configuración SMTP que Gramps Web utiliza para enviar correos electrónicos, por ejemplo, para restablecer contraseñas; deja vacío el host SMTP para omitir este paso.

Cuando hayas terminado, espera a que la configuración se complete en segundo plano

## Paso 5: Inicia Gramps Web

Tu instancia de Gramps Web debería estar disponible en la raíz de tu dominio, con un certificado SSL válido, y debería mostrar el asistente de primera ejecución.

## Cambiar la configuración más adelante

El script de configuración almacena la URL base y la configuración del correo electrónico en el archivo `/root/letsencrypt.env` como [opciones de configuración](configuration.md) con el prefijo `GRAMPSWEB_`, por ejemplo:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Para añadir o cambiar la configuración, edita este archivo en el droplet y aplica el cambio con

```bash
cd /opt/grampsweb && docker compose up -d
```
