# Cómo Gramps organiza los datos

Gramps Web almacena un árbol genealógico no como un gráfico, sino como objetos separados: personas, familias, eventos, lugares, fuentes, y así sucesivamente, que están vinculados entre sí. Una vez que sepas cómo encajan estos objetos, ingresar datos se vuelve predecible: cualquier cosa que quieras vincular debe existir primero.

Gramps Web utiliza el mismo modelo de datos que Gramps Desktop, por lo que todo en esta página se aplica a ambos.

## Los bloques de construcción

| Objeto | Lo que representa | Ejemplos |
|---|---|---|
| Persona | Un individuo | Tú, tu abuela |
| Familia | Una pareja, sus hijos, o ambos | Tus padres y sus hijos |
| Evento | Algo que ocurrió, con una fecha y un lugar | Nacimiento, matrimonio, censo, emigración |
| Lugar | Una ubicación geográfica | Un pueblo, una parroquia, un país |
| Fuente | Un documento o colección de información | Un registro parroquial, un censo, un libro |
| Citación | Una referencia específica dentro de una fuente | Página 12, entrada 3 del registro parroquial |
| Repositorio | Donde se guarda una fuente | Un archivo, una biblioteca, un sitio web |
| Nota | Texto libre | Una transcripción, observaciones de investigación |
| Objeto multimedia | Un archivo | Una foto, un certificado escaneado |

Cada tipo de objeto tiene su propia lista en Gramps Web, consulta [Listas](lists.md).

## Personas y familias

Los padres y los hijos no están vinculados entre sí directamente, sino a través de una **familia**. Una familia tiene hasta dos parejas y cualquier número de hijos:

- Tus padres y tú están vinculados a través de la familia en la que eres un hijo.
- Tus hermanos son los otros hijos de la misma familia.
- Tú y tu cónyuge forman otra familia, en la que eres un socio, junto con tus hijos.

Una persona puede ser un hijo en una familia y un socio en varias. Cada hijo tiene una relación con cada uno de los padres, como nacimiento, adopción o hijastro, y cada familia tiene un tipo de relación, como casados o unión civil.

Por eso, "agregar padres" a una persona significa agregar a la persona como un hijo a una familia, lo cual el [gráfico del árbol](tree-edit.md) hace por ti en un solo paso.

## Eventos

Un nacimiento, muerte o matrimonio no es un campo de una persona, sino un **evento** propio, con un tipo, una fecha, un lugar y una descripción. Las personas están vinculadas a un evento con un **rol**: la persona cuyo nacimiento es tiene el rol "Primario", mientras que otra persona podría estar vinculada al mismo evento como testigo.

Los eventos que conciernen a una pareja, como un matrimonio, pertenecen a la familia en lugar de a cualquiera de los socios. Un evento también puede ser compartido por varias personas, por ejemplo, un registro de censo que enumera a todo un hogar, en lugar de ser ingresado una vez por persona.

Esto afecta la edición. El evento en sí mismo, su tipo, fecha, lugar y descripción, es el mismo para todos los vinculados a él, por lo que editar un evento compartido desde la página de una persona lo cambia para todos ellos. El diálogo de edición, por lo tanto, lista primero a los otros participantes, y los campos solo se vuelven editables después de **Editar para todos**. Lo que pertenece al vínculo de una persona con el evento, el rol, y las citaciones, notas y atributos que solo se aplican a esa persona, se editan en la página del evento, en la pestaña **Participantes** en modo de edición. Allí también puedes agregar y eliminar participantes. Por ejemplo, el rol de un padrino y la nota "firmado con una marca" pertenecen al vínculo del padrino con el bautismo, no al bautismo en sí.

## Objetos compartidos: lugares y fuentes

Los lugares, fuentes, citaciones, repositorios, notas y objetos multimedia existen por derecho propio, y cualquier número de otros objetos puede referirse al mismo. Esto tiene algunas consecuencias:

- **Crear una vez, seleccionar muchas veces.** El pueblo donde nacieron diez de tus antepasados es un lugar, seleccionado en diez eventos de nacimiento. Si corriges su nombre o coordenadas, la corrección se aplica en todas partes.
- **Créalo antes de seleccionarlo.** Los formularios en Gramps Web seleccionan lugares y fuentes que ya existen. Crea un nuevo lugar o fuente primero usando el botón **+** (Agregar) en la barra de aplicaciones superior.
- **Los lugares están anidados.** Un lugar puede estar contenido por uno más grande: un pueblo por un condado, el condado por un país, así que no tienes que repetir toda la jerarquía para cada pueblo.
- **Las fuentes y citaciones son separadas.** Una fuente es el registro parroquial en su totalidad; una citación es la entrada específica que respalda un hecho, con su página, fecha y tu confianza en ella. Muchas citaciones pueden apuntar a la misma fuente.

