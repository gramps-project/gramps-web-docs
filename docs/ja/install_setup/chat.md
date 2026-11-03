# AIチャットの設定

!!! info
    AIチャットにはGramps Web APIバージョン2.5.0以上が必要です。バージョン3.6.0では、よりインテリジェントな対話のためのツール呼び出し機能が導入されました。

Gramps Web APIは、ツール呼び出しを使用して系譜データベースに関する質問を大規模言語モデル（LLM）に対して行うことをサポートしています。

## 仕組み

AIアシスタントは、系譜データを直接クエリするための専門的なツールを使用します。これらのツールにより、アシスタントはデータベースをフルテキスト検索で検索し、特定の基準で人々/イベント/家族/場所をフィルタリングし、個人間の関係を計算し、ノートを含む完全な記録を取得することができます。その後、アシスタントは調べた記録に基づいて回答し、回答内にそれらへのリンクを含めます。アシスタントは一般的な知識からではなく、ツリーからのみ回答します：ツリーに何かが記録されていない場合、アシスタントはその旨を伝えます。存在しないオブジェクトやユーザーにとってプライベートなオブジェクトへのリンクは、そのテキストに置き換えられます。

AIチャットはベクトル埋め込みモデルを必要としません。Gramps Web APIの3.24以前のバージョンでは、*セマンティック検索*（情報取得強化生成、RAG）が使用されており、質問の意味をデータベース内のすべてのオブジェクトに対して計算された数値ベクトルのインデックスと比較していました。セマンティック検索はGramps Web API 3.25で削除され、`VECTOR_EMBEDDING_MODEL`、`VECTOR_EMBEDDING_BASE_URL`、および`VECTOR_EMBEDDING_API_KEY`の設定は無視され、構成から削除できます。

Gramps Web APIでチャットエンドポイントを有効にするには、2つのステップが必要です：

1. 必要な依存関係のインストール、
2. LLMプロバイダーの設定。

この2つのステップについては、以下で順に説明します。最後に、オーナーまたは管理者は[チャット機能にアクセスできるユーザーを設定する](users.md#configuring-who-can-use-ai-chat)必要があります。

## 必要な依存関係のインストール

Gramps Webの標準Dockerイメージには、AIチャットに必要なすべての依存関係が事前にインストールされています。

`pip`を介してGramps Web APIをインストールする場合（Dockerイメージを使用する場合は必要ありません）、必要な依存関係は次のコマンドでインストールされます。

```bash
pip install gramps_webapi[ai]
```

## LLMプロバイダーの設定

LLMとの通信には、OpenAI互換APIをサポートするPydantic AIフレームワークが使用されます。これにより、Ollamaを介してローカルにデプロイされたLLM（[OllamaのOpenAI互換性](https://ollama.com/blog/openai-compatibility)を参照）や、OpenAI、Anthropic、Hugging Face TGI（テキスト生成推論）などのホスティングAPIを使用できます。LLMは、構成パラメータ`LLM_MODEL`および`LLM_BASE_URL`を介して設定されます。

OpenAI互換APIの他に、Pydantic AIのプロバイダー固有のモデルプレフィックスをOpenAI、Anthropic、Google、Mistral、Groq、AWS Bedrock、Ollamaに使用できます。Cohere、Hugging Face、xAIなどの他のプロバイダーはインストールされていませんが、Hugging Face推論プロバイダーはOpenAI互換エンドポイント（`LLM_BASE_URL`を`https://router.huggingface.co/v1`に設定）を介して使用できます。

モデルサーバーが応答の長さを制限していない場合、`LLM_MAX_OUTPUT_TOKENS`をモデルが応答ごとに生成できる最大トークン数に設定します（[構成](configuration.md)を参照）。

### OpenAI APIを介してホストされたLLMの使用

OpenAI APIを使用する場合、`LLM_BASE_URL`は設定しなくてもよく、`LLM_MODEL`はOpenAIモデルの1つ（例：`gpt-4o-mini`）に設定する必要があります。LLMはツール呼び出しを使用して質問に答えます：専門的なツールを使用してデータベースを直接クエリし、見つけた記録に基づいて回答します。深い系譜的または歴史的知識は必要ありません。したがって、小型または安価なモデルが十分かどうかを試すことができます。

アカウントにサインアップし、APIキーを取得して、`OPENAI_API_KEY`環境変数に保存する必要があります。

!!! info
    `LLM_MODEL`は構成パラメータです。環境変数を介して設定したい場合は、`GRAMPSWEB_LLM_MODEL`を使用します（[構成](configuration.md)を参照）。`OPENAI_API_KEY`は構成パラメータではなく、Pydantic AIライブラリによって直接使用される環境変数であるため、プレフィックスを付けるべきではありません。

### Mistral AIの使用

Mistral AIのホストされたモデルを使用するには、`LLM_MODEL`を設定する際にモデル名の前に`mistral:`を付けます。

Mistral AIのアカウントにサインアップし、APIキーを取得して、`MISTRAL_API_KEY`環境変数に保存する必要があります。Pydantic AIは自動的に正しいMistral APIエンドポイントを使用するため、`LLM_BASE_URL`を設定する必要はありません。

環境変数を使用してdocker composeを使用する際の例の構成：
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Ollamaを介してローカルLLMの使用

[Ollama](https://ollama.com/)は、LLMをローカルで実行する便利な方法です。詳細についてはOllamaのドキュメントを参照してください。LLMはかなりの計算リソースを必要とし、最小のモデルを除いてはGPUサポートなしでは遅すぎる可能性があります。アシスタントはツール呼び出しに依存しているため、ツールをサポートするモデルを選択してください。たとえば、[`qwen2.5`](https://ollama.com/library/qwen2.5)のようなモデルです。最初は`qwen2.5:7b`のような小型のバリアントから始め、回答が十分でない場合は大きなモデルを試してください。コミュニティと経験を共有してください！

Docker ComposeでGramps Webをデプロイする際に、Ollamaサービスを追加し、Gramps Webをそれにポイントすることができます：

```yaml
services:
  grampsweb: &grampsweb
    # ... 既存の設定 ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... 既存の設定 ...
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

サービスを起動した後、Ollamaにモデルをプルします：

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

注意すべき点：

- `LLM_MODEL`をOllamaモデル名に設定し、タグ（コロンの後の部分、例：`7b`）を含め、`ollama:`を前に付けます。このプレフィックスにより、Pydantic AIはモデルに対してOllama固有の設定を使用します。これは推奨される設定です。
- `LLM_BASE_URL`は`/v1/`で終わる必要があります。例：`http://ollama:11434/v1/`。
- `ollama:`プレフィックスを使用する場合、`OPENAI_API_KEY`や`OLLAMA_BASE_URL`環境変数は必要ありません。`LLM_BASE_URL`が設定されていない場合、Gramps Webは`OLLAMA_BASE_URL`にフォールバックします。
- あるいは、プレフィックスを省略して（例：`LLM_MODEL: qwen2.5:7b`）Ollamaをその一般的なOpenAI互換APIを介して使用することもできます。この場合、`OPENAI_API_KEY`環境変数を`ollama`（空でない任意の値）に設定する必要があります。

Ollamaに関する問題をトラブルシューティングするために、Ollamaサービスの環境で環境変数`OLLAMA_DEBUG=1`を設定してデバッグログを有効にできます。

!!! info
    Gramps Web AIチャットにOllamaを使用している場合は、コミュニティをサポートするために、欠落している詳細をこのドキュメントに追加してください。

### 他のプロバイダーの使用

他のプロバイダーに関するドキュメントを提出し、コミュニティと経験を共有してください！
