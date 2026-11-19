---
hide:
  - toc
  - navigation
---

# Características

Gramps Web es una aplicación web para genealogía colaborativa. Está construida sobre [Gramps](https://gramps-project.org/), el programa de genealogía de código abierto, y trabaja con los mismos datos. Puedes ejecutarla en tu propio servidor o utilizar un proveedor de alojamiento.

[Prueba la demostración](#demo){ .md-button .md-button--primary } [Comienza](../install_setup/setup.md){ .md-button }

## Explora tu árbol genealógico { .feature-group }

![Gráfico de abanico que muestra siete generaciones de antepasados](screenshots/fan.png){ align=right width="400"}

### Gráficos interactivos del árbol genealógico

Navega por tu árbol genealógico como un árbol de antepasados, árbol de descendientes, gráfico de reloj de arena, gráfico de relaciones o gráfico de abanico, con gráficos interactivos de alta calidad y un número configurable de generaciones.

Pasa el cursor sobre cualquier persona para ver una tarjeta de vista previa con sus datos clave, y salta directamente del gráfico a la página de detalle completo.

<div style="clear:both;"></div>

---

![Línea de tiempo de eventos familiares entre las décadas de 1940 y 1970](screenshots/timeline.png){ align=left width="400"}

### Línea de tiempo cronológica

Ve cada evento en tu árbol genealógico dispuesto en una línea de tiempo horizontal y ampliable. Desplázate y acércate a través de los siglos, luego filtra hasta una sola persona – o a todos sus antepasados o descendientes – o a todo lo que ocurrió en un lugar.

Consulta [Línea de tiempo](../user-guide/timeline.md).

<div style="clear:both;"></div>

---

![Mapa de Londres con un lugar seleccionado, mostrando su foto y eventos](screenshots/map.png){ align=right width="400"}

### Mapa interactivo

Muestra todos los lugares en tu árbol en un mapa interactivo y buscable. Busca nuevos lugares directamente en OpenStreetMap al crear un lugar, traza geográficamente a las personas en tu base de datos y sigue la vida de una sola persona conectando sus eventos con líneas en el mapa.

<div style="clear:both;"></div>

---

![Londres en la capa de OpenHistoricalMap, con el control deslizante de tiempo ajustado a 1707](screenshots/ohm.png){ align=left width="400"}

### Mapas históricos

Convierte un mapa histórico almacenado como un objeto multimedia en Gramps en una superposición de mapa personalizada.

También puedes cambiar a los mapas vectoriales históricos del proyecto [OpenHistoricalMap](https://www.openhistoricalmap.org/). Usa el control deslizante de tiempo para desplazarte a través de la evolución de los lugares en tu historia familiar y mostrar los lugares donde vivieron los antepasados o donde ocurrieron eventos.

<div style="clear:both;"></div>

---

![Resultados de búsqueda para "Albert" en personas, eventos y medios](screenshots/search.png){ align=right width="400"}

### Encuentra cualquier cosa

El motor de búsqueda de texto completo cubre todos los tipos de objetos de Gramps, incluyendo el contenido de notas de texto, y admite comodines y operadores lógicos.

Para consultas precisas, las vistas de lista de objetos ofrecen un modo de filtro avanzado basado en el [Gramps Object Query Language](../user-guide/goql.md), junto con filtros rápidos por texto, etiqueta y privacidad.

Desde la página de cualquier persona, [Búsqueda Externa](../user-guide/external-search.md) abre una búsqueda pre-rellenada en FamilySearch, Ancestry, CompGen y otros sitios – y puedes añadir los tuyos.

<div style="clear:both;"></div>

## Construir e investigar { .feature-group }

![Árbol de antepasados en modo de edición con el diálogo para añadir un miembro de la familia](screenshots/tree-edit.png){ align=left width="400"}

### Construye tu árbol directamente en el gráfico

Cambia la vista del árbol a modo de edición y haz crecer tu árbol genealógico sin salir del gráfico. Cada tarjeta de persona tiene un botón **+** para añadir un padre, madre, hijo o cónyuge – ya sea vinculando a alguien que ya está en tu base de datos o creando una persona completamente nueva en el momento. Cada cambio se guarda de inmediato.

Consulta [Editando el Árbol Familiar](../user-guide/tree-edit.md).

<div style="clear:both;"></div>

---

![El asistente de IA leyendo un certificado de nacimiento y proponiendo nuevos registros](screenshots/chat.png){ align=right width="400"}

### Asistente de IA integrado

Haz preguntas sobre tu árbol genealógico en tu propio idioma y obtén respuestas basadas en tus datos.

El asistente no solo busca: consulta directamente tu base de datos con un conjunto de herramientas, filtrando personas, eventos, familias y lugares, y calculando relaciones entre individuos. Puedes ver qué herramientas está utilizando mientras construye una respuesta, y las preguntas más largas se ejecutan como tareas en segundo plano para que puedas navegar y volver.

El asistente es opcional y necesita ser [configurado por el administrador del servidor](../install_setup/chat.md) con un proveedor de modelo de IA.

<div style="clear:both;"></div>

---

![Navegador de cromosomas mostrando los segmentos de ADN compartidos de once coincidencias](screenshots/dna.png){ align=left width="400"}

### Coincidencias de ADN, navegador de cromosomas y Y-DNA

Sube datos de coincidencias de ADN de tu proveedor de pruebas de ADN, guárdalos junto a tu árbol genealógico y visualiza tus coincidencias en un navegador de cromosomas interactivo.

Los datos crudos de SNP del cromosoma Y pueden usarse para determinar el [haplogrupo Y-DNA](../user-guide/y-dna.md) más probable de una persona y mostrar sus antepasados patrilineales en el árbol del cromosoma Y humano, con estimaciones de tiempo. El análisis se ejecuta completamente en tu propio servidor – no se envían datos a ningún tercero.

<div style="clear:both;"></div>

---

![Pintura con dos personas etiquetadas y los otros rostros detectados contorneados](screenshots/tag.png){ align=right width="400"}

### Etiqueta personas en fotos con detección automática de rostros

Identifica a los antepasados en viejas fotos familiares junto con tus familiares. Los rostros se detectan automáticamente, por lo que etiquetar a una persona requiere solo dos clics.

<div style="clear:both;"></div>

---

![Lista de tareas de investigación con estado, prioridad y etiquetas](screenshots/tasks.png){ align=left width="400"}

### Aplicación de gestión de tareas integrada

Gramps Web viene con una aplicación de gestión de tareas integrada para organizar y planificar tu investigación genealógica. Asigna a cada tarea un estado, una prioridad y etiquetas, documenta tu progreso en una descripción de texto enriquecido y adjunta los medios que recopilaste en el camino.

Las tareas se almacenan como fuentes en la base de datos de Gramps, por lo que forman parte de tus datos genealógicos y pueden ser accedidas y editadas también en Gramps Desktop.

<div style="clear:both;"></div>

---

![Publicación de blog sobre la identificación de las personas en una fotografía familiar](screenshots/blog.png){ align=right width="400"}

### Blog de genealogía incluido

Resume tu investigación en forma de historias de blog con imágenes y compártelas con tus familiares. Un editor dedicado hace que escribir una nueva publicación sea sencillo. Todos los datos se almacenan en la base de datos de Gramps.

<div style="clear:both;"></div>

## Trabaja en conjunto { .feature-group }

![Lista de personas en el árbol genealógico](screenshots/list.png){ align=left width="400"}

### Niveles de privacidad y acceso de usuarios

Puedes [marcar registros como privados](../user-guide/privacy.md) – hasta un solo nombre, enlace de evento o coincidencia de ADN – y controlar qué usuarios pueden ver registros privados. Los registros privados se filtran en la capa de base de datos para máxima seguridad. Además, puedes controlar qué pueden añadir y editar los usuarios.

Los usuarios pueden iniciar sesión con una contraseña, o a través de un proveedor de identidad externo usando [OpenID Connect](../install_setup/oidc.md) – Google y Microsoft de forma predeterminada, además de proveedores personalizados como Keycloak, Authentik y Authelia.

<div style="clear:both;"></div>

---

![Una revisión mostrando los campos cambiados en un registro de persona](screenshots/revisions.png){ align=right width="400"}

### Historial de revisiones completo – con deshacer

Cada edición de tu árbol genealógico se registra. Navega por el historial completo agrupado por transacción, profundiza en cualquier cambio individual para ver exactamente qué campos se añadieron, eliminaron o modificaron, y deshacer una transacción si resulta ser un error. La página de cada objeto también tiene su propia pestaña de revisión que muestra quién lo cambió y cuándo.

Consulta [Historial de Revisiones](../user-guide/revisions.md).

<div style="clear:both;"></div>

---

![Menú Herramientas de Gramps Desktop con la entrada de Sincronización de Gramps Web](screenshots/sync.png){ align=left width="300"}

### Integración completa con Gramps Desktop

Gramps Web utiliza el mismo modelo de datos y base de datos que [Gramps Desktop](https://gramps-project.org/). Puedes navegar y editar todos los mismos [tipos de registros](https://gramps-project.org/wiki/index.php/Gramps_Data_Model): personas, familias, eventos, lugares, repositorios, fuentes, citas, objetos multimedia y notas.

Con el [complemento de Sincronización de Gramps Web](../administration/sync.md) para Gramps Desktop, puedes sincronizar tus datos en ambas direcciones, para que puedas seguir trabajando en Gramps Desktop y en Gramps Web lado a lado.

<div style="clear:both;"></div>

## Informes y exportación de datos { .feature-group }

![Informe de antepasados generado como PDF](screenshots/report.png){ align=right width="400"}

### Generar informes imprimibles

Gramps Web está construido sobre el mismo núcleo que Gramps Desktop, por lo que puedes generar casi todos los [informes](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports) que la aplicación de escritorio admite directamente desde el navegador, incluidos gráficos de relaciones o informes de libros en PDF.

<div style="clear:both;"></div>

---

![Página de exportación con la lista de formatos de archivo disponibles](screenshots/export.png){ align=left width="300"}

### Sin bloqueo – importación y exportación de datos

Importa datos en varios formatos, incluyendo Gramps XML y GEDCOM, y descarga todos tus datos en cualquier momento – datos del árbol genealógico, archivos multimedia y cuentas de usuario – para copias de seguridad o para trasladarlos a otro servidor.

Las importaciones pueden preverse como una prueba en seco antes de que se escriba nada, y una copia de seguridad completa puede restaurarse de nuevo en el árbol.

<div style="clear:both;"></div>

## Úsalo en cualquier lugar { .feature-group }

![La misma página de persona en un escritorio y en un teléfono](screenshots/mobile.png){ align=right width="400"}

### Funciona en cualquier dispositivo

Usa Gramps Web en cualquier dispositivo con un navegador web: sube fotos, crea o edita registros, o muestra tu árbol genealógico a tus familiares en la próxima reunión familiar.

Gramps Web es una aplicación web progresiva: instálala en tu pantalla de inicio o escritorio y se comporta como una aplicación nativa. En el escritorio, los [atajos de teclado](../user-guide/shortcuts.md) te llevan a cualquier lugar en un par de pulsaciones – presiona `?` para verlos todos.

<div style="clear:both;"></div>

---

![Menú de selección de idioma](screenshots/lang.png){ align=left width="300"}

### Totalmente internacionalizado

Usa la interfaz en cualquiera de más de 50 idiomas traducidos por la comunidad de Gramps.

<div style="clear:both;"></div>

## Y más

- **Notificaciones y tareas en segundo plano** – importaciones, exportaciones, informes y reconstrucciones de índices se ejecutan en segundo plano, con progreso y errores recopilados en un solo lugar
- **Etiquetas, marcadores e historial** – organiza objetos con etiquetas codificadas por colores y vuelve a lo que estabas trabajando
- **Edición masiva** – selecciona múltiples objetos en las vistas de lista para eliminarlos a la vez, o fusionar objetos duplicados
- **Vistas de lista personalizables** – elige qué columnas mostrar y filtra por texto, etiqueta o privacidad
- **Reconocimiento de texto (OCR)** – extrae texto de documentos escaneados en tu galería multimedia
- **Verificación de datos** – revisa tu árbol en busca de fechas implausibles y otros problemas de datos
- **Calendarios** – ingresa fechas en el calendario gregoriano, juliano, hebreo, republicano francés, persa, islámico o sueco
- **Hazlo tuyo** – dale a tu sitio su propio nombre, colores de tema y texto e imagen de la página de inicio

## Demostración

Para iniciar sesión en la demostración, utiliza uno de los siguientes pares de nombre de usuario/contraseña. Cada uno representa uno de los roles de usuario en Gramps Web.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

La demostración se restablece cada dos horas, por lo que cualquier cambio que realices es temporal.

[Ir a la Demostración de Inicio de Sesión](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### Gracias

La demostración es amablemente apoyada por DigitalOcean.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="Insignia de Referencia de DigitalOcean" /></a>
