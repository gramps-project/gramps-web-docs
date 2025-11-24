# Instalación / Configuración de Gramps Web

Esta sección trata sobre la instalación y configuración de Gramps Web, así como otras opciones para comenzar.

## Comenzando con Gramps Web

Gramps Web es una aplicación web que se ejecuta en un servidor y se accede a través del navegador web. Está destinada a ser accesible para usuarios autenticados a través de Internet.

Si deseas utilizar Gramps Web para tus datos de investigación genealógica, debes elegir una de las siguientes opciones:

1. Autoalojamiento en tu propio hardware
2. Autoalojamiento en la nube
3. Registrarte para una instancia alojada

Mientras que la primera opción te brinda máxima flexibilidad y control, también puede ser técnicamente desafiante.

!!! tip
    Uno de los principios principales de Gramps Web es poner a los usuarios en control de sus propios datos en todo momento, por lo que migrar datos de una instancia a otra es simple. ¡No te preocupes por quedar atrapado después de haber elegido una de las opciones!

## Autoalojamiento en tu propio hardware

La forma más conveniente de autoalojar Gramps Web es a través de Docker Compose. También proporcionamos imágenes de Docker para la arquitectura ARM, por lo que puedes ejecutar Gramps Web en una Raspberry Pi en tu sótano.

Consulta [Implementar con Docker](deployment.md) para obtener instrucciones de configuración.

## Autoalojamiento en la nube

Instalar Gramps Web puede ser más desafiante que otras aplicaciones web simples y no es compatible con proveedores de "hosting compartido" ordinarios. Puedes registrarte para un servidor virtual e instalar Gramps Web [manualmente](deployment.md).

Una opción más sencilla es utilizar una imagen de nube preinstalada. Un ejemplo es nuestra [aplicación de un clic de DigitalOcean](digital_ocean.md).

## Registrarte para una instancia alojada

Una Gramps Web alojada es la forma más fácil de comenzar con Gramps Web, ya que no se requiere instalación ni configuración.

Aquí hay una lista de proveedores de hosting dedicados para Gramps Web (la comunidad de código abierto de Gramps no se hace responsable de sus servicios):

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), ofrecido por uno de los principales colaboradores de Gramps Web

Si utilizas una opción alojada para Gramps Web, puedes omitir el resto de esta sección y saltar directamente a la sección de [Administración](../administration/admin.md).
