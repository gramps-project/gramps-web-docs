# Setting up AI chat

!!! info
    AI chat requires Gramps Web API version 2.5.0 or higher. Version 3.6.0 introduced tool calling capabilities for more intelligent interactions.


Gramps Web API supports asking questions about the genealogical database using large language models (LLM) with tool calling.

## How it works

The AI assistant uses specialized tools to query your genealogy data directly. These tools allow the assistant to search the database with the full-text search, filter people/events/families/places by specific criteria, calculate relationships between individuals, and retrieve complete records, including notes. The assistant then answers based on the records it has looked up and links to them in its answer. It answers only from the tree, not from general knowledge: if the tree does not record something, the assistant says so. Links to objects that do not exist or that are private for the user are replaced by their text.

AI chat does not need a vector embedding model. Versions of Gramps Web API before 3.24 also used *semantic search* (retrieval-augmented generation, RAG), which compared the meaning of a question to an index of numerical vectors computed for all objects in the database. Semantic search was removed in Gramps Web API 3.25; the `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` and `VECTOR_EMBEDDING_API_KEY` settings are ignored and can be removed from your configuration.

To enable the chat endpoint in Gramps Web API, two steps are necessary:

1. Installing required dependencies,
2. Setting up an LLM provider.

The two steps are described below in turn. Finally, an owner or administrator must [configure which users can access the chat feature](users.md#configuring-who-can-use-ai-chat) in the Manage Users settings.

## Installing required dependencies

The standard docker images for Gramps Web already have all dependencies needed for AI chat pre-installed.

When installing Gramps Web API via `pip` (this is not necessary when using the Docker images) the necessary dependencies are installed with

```bash
pip install gramps_webapi[ai]
```


## Setting up an LLM provider

Communication with the LLM uses the Pydantic AI framework, which supports OpenAI-compatible APIs. This allows using a locally deployed LLM via Ollama (see [Ollama OpenAI compatibility](https://ollama.com/blog/openai-compatibility)) or hosted APIs like OpenAI, Anthropic, or Hugging Face TGI (Text Generation Inference). The LLM is configured via the configuration parameters `LLM_MODEL` and `LLM_BASE_URL`.

Besides OpenAI-compatible APIs, the provider-specific model prefixes of Pydantic AI can be used for OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock and Ollama. Other providers, such as Cohere, Hugging Face and xAI, are not installed; Hugging Face Inference Providers can still be used through their OpenAI-compatible endpoint (`LLM_BASE_URL` set to `https://router.huggingface.co/v1`).

If your model server does not limit the length of a response, set `LLM_MAX_OUTPUT_TOKENS` to the maximum number of tokens the model may generate per response (see [Configuration](configuration.md)).


### Using a hosted LLM via the OpenAI API

When using the OpenAI API, `LLM_BASE_URL` can be left unset, while `LLM_MODEL` has to be set to one of the OpenAI models, e.g. `gpt-4o-mini`. The LLM uses tool calling to answer questions: it queries the database directly using specialized tools and answers based on the records it finds. It does not require deep genealogical or historical knowledge. Therefore, you can try if a small/cheap model is sufficient.

You will also need to sign up for an account, get an API key and store it in the `OPENAI_API_KEY` environment variable.

!!! info
    `LLM_MODEL` is a configuration parameter; if you want to set it via an environment variable, use `GRAMPSWEB_LLM_MODEL` (see [Configuration](configuration.md)). `OPENAI_API_KEY` is not a configuration parameter but an environment variable directly used by the Pydantic AI library, so it should not be prefixed.


### Using Mistral AI

To use Mistral AI's hosted models, prefix the model name with `mistral:` when setting `LLM_MODEL`.

You will need to sign up for a Mistral AI account, get an API key, and store it in the `MISTRAL_API_KEY` environment variable. No need to set `LLM_BASE_URL` as Pydantic AI will automatically use the correct Mistral API endpoint.

Example configuration when using docker compose with environment variables:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```


### Using a local LLM via Ollama

[Ollama](https://ollama.com/) is a convenient way to run LLMs locally. Please consult the Ollama documentation for details. Please note that LLMs require significant computational resources and all but the smallest models will probably be too slow without GPU support. Since the assistant relies on tool calling, choose a model that supports tools, such as [`qwen2.5`](https://ollama.com/library/qwen2.5). Start with a small variant like `qwen2.5:7b` and try a larger one if the answers are not good enough. Please share any experience with the community!

When deploying Gramps Web with Docker Compose, you can add an Ollama service and point Gramps Web to it:

```yaml
services:
  grampsweb: &grampsweb
    # ... existing config ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... existing config ...
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

After starting the services, pull the model into Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

A few things to note:

- Set `LLM_MODEL` to the Ollama model name, including its tag (the part after the colon, e.g. `7b`), prefixed with `ollama:`. The prefix makes Pydantic AI use its Ollama-specific settings for the model, which is the recommended setup.
- `LLM_BASE_URL` must end in `/v1/`, e.g. `http://ollama:11434/v1/`.
- With the `ollama:` prefix, neither `OPENAI_API_KEY` nor the `OLLAMA_BASE_URL` environment variable is needed. If `LLM_BASE_URL` is not set, Gramps Web falls back to `OLLAMA_BASE_URL`.
- Alternatively, you can leave out the prefix (e.g. `LLM_MODEL: qwen2.5:7b`) and use Ollama through its generic OpenAI-compatible API. In this case, you also have to set the `OPENAI_API_KEY` environment variable to `ollama` (any non-empty value works).

To troubleshoot problems with Ollama, you can enable debug logging by setting environment variable `OLLAMA_DEBUG=1` in the Ollama service environment.

!!! info
    If you are using Ollama for Gramps Web AI chat, please support the community by completing this documentation with any missing details.

### Using other providers

Please feel free to submit documentation for other providers and share your experience with the community!