Si has creado accidentalmente el mismo lugar o fuente dos veces, puedes [fusionar los duplicados](lists.md#merge).

## Editando la página de un objeto

En la página de una fuente, repositorio u objeto multimedia, haz clic en el título en modo de edición para cambiarlo (para un objeto multimedia, su descripción). Presiona Enter, haz clic en ✓, o haz clic en otro lugar para guardar; presiona Escape o haz clic en ✕ para cancelar.

La mayoría de las listas en la página de un objeto mantienen el orden que les das, por ejemplo, los eventos, nombres, atributos, direcciones, citaciones, o los hijos de una familia. En modo de edición, selecciona una fila y muévela con los botones de arriba y abajo, o arrástrala a su nueva posición: con el mouse, presiona la fila y muévela; en una pantalla táctil, presiona y mantén la fila hasta que se levante. Presiona Escape mientras arrastras para cancelar. Los medios en la galería se pueden reordenar de la misma manera, consulta [Imágenes de perfil](media.md#profile-pictures).

## La Persona Principal

La Persona Principal es la persona desde la cual comienzan los gráficos del árbol genealógico y el punto de partida predeterminado para los informes. Consulta [Primer inicio de sesión](first-login.md) para saber cómo configurarlo.

!!! nota "Diferente de Gramps Desktop"
    En Gramps Desktop, la Persona Principal se almacena en la base de datos del árbol genealógico, por lo que es la misma para todos los que abren esa base de datos. Gramps Web no lo utiliza. En su lugar, la Persona Principal se almacena en tu navegador, por separado para cada árbol: no se comparte con otros usuarios, y no te sigue a otro navegador o dispositivo. Después de importar un árbol de Gramps Desktop, o cuando usas Gramps Web en otro dispositivo, tienes que configurarlo nuevamente.

## Un orden recomendado

Al ingresar una nueva familia a mano, este orden evita saltar de un formulario a otro:

1. **Lugares y fuentes.** Crea los lugares que necesitas y, si registras fuentes, la fuente de la que estás trabajando.
2. **Personas.** Agrega las personas con sus fechas y lugares de nacimiento y muerte. Esto es más rápido en el modo de edición del gráfico del árbol genealógico, que crea las familias por ti – consulta [Iniciar un nuevo árbol](start-tree.md) y [Editando el árbol genealógico](tree-edit.md).
3. **Eventos adicionales.** Abre una familia (por ejemplo, desde la pestaña Relaciones de una persona) para agregar el matrimonio, y una página de persona para agregar otros eventos.
4. **Citas.** En la pestaña de Citaciones de la fuente de la persona, evento u otro objeto que una fuente respalda, agrega una nueva citación, selecciona la fuente e ingresa la página.
5. **Notas y medios.** Adjunta transcripciones, fotos y escaneos – consulta [Agregar archivos multimedia](media.md).

## Ingresando fechas

Una fecha se ingresa como campos separados de año, mes y día, que también se pueden completar utilizando un selector de fecha. Omite las partes que no conoces: un año solo es una fecha válida. En lugar de adivinar un día exacto, describe lo que realmente sabes eligiendo el tipo de fecha con las fichas sobre los campos. Una pista debajo de las fichas explica el tipo seleccionado:

| Lo que sabes | Tipo | Ejemplo |
|---|---|---|
| La fecha exacta, o parte de ella | Regular | 12 de marzo de 1850, o solo 1850 |
| Una fecha aproximada | Acerca de | alrededor de 1850 |
| Un límite | Antes, Después | antes de 1900 |
| La fecha se encuentra en algún lugar dentro de un período | Rango | entre 1850 y 1855 (campos "Más antiguo" y "Más reciente") |
| Algo duró un período | Duración | de 1850 a 1855 |

Para una Duración, cualquiera de las dos fechas ("Desde" y "Hasta") puede dejarse vacía, por lo que "de 1850" o "hasta 1855" es una Duración con solo una fecha.

Los campos de **Calidad** y **Calendario** están bajo **Más opciones**, que se abre automáticamente cuando una fecha utiliza cualquiera de ellos. La calidad registra cómo llegaste a una fecha: "Estimado" para una suposición educada, "Calculado" para una fecha derivada de otra información, como un año de nacimiento calculado a partir de una edad al morir.

!!! advertencia "Las fechas Acerca de y estimadas cubren 50 años en cualquier dirección"
    Cuando Gramps compara fechas, trata una fecha del tipo "acerca de" – y cualquier fecha con la calidad "Estimado" – como un rango que abarca desde 50 años antes hasta 50 años después de la fecha dada. Por ejemplo, filtrar la lista de Personas para personas nacidas entre 1840 y 1860 también encuentra a una persona nacida "alrededor de 1880", porque esa fecha se considera que cubre de 1830 a 1930. De la misma manera, "antes" y "después" se consideran que alcanzan hasta 50 años antes o después de la fecha.

    Esto puede llevar a resultados sorprendentes, así que usa "acerca de" y "Estimado" solo cuando no puedas acotar la fecha. Si conoces un período más corto, un Rango como "entre 1878 y 1882" es más preciso.

El calendario te permite ingresar una fecha en el calendario utilizado en el registro original, como el calendario juliano, en lugar de convertirlo tú mismo.
