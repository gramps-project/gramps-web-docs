# 设置 AI 聊天

!!! info
    AI 聊天需要 Gramps Web API 版本 2.5.0 或更高版本。版本 3.6.0 引入了工具调用功能，以实现更智能的交互。

Gramps Web API 支持通过一种称为检索增强生成（RAG）结合工具调用的技术，使用大型语言模型（LLM）询问关于家谱数据库的问题。

## 工作原理

AI 助手使用两种互补的方法：

**检索增强生成（RAG）**：一个 *向量嵌入模型* 创建一个 Gramps 数据库中所有对象的索引，以数值向量的形式编码对象的含义。当用户提出问题时，该问题也会被转换为向量，并与数据库中的对象进行比较。这个 *语义搜索* 返回与问题在语义上最相似的对象。

**工具调用（v3.6.0+）**：AI 助手现在可以使用专门的工具直接查询您的家谱数据。这些工具允许助手搜索数据库，按特定标准过滤人员/事件/家庭/地点，计算个体之间的关系，并检索详细的对象信息。这使得助手能够更准确地回答复杂的家谱问题。

要在 Gramps Web API 中启用聊天端点，需要三个步骤：

1. 安装所需的依赖项，
2. 启用语义搜索，
3. 设置 LLM 提供者。

这三个步骤将在下面逐一描述。最后，所有者或管理员必须在管理用户设置中 [配置哪些用户可以访问聊天功能](users.md#configuring-who-can-use-ai-chat)。

## 安装所需的依赖项

AI 聊天需要安装 Sentence Transformers 和 PyTorch 库。

Gramps Web 的标准 Docker 镜像已经为 `amd64`（例如 64 位桌面 PC）和 `arm64`（例如 64 位 Raspberry Pi）架构预安装了这些库。不幸的是，由于缺乏 PyTorch 支持，AI 聊天不支持 `armv7`（例如 32 位 Raspberry Pi）架构。

通过 `pip` 安装 Gramps Web API 时（使用 Docker 镜像时不需要此步骤），可以通过以下命令安装所需的依赖项：

```bash
pip install gramps_webapi[ai]
```

## 启用语义搜索

如果已安装所需的依赖项，启用语义搜索可以像设置 `VECTOR_EMBEDDING_MODEL` 配置选项一样简单（例如，通过设置 `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` 环境变量），请参见 [服务器配置](configuration.md)。这可以是任何由 [Sentence Transformers](https://sbert.net/) 库支持的模型字符串。有关详细信息和可用模型，请参阅该项目的文档。

!!! warning
    请注意，默认的 Docker 镜像不包括支持 GPU 的 PyTorch 版本。如果您可以访问 GPU（这将显著加快语义索引的速度），请安装支持 GPU 的 PyTorch 版本。

选择模型时需要考虑几个因素。

- 当您更改模型时，必须手动重新创建您树的语义搜索索引（或在多树设置中重新创建所有树的索引），否则您将遇到错误或无意义的结果。
- 模型在准确性/通用性和计算时间/存储空间之间是一个权衡。如果您不是在拥有强大 GPU 的系统上运行 Gramps Web API，通常较大的模型在实践中会太慢。
- 除非您的整个数据库都是英文，并且所有用户仅期望用英文提问聊天问题，否则您将需要一个多语言嵌入模型，这比纯英文模型更为稀缺。

如果模型不在本地缓存中，它将在首次使用新配置启动 Gramps Web API 时下载。使用标准 Docker 镜像时，模型 `sentence-transformers/distiluse-base-multilingual-cased-v2` 已经在本地可用。该模型是一个不错的起点，并支持多语言输入。

请与社区分享关于不同模型的经验！

!!! info
    Sentence Transformers 库消耗大量内存，这可能导致工作进程被杀死。作为经验法则，启用语义搜索时，每个 Gunicorn 工作进程大约消耗 200 MB 内存，每个 Celery 工作进程即使在空闲时也消耗约 500 MB 内存，在计算嵌入时可高达 1 GB。请参见 [限制 CPU 和内存使用](cpu-limited.md) 以获取限制内存使用的设置。此外，建议配置足够大的交换分区，以防止因瞬时内存使用峰值而导致的 OOM 错误。

## 设置 LLM 提供者

与 LLM 的通信使用 Pydantic AI 框架，该框架支持与 OpenAI 兼容的 API。这允许通过 Ollama 使用本地部署的 LLM（请参见 [Ollama OpenAI 兼容性](https://ollama.com/blog/openai-compatibility)）或托管 API，如 OpenAI、Anthropic 或 Hugging Face TGI（文本生成推理）。LLM 通过配置参数 `LLM_MODEL` 和 `LLM_BASE_URL` 进行配置。

### 通过 OpenAI API 使用托管 LLM

使用 OpenAI API 时，可以不设置 `LLM_BASE_URL`，而 `LLM_MODEL` 必须设置为 OpenAI 模型之一，例如 `gpt-4o-mini`。LLM 使用 RAG 和工具调用来回答问题：它从语义搜索结果中选择相关信息，并可以使用专门的工具直接查询数据库。它不需要深厚的家谱或历史知识。因此，您可以尝试小型/廉价模型是否足够。

您还需要注册一个帐户，获取 API 密钥并将其存储在 `OPENAI_API_KEY` 环境变量中。

!!! info
    `LLM_MODEL` 是一个配置参数；如果您想通过环境变量设置它，请使用 `GRAMPSWEB_LLM_MODEL`（请参见 [配置](configuration.md)）。`OPENAI_API_KEY` 不是配置参数，而是 Pydantic AI 库直接使用的环境变量，因此不应加前缀。

### 使用 Mistral AI

要使用 Mistral AI 的托管模型，在设置 `LLM_MODEL` 时将模型名称前缀为 `mistral:`。

您需要注册一个 Mistral AI 帐户，获取 API 密钥，并将其存储在 `MISTRAL_API_KEY` 环境变量中。无需设置 `LLM_BASE_URL`，因为 Pydantic AI 会自动使用正确的 Mistral API 端点。

使用 Docker Compose 和环境变量时的示例配置：
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### 通过 Ollama 使用本地 LLM

[Ollama](https://ollama.com/) 是一种方便的本地运行 LLM 的方式。请查阅 Ollama 文档以获取详细信息。请注意，LLM 需要大量计算资源，除了最小的模型外，其他模型在没有 GPU 支持的情况下可能会太慢。您可以尝试 [`tinyllama`](https://ollama.com/library/tinyllama) 是否满足您的需求。如果不满足，请尝试更大的模型。请与社区分享任何经验！

在使用 Docker Compose 部署 Gramps Web 时，您可以添加 Ollama 服务：

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

然后将 `LLM_BASE_URL` 配置参数设置为 `http://ollama:11434/v1`。将 `LLM_MODEL` 设置为 Ollama 支持的模型，并在您的容器中使用 `ollama pull <model>` 下载它。最后，将 `OPENAI_API_KEY` 设置为 `ollama`。

要排查 Ollama 的问题，您可以通过在 Ollama 服务环境中设置环境变量 `OLLAMA_DEBUG=1` 来启用调试日志。

!!! info
    如果您在 Gramps Web AI 聊天中使用 Ollama，请通过补充任何缺失的细节来支持社区。

### 使用其他提供者

请随时提交其他提供者的文档，并与社区分享您的经验！
