# 设置 AI 聊天

!!! info
    AI 聊天需要 Gramps Web API 版本 2.5.0 或更高版本。版本 3.6.0 引入了工具调用功能，以实现更智能的交互。

Gramps Web API 支持使用工具调用的语言模型（LLM）对家谱数据库进行提问。

## 工作原理

AI 助手使用专门的工具直接查询您的家谱数据。这些工具允许助手使用全文搜索在数据库中搜索，按特定标准过滤人员/事件/家庭/地点，计算个体之间的关系，并检索完整记录，包括备注。助手随后根据查找的记录进行回答，并在其答案中链接到这些记录。

自 Gramps Web API 3.24 起，AI 聊天不再需要向量嵌入模型。早期版本还使用 *语义搜索*（检索增强生成，RAG），它将问题的含义与为数据库中所有对象计算的数值向量索引进行比较。语义搜索已被弃用，并将在 Gramps Web API 3.25 中移除，请参见下面的 [语义搜索（已弃用）](#semantic-search-deprecated)。

要在 Gramps Web API 中启用聊天端点，需要两个步骤：

1. 安装所需的依赖项，
2. 设置 LLM 提供者。

这两个步骤将在下面依次描述。最后，所有者或管理员必须在管理用户设置中 [配置哪些用户可以访问聊天功能](users.md#configuring-who-can-use-ai-chat)。

## 安装所需的依赖项

Gramps Web 的标准 Docker 镜像已经预装了 AI 聊天所需的所有依赖项。

通过 `pip` 安装 Gramps Web API 时（使用 Docker 镜像时不需要），可以使用以下命令安装必要的依赖项：

```bash
pip install gramps_webapi[ai]
```

## 语义搜索（已弃用）

!!! warning "语义搜索已弃用"
    自 Gramps Web API 3.24 起，语义搜索已被弃用，并将在版本 3.25 中移除。AI 聊天和 [全文搜索](../user-guide/search.md) 不需要它。移除后，`VECTOR_EMBEDDING_MODEL` 设置仍然被接受但会被忽略。如果您仅设置它以启用 AI 聊天，您可以现在将其删除，以及其他 `VECTOR_EMBEDDING_*` 设置，这也节省了嵌入模型所需的内存。

本节的其余部分描述了仍在使用 Gramps Web API 3.24 的服务器的语义搜索。

如果安装了必要的依赖项，启用语义搜索可以简单地通过设置 `VECTOR_EMBEDDING_MODEL` 配置选项（例如，通过设置 `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` 环境变量）来实现，请参见 [服务器配置](configuration.md)。这可以是任何由 [Sentence Transformers](https://sbert.net/) 库支持的模型字符串。有关详细信息和可用模型，请参见该项目的文档。

!!! warning
    请注意，默认的 Docker 镜像不包括支持 GPU 的 PyTorch 版本。如果您可以访问 GPU（这将显著加快语义索引），请安装支持 GPU 的 PyTorch 版本。

选择模型时需要考虑几个因素。

- 当您更改模型时，必须手动重新创建树（或多树设置中的所有树）的语义搜索索引，否则您将遇到错误或无意义的结果。Gramps Web 会检测到配置的嵌入模型与现有索引不再匹配，并向管理员显示持续通知，提示他们从 [管理设置](../administration/settings.md#semantic-search-index) 触发完整重新索引。
- 模型在准确性/通用性与计算时间/存储空间之间存在权衡。如果您不是在具有强大 GPU 的系统上运行 Gramps Web API，则通常较大的模型在实践中速度太慢。
- 除非您的整个数据库都是英文，并且所有用户仅期望用英文提问，否则您将需要一个多语言嵌入模型，这种模型比纯英文模型更为稀缺。

如果模型不在本地缓存中，它将在第一次使用新配置启动 Gramps Web API 时下载。使用标准 Docker 镜像时，模型 `sentence-transformers/distiluse-base-multilingual-cased-v2` 已经在本地可用。该模型是一个不错的起点，并支持多语言输入。

请与社区分享有关不同模型的经验！

!!! info
    Sentence Transformers 库消耗大量内存，这可能导致工作进程被终止。作为经验法则，启用语义搜索时，每个 Gunicorn 工作进程大约消耗 200 MB 内存，每个 celery 工作进程即使在空闲时也消耗约 500 MB 内存，在计算嵌入时可高达 1 GB。有关限制内存使用的设置，请参见 [限制 CPU 和内存使用](cpu-limited.md)。此外，建议配置足够大的交换分区，以防止由于瞬时内存使用峰值而导致的 OOM 错误。

### 使用远程嵌入 API

作为运行本地 Sentence Transformers 模型的替代方案，您可以使用兼容 OpenAI 的远程嵌入 API 进行语义搜索。如果您希望将嵌入计算卸载到单独的服务（例如 [Ollama](https://ollama.com/)）、使用云嵌入提供者（例如 OpenAI），或避免将 Sentence Transformers 和 PyTorch 库加载到内存中，这将非常有用。

远程 API 必须与 [OpenAI 嵌入端点](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`) 兼容。

要使用远程嵌入 API，请设置以下配置选项（请参见 [服务器配置](configuration.md)）：

| 键 | 描述 |
|----|------|
| `VECTOR_EMBEDDING_MODEL` | 传递给远程提供者的模型名称 |
| `VECTOR_EMBEDDING_BASE_URL` | 远程 API 的基本 URL |
| `VECTOR_EMBEDDING_API_KEY` | API 密钥（仅在提供者需要身份验证时需要） |

#### 使用 Ollama 进行嵌入

在使用 Docker Compose 部署 Gramps Web 时，您可以添加一个 Ollama 服务，并将其用于嵌入和（可选）LLM：

```yaml
services:
  grampsweb: &grampsweb
    # ... 现有配置 ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... 现有配置 ...
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

启动服务后，将嵌入模型拉入 Ollama：

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    使用 Ollama 进行嵌入时，不需要 Sentence Transformers 和 PyTorch 库，这显著减少了 Gramps Web API 工作进程的内存使用。

#### 使用 OpenAI 进行嵌入

要使用 OpenAI 嵌入 API，请将基本 URL 设置为 OpenAI API，并提供您的 API 密钥：

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    更改嵌入模型需要重新索引您树中的所有记录（或多树设置中的所有树），因为不同模型生成的向量具有不同的维度。

## 设置 LLM 提供者

与 LLM 的通信使用 Pydantic AI 框架，支持兼容 OpenAI 的 API。这允许通过 Ollama 使用本地部署的 LLM（请参见 [Ollama OpenAI 兼容性](https://ollama.com/blog/openai-compatibility)）或托管 API，如 OpenAI、Anthropic 或 Hugging Face TGI（文本生成推理）。LLM 通过配置参数 `LLM_MODEL` 和 `LLM_BASE_URL` 进行配置。

### 通过 OpenAI API 使用托管 LLM

在使用 OpenAI API 时，可以不设置 `LLM_BASE_URL`，而 `LLM_MODEL` 必须设置为 OpenAI 模型之一，例如 `gpt-4o-mini`。LLM 使用工具调用来回答问题：它使用专门的工具直接查询数据库，并根据找到的记录进行回答。它不需要深厚的家谱或历史知识。因此，您可以尝试小型/便宜的模型是否足够。

您还需要注册一个帐户，获取 API 密钥并将其存储在 `OPENAI_API_KEY` 环境变量中。

!!! info
    `LLM_MODEL` 是一个配置参数；如果您想通过环境变量设置它，请使用 `GRAMPSWEB_LLM_MODEL`（请参见 [配置](configuration.md)）。`OPENAI_API_KEY` 不是配置参数，而是 Pydantic AI 库直接使用的环境变量，因此不应加前缀。

### 使用 Mistral AI

要使用 Mistral AI 的托管模型，在设置 `LLM_MODEL` 时将模型名称前缀为 `mistral:`。

您需要注册一个 Mistral AI 帐户，获取 API 密钥，并将其存储在 `MISTRAL_API_KEY` 环境变量中。无需设置 `LLM_BASE_URL`，因为 Pydantic AI 将自动使用正确的 Mistral API 端点。

使用 Docker Compose 和环境变量时的示例配置：
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### 通过 Ollama 使用本地 LLM

[Ollama](https://ollama.com/) 是在本地运行 LLM 的便捷方式。请查阅 Ollama 文档以获取详细信息。请注意，LLM 需要大量计算资源，除了最小的模型外，其他模型在没有 GPU 支持的情况下可能会太慢。由于助手依赖于工具调用，因此选择支持工具的模型，例如 [`qwen2.5`](https://ollama.com/library/qwen2.5)。从小型变体 `qwen2.5:7b` 开始，如果答案不够好，再尝试更大的模型。请与社区分享任何经验！

在使用 Docker Compose 部署 Gramps Web 时，您可以添加一个 Ollama 服务并将 Gramps Web 指向它：

```yaml
services:
  grampsweb: &grampsweb
    # ... 现有配置 ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... 现有配置 ...
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

启动服务后，将模型拉入 Ollama：

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

需要注意几点：

- 将 `LLM_MODEL` 设置为 Ollama 模型名称，包括其标签（冒号后的部分，例如 `7b`），前缀为 `ollama:`。该前缀使 Pydantic AI 使用其 Ollama 特定的模型设置，这是推荐的设置。
- `LLM_BASE_URL` 必须以 `/v1/` 结尾，例如 `http://ollama:11434/v1/`。
- 使用 `ollama:` 前缀时，无需 `OPENAI_API_KEY` 或 `OLLAMA_BASE_URL` 环境变量。如果未设置 `LLM_BASE_URL`，Gramps Web 将回退到 `OLLAMA_BASE_URL`。
- 或者，您可以省略前缀（例如 `LLM_MODEL: qwen2.5:7b`），通过其通用的兼容 OpenAI API 使用 Ollama。在这种情况下，您还必须将 `OPENAI_API_KEY` 环境变量设置为 `ollama`（任何非空值均可）。

要排查 Ollama 的问题，您可以通过在 Ollama 服务环境中设置环境变量 `OLLAMA_DEBUG=1` 来启用调试日志。

!!! info
    如果您使用 Ollama 进行 Gramps Web AI 聊天，请通过补充任何缺失的细节来支持社区完成此文档。

### 使用其他提供者

请随时提交其他提供者的文档，并与社区分享您的经验！
