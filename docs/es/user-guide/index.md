---
hide:
  - toc
---

# Guía del Usuario

Esta sección documenta las características disponibles para los usuarios de Gramps Web.

!!! note "¿No ves todas las funciones?"
    Gramps Web utiliza un sistema de permisos basado en roles. Algunas funciones, como editar datos, gestionar etiquetas o ver registros privados, solo están disponibles para usuarios con permisos suficientes. Puedes verificar tu rol actual en [Configuración del Usuario](settings.md). Si necesitas más acceso, contacta a tu propietario del árbol o administrador. Consulta [Sistema de Usuarios](../install_setup/users.md) para una descripción de todos los roles.

## Navegando por la interfaz

### Navegación principal

La barra lateral (o menú hamburguesa en móvil) es la forma principal de moverse entre secciones:

- **Inicio** – el panel de control (ver más abajo)
- **Blog** – historias de historia familiar escritas como publicaciones de blog
- **Árbol Familiar** – gráficos de árbol interactivos
- **Línea de Tiempo** – vista cronológica de eventos a través del árbol (requiere una versión suficientemente reciente de la API de Gramps Web)
- **Mapa** – vista geográfica de lugares en el árbol
- **ADN** – herramientas de análisis de coincidencias de ADN
- **Listas** – explorar todos los objetos de cada tipo: Personas, Familias, Eventos, Lugares, Fuentes, Citaciones, Repositorios, Notas
- **Medios** – explorar todos los archivos multimedia (fotos, documentos, etc.)
- **Asistente** – asistente de chat AI (si está habilitado por el administrador)
- **Historial** – objetos cambiados recientemente
- **Marcadores** – tus marcadores guardados
- **Tareas** – tareas de investigación
- **Informes** – generar informes
- **Exportar** – exportar el árbol familiar
- **Revisiones** – historial completo de transacciones (visible para miembros y superiores)

!!! note
    Las etiquetas ya no se gestionan desde la barra lateral; la gestión de etiquetas se ha trasladado a [Configuración de Administración](../administration/settings.md#tags) (solo Propietario/Administrador). Consulta [Etiquetas](tags.md) para ver cómo se utilizan las etiquetas.

### Barra de aplicaciones superior

La barra en la parte superior de cada página contiene:

- **Agregar** (icono de más, visible para colaboradores y superiores) – abre un menú para crear un nuevo objeto: Persona, Familia, Evento, Lugar, Fuente, Citación, Repositorio, Nota, Objeto Multimedia o Tarea
- **Buscar** (lupa) – abre la página de búsqueda
- **Campana** – abre las [notificaciones](notifications.md), incluidos cambios de otros usuarios y tareas en segundo plano finalizadas
- **Icono de usuario** – abre el menú de configuración: Configuración del Usuario, Administración (solo propietarios), Gestionar Usuarios (solo propietarios), Información del Sistema

## La página de inicio (panel de control)

El panel de control se muestra cuando inicias sesión por primera vez. Tiene dos columnas:

**Columna izquierda:**

- **Tarjeta de persona principal** – muestra el nombre, foto (si está disponible) y datos clave de tu persona principal elegida, con un enlace a su perfil completo y navegación rápida al árbol familiar. Haz clic en el botón **Establecer Persona Principal** en la tarjeta para buscar y seleccionar a otra persona.
- **Aniversarios** – próximos cumpleaños y aniversarios del árbol, basados en la fecha de hoy.
- **Recientemente cambiado** – una lista corta de los objetos modificados más recientemente, útil para rastrear ediciones colaborativas.

**Columna derecha:**

- **Publicaciones de blog recientes** – las últimas entradas del [blog](blog.md), si existen.
- **Estadísticas** – un resumen de los conteos de objetos en el árbol (número de personas, familias, eventos, etc.).

Mientras el árbol esté vacío, el panel de control oculta los paneles que no tendrían nada que mostrar y en su lugar muestra una tarjeta de **Comenzar** para usuarios con permisos de edición: primero ofrece crear una persona o importar un archivo de árbol familiar, y una vez que existan personas, conectarlas creando una familia. La tarjeta desaparece tan pronto como el árbol contiene una familia.

Si el administrador del árbol ha configurado una **nota de página de inicio** y/o una **imagen de página de inicio**, estas se muestran de manera prominente sobre las columnas principales. La imagen aparece junto al texto de la nota cuando ambas están configuradas. Consulta [Configuración de Administración](../administration/customization.md) para saber cómo configurarlas.

!!! tip
    Si el árbol está vacío y tienes permisos de edición, el panel de control muestra un aviso de "Comenzar" con botones para agregar tu primera persona o importar un archivo de árbol familiar.

## Instalando Gramps Web como una aplicación

Gramps Web es una aplicación web progresiva (PWA), lo que significa que tu navegador puede instalarla junto a tus otras aplicaciones en lugar de mantenerla en una pestaña del navegador. Luego obtiene su propio icono y se abre en su propia ventana, sin la barra de direcciones ni las barras de herramientas del navegador.

Cómo la instalas depende de tu navegador:

- **Android (Chrome)** – abre el menú y elige "Instalar aplicación" o "Agregar a la pantalla de inicio".
- **iOS/iPadOS (Safari)** – toca el botón de compartir y elige "Agregar a la pantalla de inicio".
- **Escritorio (Chrome, Edge)** – haz clic en el icono de instalación en el extremo derecho de la barra de direcciones, o usa la entrada "Instalar" del menú del navegador.
- **Escritorio (Firefox, Safari)** – la instalación no es compatible; usa una pestaña o ventana normal del navegador.

Nada cambia en cómo funciona Gramps Web, y no se almacenan datos de manera diferente; es la misma aplicación, solo presentada como una aplicación independiente.

!!! note
    Gramps Web aún necesita acceder a tu servidor para mostrar tus datos, por lo que una aplicación instalada no te permite navegar por tu árbol familiar sin conexión.
