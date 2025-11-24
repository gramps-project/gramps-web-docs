# Telemetría

A partir de la versión 3.2.0 de la API web de Gramps, Gramps Web envía por defecto datos de telemetría completamente anonimizados cada 24 horas a un punto final de análisis controlado por el equipo de Gramps Web. Esta página contiene información sobre los datos de telemetría recopilados, cómo se utilizan y cómo desactivarlos si se desea.

## ¿Qué datos se recopilan?

Los datos de telemetría son una pequeña carga útil en formato JSON de la siguiente forma:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Como puedes comprobar [en el código fuente](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87), los identificadores del servidor y del árbol son únicos para el servidor y el árbol, pero no contienen ninguna información personal identificable. El `timestamp` es la hora actual como un timestamp Unix.

## ¿Por qué se recopilan los datos?

Enviar un identificador único una vez al día permite al equipo de Gramps Web rastrear cuántos servidores únicos están ejecutando Gramps Web y cuántos árboles únicos se están utilizando.

Esto es importante para entender el impacto en los servicios externos que son utilizados por Gramps Web, como los mosaicos de mapas.

## ¿Cómo se recopilan los datos?

Cuando se realiza una solicitud a tu servidor de API web de Gramps, este verifica si se ha enviado telemetría en las últimas 24 horas (comprobando una clave en la caché local). Si no, se envía la carga útil anterior a un punto final que registra los datos.

El punto final de registro está alojado en Google Cloud Run y se despliega directamente desde un [repositorio de código abierto](https://github.com/DavidMStraub/cloud-run-telemetry), por lo que puedes inspeccionar cómo se procesan los datos.

## ¿Qué se hará con los datos?

Primero y ante todo, ningún dato más allá de la carga útil anonimizadas, que hipotéticamente podría ser recopilado (como la dirección IP del servidor), será utilizado por el equipo de Gramps Web.

Los IDs anonimizados y el timestamp recopilados se agregarán para producir gráficos como:

- Número de instalaciones activas de Gramps Web en función del tiempo
- Número de árboles activos de Gramps Web en función del tiempo

Estos gráficos se publicarán en el sitio de documentación de Gramps Web.

## ¿Cómo desactivar la telemetría?

Dado que los datos estadísticos son útiles para el equipo de Gramps Web y hemos asegurado que no se envían datos personales identificables, **¡agradeceríamos que no desactivaras la telemetría!**

Sin embargo, Gramps Web pone a los usuarios en pleno control, así que, por supuesto, puedes elegir desactivar la función si lo deseas.

Para hacerlo, simplemente establece la opción de configuración `DISABLE_TELEMETRY` en `True` (por ejemplo, configurando la variable de entorno `GRAMPSWEB_DISABLE_TELEMETRY` en `true` &ndash; consulta la [documentación de configuración](configuration.md) para más detalles).
