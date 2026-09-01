---
hide:
  - toc
---

# Guía del usuario

Esta sección documenta las características disponibles para los usuarios de Gramps Web.

!!! note "¿No ves todas las funciones?"
    Gramps Web utiliza un sistema de permisos basado en roles. Algunas funciones, como editar datos, gestionar etiquetas o ver registros privados, solo están disponibles para usuarios con permisos suficientes. Puedes verificar tu rol actual en [Configuración del usuario](settings.md). Si necesitas más acceso, contacta a tu propietario del árbol o administrador. Consulta [Sistema de usuarios](../install_setup/users.md) para una descripción de todos los roles.

## Navegando por la interfaz

### Navegación principal

La barra lateral (o menú hamburguesa en dispositivos móviles) es la forma principal de moverse entre secciones:

- **Inicio** – el panel de control (ver más abajo)
- **Blog** – historias de historia familiar escritas como publicaciones de blog
- **Árbol genealógico** – gráficos de árbol interactivos
- **Línea de tiempo** – vista cronológica de eventos a través del árbol (requiere una versión de API de Gramps Web suficientemente reciente)
- **Mapa** – vista geográfica de lugares en el árbol
- **ADN** – herramientas de análisis de coincidencias de ADN
- **Listas** – navegar por todos los objetos de cada tipo: Personas, Familias, Eventos, Lugares, Fuentes, Citas, Repositorios, Notas
- **Medios** – navegar por todos los archivos multimedia (fotos, documentos, etc.)
- **Asistente** – asistente de chat AI (si está habilitado por el administrador)
- **Historial** – objetos cambiados recientemente
- **Marcadores** – tus marcadores guardados
- **Tareas** – tareas de investigación
- **Informes** – generar informes
- **Exportar** – exportar el árbol genealógico
- **Revisiones** – historial completo de transacciones (visible para miembros y superiores)
- **Notificaciones** – notificaciones pasadas

!!! note
    Las etiquetas ya no se gestionan desde la barra lateral; la gestión de etiquetas se ha trasladado a [Configuración de administración](../administration/settings.md#tags) (solo propietario/administrador). Consulta [Etiquetas](tags.md) para ver cómo se utilizan las etiquetas.

### Barra superior de la aplicación

La barra en la parte superior de cada página contiene:

- **Agregar** (icono de más, visible para colaboradores y superiores) – abre un menú para crear un nuevo objeto: Persona, Familia, Evento, Lugar, Fuente, Cita, Repositorio, Nota, Objeto Multimedia o Tarea
- **Buscar** (lupa) – abre la página de búsqueda
- **Icono de usuario** – abre el menú de configuración: Configuración del usuario, Administración (solo propietarios), Gestionar usuarios (solo propietarios), Información del sistema

## La página de inicio (panel de control)

El panel de control se muestra cuando inicias sesión por primera vez. Tiene dos columnas:

**Columna izquierda:**

- **Tarjeta de persona en casa** – muestra el nombre, foto (si está disponible) y datos clave de tu persona en casa elegida, con un enlace a su perfil completo y navegación rápida al árbol genealógico. Haz clic en el botón **Establecer persona en casa** en la tarjeta para buscar y seleccionar a otra persona.
- **Aniversarios** – próximos cumpleaños y aniversarios del árbol, basados en la fecha de hoy.
- **Recientemente cambiado** – una lista corta de los objetos modificados más recientemente, útil para rastrear ediciones colaborativas.

**Columna derecha:**

- **Publicaciones de blog recientes** – las últimas entradas del [blog](blog.md), si existen.
- **Estadísticas** – un resumen de los conteos de objetos en el árbol (número de personas, familias, eventos, etc.).

Si el administrador del árbol ha configurado una **nota de página de inicio** y/o una **imagen de página de inicio**, estas se muestran de manera prominente sobre las columnas principales. La imagen aparece junto al texto de la nota cuando ambas están configuradas. Consulta [Configuración de administración](../administration/settings.md#customization) para saber cómo configurarlas.

!!! tip
    Si el árbol está vacío y tienes permisos de edición, el panel de control muestra un aviso de "Comenzar" con botones para agregar tu primera persona o importar un archivo de árbol genealógico.

## Instalando Gramps Web como una aplicación

Gramps Web es una aplicación web progresiva (PWA), lo que significa que tu navegador puede instalarla junto a tus otras aplicaciones en lugar de mantenerla en una pestaña del navegador. Luego obtiene su propio icono y se abre en su propia ventana, sin la barra de direcciones ni las barras de herramientas del navegador.

Cómo la instalas depende de tu navegador:

- **Android (Chrome)** – abre el menú y elige "Instalar aplicación" o "Agregar a la pantalla de inicio".
- **iOS/iPadOS (Safari)** – toca el botón de compartir y elige "Agregar a la pantalla de inicio".
- **Escritorio (Chrome, Edge)** – haz clic en el icono de instalación en el extremo derecho de la barra de direcciones, o usa la entrada "Instalar" del menú del navegador.
- **Escritorio (Firefox, Safari)** – la instalación no está soportada; usa una pestaña o ventana normal del navegador.

Nada cambia sobre cómo funciona Gramps Web, y no se almacenan datos de manera diferente; es la misma aplicación, solo presentada como una aplicación independiente.

!!! note
    Gramps Web aún necesita acceder a tu servidor para mostrar tus datos, por lo que una aplicación instalada no te permite navegar por tu árbol genealógico sin conexión.
