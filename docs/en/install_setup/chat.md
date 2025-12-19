# Setting up AI chat

!!! info
    AI chat requires Gramps Web API version 2.5.0 or higher. Version 3.6.0 introduced tool calling capabilities for more intelligent interactions.



Gramps Web API supports asking questions about the genealogical database using large language models (LLM) via a technique called retrieval-augmented generation (RAG) combined with tool calling.

## How it works

The AI assistant uses two complementary approaches:

**Retrieval-Augmented Generation (RAG)**: A *vector embedding model* creates an index of all objects in the Gramps database in the form of numerical vectors that encode the objects' meaning. When a user asks a question, that question is converted to a vector as well, and compared to the objects in the database. This *semantic search* returns objects that are most semantically similar to the question.

**Tool Calling (v3.6.0+)**: The AI assistant can now use specialized tools to query your genealogy data directly. These tools allow the assistant to search the database, filter people/events/families/places by specific criteria, calculate relationships between individuals, and retrieve detailed object information. This makes the assistant much more capable of answering complex genealogical questions accurately.

To enable the chat endpoint in Gramps Web API, three steps are necessary:

1. Installing required dependencies,
2. Enabling semantic search,
3. Setting up an LLM provider.

The three step are described below in turn. Finally, an owner or administrator must [configure which users can access the chat feature](users.md#configuring-who-can-use-ai-chat) in the Manage Users settings.

## Installing required dependencies

AI chat requires the Sentence Transformers and PyTorch libraries to be installed.

The standard docker images for Gramps Web already have them pre-installed for the `amd64` (e.g. 64-bit desktop PC) and `arm64` (e.g. 64-bit Raspberry Pi) architectures. Unfortunately, AI chat is not supported on the `armv7` (e.g. 32-bit Raspberry Pi) architecture due to the lack of PyTorch support.

When installing Gramps Web API via `pip` (this is not necessary when using the Docker images) the necessary dependencies are installed with

```bash
pip install gramps_webapi[ai]
```


## Enabling semantic search

If the necessary dependencies are installed, enabling semantic search can be as simple as setting the `VECTOR_EMBEDDING_MODEL` configuration option (e.g. by setting the `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` environment variable), see [Server Configuration](configuration.md). This can be any string of a model supported by the [Sentence Transformers](https://sbert.net/) library. See the documentation of this project for details and the available models.


!!! warning
    Note that the default docker images do not include a PyTorch version with GPU support. If you have access to a GPU (which will speed up the semantic indexing significantly), please install a GPU-enabled version of PyTorch.

There are several considerations to make when choosing a model.

- When you change the model, you have to manually recreate the semantic search index for your tree (or all trees in a multi-tree setup), otherwise you will encounter errors or meaningless results.
- The models are a tradeoff between accuracy/generality on the one hand and computational time/storage space on the other. If you aren't running Gramps Web API on a system that has access to a powerful GPU, bigger models are usually too slow in practice.
- Unless your entire database is in English and all your users are only expected to ask chat questions in English, you will need a multilingual embedding model, which are more rare than pure English models.


If the model is not present in the local cache, it will be downloaded when Gramps Web API is started for the first time with the new configuration. The model `sentence-transformers/distiluse-base-multilingual-cased-v2` is already available locally when using the standard docker images. This model is a good starting point and supports multilingual input.

Please share learnings about different models with the community!

!!! info
    The sentence transformers library consumes a significant amount of memory, which might cause worker processes being killed. As a rule of thumb, with semantic search enabled, each Gunicorn worker consumes around 200 MB of memory and each celery worker around 500 MB of memory even when idle, and up to 1 GB when computing embeddings. See [Limit CPU and memory usage](cpu-limited.md) for settings that limit memory usage. In addition, it is advisable to provision a sufficiently large swap partition to prevent OOM errors due to transient memory usage spikes.

## Setting up an LLM provider

Communication with the LLM uses the Pydantic AI framework, which supports OpenAI-compatible APIs. This allows using a locally deployed LLM via Ollama (see [Ollama OpenAI compatibility](https://ollama.com/blog/openai-compatibility)) or hosted APIs like OpenAI, Anthropic, or Hugging Face TGI (Text Generation Inference). The LLM is configured via the configuration parameters `LLM_MODEL` and `LLM_BASE_URL`.


### Using a hosted LLM via the OpenAI API

When using the OpenAI API, `LLM_BASE_URL` can be left unset, while `LLM_MODEL` has to be set to one of the OpenAI models, e.g. `gpt-4o-mini`. The LLM uses both RAG and tool calling to answer questions: it selects relevant information from semantic search results and can directly query the database using specialized tools. It does not require deep genealogical or historical knowledge. Therefore, you can try if a small/cheap model is sufficient.

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
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```


### Using a local LLM via Ollama

[Ollama](https://ollama.com/) is a convenient way to run LLMs locally. Please consult the Ollama documentation for details. Please note that LLMs require significant computational resources and all but the smallest models will probably be too slow without GPU support. You can try whether [`tinyllama`](https://ollama.com/library/tinyllama) meets you needs. If not, try one of the larger models. Please share any experience with the community!

When deploying Gramps Web with Docker Compose, you can add an Ollama service

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

and then set the `LLM_BASE_URL` configuration parameter to `http://ollama:11434/v1`. Set `LLM_MODEL` to a model supported by Ollama, and pull it down in your container with `ollama pull <model>`.  Finally, set `OPENAI_API_KEY` to `ollama`.

To troubleshoot problems with Ollama, you can enable debug logging by setting environment variable `OLLAMA_DEBUG=1` in the Ollama service environment.

!!! info
    If you are using Ollama for Gramps Web AI chat, please support the community by completing this documentation with any missing details.

### Using other providers

Please feel free to submit documentation for other providers and share your experience with the community!