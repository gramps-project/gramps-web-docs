# Registros privados

Cualquier registro en el árbol puede ser marcado como privado. Junto con los [roles de usuario](../install_setup/users.md#user-roles), esto decide quién ve qué.

## Quién puede ver qué

Gramps Web nunca está abierto al público: solo los usuarios con una cuenta pueden ver algo. "Público" en Gramps simplemente significa "no privado", es decir, visible para cada usuario que haya iniciado sesión en el árbol.

| Rol | Registros públicos | Registros privados |
|---|---|---|
| Invitado | ver | – |
| Miembro | ver | ver |
| Colaborador | ver, añadir | ver, añadir |
| Editor, Propietario, Administrador | ver, añadir, editar, eliminar | ver, añadir, editar, eliminar |

Para los invitados, los registros privados no existen: se omiten de páginas, listas, resultados de búsqueda, gráficos, informes, exportaciones y respuestas del asistente de IA. Esto se aplica donde el servidor lee la base de datos, no ocultando cosas en la aplicación, por lo que un invitado no puede acceder a datos privados de ninguna otra manera.

Las cuentas que aún no han sido aprobadas (después de la [autoregistración](registration.md)) no pueden iniciar sesión en absoluto.

Así que si los familiares u otras personas con una cuenta de invitado no deben ver cierta información, márcala como privada. Si todos los usuarios de un árbol pueden ver todo, dales el rol de miembro (o superior) y no hay necesidad de marcar nada como privado.

## Las personas vivas no son privadas automáticamente

Nada se hace privado automáticamente, ni siquiera las personas que aún están vivas. Los datos de las personas vivas son visibles para los invitados hasta que los marques como privados. Esto también se aplica a los árboles importados.

Para hacer que las personas que probablemente están vivas sean privadas en Gramps Web:

1. En la lista de personas, abre el [filtro avanzado](lists.md#advanced-filter) y añade la condición "Personas probablemente vivas" (deja la fecha vacía para hoy). Aplica el filtro.
2. Haz clic en **Seleccionar**, marca la casilla en el encabezado y elige **Seleccionar todo**.
3. Elige la acción **Privacidad** y marca los registros como privados.

"Probablemente vivas" se estima a partir de las fechas de la persona y sus familiares. Las personas sin fechas utilizables se consideran vivas. Verifica el resultado y ten en cuenta que la estimación puede cambiar a medida que añades datos.

Marcar a una persona como privada oculta a la persona, pero no sus eventos, notas, medios o familias – ver más abajo. Gramps Desktop tiene más herramientas para establecer la privacidad de muchos registros relacionados a la vez, que puedes usar con el [complemento de sincronización](../administration/sync.md).

Las personas que mueren más tarde tampoco se vuelven públicas automáticamente. Si deseas eso, depende de ti: muchos investigadores prefieren mantener la información recopilada privada durante algún tiempo.

## Leyendo los íconos de candado

Los usuarios que pueden ver datos privados ven un candado junto a los elementos privados. Hay dos tipos:

- **Candado lleno** – el registro en sí es privado. En la página de una persona, por ejemplo, un candado lleno junto a un evento significa que el evento es privado, y junto a un hijo que el hijo es privado.
- **Candado contorneado** – solo el *enlace* es privado, no el registro al que conduce. Por ejemplo, el enlace de una persona a un evento puede ser privado mientras que el evento en sí es público. El evento está entonces oculto de la página de esa persona pero sigue siendo visible en otros lugares, como en las páginas de otros participantes o en la lista de eventos.

Si tanto el registro como su enlace son privados, se muestra el candado lleno.

La misma distinción se aplica a los hijos (el hijo o el enlace del hijo a la familia), asociaciones, enlaces de repositorio de una fuente y medios en una galería. Nombres, atributos, direcciones y URLs pertenecen a su registro y solo tienen el candado lleno.

## Haciendo algo privado

Necesitas permisos de edición para cambiar la privacidad.

- **Un registro completo**: abre su página, entra en modo de edición y haz clic en el botón de candado en la barra de herramientas.
- **Parte de un registro** – un nombre alternativo, atributo, dirección, URL, asociación, enlace de hijo o enlace de repositorio: abre el diálogo de edición de ese elemento y activa el interruptor **Privado**. El nombre principal no tiene interruptor, ya que de lo contrario la persona aparecería como "Privada".
- **Un evento de la página de una persona o familia**: el diálogo de edición del evento tiene un interruptor de privacidad para el evento en sí. Si el evento se comparte con otras personas, solo se vuelve editable después de **Editar para todos**, ya que es privado para todos ellos.
- **El enlace de una persona a un evento**: en la página del evento, abre la fila del participante en modo de edición. El interruptor de privacidad allí se aplica solo al enlace de ese participante, por lo que el evento permanece visible para los otros participantes.
- **Un objeto de medios en una galería**: en modo de edición, haz clic en el candado en la esquina de la ficha.
- **Muchos registros a la vez**: selecciónalos en una lista y usa la acción **Privacidad**, consulta [Listas](lists.md#tags-and-privacy).

Para verificar qué registros en una lista son privados, activa la columna **Privacidad** en el selector de columnas de la lista.

## Cosas a tener en cuenta

- Hacer un registro privado no hace que los registros a los que se vincula sean privados. Si una persona es privada, sus eventos, las familias a las que pertenece y las notas adjuntas a ellos siguen siendo visibles a menos que sean privadas por sí mismas. Usa el filtro avanzado o la columna **Privacidad** para verificar registros relacionados.
- Hacer que una familia o evento sea privado lo oculta, pero no a las personas en él.
- [Coincidencias de ADN y datos de Y-DNA](dna-matches.md#private-matches) tienen su propio interruptor **Privado** en sus diálogos.
- Las exportaciones y archivos de medios realizados por un usuario que no puede ver datos privados no contienen registros o archivos privados.
- La privacidad es una característica de Gramps, por lo que los registros marcados como privados en Gramps Desktop son privados en Gramps Web también, y viceversa.
