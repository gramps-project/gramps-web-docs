# Settung up AI chat

!!! info
    AI chat requires Gramps Web API version 2.5.0 or higher.


Gramps Web API supports asking questions about the genealogical database using large language modes (LLM) via a technique called reasearch augmented generation (RAG).

RAG works as follows. First, a *vector embedding model* is used to create an index of all objects in the Gramps database in the form of numerical vectors that encode the objects' meaning. This process is similar to the creation of the full-text search index, but more computationally expensive.

Next, when a user asks a question via the chat enpoint, that question is converted to a vector as well, by the same embedding model,  and compared the objects in the Gramps database. This *semantic search* will return objects in the database that are most semantically similar to the question.

In the final step, the question and the retrieved objects are sent to an LLM to formulate an answer based on the provided information. In this way, the chatbot has access to detailed information about the contents of the genealogical database instead of relying solely on pre-existing knowledge.

To enable the chat endpoint in Gramps Web API, three steps are necessary:

1. Installing required dependencies,
2. Enabling semantic search,
3. Setting up an LLM provider.

The three step are described below in turn.

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

## Setting up an LLM provider

Communication with the LLM uses an OpenAI compatible API using the `openai-python` library. This allows using a locally deployed LLM via Ollama (see [Ollama OpenAI compatibility](https://ollama.com/blog/openai-compatibility)) or an API like OpenAI or Huggingface TGI. The LLM is configured via the configuration parameters `LLM_MODEL` and `LLM_BASE_URL`.


### Using a hosted LLM via the OpenAI API

When using the OpenAI API, `LLM_BASE_URL` can be left unset, while `LLM_MODEL` has to be set to one of the OpenAI models, e.g. `gpt-4o-mini`. Note that, due to the RAG approach, the LLM is "only" used to select the right information from the semantic search results and formulate an answer, it does not require deep genealogical or historical knowledge. Therefore, you can try if a small/cheap model is sufficient.

You will also need to sign up for an account, get an API key and store it in the `OPENAI_API_KEY` environment variable.

!!! info
    `LLM_MODEL` is a configuration parameter; if you want to set it via an environment variable, use `GRAMPSWEB_LLM_MODEL` (see [Configuration](configuration.md)). `OPENAI_API_KEY` is not a configuration parameter but an environment variable directly used by the `openai-python` library, so it should not be prefixed.


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
      ollama_data:/root/.ollama

volumes:
    ollama_data:
```

and then set the `LLM_BASE_URL` configuration parameter to `http://ollama:11434/v1` and the `LLM_MODEL` to a model supported by Ollama.

!!! info
    If you are using Ollama for Gramps Web AI chat, please support the community by completing this documentation with any missing details.

### Using other providers

Please feel free to submit documentation for other providers and share your experience with the community!