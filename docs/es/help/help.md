---
hide:
  - navigation
---

Si te encuentras con problemas o necesitas ayuda con Gramps Web, por favor elige una de las siguientes opciones.

[Foro :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Problemas de backend :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Problemas de frontend :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Consulta a continuación algunas pautas sobre por dónde empezar.

## Hacer preguntas

El foro oficial de Gramps Discourse tiene una [categoría separada para Gramps Web](https://gramps.discourse.group/c/gramps-web/). Por favor, utilízala para hacer cualquier pregunta que puedas tener sobre Gramps Web, por ejemplo:

- Preguntas sobre el uso de Gramps Web
- Preguntas sobre la configuración de Gramps Web
- Solución de problemas en una implementación de Gramps Web
- Ideas sobre mejoras para Gramps Web
- ...

## Informar problemas

Si encuentras un problema que crees que es un error en Gramps Web, por favor infórmalo a través de GitHub.

Hay dos repositorios de GitHub separados para el código utilizado en Gramps Web, uno para la interfaz de usuario (“frontend”) y otro para el código del servidor (“backend”):

- [Problemas de frontend](https://github.com/gramps-project/gramps-web/issues)
- [Problemas de backend](https://github.com/gramps-project/gramps-web-api/issues)

Si no estás seguro de dónde presentar un problema, no te preocupes y simplemente elige cualquiera de los dos; los mantenedores podrán transferir el problema si es necesario.

En cualquier caso, por favor incluye siempre la siguiente información en tu informe:

- Detalles sobre tu configuración (por ejemplo, un archivo docker-compose con valores sensibles redactados, o si estás utilizando una versión alojada, como Grampshub, o una imagen preconfigurada, como DigitalOcean)
- Información de la versión. Para obtenerla, ve a la pestaña "Información del sistema" en la página de Configuración en Gramps Web y copia/pega los valores en el cuadro, que deberían verse algo así:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## Sugerir mejoras

Para ideas generales y discusión sobre futuras mejoras, siéntete libre de abrir una discusión en el [foro](https://gramps.discourse.group/c/gramps-web/). También puedes querer revisar las páginas de problemas (ver enlaces arriba) para ver si una característica particular ya está planificada o en desarrollo.

Para mejoras específicas con un alcance limitado, siéntete libre de abrir directamente un problema con una solicitud de función en el repositorio de GitHub de frontend o backend apropiado.
