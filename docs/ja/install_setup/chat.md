# AIチャットの設定

!!! info
    AIチャットにはGramps Web APIバージョン2.5.0以上が必要です。バージョン3.6.0では、よりインテリジェントな対話のためのツール呼び出し機能が導入されました。

Gramps Web APIは、ツール呼び出しを使用して系譜データベースに関する質問を行うための大規模言語モデル（LLM）をサポートしています。

## 仕組み

AIアシスタントは、系譜データを直接照会するための専門的なツールを使用します。これらのツールにより、アシスタントはデータベースをフルテキスト検索し、特定の基準で人々/イベント/家族/場所をフィルタリングし、個人間の関係を計算し、メモを含む完全な記録を取得することができます。アシスタントは、検索した記録に基づいて回答し、回答内でそれらへのリンクを提供します。アシスタントは、一般的な知識からではなく、ツリーからのみ回答します。ツリーに記録がない場合、アシスタントはその旨を伝えます。存在しないオブジェクトやユーザーにとってプライベートなオブジェクトへのリンクは、そのテキストに置き換えられます。

AIチャットにはベクトル埋め込みモデルは必要ありません。Gramps Web APIのバージョン3.24以前では、*意味検索*（情報強化生成、RAG）が使用されており、質問の意味をデータベース内のすべてのオブジェクトに対して計算された数値ベクトルのインデックスと比較していました。意味検索はGramps Web API 3.25で削除され、`VECTOR_EMBEDDING_MODEL`、`VECTOR_EMBEDDING_BASE_URL`、および`VECTOR_EMBEDDING_API_KEY`の設定は無視され、構成から削除できます。

Gramps Web APIでチャットエンドポイントを有効にするには、2つのステップが必要です。

1. 必要な依存関係のインストール、
2. LLMプロバイダーの設定。

