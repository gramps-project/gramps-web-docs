# Usando el chat de IA

!!! info
    El chat de IA requiere Gramps Web API versión 2.5.0 o superior y Gramps Web versión 24.10.0 o superior.


La vista de chat en Gramps Web (si está disponible en tu instalación) da acceso a un asistente de IA que puede responder preguntas sobre tu árbol genealógico.

!!! warning
    Dado que esta sigue siendo una función nueva y en evolución, algunos tipos de preguntas funcionan bien mientras que otros no. Además, al igual que con cualquier asistente de IA, puede dar respuestas factualmente incorrectas, así que asegúrate de verificar siempre.

## Cómo funciona

Para entender qué tipos de preguntas puede responder el asistente, es útil comprender cómo funciona por dentro:

1. El usuario hace una pregunta.
2. Gramps Web identifica un número de (por ejemplo, diez) objetos de Gramps que probablemente contengan la información que responde a la pregunta. Para ello, utiliza una técnica llamada "búsqueda semántica". Por ejemplo, si preguntas "¿Cuál es el nombre de los hijos de John Doe?", si existe una familia con John Doe como padre, es probable que esté entre los resultados principales.
3. Gramps Web envía la pregunta del usuario junto con la información de contexto recuperada a un modelo de lenguaje grande ("chatbot") y le pide que extraiga la respuesta correcta.
4. La respuesta se muestra al usuario.

## Cómo hacer una pregunta

Debido a la forma en que funciona el chat, no es (actualmente) posible que el asistente de IA responda preguntas sobre relaciones específicas que no sean padres o hijos, a menos que esta información esté contenida como texto en una nota.

Dado que cada respuesta se basa en un número limitado de los principales resultados de búsqueda semántica, tampoco puede responder preguntas sobre estadísticas ("¿cuántas personas hay en mi base de datos ...?").

Para evitar ambigüedades y malentendidos, es útil formular la pregunta de la manera más detallada posible.

Ten en cuenta que los modelos de lenguaje grandes son multilingües, por lo que puedes hablarle en tu propio idioma y te responderá en el mismo idioma.

!!! tip
    Por favor, comparte tu experiencia sobre lo que funciona y lo que no funciona con la comunidad.
