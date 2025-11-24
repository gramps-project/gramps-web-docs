---
hide:
  - toc
---

# Desarrollo de Gramps Web: visión general

Gramps Web es una aplicación web que consta de dos componentes que se desarrollan por separado:

- **Gramps Web API** es una API RESTful escrita en Python y basada en Flask. El código fuente está alojado en [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/). Gestiona el acceso a la base de datos y las funciones genealógicas aprovechando directamente la biblioteca Gramps de Python. Sirve como el backend de Gramps Web. Para la documentación de desarrollo, consulta [Backend](backend/index.md).
- **Gramps Web Frontend** es una aplicación web en Javascript que sirve como el frontend de Gramps Web. El código fuente está alojado en [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/). Para la documentación de desarrollo, consulta [Frontend](frontend/index.md).

Una nota sobre el versionado: Gramps Web API y el frontend de Gramps Web se versionan de manera independiente. En la actualidad, "Gramps Web" &ndash; la aplicación combinada &ndash; no tiene un número de versión separado. Ambos proyectos se adhieren a [SemVer](https://semver.org/).

Si no eres un desarrollador de Python o Javascript pero aún así te gustaría contribuir a Gramps Web, consulta [Contribuir](../contribute/contribute.md).
