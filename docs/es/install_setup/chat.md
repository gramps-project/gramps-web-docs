# Configuración del chat de IA

!!! info
    El chat de IA requiere la versión 2.5.0 o superior de la API web de Gramps. La versión 3.6.0 introdujo capacidades de llamada a herramientas para interacciones más inteligentes.

La API web de Gramps admite hacer preguntas sobre la base de datos genealógica utilizando modelos de lenguaje grandes (LLM) a través de una técnica llamada generación aumentada por recuperación (RAG) combinada con la llamada a herramientas.

## Cómo funciona

El asistente de IA utiliza dos enfoques complementarios:

**Generación Aumentada por Recuperación (RAG)**: Un *modelo de incrustación vectorial* crea un índice de todos los objetos en la base de datos de Gramps en forma de vectores numéricos que codifican el significado de los objetos. Cuando un usuario hace una pregunta, esa pregunta también se convierte en un vector y se compara con los objetos en la base de datos. Esta *búsqueda semántica* devuelve los objetos que son más semánticamente similares a la pregunta.

**Llamada a Herramientas (v3.6.0+)**: El asistente de IA ahora puede utilizar herramientas especializadas para consultar directamente sus datos genealógicos. Estas herramientas permiten al asistente buscar en la base de datos, filtrar personas/eventos/familias/lugares por criterios específicos, calcular relaciones entre individuos y recuperar información detallada de los objetos. Esto hace que el asistente sea mucho más capaz de responder preguntas genealógicas complejas con precisión.

Para habilitar el punto final de chat en la API web de Gramps, son necesarios tres pasos:

1. Instalar las dependencias requeridas,
2. Habilitar la búsqueda semántica,
3. Configurar un proveedor de LLM.

