# AIチャットの設定

!!! info
    AIチャットにはGramps Web APIバージョン2.5.0以上が必要です。バージョン3.6.0では、よりインテリジェントな対話のためのツール呼び出し機能が導入されました。

Gramps Web APIは、ツール呼び出しと組み合わせたリトリーバル拡張生成（RAG）という手法を通じて、大規模言語モデル（LLM）を使用して系譜データベースに関する質問をすることをサポートしています。

## 仕組み

AIアシスタントは、2つの補完的なアプローチを使用します。

**リトリーバル拡張生成（RAG）**: *ベクトル埋め込みモデル*が、Grampsデータベース内のすべてのオブジェクトのインデックスを、オブジェクトの意味をエンコードする数値ベクトルの形で作成します。ユーザーが質問をすると、その質問もベクトルに変換され、データベース内のオブジェクトと比較されます。この*セマンティック検索*は、質問に最も意味的に類似したオブジェクトを返します。

**ツール呼び出し（v3.6.0+）**: AIアシスタントは、系譜データを直接照会するために専門のツールを使用できるようになりました。これらのツールにより、アシスタントはデータベースを検索し、特定の基準で人々/イベント/家族/場所をフィルタリングし、個人間の関係を計算し、詳細なオブジェクト情報を取得できます。これにより、アシスタントは複雑な系譜の質問に正確に答える能力が大幅に向上します。

Gramps Web APIでチャットエンドポイントを有効にするには、3つのステップが必要です。

1. 必要な依存関係のインストール、
2. セマンティック検索の有効化、
3. LLMプロバイダーの設定。

