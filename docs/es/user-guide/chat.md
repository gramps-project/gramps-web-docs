# Uso del Asistente de IA

!!! info
    El Asistente de IA requiere la versión 2.5.0 o superior de la API de Gramps Web y la versión 24.10.0 o superior de Gramps Web. La versión 3.6.0 de la API de Gramps Web introdujo capacidades de llamada a herramientas para interacciones más inteligentes.

La vista de **Asistente** en Gramps Web (si está disponible en tu instalación, etiquetada como "Chat" en versiones anteriores) da acceso a un asistente de IA que puede responder preguntas sobre tu árbol genealógico.

!!! warning
    Dado que esta sigue siendo una función nueva y en evolución, algunos tipos de preguntas funcionan bien mientras que otras no. Además, como con cualquier asistente de IA, puede dar respuestas factualmente incorrectas, así que asegúrate de siempre verificar.

## Cómo funciona

Para entender qué tipos de preguntas puede responder el asistente, es útil comprender cómo funciona por dentro:

1. El usuario hace una pregunta.
2. El asistente de IA puede usar múltiples enfoques para encontrar respuestas:
   - **Búsqueda Semántica**: Gramps Web identifica objetos en tu árbol genealógico que probablemente contengan información relevante. Por ejemplo, si preguntas "¿Cuál es el nombre de los hijos de John Doe?", las familias con John Doe como padre estarán entre los principales resultados.
   - **Llamada a Herramientas (API de Gramps Web v3.6.0+)**: El asistente puede consultar directamente tu base de datos utilizando herramientas especializadas para buscar, filtrar personas/eventos/familias/lugares por criterios específicos, calcular relaciones entre individuos y recuperar información detallada.
3. Gramps Web envía la pregunta junto con la información recuperada a un modelo de lenguaje grande para formular una respuesta.
4. La respuesta se muestra para ti.

Mientras el asistente está trabajando, los indicadores muestran qué herramientas está utilizando actualmente (por ejemplo, buscando personas, buscando relaciones) para que puedas seguir el progreso mientras construye su respuesta. Las preguntas que tardan más en procesarse se manejan como tareas en segundo plano: puedes navegar a otra parte y volver, y el progreso también se refleja en [Notificaciones](notifications.md). Las respuestas están formateadas con Markdown (listas, énfasis, enlaces, etc.) para facilitar la lectura.

## Qué puedes preguntar

Con las capacidades de llamada a herramientas introducidas en la versión 3.6.0 de la API de Gramps Web, el asistente de IA ahora puede manejar preguntas más complejas:

- **Relaciones familiares**: "¿Quiénes son los abuelos de Jane Smith?" o "¿Cómo está relacionado John Doe con Mary Johnson?"
- **Búsquedas filtradas**: "Muéstrame todas las personas nacidas en Londres después de 1850" o "¿Qué eventos ocurrieron en París?"
- **Consultas basadas en fechas**: "¿Quién murió antes de 1900?" o "Lista de matrimonios que tuvieron lugar entre 1920 y 1950"
- **Información sobre lugares**: "¿Qué lugares hay en Francia?" o "Háblame sobre la Iglesia de Santa María"
- **Preguntas generales**: "¿Cuál es el nombre de los hijos de John Doe?" o "¿Cuándo nació Mary Smith?"

## Consejos para hacer preguntas

Para obtener los mejores resultados del asistente de IA:

- **Sé específico**: Formula tu pregunta con el mayor detalle posible para evitar ambigüedades. Por ejemplo, "¿Cuándo se casó John Smith, nacido en 1850 en Boston?" es mejor que "¿Cuándo se casó John Smith?"
- **Usa nombres propios**: Menciona nombres, lugares y fechas específicas cuando sea relevante.
- **Pregunta una cosa a la vez**: Divide preguntas complejas en partes más simples para obtener mejores resultados.
- **Usa tu idioma**: Los modelos de lenguaje grandes son multilingües, por lo que puedes hacer preguntas en tu propio idioma y recibir respuestas en el mismo idioma.

!!! tip
    Por favor, comparte tu experiencia sobre lo que funciona y lo que no funciona con la comunidad.
