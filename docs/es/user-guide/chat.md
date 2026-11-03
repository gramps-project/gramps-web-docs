# Usando el Asistente de IA

!!! info
    El Asistente de IA requiere la versión 2.5.0 o superior de la API de Gramps Web y la versión 24.10.0 o superior de Gramps Web. La versión 3.6.0 de la API de Gramps Web introdujo capacidades de llamada de herramientas para interacciones más inteligentes.

La vista de **Asistente** en Gramps Web (si está disponible en tu instalación, etiquetada como "Chat" en versiones más antiguas) da acceso a un asistente de IA que puede responder preguntas sobre tu árbol genealógico.

!!! warning
    Dado que esta sigue siendo una función nueva y en evolución, algunos tipos de preguntas funcionan bien mientras que otros no. Además, como con cualquier asistente de IA, puede dar respuestas incorrectas desde el punto de vista factual, así que asegúrate de verificar siempre.

## Cómo funciona

Para entender qué tipos de preguntas puede responder el asistente, es útil comprender cómo funciona por dentro:

1. El usuario hace una pregunta.
2. El asistente consulta tu base de datos directamente utilizando herramientas especializadas: busca en el árbol con la [búsqueda de texto completo](search.md), filtra personas/eventos/familias/lugares por criterios específicos, calcula relaciones entre individuos y busca registros completos, incluyendo sus notas.
3. Un modelo de lenguaje grande formula una respuesta basada en los registros que ha encontrado.
4. La respuesta se muestra a ti, con enlaces a los registros en los que se basa.

El asistente responde solo a partir de tu árbol, no del conocimiento general del modelo de lenguaje, incluso sobre personas bien conocidas. Si el árbol no registra algo, lo menciona, indicando información relacionada que encontró, por ejemplo, en una nota. Los enlaces a objetos que no tienes permiso para ver se muestran como texto plano.

Las preguntas de seguimiento mantienen el contexto de preguntas anteriores en la misma conversación, por lo que puedes preguntar "¿Y cuándo murió?" después de preguntar sobre una persona.

Mientras el asistente está trabajando, indicadores muestran qué herramientas está utilizando actualmente (por ejemplo, buscando personas, buscando relaciones) para que puedas seguir mientras construye su respuesta. Las preguntas que tardan más en procesarse se manejan como tareas en segundo plano: puedes navegar a otra parte y volver, y el progreso también se refleja en [Notificaciones](notifications.md). Las respuestas están formateadas con Markdown (listas, énfasis, enlaces, etc.) para una lectura más fácil.

## Qué puedes preguntar

Con las capacidades de llamada de herramientas introducidas en la versión 3.6.0 de la API de Gramps Web, el asistente de IA ahora puede manejar preguntas más complejas:

- **Relaciones familiares**: "¿Quiénes son los abuelos de Jane Smith?" o "¿Cómo está relacionado John Doe con Mary Johnson?"
- **Búsquedas filtradas**: "Muéstrame todas las personas nacidas en Londres después de 1850" o "¿Qué eventos ocurrieron en París?"
- **Consultas basadas en fechas**: "¿Quién murió antes de 1900?" o "Lista de matrimonios que tuvieron lugar entre 1920 y 1950"
- **Información sobre lugares**: "¿Qué lugares hay en Francia?" o "Cuéntame sobre la Iglesia de Santa María"
- **Preguntas generales**: "¿Cuál es el nombre de los hijos de John Doe?" o "¿Cuándo nació Mary Smith?"

## Consejos para hacer preguntas

Para obtener los mejores resultados del asistente de IA:

- **Sé específico**: Formula tu pregunta con el mayor detalle posible para evitar ambigüedades. Por ejemplo, "¿Cuándo se casó John Smith, nacido en 1850 en Boston?" es mejor que "¿Cuándo se casó John Smith?"
- **Usa nombres propios**: Menciona nombres, lugares y fechas específicas cuando sea relevante.
- **Pregunta una cosa a la vez**: Divide preguntas complejas en partes más simples para obtener mejores resultados.
- **Usa tu idioma**: Los modelos de lenguaje grandes son multilingües, así que puedes hacer preguntas en tu propio idioma y recibir respuestas en el mismo idioma.

!!! tip
    Por favor, comparte tu experiencia sobre lo que funciona y lo que no funciona con la comunidad.
