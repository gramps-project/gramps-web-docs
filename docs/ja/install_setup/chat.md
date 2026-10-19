# AIチャットの設定

!!! info
    AIチャットにはGramps Web APIバージョン2.5.0以上が必要です。バージョン3.6.0では、よりインテリジェントなインタラクションのためのツール呼び出し機能が導入されました。

Gramps Web APIは、ツール呼び出しを使用して系譜データベースに関する質問を大規模言語モデル（LLM）に対して行うことをサポートしています。

## 仕組み

AIアシスタントは、系譜データを直接クエリするための専門的なツールを使用します。これらのツールにより、アシスタントはデータベースをフルテキスト検索で検索し、特定の基準に基づいて人々/イベント/家族/場所をフィルタリングし、個人間の関係を計算し、ノートを含む完全な記録を取得します。アシスタントは、調べた記録に基づいて回答し、それらへのリンクを回答に含めます。

Gramps Web API 3.24以降、AIチャットはもはやベクトル埋め込みモデルを必要としません。以前のバージョンでは、*セマンティック検索*（情報取得拡張生成、RAG）も使用されており、これは質問の意味をデータベース内のすべてのオブジェクトに対して計算された数値ベクトルのインデックスと比較します。セマンティック検索は非推奨となり、Gramps Web API 3.25で削除される予定です。詳細は以下の[セマンティック検索（非推奨）](#semantic-search-deprecated)を参照してください。

Gramps Web APIでチャットエンドポイントを有効にするには、2つのステップが必要です。

1. 必要な依存関係のインストール
2. LLMプロバイダーの設定

この2つのステップについては、以下で順に説明します。最後に、オーナーまたは管理者は[どのユーザーがチャット機能にアクセスできるかを設定](users.md#configuring-who-can-use-ai-chat)する必要があります。

## 必要な依存関係のインストール

Gramps Webの標準Dockerイメージには、AIチャットに必要なすべての依存関係が事前にインストールされています。

`pip`を使用してGramps Web APIをインストールする場合（Dockerイメージを使用している場合は必要ありません）、必要な依存関係は次のコマンドでインストールされます。

```bash
pip install gramps_webapi[ai]
```

## セマンティック検索（非推奨）

!!! warning "セマンティック検索は非推奨です"
    セマンティック検索はGramps Web API 3.24以降非推奨となり、バージョン3.25で削除されます。AIチャットおよび[フルテキスト検索](../user-guide/search.md)はそれを必要としません。削除後、`VECTOR_EMBEDDING_MODEL`設定は引き続き受け入れられますが、無視されます。AIチャットを有効にするためだけに設定している場合は、他の`VECTOR_EMBEDDING_*`設定とともに削除できます。これにより、埋め込みモデルが必要とするメモリも節約できます。

このセクションの残りの部分では、Gramps Web API 3.24でまだセマンティック検索を使用しているサーバー向けに説明します。

必要な依存関係がインストールされている場合、セマンティック検索を有効にするのは、`VECTOR_EMBEDDING_MODEL`構成オプションを設定する（例：`GRAMPSWEB_VECTOR_EMBEDDING_MODEL`環境変数を設定する）だけで簡単です。詳細は[サーバー構成](configuration.md)を参照してください。これは、[Sentence Transformers](https://sbert.net/)ライブラリによってサポートされている任意のモデル名の文字列である必要があります。このプロジェクトのドキュメントで詳細と利用可能なモデルを確認してください。

!!! warning
    デフォルトのDockerイメージには、GPUサポートのあるPyTorchバージョンが含まれていないことに注意してください。GPUにアクセスできる場合（セマンティックインデックスを大幅に高速化します）、GPU対応のPyTorchバージョンをインストールしてください。

モデルを選択する際には、いくつかの考慮事項があります。

- モデルを変更すると、ツリー（またはマルチツリー構成のすべてのツリー）のセマンティック検索インデックスを手動で再作成する必要があります。そうしないと、エラーや無意味な結果が発生します。Gramps Webは、構成された埋め込みモデルが既存のインデックスと一致しなくなったときに検出し、管理者に完全な再インデックスをトリガーするよう促す持続的な通知を表示します。[管理設定](../administration/settings.md#semantic-search-index)から再インデックスをトリガーできます。
- モデルは、正確性/一般性と計算時間/ストレージスペースのトレードオフです。強力なGPUにアクセスできないシステムでGramps Web APIを実行している場合、大きなモデルは実際には通常遅すぎます。
- データベース全体が英語であり、すべてのユーザーが英語でチャット質問をすることが期待されている場合を除き、多言語埋め込みモデルが必要です。これは、純粋な英語モデルよりも珍しいです。

モデルがローカルキャッシュに存在しない場合、新しい構成でGramps Web APIが初めて起動されるときにダウンロードされます。標準のDockerイメージを使用している場合、モデル`sentence-transformers/distiluse-base-multilingual-cased-v2`はすでにローカルに利用可能です。このモデルは良い出発点であり、多言語入力をサポートしています。

異なるモデルについての学びをコミュニティと共有してください！

!!! info
    Sentence Transformersライブラリは大量のメモリを消費するため、ワーカープロセスが終了する可能性があります。一般的な目安として、セマンティック検索が有効な場合、各Gunicornワーカーは約200MBのメモリを消費し、各Celeryワーカーはアイドル状態でも約500MBのメモリを消費し、埋め込みを計算しているときは最大1GBになります。メモリ使用量を制限する設定については[CPUおよびメモリ使用量の制限](cpu-limited.md)を参照してください。さらに、一時的なメモリ使用量のスパイクによるOOMエラーを防ぐために、十分に大きなスワップパーティションを用意することをお勧めします。

### リモート埋め込みAPIの使用

ローカルのSentence Transformersモデルを実行する代わりに、セマンティック検索のためにリモートのOpenAI互換埋め込みAPIを使用することができます。これは、埋め込み計算を別のサービス（例：[Ollama](https://ollama.com/)）にオフロードしたり、クラウド埋め込みプロバイダー（例：OpenAI）を使用したり、Sentence TransformersおよびPyTorchライブラリをメモリにロードするのを避けたりするのに便利です。

リモートAPIは、[OpenAI埋め込みエンドポイント](https://platform.openai.com/docs/api-reference/embeddings)（`/v1/embeddings`）と互換性がある必要があります。

リモート埋め込みAPIを使用するには、次の構成オプションを設定します（[サーバー構成](configuration.md)を参照）：

キー | 説明
----|-------------
`VECTOR_EMBEDDING_MODEL` | リモートプロバイダーに渡すモデル名
`VECTOR_EMBEDDING_BASE_URL` | リモートAPIのベースURL
`VECTOR_EMBEDDING_API_KEY` | APIキー（プロバイダーが認証を必要とする場合のみ必要）

#### Ollamaを使用した埋め込み

Docker ComposeでGramps Webをデプロイする際に、Ollamaサービスを追加し、埋め込みと（オプションで）LLMの両方に使用できます：

```yaml
services:
  grampsweb: &grampsweb
    # ... 既存の設定 ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... 既存の設定 ...
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

サービスを起動した後、Ollamaに埋め込みモデルをプルします：

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Ollamaを埋め込みに使用する場合、Sentence TransformersおよびPyTorchライブラリは必要なく、Gramps Web APIワーカーのメモリ使用量が大幅に削減されます。

#### OpenAIを使用した埋め込み

OpenAI埋め込みAPIを使用するには、ベースURLをOpenAI APIに設定し、APIキーを提供します：

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    埋め込みモデルを変更すると、ツリー（またはマルチツリー構成のすべてのツリー）のすべてのレコードを再インデックスする必要があります。なぜなら、異なるモデルは異なる次元のベクトルを生成するからです。

## LLMプロバイダーの設定

LLMとの通信には、OpenAI互換APIをサポートするPydantic AIフレームワークを使用します。これにより、Ollamaを介してローカルにデプロイされたLLM（[OllamaのOpenAI互換性](https://ollama.com/blog/openai-compatibility)を参照）や、OpenAI、Anthropic、Hugging Face TGI（テキスト生成推論）などのホスティングされたAPIを使用できます。LLMは、構成パラメータ`LLM_MODEL`および`LLM_BASE_URL`を介して設定されます。

### OpenAI APIを介したホスティングされたLLMの使用

OpenAI APIを使用する場合、`LLM_BASE_URL`は設定しなくてもよく、`LLM_MODEL`はOpenAIモデルの1つ（例：`gpt-4o-mini`）に設定する必要があります。LLMはツール呼び出しを使用して質問に回答します：専門的なツールを使用してデータベースを直接クエリし、見つけた記録に基づいて回答します。系譜や歴史に関する深い知識は必要ありません。したがって、小さな/安価なモデルで十分かどうかを試すことができます。

また、アカウントにサインアップし、APIキーを取得して`OPENAI_API_KEY`環境変数に保存する必要があります。

!!! info
    `LLM_MODEL`は構成パラメータです。環境変数を介して設定したい場合は、`GRAMPSWEB_LLM_MODEL`を使用します（[構成](configuration.md)を参照）。`OPENAI_API_KEY`は構成パラメータではなく、Pydantic AIライブラリによって直接使用される環境変数であるため、プレフィックスを付けるべきではありません。

### Mistral AIの使用

Mistral AIのホスティングされたモデルを使用するには、`LLM_MODEL`を設定する際にモデル名の前に`mistral:`を付けます。

Mistral AIのアカウントにサインアップし、APIキーを取得して`MISTRAL_API_KEY`環境変数に保存する必要があります。Pydantic AIは自動的に正しいMistral APIエンドポイントを使用するため、`LLM_BASE_URL`を設定する必要はありません。

環境変数を使用してDocker Composeで使用する際の例の設定：
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Ollamaを介したローカルLLMの使用

[Ollama](https://ollama.com/)は、LLMをローカルで実行する便利な方法です。詳細についてはOllamaのドキュメントを参照してください。LLMはかなりの計算リソースを必要とし、最小のモデルを除いて、GPUサポートなしではおそらく遅すぎることに注意してください。アシスタントはツール呼び出しに依存しているため、ツールをサポートするモデルを選択してください。例えば、[`qwen2.5`](https://ollama.com/library/qwen2.5)などです。最初は`qwen2.5:7b`のような小さなバリアントから始め、回答が十分でない場合は大きなものを試してください。コミュニティと経験を共有してください！

Docker ComposeでGramps Webをデプロイする際に、Ollamaサービスを追加し、Gramps Webをそれに指し示すことができます：

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

- `LLM_MODEL`をOllamaモデル名に設定し、そのタグ（コロンの後の部分、例：`7b`）を含めて`ollama:`でプレフィックスを付けます。このプレフィックスにより、Pydantic AIはモデルのOllama固有の設定を使用します。これが推奨される設定です。
- `LLM_BASE_URL`は`/v1/`で終わる必要があります。例：`http://ollama:11434/v1/`。
- `ollama:`プレフィックスを使用する場合、`OPENAI_API_KEY`や`OLLAMA_BASE_URL`環境変数は必要ありません。`LLM_BASE_URL`が設定されていない場合、Gramps Webは`OLLAMA_BASE_URL`にフォールバックします。
- 代わりにプレフィックスを省略して（例：`LLM_MODEL: qwen2.5:7b`）Ollamaを一般的なOpenAI互換APIを介して使用することもできます。この場合、`OPENAI_API_KEY`環境変数を`ollama`（空でない任意の値）に設定する必要があります。

Ollamaに関する問題をトラブルシューティングするには、Ollamaサービス環境で環境変数`OLLAMA_DEBUG=1`を設定してデバッグログを有効にできます。

!!! info
    Gramps Web AIチャットにOllamaを使用している場合、コミュニティをサポートするために、欠落している詳細をこのドキュメントに追加してください。

### 他のプロバイダーの使用

他のプロバイダーに関するドキュメントを提出し、コミュニティと経験を共有してください！