これらの2つのステップについては、以下で順に説明します。最後に、オーナーまたは管理者は[チャット機能にアクセスできるユーザーを設定する](users.md#configuring-who-can-use-ai-chat)必要があります。

## 必要な依存関係のインストール

Gramps Webの標準Dockerイメージには、AIチャットに必要なすべての依存関係が事前にインストールされています。

`pip`を使用してGramps Web APIをインストールする場合（Dockerイメージを使用する場合は必要ありません）、必要な依存関係は以下のコマンドでインストールされます。

```bash
pip install gramps_webapi[ai]
```

## LLMプロバイダーの設定

LLMとの通信には、OpenAI互換APIをサポートするPydantic AIフレームワークが使用されます。これにより、Ollamaを介してローカルにデプロイされたLLM（[OllamaのOpenAI互換性](https://ollama.com/blog/openai-compatibility)を参照）や、OpenAI、Anthropic、Hugging Face TGI（テキスト生成推論）などのホスティングAPIを使用できます。LLMは、設定パラメーター`LLM_MODEL`と`LLM_BASE_URL`を介して構成されます。

OpenAI互換APIの他に、Pydantic AIのプロバイダー固有のモデルプレフィックスは、OpenAI、Anthropic、Google、Mistral、Groq、AWS Bedrock、Ollamaに使用できます。Cohere、Hugging Face、xAIなどの他のプロバイダーはインストールされていませんが、Hugging Face Inference ProvidersはOpenAI互換エンドポイント（`LLM_BASE_URL`を`https://router.huggingface.co/v1`に設定）を介して使用できます。

モデルサーバーが応答の長さを制限していない場合は、`LLM_MAX_OUTPUT_TOKENS`をモデルが応答ごとに生成できる最大トークン数に設定してください（[設定](configuration.md)を参照）。

### OpenAI APIを介したホスティングされたLLMの使用

OpenAI APIを使用する場合、`LLM_BASE_URL`は設定しなくてもよく、`LLM_MODEL`はOpenAIモデルの1つ（例：`gpt-4o-mini`）に設定する必要があります。LLMはツール呼び出しを使用して質問に回答します：専門的なツールを使用してデータベースを直接照会し、見つけた記録に基づいて回答します。深い系譜学や歴史的知識は必要ありません。したがって、小さな/安価なモデルで十分かどうか試すことができます。

また、アカウントにサインアップし、APIキーを取得して、`OPENAI_API_KEY`環境変数に保存する必要があります。

!!! info
    `LLM_MODEL`は設定パラメーターです。環境変数を介して設定したい場合は、`GRAMPSWEB_LLM_MODEL`を使用してください（[設定](configuration.md)を参照）。`OPENAI_API_KEY`は設定パラメーターではなく、Pydantic AIライブラリによって直接使用される環境変数であるため、プレフィックスを付けないでください。

### Mistral AIの使用

Mistral AIのホスティングモデルを使用するには、`LLM_MODEL`を設定する際にモデル名の前に`mistral:`を付けます。

Mistral AIアカウントにサインアップし、APIキーを取得して、`MISTRAL_API_KEY`環境変数に保存する必要があります。Pydantic AIは自動的に正しいMistral APIエンドポイントを使用するため、`LLM_BASE_URL`を設定する必要はありません。

環境変数を使用してdocker composeを使用する際の例の設定：
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Ollamaを介したローカルLLMの使用

[Ollama](https://ollama.com/)は、LLMをローカルで実行する便利な方法です。詳細についてはOllamaのドキュメントを参照してください。LLMはかなりの計算リソースを必要とし、最小のモデルを除いて、GPUサポートなしではおそらく遅すぎることに注意してください。アシスタントはツール呼び出しに依存しているため、ツールをサポートするモデルを選択してください。例えば、[`qwen2.5`](https://ollama.com/library/qwen2.5)のようなモデルです。最初は`qwen2.5:7b`のような小さなバリアントから始め、回答が十分でない場合は大きなものを試してください。コミュニティと経験を共有してください！

Docker ComposeでGramps Webをデプロイする際には、Ollamaサービスを追加し、Gramps Webをそれにポイントできます：

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

いくつかの注意点：

- `LLM_MODEL`をOllamaモデル名に設定し、そのタグ（コロンの後の部分、例：`7b`）を付けて、`ollama:`をプレフィックスとして付けます。このプレフィックスにより、Pydantic AIはモデルに対してOllama固有の設定を使用します。これが推奨される設定です。
- `LLM_BASE_URL`は`/v1/`で終わる必要があります。例：`http://ollama:11434/v1/`。
- `ollama:`プレフィックスを使用する場合、`OPENAI_API_KEY`や`OLLAMA_BASE_URL`環境変数は必要ありません。`LLM_BASE_URL`が設定されていない場合、Gramps Webは`OLLAMA_BASE_URL`にフォールバックします。
- 代わりにプレフィックスを省略（例：`LLM_MODEL: qwen2.5:7b`）し、Ollamaを一般的なOpenAI互換APIを介して使用することもできます。この場合、`OPENAI_API_KEY`環境変数を`ollama`（空でない任意の値）に設定する必要があります。

Ollamaに関する問題をトラブルシューティングするには、Ollamaサービスの環境で環境変数`OLLAMA_DEBUG=1`を設定してデバッグログを有効にできます。

!!! info
    Gramps Web AIチャットにOllamaを使用している場合は、コミュニティをサポートするために、欠けている詳細をこのドキュメントに追加してください。

### 他のプロバイダーの使用

他のプロバイダーのドキュメントを提出し、コミュニティと経験を共有してください！

## オプション機能

### 質問に画像を含める

モデルが画像を受け入れる場合、`LLM_VISION`を`True`に設定して、ユーザーが質問に画像を添付できるようにします。たとえば、記録のスキャン（Gramps Web API 3.26以上）。画像は、モデルに送信される前に、長辺が最大1568ピクセルになるように縮小されます。モデルが本当に画像入力をサポートしていることを確認してください：多くの小さなローカルモデルはサポートしておらず、プロバイダーは画像を含む質問を拒否します。

### アシスタントに変更を提案させる

`LLM_ALLOW_WRITE_PROPOSALS`を`True`に設定すると（Gramps Web API 3.26以上）、アシスタントは[ツリーに変更を提案する](../user-guide/chat.md#letting-the-assistant-change-your-tree)ことができ、ユーザーはそれをレビューした後に適用します。アシスタント自体はデータベースに書き込むことはありません。提案は、オブジェクトを追加、編集、削除できるユーザー、すなわちエディター以上のユーザーにのみ提供され、チャットを使用できるユーザーに限ります。

正しい提案を書くことは、質問に答えるよりもモデルにとって難しいため、ユーザーに対して有効にする前にモデルでテストしてください。追加のツールにより、モデルへの各リクエストも若干大きくなります。
