# Set up AI chat

By default, the chat assistant is disabled. To enable it, three configuration options need to be set: for the vector embedding model, chat API endpoint, and chat model.

## Set up vector embedding model

To enable semantic search that is needed for the chat assistant to work, you need an embedding model that takes a text representation of each Gramps object and converts it to a numerical vector encoding the semantic meaning of the text. Gramps Web API uses the [Sentence Transformers](https://sbert.net/) library to access these models. See the documentation of this project for details and the available models.

There are several considerations to make when choosing a model.

- When you change the model, you have to manually recreate the semantic search index for your tree (or all tree in a multi-tree setup), otherwise you will encounter errors or meaningless results.
- The models are a tradeoff between accuracy/generality on the one hand and computational time/storage space on the other. If you aren't running Gramps Web API on a system that has access to a powerful GPU, bigger models are usually too slow in practice.
- Unless your entire database is in English and all your users are only expected to ask chat questions in English, you will need a multilingual embedding model, which are more rare than pure English models.

`intfloat/multilingual-e5-small` seems to be a reasonable choice for less powerful hardware and multilingual content.

Please share learnings about different models with the community!

## Set up Chat API

The chat assistant uses the [`openai-python`](https://github.com/openai/openai-python) library to talk to large language models (LLMs). This allows you to use either an API provider or a self-hosted model.

### Using OpenAI API

If you leave the `LLM_BASE_URL` configuration option at its default, chat will use the OpenAI API. You will need to sign up for an account, get an API key and store it in the `OPENAI_API_KEY` environment variable.

### Using Ollama

[Ollama](https://ollama.com) allows running open-source LLMs locally. You can also run it in docker, e.g. using a docker-compose service as follows,

```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped

volumes:
  ollama_data:
```

The appropriate setting for `LLM_BASE_URL` would then be `http://ollama:11434/v1`.

### Using other providers

Please feel free to submit documentation for other providers and share your experience with the community!

## Set up chat model

After having set up a vector embedding model and a chat API (local or hosted), you need to choose the large language model itself. Note that the Gramps Web AI assistant mostly summarizes data that is retrieved from your genealogical database, so it doesn't kneed to be very "knowledgable" and smaller models should work reasonably well.

For OpenAI, `gpt4o-mini` is a reasonable choice. For Ollama, you can try whether [`tinyllama`](https://ollama.com/library/tinyllama) meets you needs. If not, try one of the larger models. If you find out something interesting, please share your experience with the community!