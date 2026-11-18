# Usando el Asistente de IA

La vista del **Asistente** en Gramps Web (si está habilitada en tu instalación) da acceso a un asistente de IA que responde preguntas sobre tu árbol genealógico.

!!! warning
    Al igual que con cualquier asistente de IA, las respuestas pueden ser incorrectas. Usa los enlaces en la respuesta para verificar los registros en los que se basa.

## Cómo funciona

El asistente no conoce tu árbol de antemano. Para responder a una pregunta, un modelo de lenguaje grande busca los registros que necesita, de manera similar a como lo harías tú:

- busca en el árbol con la [búsqueda de texto completo](search.md),
- filtra personas, eventos y familias por criterios como nombres, fechas, lugares o el número de hijos,
- encuentra ancestros, descendientes y otros parientes de una persona, con su relación,
- lee registros completos de personas, familias, eventos, lugares y notas.

Luego responde en función de los registros que ha encontrado, con enlaces a ellos. Mientras trabaja, se muestran las herramientas que está utilizando, para que puedas seguir el proceso. Las preguntas que tardan más se ejecutan en segundo plano; puedes navegar a otra parte y volver.

El asistente responde solo a partir de tu árbol, no del conocimiento general del modelo de lenguaje, incluso sobre personas conocidas. Si el árbol no registra algo, lo menciona, indicando información relacionada que encontró, por ejemplo, en una nota. Solo ve lo que tienes permitido ver: los enlaces a registros privados se muestran como texto plano para los usuarios que no pueden visualizarlos.

Las preguntas de seguimiento mantienen el contexto de preguntas anteriores en la misma conversación, por lo que puedes preguntar "¿Y cuándo murió?" después de preguntar sobre una persona.

## Lo que puedes preguntar

- **Hechos sobre personas**: "¿Cuándo nació Mary Smith?" o "¿Cuáles son los nombres de los hijos de John Doe?"
- **Parientes**: "¿Quiénes son los abuelos de Jane Smith?" o "¿Qué descendientes de Johann Meyer emigraron a América?"
- **Búsquedas con criterios**: "¿Quién nació en Londres después de 1850?", "Lista de matrimonios entre 1920 y 1950", o "¿Qué parejas tuvieron cinco o más hijos?"
- **Lugares**: "¿Qué eventos ocurrieron en París?" o "¿Quién nació en Dinamarca?" – se incluyen lugares dentro de un lugar más grande.
- **Notas**: "¿Qué dicen las notas sobre la granja de la familia Meyer?"

Las preguntas que necesitan todo el árbol a la vez, como "¿Cuál es el nombre de pila más común?", funcionan menos bien, ya que el asistente solo ve un número limitado de registros por búsqueda.

## Preguntando sobre imágenes

Si el administrador del servidor lo ha habilitado, el aviso tiene un botón para adjuntar imágenes. También puedes pegar una imagen o soltar archivos de imagen en el aviso. Se pueden adjuntar hasta cuatro imágenes a una pregunta, por ejemplo, un escaneo de un registro de iglesia para preguntar "¿Quién se menciona en esta entrada, y están en mi árbol?"

Las imágenes solo se envían con la pregunta a la que están adjuntas. Las preguntas de seguimiento pueden referirse a lo que el asistente dijo sobre ellas, pero no a las imágenes en sí, por lo que debes adjuntarlas nuevamente si es necesario. Si tu árbol tiene un límite en el uso de IA, cada imagen cuenta como una pregunta adicional.

## Permitiendo que el asistente cambie tu árbol

Si el administrador del servidor lo ha habilitado, los editores, propietarios y administradores pueden pedir al asistente que cambie el árbol, por ejemplo, "Añadir un bautismo el 3 de mayo de 1802 en St. Mary's a Johann Meyer" o "Corregir el año de nacimiento de Anna Smith, debería ser 1871".

El asistente nunca cambia nada por su cuenta. Responde con una tarjeta de **Cambios propuestos** que lista cada registro que añadiría, editaría o eliminaría, con los valores antiguos tachados y los nuevos valores destacados. No ocurre nada hasta que hagas clic en **Aplicar**. Los cambios se realizan en un solo paso, que puedes deshacer como cualquier otra edición, desde el mensaje que aparece o en el [historial de revisiones](revisions.md).

Revisa una propuesta cuidadosamente antes de aplicarla, en particular que el asistente haya seleccionado a la persona correcta y que no haya añadido un nuevo registro (como un lugar o fuente) que ya existe en tu árbol bajo un nombre ligeramente diferente. Si una propuesta no es del todo correcta, indica qué cambiar, y el asistente propondrá nuevamente.

Una vez que se ha aplicado una propuesta, las propuestas más antiguas en la misma conversación ya no se pueden aplicar, ya que fueron hechas para el árbol tal como estaba antes. Lo mismo ocurre si uno de los registros afectados ha sido cambiado en el ínterin.

## Consejos para hacer preguntas

- **Nombra a las personas.** El asistente no sabe quién eres ni quién es tu persona principal, así que en lugar de "mi abuela", pregunta sobre "la abuela de Anna Smith (nacida en 1950)". También puedes usar IDs de Gramps, por ejemplo, "los hijos de I0042".
- **Sé específico** cuando los nombres son comunes: "¿Cuándo se casó el John Smith nacido en 1850 en Boston?" es mejor que "¿Cuándo se casó John Smith?"
- **Usa tu idioma.** Puedes preguntar en tu propio idioma y recibir respuestas en el mismo idioma.
- **Pregunta de nuevo de manera diferente** si una respuesta parece incompleta, por ejemplo, nombrando el lugar o el período de tiempo que te interesa.

!!! tip
    Comparte tu experiencia sobre lo que funciona y lo que no funciona con la comunidad.