Los tres pasos se describen a continuación. Finalmente, un propietario o administrador debe [configurar qué usuarios pueden acceder a la función de chat](users.md#configuring-who-can-use-ai-chat) en la configuración de Administrar Usuarios.

## Instalación de las dependencias requeridas

El chat de IA requiere que se instalen las bibliotecas Sentence Transformers y PyTorch.

Las imágenes estándar de Docker para Gramps Web ya las tienen preinstaladas para las arquitecturas `amd64` (por ejemplo, PC de escritorio de 64 bits) y `arm64` (por ejemplo, Raspberry Pi de 64 bits). Desafortunadamente, el chat de IA no es compatible con la arquitectura `armv7` (por ejemplo, Raspberry Pi de 32 bits) debido a la falta de soporte de PyTorch.

Al instalar la API web de Gramps a través de `pip` (esto no es necesario al usar las imágenes de Docker), las dependencias necesarias se instalan con

```bash
pip install gramps_webapi[ai]
```

## Habilitar la búsqueda semántica

Si las dependencias necesarias están instaladas, habilitar la búsqueda semántica puede ser tan simple como establecer la opción de configuración `VECTOR_EMBEDDING_MODEL` (por ejemplo, configurando la variable de entorno `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), consulte [Configuración del Servidor](configuration.md). Esto puede ser cualquier cadena de un modelo compatible con la biblioteca [Sentence Transformers](https://sbert.net/). Consulte la documentación de este proyecto para más detalles y los modelos disponibles.

!!! warning
    Tenga en cuenta que las imágenes de Docker predeterminadas no incluyen una versión de PyTorch con soporte para GPU. Si tiene acceso a una GPU (lo que acelerará significativamente la indexación semántica), instale una versión de PyTorch habilitada para GPU.

Hay varias consideraciones a tener en cuenta al elegir un modelo.

- Cuando cambie el modelo, deberá recrear manualmente el índice de búsqueda semántica para su árbol (o todos los árboles en una configuración de múltiples árboles), de lo contrario, encontrará errores o resultados sin sentido.
- Los modelos son un compromiso entre precisión/generalidad por un lado y tiempo de computación/espacio de almacenamiento por el otro. Si no está ejecutando la API web de Gramps en un sistema que tenga acceso a una GPU potente, los modelos más grandes suelen ser demasiado lentos en la práctica.
- A menos que toda su base de datos esté en inglés y se espere que todos sus usuarios solo hagan preguntas en inglés, necesitará un modelo de incrustación multilingüe, que son más raros que los modelos puramente en inglés.

Si el modelo no está presente en la caché local, se descargará cuando la API web de Gramps se inicie por primera vez con la nueva configuración. El modelo `sentence-transformers/distiluse-base-multilingual-cased-v2` ya está disponible localmente al usar las imágenes de Docker estándar. Este modelo es un buen punto de partida y admite entrada multilingüe.

¡Comparta sus aprendizajes sobre diferentes modelos con la comunidad!

!!! info
    La biblioteca de transformers de oraciones consume una cantidad significativa de memoria, lo que podría causar que se terminen los procesos de trabajo. Como regla general, con la búsqueda semántica habilitada, cada trabajador de Gunicorn consume alrededor de 200 MB de memoria y cada trabajador de celery alrededor de 500 MB de memoria incluso cuando está inactivo, y hasta 1 GB al calcular incrustaciones. Consulte [Limitar el uso de CPU y memoria](cpu-limited.md) para configuraciones que limiten el uso de memoria. Además, es aconsejable provisionar una partición de intercambio lo suficientemente grande para evitar errores OOM debido a picos transitorios en el uso de memoria.

## Configuración de un proveedor de LLM

La comunicación con el LLM utiliza el marco de IA Pydantic, que admite API compatibles con OpenAI. Esto permite usar un LLM desplegado localmente a través de Ollama (consulte [Compatibilidad de Ollama con OpenAI](https://ollama.com/blog/openai-compatibility)) o API alojadas como OpenAI, Anthropic o Hugging Face TGI (Inferencia de Generación de Texto). El LLM se configura a través de los parámetros de configuración `LLM_MODEL` y `LLM_BASE_URL`.

### Usando un LLM alojado a través de la API de OpenAI

Al usar la API de OpenAI, `LLM_BASE_URL` puede dejarse sin establecer, mientras que `LLM_MODEL` debe configurarse en uno de los modelos de OpenAI, por ejemplo, `gpt-4o-mini`. El LLM utiliza tanto RAG como la llamada a herramientas para responder preguntas: selecciona información relevante de los resultados de búsqueda semántica y puede consultar directamente la base de datos utilizando herramientas especializadas. No requiere un profundo conocimiento genealógico o histórico. Por lo tanto, puede probar si un modelo pequeño/barato es suficiente.

También necesitará registrarse para obtener una cuenta, obtener una clave API y almacenarla en la variable de entorno `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` es un parámetro de configuración; si desea configurarlo a través de una variable de entorno, use `GRAMPSWEB_LLM_MODEL` (consulte [Configuración](configuration.md)). `OPENAI_API_KEY` no es un parámetro de configuración, sino una variable de entorno utilizada directamente por la biblioteca de IA Pydantic, por lo que no debe tener prefijo.

### Usando Mistral AI

Para usar los modelos alojados de Mistral AI, prefije el nombre del modelo con `mistral:` al establecer `LLM_MODEL`.

Necesitará registrarse para obtener una cuenta de Mistral AI, obtener una clave API y almacenarla en la variable de entorno `MISTRAL_API_KEY`. No es necesario establecer `LLM_BASE_URL`, ya que Pydantic AI utilizará automáticamente el punto final correcto de la API de Mistral.

Ejemplo de configuración al usar docker compose con variables de entorno:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Usando un LLM local a través de Ollama

[Ollama](https://ollama.com/) es una forma conveniente de ejecutar LLMs localmente. Consulte la documentación de Ollama para más detalles. Tenga en cuenta que los LLMs requieren recursos computacionales significativos y todos menos los modelos más pequeños probablemente serán demasiado lentos sin soporte de GPU. Puede probar si [`tinyllama`](https://ollama.com/library/tinyllama) satisface sus necesidades. Si no, pruebe uno de los modelos más grandes. ¡Comparta cualquier experiencia con la comunidad!

Al desplegar Gramps Web con Docker Compose, puede agregar un servicio de Ollama

```yaml
services:
  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
    ollama_data:
```

y luego establecer el parámetro de configuración `LLM_BASE_URL` en `http://ollama:11434/v1`. Establezca `LLM_MODEL` en un modelo compatible con Ollama y descárguelo en su contenedor con `ollama pull <model>`. Finalmente, establezca `OPENAI_API_KEY` en `ollama`.

Para solucionar problemas con Ollama, puede habilitar el registro de depuración configurando la variable de entorno `OLLAMA_DEBUG=1` en el entorno del servicio de Ollama.

!!! info
    Si está utilizando Ollama para el chat de IA de Gramps Web, apoye a la comunidad completando esta documentación con cualquier detalle que falte.

### Usando otros proveedores

¡No dude en enviar documentación para otros proveedores y compartir su experiencia con la comunidad!
