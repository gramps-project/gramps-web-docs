# AIチャットの設定

!!! info
    AIチャットにはGramps Web APIバージョン2.5.0以上が必要です。バージョン3.6.0では、よりインテリジェントな対話のためのツール呼び出し機能が導入されました。

Gramps Web APIは、リトリーバル拡張生成（RAG）とツール呼び出しを組み合わせた技術を使用して、大規模言語モデル（LLM）を介して系譜データベースに関する質問を行うことをサポートしています。

## 仕組み

AIアシスタントは、2つの補完的なアプローチを使用します。

**リトリーバル拡張生成（RAG）**: *ベクトル埋め込みモデル*が、Grampsデータベース内のすべてのオブジェクトのインデックスを、オブジェクトの意味をエンコードした数値ベクトルの形で作成します。ユーザーが質問をすると、その質問もベクトルに変換され、データベース内のオブジェクトと比較されます。この*セマンティック検索*は、質問に最も意味的に類似したオブジェクトを返します。

**ツール呼び出し（v3.6.0+）**: AIアシスタントは、系譜データを直接クエリするために専門のツールを使用できるようになりました。これらのツールを使用することで、アシスタントはデータベースを検索し、特定の基準で人々/イベント/家族/場所をフィルタリングし、個人間の関係を計算し、詳細なオブジェクト情報を取得することができます。これにより、アシスタントは複雑な系譜の質問に正確に答える能力が大幅に向上します。

Gramps Web APIでチャットエンドポイントを有効にするには、3つのステップが必要です。

1. 必要な依存関係のインストール、
2. セマンティック検索の有効化、
3. LLMプロバイダーの設定。

