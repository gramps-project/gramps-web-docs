# Configuración del chat de IA

!!! info
    El chat de IA requiere la versión 2.5.0 o superior de la API web de Gramps. La versión 3.6.0 introdujo capacidades de llamada a herramientas para interacciones más inteligentes.

La API web de Gramps admite hacer preguntas sobre la base de datos genealógica utilizando modelos de lenguaje grandes (LLM) con llamada a herramientas.

## Cómo funciona

El asistente de IA utiliza herramientas especializadas para consultar directamente tus datos de genealogía. Estas herramientas permiten al asistente buscar en la base de datos con búsqueda de texto completo, filtrar personas/eventos/familias/lugares por criterios específicos, calcular relaciones entre individuos y recuperar registros completos, incluidas notas. Luego, el asistente responde en función de los registros que ha consultado y los vincula en su respuesta.

Desde la API web de Gramps 3.24, el chat de IA ya no requiere un modelo de incrustación vectorial. Las versiones anteriores también utilizaban *búsqueda semántica* (generación aumentada por recuperación, RAG), que compara el significado de una pregunta con un índice de vectores numéricos calculados para todos los objetos en la base de datos. La búsqueda semántica está en desuso y se eliminará en la API web de Gramps 3.25, consulta [Búsqueda semántica (en desuso)](#semantic-search-deprecated) a continuación.

Para habilitar el punto final de chat en la API web de Gramps, son necesarios dos pasos:

1. Instalar las dependencias requeridas,
2. Configurar un proveedor de LLM.

Los dos pasos se describen a continuación. Finalmente, un propietario o administrador debe [configurar qué usuarios pueden acceder a la función de chat](users.md#configuring-who-can-use-ai-chat) en la configuración de Administrar Usuarios.

## Instalación de las dependencias requeridas

Las imágenes estándar de Docker para Gramps Web ya tienen todas las dependencias necesarias para el chat de IA preinstaladas.

Al instalar la API web de Gramps a través de `pip` (esto no es necesario al usar las imágenes de Docker), las dependencias necesarias se instalan con

```bash
pip install gramps_webapi[ai]
```

## Búsqueda semántica (en desuso)

!!! warning "La búsqueda semántica está en desuso"
    La búsqueda semántica está en desuso desde la API web de Gramps 3.24 y se eliminará en la versión 3.25. El chat de IA y la [búsqueda de texto completo](../user-guide/search.md) no la necesitan. Después de la eliminación, la configuración `VECTOR_EMBEDDING_MODEL` seguirá siendo aceptada pero será ignorada. Si la configuras solo para habilitar el chat de IA, puedes eliminarla ahora, junto con las otras configuraciones `VECTOR_EMBEDDING_*`, lo que también ahorra la memoria que necesita el modelo de incrustación.

El resto de esta sección describe la búsqueda semántica para servidores que aún la utilizan con la API web de Gramps 3.24.

Si las dependencias necesarias están instaladas, habilitar la búsqueda semántica puede ser tan simple como configurar la opción de configuración `VECTOR_EMBEDDING_MODEL` (por ejemplo, configurando la variable de entorno `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), consulta [Configuración del servidor](configuration.md). Esto puede ser cualquier cadena de un modelo compatible con la biblioteca [Sentence Transformers](https://sbert.net/). Consulta la documentación de este proyecto para obtener detalles y los modelos disponibles.

!!! warning
    Ten en cuenta que las imágenes de Docker predeterminadas no incluyen una versión de PyTorch con soporte para GPU. Si tienes acceso a una GPU (lo que acelerará significativamente la indexación semántica), instala una versión de PyTorch habilitada para GPU.

Hay varias consideraciones a tener en cuenta al elegir un modelo.

- Cuando cambias el modelo, debes recrear manualmente el índice de búsqueda semántica para tu árbol (o todos los árboles en una configuración de múltiples árboles), de lo contrario, encontrarás errores o resultados sin sentido. Gramps Web detecta cuando el modelo de incrustación configurado ya no coincide con el índice existente y muestra un aviso persistente a los administradores pidiéndoles que inicien un reindexado completo desde [Configuración de administración](../administration/settings.md#semantic-search-index).
- Los modelos son un compromiso entre precisión/generalidad por un lado y tiempo de computación/espacio de almacenamiento por el otro. Si no estás ejecutando la API web de Gramps en un sistema que tenga acceso a una GPU potente, los modelos más grandes suelen ser demasiado lentos en la práctica.
- A menos que toda tu base de datos esté en inglés y se espere que todos tus usuarios solo hagan preguntas en inglés, necesitarás un modelo de incrustación multilingüe, que son más raros que los modelos puramente en inglés.

Si el modelo no está presente en la caché local, se descargará cuando la API web de Gramps se inicie por primera vez con la nueva configuración. El modelo `sentence-transformers/distiluse-base-multilingual-cased-v2` ya está disponible localmente al usar las imágenes de Docker estándar. Este modelo es un buen punto de partida y admite entrada multilingüe.

¡Por favor, comparte tus aprendizajes sobre diferentes modelos con la comunidad!

!!! info
    La biblioteca de transformers de oraciones consume una cantidad significativa de memoria, lo que puede causar que se terminen los procesos de trabajo. Como regla general, con la búsqueda semántica habilitada, cada trabajador de Gunicorn consume alrededor de 200 MB de memoria y cada trabajador de celery alrededor de 500 MB de memoria incluso cuando está inactivo, y hasta 1 GB al calcular incrustaciones. Consulta [Limitar el uso de CPU y memoria](cpu-limited.md) para configuraciones que limitan el uso de memoria. Además, es aconsejable provisionar una partición de intercambio lo suficientemente grande para evitar errores OOM debido a picos transitorios en el uso de memoria.

### Uso de una API de incrustación remota

Como alternativa a ejecutar un modelo de Sentence Transformers localmente, puedes utilizar una API de incrustación compatible con OpenAI para la búsqueda semántica. Esto es útil si deseas descargar el cálculo de incrustaciones a un servicio separado (por ejemplo, [Ollama](https://ollama.com/)), utilizar un proveedor de incrustaciones en la nube (por ejemplo, OpenAI) o evitar cargar las bibliotecas de Sentence Transformers y PyTorch en memoria.

La API remota debe ser compatible con el [punto final de incrustaciones de OpenAI](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`).

Para utilizar una API de incrustación remota, configura las siguientes opciones de configuración (consulta [Configuración del servidor](configuration.md)):

Clave | Descripción
----|-------------
`VECTOR_EMBEDDING_MODEL` | El nombre del modelo que se pasará al proveedor remoto
`VECTOR_EMBEDDING_BASE_URL` | URL base de la API remota
`VECTOR_EMBEDDING_API_KEY` | Clave API (solo necesaria si el proveedor requiere autenticación)

#### Uso de Ollama para incrustaciones

Al implementar Gramps Web con Docker Compose, puedes agregar un servicio de Ollama y usarlo tanto para incrustaciones como (opcionalmente) para el LLM:

```yaml
services:
  grampsweb: &grampsweb
    # ... configuración existente ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... configuración existente ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

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

Después de iniciar los servicios, descarga el modelo de incrustación en Ollama:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Al usar Ollama para incrustaciones, no se requieren las bibliotecas de Sentence Transformers y PyTorch, lo que reduce significativamente el uso de memoria de los trabajadores de la API web de Gramps.

#### Uso de OpenAI para incrustaciones

Para utilizar la API de incrustaciones de OpenAI, establece la URL base en la API de OpenAI y proporciona tu clave API:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Cambiar el modelo de incrustación requiere reindexar todos los registros de tu árbol (o todos los árboles en una configuración de múltiples árboles), ya que diferentes modelos producen vectores con diferentes dimensiones.

## Configuración de un proveedor de LLM

La comunicación con el LLM utiliza el marco de IA Pydantic, que admite APIs compatibles con OpenAI. Esto permite usar un LLM desplegado localmente a través de Ollama (consulta [Compatibilidad de Ollama con OpenAI](https://ollama.com/blog/openai-compatibility)) o APIs alojadas como OpenAI, Anthropic o Hugging Face TGI (Text Generation Inference). El LLM se configura a través de los parámetros de configuración `LLM_MODEL` y `LLM_BASE_URL`.

### Uso de un LLM alojado a través de la API de OpenAI

Al usar la API de OpenAI, `LLM_BASE_URL` puede dejarse sin establecer, mientras que `LLM_MODEL` debe configurarse en uno de los modelos de OpenAI, por ejemplo, `gpt-4o-mini`. El LLM utiliza la llamada a herramientas para responder preguntas: consulta la base de datos directamente utilizando herramientas especializadas y responde en función de los registros que encuentra. No requiere un conocimiento genealógico o histórico profundo. Por lo tanto, puedes probar si un modelo pequeño/económico es suficiente.

También necesitarás registrarte para obtener una cuenta, obtener una clave API y almacenarla en la variable de entorno `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` es un parámetro de configuración; si deseas configurarlo a través de una variable de entorno, usa `GRAMPSWEB_LLM_MODEL` (consulta [Configuración](configuration.md)). `OPENAI_API_KEY` no es un parámetro de configuración, sino una variable de entorno utilizada directamente por la biblioteca de IA Pydantic, por lo que no debe tener prefijo.

### Uso de Mistral AI

Para utilizar los modelos alojados de Mistral AI, antepone el nombre del modelo con `mistral:` al configurar `LLM_MODEL`.

Necesitarás registrarte para obtener una cuenta de Mistral AI, obtener una clave API y almacenarla en la variable de entorno `MISTRAL_API_KEY`. No es necesario establecer `LLM_BASE_URL`, ya que Pydantic AI utilizará automáticamente el punto final correcto de la API de Mistral.

Ejemplo de configuración al usar Docker Compose con variables de entorno:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Uso de un LLM local a través de Ollama

[Ollama](https://ollama.com/) es una forma conveniente de ejecutar LLMs localmente. Consulta la documentación de Ollama para obtener detalles. Ten en cuenta que los LLMs requieren recursos computacionales significativos y todos los modelos excepto los más pequeños probablemente serán demasiado lentos sin soporte de GPU. Dado que el asistente depende de la llamada a herramientas, elige un modelo que soporte herramientas, como [`qwen2.5`](https://ollama.com/library/qwen2.5). Comienza con una variante pequeña como `qwen2.5:7b` y prueba una más grande si las respuestas no son lo suficientemente buenas. ¡Por favor, comparte cualquier experiencia con la comunidad!

Al implementar Gramps Web con Docker Compose, puedes agregar un servicio de Ollama y apuntar Gramps Web a él:

```yaml
services:
  grampsweb: &grampsweb
    # ... configuración existente ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... configuración existente ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

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

Después de iniciar los servicios, descarga el modelo en Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Algunas cosas a tener en cuenta:

- Establece `LLM_MODEL` en el nombre del modelo de Ollama, incluyendo su etiqueta (la parte después de los dos puntos, por ejemplo, `7b`), precedido por `ollama:`. El prefijo hace que Pydantic AI use su configuración específica de Ollama para el modelo, que es la configuración recomendada.
- `LLM_BASE_URL` debe terminar en `/v1/`, por ejemplo, `http://ollama:11434/v1/`.
- Con el prefijo `ollama:`, ni `OPENAI_API_KEY` ni la variable de entorno `OLLAMA_BASE_URL` son necesarias. Si `LLM_BASE_URL` no está configurada, Gramps Web recurrirá a `OLLAMA_BASE_URL`.
- Alternativamente, puedes omitir el prefijo (por ejemplo, `LLM_MODEL: qwen2.5:7b`) y usar Ollama a través de su API genérica compatible con OpenAI. En este caso, también debes establecer la variable de entorno `OPENAI_API_KEY` en `ollama` (cualquier valor no vacío funciona).

Para solucionar problemas con Ollama, puedes habilitar el registro de depuración configurando la variable de entorno `OLLAMA_DEBUG=1` en el entorno del servicio de Ollama.

!!! info
    Si estás utilizando Ollama para el chat de IA de Gramps Web, por favor apoya a la comunidad completando esta documentación con cualquier detalle que falte.

### Uso de otros proveedores

¡No dudes en enviar documentación para otros proveedores y compartir tu experiencia con la comunidad!
