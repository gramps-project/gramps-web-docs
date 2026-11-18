# Configuración del chat de IA

!!! info
    El chat de IA requiere Gramps Web API versión 2.5.0 o superior. La versión 3.6.0 introdujo capacidades de llamada a herramientas para interacciones más inteligentes.


Gramps Web API admite hacer preguntas sobre la base de datos genealógica utilizando modelos de lenguaje grandes (LLM) con llamada a herramientas.

## Cómo funciona

El asistente de IA utiliza herramientas especializadas para consultar directamente sus datos de genealogía. Estas herramientas permiten al asistente buscar en la base de datos con búsqueda de texto completo, filtrar personas/eventos/familias/lugares por criterios específicos, calcular relaciones entre individuos y recuperar registros completos, incluidas notas. Luego, el asistente responde en función de los registros que ha consultado y proporciona enlaces a ellos en su respuesta. Responde solo a partir del árbol, no de conocimientos generales: si el árbol no registra algo, el asistente lo dice. Los enlaces a objetos que no existen o que son privados para el usuario se reemplazan por su texto.

El chat de IA no necesita un modelo de incrustación vectorial. Las versiones de Gramps Web API anteriores a la 3.24 también usaban *búsqueda semántica* (generación aumentada por recuperación, RAG), que comparaba el significado de una pregunta con un índice de vectores numéricos calculados para todos los objetos en la base de datos. La búsqueda semántica se eliminó en Gramps Web API 3.25; los ajustes `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` y `VECTOR_EMBEDDING_API_KEY` se ignoran y pueden eliminarse de su configuración.

Para habilitar el punto final de chat en Gramps Web API, son necesarios dos pasos:

1. Instalar las dependencias requeridas,
2. Configurar un proveedor de LLM.

