---
hide:
  - toc
---

# Guía del Usuario

Esta sección documenta las características disponibles para los usuarios de Gramps Web.

!!! note "¿No ves todas las funciones?"
    Gramps Web utiliza un sistema de permisos basado en roles. Algunas funciones, como editar datos, gestionar etiquetas o ver registros privados, solo están disponibles para usuarios con permisos suficientes. Puedes verificar tu rol actual en [Configuración de Usuario](settings.md). Si necesitas más acceso, contacta a tu propietario del árbol o administrador. Consulta [Sistema de Usuarios](../install_setup/users.md) para una descripción de todos los roles.

## Navegando por la interfaz

### Navegación principal

La barra lateral (o menú hamburguesa en móvil) es la forma principal de moverse entre secciones:

- **Inicio** – el panel de control (ver más abajo)
- **Blog** – historias de historia familiar escritas como publicaciones de blog
- **Árbol Familiar** – gráficos de árbol interactivos
- **Línea de Tiempo** – vista cronológica de eventos a través del árbol (requiere una versión suficientemente reciente de la API de Gramps Web)
- **Mapa** – vista geográfica de lugares en el árbol
- **ADN** – herramientas de análisis de coincidencias de ADN
- **Listas** – navegar por todos los objetos de cada tipo: Personas, Familias, Eventos, Lugares, Fuentes, Citas, Repositorios, Notas
- **Medios** – navegar por todos los archivos multimedia (fotos, documentos, etc.)
- **Asistente** – asistente de chat AI (si está habilitado por el administrador)
- **Historial** – objetos cambiados recientemente
- **Marcadores** – tus marcadores guardados
- **Tareas** – tareas de investigación
- **Informes** – generar informes
- **Exportar** – exportar el árbol familiar
- **Revisiones** – historial completo de transacciones (visible para miembros y superiores)
- **Notificaciones** – notificaciones pasadas

!!! note
    Las etiquetas ya no se gestionan desde la barra lateral; la gestión de etiquetas se ha trasladado a [Configuración de Administración](../administration/settings.md#tags) (solo propietario/administrador). Consulta [Etiquetas](tags.md) para ver cómo se utilizan las etiquetas.

### Barra superior de la aplicación

La barra en la parte superior de cada página contiene:

- **Agregar** (icono de más, visible para colaboradores y superiores) – abre un menú para crear un nuevo objeto: Persona, Familia, Evento, Lugar, Fuente, Cita, Repositorio, Nota, Objeto Multimedia o Tarea
- **Buscar** (lupa) – abre la página de búsqueda
- **Icono de usuario** – abre el menú de configuración: Configuración de Usuario, Administración (solo propietarios), Gestionar Usuarios (solo propietarios), Información del Sistema

## La página de inicio (panel de control)

El panel de control se muestra cuando inicias sesión por primera vez. Tiene dos columnas:

**Columna izquierda:**

- **Tarjeta de persona en casa** – muestra el nombre, foto (si está disponible) y datos clave de tu persona en casa elegida, con un enlace a su perfil completo y navegación rápida al árbol familiar. Haz clic en el botón **Establecer Persona en Casa** en la tarjeta para buscar y seleccionar a otra persona.
- **Aniversarios** – próximos cumpleaños y aniversarios del árbol, basados en la fecha de hoy.
- **Recientemente cambiado** – una lista corta de los objetos modificados más recientemente, útil para rastrear ediciones colaborativas.

**Columna derecha:**

- **Publicaciones recientes del blog** – las últimas entradas del [blog](blog.md), si existen.
- **Estadísticas** – un resumen de los conteos de objetos en el árbol (número de personas, familias, eventos, etc.).

Si el administrador del árbol ha configurado una **nota de página de inicio** y/o una **imagen de página de inicio**, estas se muestran de manera destacada sobre las columnas principales. La imagen aparece junto al texto de la nota cuando ambos están configurados. Consulta [Configuración de Administración](../administration/settings.md#customization) para saber cómo configurar esto.

!!! tip
    Si el árbol está vacío y tienes permisos de edición, el panel de control muestra un aviso de "Comenzar" con botones para agregar tu primera persona o importar un archivo de árbol familiar.