これらの3つのステップについては、以下で順に説明します。最後に、オーナーまたは管理者は[どのユーザーがチャット機能にアクセスできるかを設定する](users.md#configuring-who-can-use-ai-chat)必要があります。

## 必要な依存関係のインストール

AIチャットには、Sentence TransformersとPyTorchライブラリのインストールが必要です。

Gramps Webの標準Dockerイメージには、`amd64`（例：64ビットデスクトップPC）および`arm64`（例：64ビットRaspberry Pi）アーキテクチャ用にこれらが事前にインストールされています。残念ながら、AIチャットはPyTorchのサポートがないため、`armv7`（例：32ビットRaspberry Pi）アーキテクチャではサポートされていません。

Gramps Web APIを`pip`経由でインストールする際（Dockerイメージを使用している場合は必要ありません）、必要な依存関係は次のコマンドでインストールされます。

```bash
pip install gramps_webapi[ai]
```

## セマンティック検索の有効化

必要な依存関係がインストールされている場合、セマンティック検索の有効化は、`VECTOR_EMBEDDING_MODEL`設定オプションを設定すること（例：`GRAMPSWEB_VECTOR_EMBEDDING_MODEL`環境変数を設定すること）で簡単に行えます。詳細については[サーバー設定](configuration.md)を参照してください。これは、[Sentence Transformers](https://sbert.net/)ライブラリによってサポートされているモデルの任意の文字列である必要があります。このプロジェクトのドキュメントで詳細と利用可能なモデルを確認してください。

!!! warning
    デフォルトのDockerイメージには、GPUサポートのあるPyTorchバージョンは含まれていないことに注意してください。GPUにアクセスできる場合（セマンティックインデックスの速度が大幅に向上します）、GPU対応のPyTorchバージョンをインストールしてください。

モデルを選択する際には、いくつかの考慮事項があります。

- モデルを変更すると、ツリー（またはマルチツリー設定のすべてのツリー）のセマンティック検索インデックスを手動で再作成する必要があります。そうしないと、エラーや無意味な結果が発生します。Gramps Webは、設定された埋め込みモデルが既存のインデックスと一致しなくなったときに検出し、管理者に完全な再インデックスをトリガーするよう促す持続的な通知を表示します。[管理設定](../administration/settings.md#semantic-search-index)から再インデックスを実行できます。
- モデルは、精度/一般性と計算時間/ストレージスペースのトレードオフです。強力なGPUにアクセスできないシステムでGramps Web APIを実行している場合、大きなモデルは通常、実際には遅すぎます。
- データベース全体が英語であり、すべてのユーザーが英語でチャット質問をすることが期待される場合を除き、多言語埋め込みモデルが必要です。これは、純粋な英語モデルよりもはるかに稀です。

モデルがローカルキャッシュに存在しない場合、新しい設定で初めてGramps Web APIが起動されるときにダウンロードされます。標準のDockerイメージを使用する場合、モデル`sentence-transformers/distiluse-base-multilingual-cased-v2`はすでにローカルで利用可能です。このモデルは良い出発点であり、多言語入力をサポートしています。

異なるモデルについての学びをコミュニティと共有してください！

!!! info
    Sentence Transformersライブラリは、かなりの量のメモリを消費するため、ワーカープロセスが強制終了される可能性があります。一般的な目安として、セマンティック検索が有効な場合、各Gunicornワーカーは約200MBのメモリを消費し、各Celeryワーカーはアイドル時でも約500MBのメモリを消費し、埋め込みを計算しているときは最大1GBに達します。[CPUとメモリ使用量の制限](cpu-limited.md)を参照して、メモリ使用量を制限する設定を確認してください。さらに、一時的なメモリ使用量のスパイクによるOOMエラーを防ぐために、十分に大きなスワップパーティションを用意することをお勧めします。

## リモート埋め込みAPIの使用

ローカルのSentence Transformersモデルを実行する代わりに、セマンティック検索のためにリモートのOpenAI互換埋め込みAPIを使用することができます。これは、埋め込み計算を別のサービス（例：[Ollama](https://ollama.com/)）にオフロードしたり、クラウド埋め込みプロバイダー（例：OpenAI）を使用したり、Sentence TransformersおよびPyTorchライブラリをメモリに読み込むのを避けたりするのに便利です。

リモートAPIは、[OpenAI埋め込みエンドポイント](https://platform.openai.com/docs/api-reference/embeddings)（`/v1/embeddings`）と互換性がある必要があります。

リモート埋め込みAPIを使用するには、次の設定オプションを設定します（[サーバー設定](configuration.md)を参照）：

Key | Description
----|-------------
`VECTOR_EMBEDDING_MODEL` | リモートプロバイダーに渡すモデル名
`VECTOR_EMBEDDING_BASE_URL` | リモートAPIのベースURL
`VECTOR_EMBEDDING_API_KEY` | APIキー（プロバイダーが認証を必要とする場合のみ必要）

### Ollamaを使用した埋め込み

Docker ComposeでGramps Webをデプロイする際、Ollamaサービスを追加し、埋め込みと（オプションで）LLMの両方に使用することができます：

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

サービスを起動した後、埋め込みモデルをOllamaにプルします：

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Ollamaを埋め込みに使用する場合、Sentence TransformersおよびPyTorchライブラリは必要なく、Gramps Web APIワーカーのメモリ使用量が大幅に削減されます。

### OpenAIを使用した埋め込み

OpenAI埋め込みAPIを使用するには、ベースURLをOpenAI APIに設定し、APIキーを提供します：

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    埋め込みモデルを変更すると、ツリー（またはマルチツリー設定のすべてのツリー）のすべてのレコードを再インデックスする必要があります。異なるモデルは異なる次元のベクトルを生成するためです。

## LLMプロバイダーの設定

LLMとの通信には、OpenAI互換APIをサポートするPydantic AIフレームワークを使用します。これにより、Ollamaを介してローカルにデプロイされたLLM（[Ollama OpenAI互換性](https://ollama.com/blog/openai-compatibility)を参照）や、OpenAI、Anthropic、Hugging Face TGI（テキスト生成推論）などのホスティングAPIを使用できます。LLMは、設定パラメータ`LLM_MODEL`と`LLM_BASE_URL`を介して構成されます。

### OpenAI APIを介してホストされたLLMの使用

OpenAI APIを使用する場合、`LLM_BASE_URL`は設定しなくてもよく、`LLM_MODEL`はOpenAIモデルの1つ（例：`gpt-4o-mini`）に設定する必要があります。LLMは、RAGとツール呼び出しの両方を使用して質問に答えます：セマンティック検索結果から関連情報を選択し、専門のツールを使用してデータベースに直接クエリを実行できます。系譜や歴史に関する深い知識は必要ありません。したがって、小さな/安価なモデルで十分かどうか試すことができます。

アカウントにサインアップし、APIキーを取得して、`OPENAI_API_KEY`環境変数に保存する必要があります。

!!! info
    `LLM_MODEL`は設定パラメータです。環境変数を介して設定したい場合は、`GRAMPSWEB_LLM_MODEL`を使用してください（[設定](configuration.md)を参照）。`OPENAI_API_KEY`は設定パラメータではなく、Pydantic AIライブラリによって直接使用される環境変数であるため、プレフィックスを付ける必要はありません。

### Mistral AIの使用

Mistral AIのホストされたモデルを使用するには、`LLM_MODEL`を設定する際にモデル名の前に`mistral:`を付けます。

Mistral AIのアカウントにサインアップし、APIキーを取得して、`MISTRAL_API_KEY`環境変数に保存する必要があります。Pydantic AIは自動的に正しいMistral APIエンドポイントを使用するため、`LLM_BASE_URL`を設定する必要はありません。

Docker Composeを使用して環境変数で設定する例：
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Ollamaを介してローカルLLMの使用

[Ollama](https://ollama.com/)は、LLMをローカルで実行する便利な方法です。詳細についてはOllamaのドキュメントを参照してください。LLMはかなりの計算リソースを必要とし、最小のモデルを除いてはGPUサポートなしでは遅すぎる可能性があることに注意してください。アシスタントはツール呼び出しに依存しているため、ツールをサポートするモデル（例：[`qwen2.5`](https://ollama.com/library/qwen2.5)）を選択してください。最初は`qwen2.5:7b`のような小さなバリアントから始め、回答が十分でない場合は大きなものを試してください。コミュニティと経験を共有してください！

Docker ComposeでGramps Webをデプロイする際、Ollamaサービスを追加し、Gramps Webをそれにポイントすることができます：

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

サービスを起動した後、モデルをOllamaにプルします：

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

いくつかの注意点：

- `LLM_MODEL`をOllamaモデル名に設定し、タグ（コロンの後の部分、例：`7b`）を含め、`ollama:`をプレフィックスとして付けます。このプレフィックスにより、Pydantic AIはモデルのOllama特有の設定を使用します。これは推奨される設定です。
- `LLM_BASE_URL`は`/v1/`で終わる必要があります。例：`http://ollama:11434/v1/`。
- `ollama:`プレフィックスを使用する場合、`OPENAI_API_KEY`や`OLLAMA_BASE_URL`環境変数は必要ありません。`LLM_BASE_URL`が設定されていない場合、Gramps Webは`OLLAMA_BASE_URL`にフォールバックします。
- 代わりにプレフィックスを省略して（例：`LLM_MODEL: qwen2.5:7b`）Ollamaを一般的なOpenAI互換APIを介して使用することもできます。この場合、`OPENAI_API_KEY`環境変数に`ollama`（空でない任意の値）を設定する必要があります。

Ollamaに関する問題をトラブルシューティングするには、Ollamaサービスの環境で環境変数`OLLAMA_DEBUG=1`を設定してデバッグログを有効にできます。

!!! info
    Gramps Web AIチャットにOllamaを使用している場合は、コミュニティをサポートするために、欠落している詳細でこのドキュメントを完成させてください。

### その他のプロバイダーの使用

他のプロバイダーに関するドキュメントを提出し、コミュニティと経験を共有してください！