Los dos pasos se describen a continuación. Finalmente, un propietario o administrador debe [configurar qué usuarios pueden acceder a la función de chat](users.md#configuring-who-can-use-ai-chat) en la configuración de Administrar Usuarios.

## Instalación de dependencias requeridas

Las imágenes estándar de Docker para Gramps Web ya tienen todas las dependencias necesarias para el chat de IA preinstaladas.

Al instalar Gramps Web API a través de `pip` (esto no es necesario al usar las imágenes de Docker), las dependencias necesarias se instalan con

```bash
pip install gramps_webapi[ai]
```


## Configuración de un proveedor de LLM

La comunicación con el LLM utiliza el marco de IA Pydantic, que admite APIs compatibles con OpenAI. Esto permite usar un LLM desplegado localmente a través de Ollama (ver [Compatibilidad de Ollama con OpenAI](https://ollama.com/blog/openai-compatibility)) o APIs alojadas como OpenAI, Anthropic o Hugging Face TGI (Text Generation Inference). El LLM se configura a través de los parámetros de configuración `LLM_MODEL` y `LLM_BASE_URL`.

Además de las APIs compatibles con OpenAI, se pueden usar los prefijos de modelo específicos del proveedor de Pydantic AI para OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock y Ollama. Otros proveedores, como Cohere, Hugging Face y xAI, no están instalados; los Proveedores de Inferencia de Hugging Face aún se pueden usar a través de su punto final compatible con OpenAI (`LLM_BASE_URL` configurado como `https://router.huggingface.co/v1`).

Si su servidor de modelos no limita la longitud de una respuesta, configure `LLM_MAX_OUTPUT_TOKENS` al número máximo de tokens que el modelo puede generar por respuesta (ver [Configuración](configuration.md)).


### Uso de un LLM alojado a través de la API de OpenAI

Al usar la API de OpenAI, `LLM_BASE_URL` puede dejarse sin configurar, mientras que `LLM_MODEL` debe establecerse en uno de los modelos de OpenAI, por ejemplo, `gpt-4o-mini`. El LLM utiliza llamada a herramientas para responder preguntas: consulta la base de datos directamente utilizando herramientas especializadas y responde en función de los registros que encuentra. No requiere un profundo conocimiento genealógico o histórico. Por lo tanto, puede probar si un modelo pequeño/barato es suficiente.

También necesitará registrarse para obtener una cuenta, obtener una clave API y almacenarla en la variable de entorno `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` es un parámetro de configuración; si desea configurarlo a través de una variable de entorno, use `GRAMPSWEB_LLM_MODEL` (ver [Configuración](configuration.md)). `OPENAI_API_KEY` no es un parámetro de configuración, sino una variable de entorno utilizada directamente por la biblioteca Pydantic AI, por lo que no debe tener prefijo.


### Uso de Mistral AI

Para usar los modelos alojados de Mistral AI, prefije el nombre del modelo con `mistral:` al configurar `LLM_MODEL`.

Necesitará registrarse para obtener una cuenta de Mistral AI, obtener una clave API y almacenarla en la variable de entorno `MISTRAL_API_KEY`. No es necesario configurar `LLM_BASE_URL`, ya que Pydantic AI utilizará automáticamente el punto final correcto de la API de Mistral.

Ejemplo de configuración al usar docker compose con variables de entorno:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```


### Uso de un LLM local a través de Ollama

[Ollama](https://ollama.com/) es una forma conveniente de ejecutar LLMs localmente. Consulte la documentación de Ollama para obtener detalles. Tenga en cuenta que los LLMs requieren recursos computacionales significativos y todos menos los modelos más pequeños probablemente serán demasiado lentos sin soporte de GPU. Dado que el asistente depende de la llamada a herramientas, elija un modelo que admita herramientas, como [`qwen2.5`](https://ollama.com/library/qwen2.5). Comience con una variante pequeña como `qwen2.5:7b` y pruebe una más grande si las respuestas no son lo suficientemente buenas. ¡Comparta cualquier experiencia con la comunidad!

Al implementar Gramps Web con Docker Compose, puede agregar un servicio de Ollama y apuntar Gramps Web a él:

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

Después de iniciar los servicios, descargue el modelo en Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Algunas cosas a tener en cuenta:

- Configure `LLM_MODEL` al nombre del modelo de Ollama, incluyendo su etiqueta (la parte después de los dos puntos, por ejemplo, `7b`), prefijado con `ollama:`. El prefijo hace que Pydantic AI use su configuración específica de Ollama para el modelo, que es la configuración recomendada.
- `LLM_BASE_URL` debe terminar en `/v1/`, por ejemplo, `http://ollama:11434/v1/`.
- Con el prefijo `ollama:`, ni `OPENAI_API_KEY` ni la variable de entorno `OLLAMA_BASE_URL` son necesarias. Si `LLM_BASE_URL` no está configurado, Gramps Web recurrirá a `OLLAMA_BASE_URL`.
- Alternativamente, puede omitir el prefijo (por ejemplo, `LLM_MODEL: qwen2.5:7b`) y usar Ollama a través de su API genérica compatible con OpenAI. En este caso, también debe configurar la variable de entorno `OPENAI_API_KEY` a `ollama` (cualquier valor no vacío funciona).

Para solucionar problemas con Ollama, puede habilitar el registro de depuración configurando la variable de entorno `OLLAMA_DEBUG=1` en el entorno del servicio Ollama.

!!! info
    Si está utilizando Ollama para el chat de IA de Gramps Web, apoye a la comunidad completando esta documentación con cualquier detalle que falte.

### Uso de otros proveedores

¡No dude en enviar documentación para otros proveedores y compartir su experiencia con la comunidad!

## Características opcionales

### Imágenes en preguntas

Si su modelo acepta imágenes, configure `LLM_VISION` en `True` para permitir que los usuarios adjunten imágenes a sus preguntas, por ejemplo, escaneos de registros (Gramps Web API 3.26+). Las imágenes se reducen a un máximo de 1568 píxeles en el lado largo antes de enviarse al modelo. Verifique que el modelo realmente admita la entrada de imágenes: muchos modelos locales pequeños no lo hacen, y el proveedor luego rechaza preguntas con imágenes.

### Permitir que el asistente proponga cambios

Con `LLM_ALLOW_WRITE_PROPOSALS` configurado en `True` (Gramps Web API 3.26+), el asistente puede [proponer cambios al árbol](../user-guide/chat.md#letting-the-assistant-change-your-tree), que los usuarios aplican después de revisarlos. El asistente mismo nunca escribe en la base de datos. Las propuestas solo se ofrecen a los usuarios que tienen permiso para agregar, editar y eliminar objetos, es decir, editores y superiores, y que tienen permiso para usar el chat.

Escribir propuestas correctas es más difícil para un modelo que responder preguntas, así que pruébelo con su modelo antes de habilitarlo para sus usuarios. Las herramientas adicionales también hacen que cada solicitud al modelo sea algo más grande.
