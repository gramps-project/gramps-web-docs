# 设置 AI 聊天

!!! info
    AI 聊天需要 Gramps Web API 版本 2.5.0 或更高版本。版本 3.6.0 引入了工具调用功能，以实现更智能的交互。

Gramps Web API 支持使用大型语言模型（LLM）通过工具调用询问关于家谱数据库的问题。

## 工作原理

AI 助手使用专门的工具直接查询您的家谱数据。这些工具允许助手使用全文搜索在数据库中搜索，按特定标准过滤人员/事件/家庭/地点，计算个体之间的关系，并检索完整记录，包括备注。然后，助手根据查找的记录回答，并在其回答中链接到这些记录。它只从树中回答，而不是从一般知识中回答：如果树中没有记录某些内容，助手会说明这一点。对于不存在或对用户私有的对象，链接将被其文本替换。

AI 聊天不需要向量嵌入模型。Gramps Web API 3.24 之前的版本也使用了 *语义搜索*（检索增强生成，RAG），它将问题的含义与为数据库中所有对象计算的数值向量索引进行比较。语义搜索在 Gramps Web API 3.25 中被移除；`VECTOR_EMBEDDING_MODEL`、`VECTOR_EMBEDDING_BASE_URL` 和 `VECTOR_EMBEDDING_API_KEY` 设置将被忽略，可以从您的配置中移除。

要在 Gramps Web API 中启用聊天端点，需要两个步骤：

1. 安装所需的依赖项，
2. 设置 LLM 提供者。

这两个步骤将在下面依次描述。最后，所有者或管理员必须 [配置哪些用户可以访问聊天功能](users.md#configuring-who-can-use-ai-chat) 在管理用户设置中。

## 安装所需的依赖项

Gramps Web 的标准 Docker 镜像已经预装了 AI 聊天所需的所有依赖项。

通过 `pip` 安装 Gramps Web API 时（使用 Docker 镜像时不需要），可以使用以下命令安装必要的依赖项：

```bash
pip install gramps_webapi[ai]
```

## 设置 LLM 提供者

与 LLM 的通信使用 Pydantic AI 框架，该框架支持与 OpenAI 兼容的 API。这允许通过 Ollama 使用本地部署的 LLM（请参阅 [Ollama OpenAI 兼容性](https://ollama.com/blog/openai-compatibility)）或托管 API，如 OpenAI、Anthropic 或 Hugging Face TGI（文本生成推理）。LLM 通过配置参数 `LLM_MODEL` 和 `LLM_BASE_URL` 进行配置。

除了 OpenAI 兼容的 API，Pydantic AI 的提供者特定模型前缀可用于 OpenAI、Anthropic、Google、Mistral、Groq、AWS Bedrock 和 Ollama。其他提供者，如 Cohere、Hugging Face 和 xAI，未被安装；Hugging Face 推理提供者仍然可以通过其 OpenAI 兼容端点使用（`LLM_BASE_URL` 设置为 `https://router.huggingface.co/v1`）。

如果您的模型服务器不限制响应的长度，请将 `LLM_MAX_OUTPUT_TOKENS` 设置为模型每次响应可能生成的最大令牌数量（请参见 [配置](configuration.md)）。

### 通过 OpenAI API 使用托管 LLM

使用 OpenAI API 时，可以不设置 `LLM_BASE_URL`，而 `LLM_MODEL` 必须设置为 OpenAI 模型之一，例如 `gpt-4o-mini`。LLM 使用工具调用来回答问题：它直接使用专门的工具查询数据库，并根据找到的记录回答。它不需要深厚的家谱或历史知识。因此，您可以尝试使用一个小型/便宜的模型是否足够。

您还需要注册一个帐户，获取 API 密钥并将其存储在 `OPENAI_API_KEY` 环境变量中。

!!! info
    `LLM_MODEL` 是一个配置参数；如果您想通过环境变量设置它，请使用 `GRAMPSWEB_LLM_MODEL`（请参见 [配置](configuration.md)）。`OPENAI_API_KEY` 不是配置参数，而是 Pydantic AI 库直接使用的环境变量，因此不应加前缀。

### 使用 Mistral AI

要使用 Mistral AI 的托管模型，在设置 `LLM_MODEL` 时将模型名称前缀为 `mistral:`。

您需要注册一个 Mistral AI 帐户，获取 API 密钥，并将其存储在 `MISTRAL_API_KEY` 环境变量中。无需设置 `LLM_BASE_URL`，因为 Pydantic AI 会自动使用正确的 Mistral API 端点。

使用 Docker Compose 和环境变量的示例配置：
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### 通过 Ollama 使用本地 LLM

[Ollama](https://ollama.com/) 是一个方便的本地运行 LLM 的方式。请查阅 Ollama 文档以获取详细信息。请注意，LLM 需要大量计算资源，除了最小的模型外，其他模型在没有 GPU 支持的情况下可能会太慢。由于助手依赖于工具调用，请选择支持工具的模型，例如 [`qwen2.5`](https://ollama.com/library/qwen2.5)。从小型变体开始，例如 `qwen2.5:7b`，如果答案不够好，可以尝试更大的模型。请与社区分享任何经验！

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
- 另外，您可以省略前缀（例如 `LLM_MODEL: qwen2.5:7b`），通过其通用的 OpenAI 兼容 API 使用 Ollama。在这种情况下，您还必须将 `OPENAI_API_KEY` 环境变量设置为 `ollama`（任何非空值均可）。

要排查 Ollama 的问题，您可以通过在 Ollama 服务环境中设置环境变量 `OLLAMA_DEBUG=1` 来启用调试日志记录。

!!! info
    如果您在 Gramps Web AI 聊天中使用 Ollama，请通过补充任何缺失的细节来支持社区完成此文档。

### 使用其他提供者

请随时提交其他提供者的文档，并与社区分享您的经验！