これらの3つのステップについて、以下で順に説明します。最後に、オーナーまたは管理者は[チャット機能にアクセスできるユーザーを設定する](users.md#configuring-who-can-use-ai-chat)必要があります。

## 必要な依存関係のインストール

AIチャットには、Sentence TransformersおよびPyTorchライブラリがインストールされている必要があります。

Gramps Webの標準Dockerイメージには、`amd64`（例：64ビットデスクトップPC）および`arm64`（例：64ビットRaspberry Pi）アーキテクチャ用にこれらが事前にインストールされています。残念ながら、AIチャットはPyTorchのサポートがないため、`armv7`（例：32ビットRaspberry Pi）アーキテクチャではサポートされていません。

Gramps Web APIを`pip`経由でインストールする場合（Dockerイメージを使用している場合は必要ありません）、必要な依存関係は以下のコマンドでインストールされます。

```bash
pip install gramps_webapi[ai]
```

## セマンティック検索の有効化

必要な依存関係がインストールされている場合、セマンティック検索の有効化は、`VECTOR_EMBEDDING_MODEL`構成オプションを設定するだけで済む場合があります（例：`GRAMPSWEB_VECTOR_EMBEDDING_MODEL`環境変数を設定することによって）。詳細は[サーバー構成](configuration.md)を参照してください。これは、[Sentence Transformers](https://sbert.net/)ライブラリによってサポートされているモデルの任意の文字列であることができます。このプロジェクトのドキュメントで詳細と利用可能なモデルを確認してください。

!!! warning
    デフォルトのDockerイメージには、GPUサポートのあるPyTorchバージョンが含まれていないことに注意してください。GPUにアクセスできる場合（これはセマンティックインデックスを大幅に高速化します）、GPU対応のPyTorchバージョンをインストールしてください。

モデルを選択する際には、いくつかの考慮事項があります。

- モデルを変更すると、ツリー（またはマルチツリーセットアップ内のすべてのツリー）のセマンティック検索インデックスを手動で再作成する必要があります。そうしないと、エラーや無意味な結果が発生します。Gramps Webは、構成された埋め込みモデルが既存のインデックスと一致しなくなったことを検出し、管理者に[管理設定](../administration/settings.md#semantic-search-index)から完全な再インデックスをトリガーするように促す持続的な通知を表示します。
- モデルは、精度/一般性と計算時間/ストレージスペースの間のトレードオフです。強力なGPUにアクセスできないシステムでGramps Web APIを実行している場合、大きなモデルは通常、実際には遅すぎます。
- データベース全体が英語であり、すべてのユーザーが英語でチャット質問をすることが期待される場合を除き、多言語埋め込みモデルが必要です。これは、純粋な英語モデルよりもはるかに少ないです。

モデルがローカルキャッシュに存在しない場合、Gramps Web APIが新しい構成で初めて起動されるときにダウンロードされます。標準のDockerイメージを使用している場合、モデル`sentence-transformers/distiluse-base-multilingual-cased-v2`はすでにローカルに利用可能です。このモデルは良い出発点であり、多言語入力をサポートしています。

異なるモデルに関する学びをコミュニティと共有してください！

!!! info
    Sentence Transformersライブラリはかなりの量のメモリを消費するため、ワーカープロセスが強制終了される可能性があります。一般的な目安として、セマンティック検索が有効な場合、各Gunicornワーカーは約200MBのメモリを消費し、各Celeryワーカーはアイドル時でも約500MBのメモリを消費し、埋め込み計算中は最大1GBに達します。[CPUおよびメモリ使用量の制限](cpu-limited.md)に、メモリ使用量を制限するための設定があります。さらに、トランジェントメモリ使用量のスパイクによるOOMエラーを防ぐために、十分に大きなスワップパーティションを用意することをお勧めします。

## リモート埋め込みAPIの使用

ローカルのSentence Transformersモデルを実行する代わりに、セマンティック検索のためにリモートのOpenAI互換埋め込みAPIを使用することができます。これは、埋め込み計算を別のサービス（例：[Ollama](https://ollama.com/)）にオフロードしたり、クラウド埋め込みプロバイダー（例：OpenAI）を使用したり、Sentence TransformersおよびPyTorchの依存関係をインストールせずに済むために便利です。

リモートAPIは、[OpenAI埋め込みエンドポイント](https://platform.openai.com/docs/api-reference/embeddings)（`/v1/embeddings`）と互換性がある必要があります。

リモート埋め込みAPIを使用するには、次の構成オプションを設定します（[サーバー構成](configuration.md)を参照）：

キー | 説明
----|-------------
`VECTOR_EMBEDDING_MODEL` | リモートプロバイダーに渡すモデル名
`VECTOR_EMBEDDING_BASE_URL` | リモートAPIのベースURL
`VECTOR_EMBEDDING_API_KEY` | APIキー（プロバイダーが認証を必要とする場合のみ必要）

### Ollamaを使用した埋め込み

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

### OpenAIを使用した埋め込み

OpenAI埋め込みAPIを使用するには、ベースURLをOpenAI APIに設定し、APIキーを提供します：

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    埋め込みモデルを変更すると、ツリー（またはマルチツリーセットアップ内のすべてのツリー）のすべてのレコードを再インデックスする必要があります。異なるモデルは異なる次元のベクトルを生成するためです。

## LLMプロバイダーの設定

LLMとの通信は、OpenAI互換APIをサポートするPydantic AIフレームワークを使用します。これにより、Ollamaを介してローカルにデプロイされたLLM（[OllamaのOpenAI互換性](https://ollama.com/blog/openai-compatibility)を参照）や、OpenAI、Anthropic、Hugging Face TGI（テキスト生成推論）などのホスティングAPIを使用できます。LLMは、構成パラメーター`LLM_MODEL`および`LLM_BASE_URL`を介して設定されます。

### OpenAI API経由でホストされたLLMの使用

OpenAI APIを使用する場合、`LLM_BASE_URL`は設定しなくてもよく、`LLM_MODEL`はOpenAIモデルの1つ（例：`gpt-4o-mini`）に設定する必要があります。LLMは、RAGとツール呼び出しの両方を使用して質問に答えます：セマンティック検索結果から関連情報を選択し、専門のツールを使用してデータベースを直接照会できます。深い系譜学的または歴史的知識は必要ありません。したがって、小型または安価なモデルが十分かどうか試してみることができます。

また、アカウントにサインアップし、APIキーを取得して`OPENAI_API_KEY`環境変数に保存する必要があります。

!!! info
    `LLM_MODEL`は構成パラメーターです。環境変数を介して設定したい場合は、`GRAMPSWEB_LLM_MODEL`を使用してください（[構成](configuration.md)を参照）。`OPENAI_API_KEY`は構成パラメーターではなく、Pydantic AIライブラリによって直接使用される環境変数であるため、接頭辞を付けないでください。

### Mistral AIの使用

Mistral AIのホストされたモデルを使用するには、`LLM_MODEL`を設定する際にモデル名の前に`mistral:`を付けます。

Mistral AIアカウントにサインアップし、APIキーを取得して`MISTRAL_API_KEY`環境変数に保存する必要があります。Pydantic AIは自動的に正しいMistral APIエンドポイントを使用するため、`LLM_BASE_URL`を設定する必要はありません。

環境変数を使用してDocker Composeを使用する際の例の設定：
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Ollamaを介してローカルLLMを使用

[Ollama](https://ollama.com/)は、LLMをローカルで実行する便利な方法です。詳細についてはOllamaのドキュメントを参照してください。LLMはかなりの計算リソースを必要とし、最小のモデルを除いてはGPUサポートなしではおそらく遅すぎることに注意してください。[`tinyllama`](https://ollama.com/library/tinyllama)がニーズを満たすかどうか試してみてください。満たさない場合は、より大きなモデルを試してください。コミュニティと経験を共有してください！

Docker ComposeでGramps Webをデプロイする際に、Ollamaサービスを追加できます。

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

その後、`LLM_BASE_URL`構成パラメーターを`http://ollama:11434/v1`に設定します。`LLM_MODEL`をOllamaがサポートするモデルに設定し、コンテナ内で`ollama pull <model>`を使用してダウンロードします。最後に、`OPENAI_API_KEY`を`ollama`に設定します。

Ollamaに関する問題をトラブルシューティングするには、Ollamaサービスの環境で環境変数`OLLAMA_DEBUG=1`を設定してデバッグログを有効にできます。

!!! info
    Gramps Web AIチャットにOllamaを使用している場合は、コミュニティをサポートするために、欠落している詳細をこのドキュメントに追加してください。

### 他のプロバイダーの使用

他のプロバイダーに関するドキュメントを提出し、コミュニティと経験を共有してください！
