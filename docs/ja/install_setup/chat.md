# AIチャットの設定

!!! info
    AIチャットにはGramps Web APIバージョン2.5.0以上が必要です。バージョン3.6.0では、よりインテリジェントな対話のためのツール呼び出し機能が導入されました。

Gramps Web APIは、リトリーバル拡張生成（RAG）とツール呼び出しを組み合わせた手法を使用して、大規模言語モデル（LLM）を介して系譜データベースに関する質問をすることをサポートしています。

## 仕組み

AIアシスタントは、2つの補完的なアプローチを使用します。

**リトリーバル拡張生成（RAG）**：*ベクトル埋め込みモデル*が、Grampsデータベース内のすべてのオブジェクトのインデックスを、オブジェクトの意味をエンコードした数値ベクトルの形で作成します。ユーザーが質問をすると、その質問もベクトルに変換され、データベース内のオブジェクトと比較されます。この*セマンティックサーチ*は、質問に最も意味的に類似したオブジェクトを返します。

**ツール呼び出し（v3.6.0+）**：AIアシスタントは、系譜データを直接クエリするために専門のツールを使用できるようになりました。これらのツールを使用すると、アシスタントはデータベースを検索し、特定の基準で人々/イベント/家族/場所をフィルタリングし、個人間の関係を計算し、詳細なオブジェクト情報を取得できます。これにより、アシスタントは複雑な系譜の質問に正確に答える能力が大幅に向上します。

Gramps Web APIでチャットエンドポイントを有効にするには、3つのステップが必要です。

1. 必要な依存関係のインストール
2. セマンティックサーチの有効化
3. LLMプロバイダーの設定

これらの3つのステップについては、以下で順に説明します。最後に、オーナーまたは管理者は[どのユーザーがチャット機能にアクセスできるかを設定する](users.md#configuring-who-can-use-ai-chat)必要があります。

## 必要な依存関係のインストール

AIチャットには、Sentence TransformersおよびPyTorchライブラリをインストールする必要があります。

Gramps Webの標準Dockerイメージには、`amd64`（例：64ビットデスクトップPC）および`arm64`（例：64ビットRaspberry Pi）アーキテクチャ用にそれらが事前にインストールされています。残念ながら、AIチャットはPyTorchのサポートがないため、`armv7`（例：32ビットRaspberry Pi）アーキテクチャではサポートされていません。

`pip`を介してGramps Web APIをインストールする際（Dockerイメージを使用する場合は必要ありません）、必要な依存関係は以下のコマンドでインストールされます。

```bash
pip install gramps_webapi[ai]
```

## セマンティックサーチの有効化

必要な依存関係がインストールされている場合、セマンティックサーチを有効にするのは、`VECTOR_EMBEDDING_MODEL`構成オプションを設定するだけで済む場合があります（例：`GRAMPSWEB_VECTOR_EMBEDDING_MODEL`環境変数を設定することによって）。詳細は[サーバー構成](configuration.md)を参照してください。これは、[Sentence Transformers](https://sbert.net/)ライブラリによってサポートされているモデルの任意の文字列にすることができます。このプロジェクトのドキュメントで詳細と利用可能なモデルを確認してください。

!!! warning
    デフォルトのDockerイメージには、GPUサポートのあるPyTorchバージョンが含まれていないことに注意してください。GPUにアクセスできる場合（これはセマンティックインデックスを大幅に高速化します）、GPU対応のPyTorchバージョンをインストールしてください。

モデルを選択する際には、いくつかの考慮事項があります。

- モデルを変更すると、ツリー（またはマルチツリー設定のすべてのツリー）に対してセマンティックサーチインデックスを手動で再作成する必要があります。そうしないと、エラーや無意味な結果が発生します。Gramps Webは、設定された埋め込みモデルが既存のインデックスと一致しなくなったことを検出し、管理者に[管理設定](../administration/settings.md#semantic-search-index)から完全な再インデックスをトリガーするよう促す持続的な通知を表示します。
- モデルは、正確性/一般性と計算時間/ストレージスペースの間のトレードオフです。強力なGPUにアクセスできないシステムでGramps Web APIを実行している場合、大きなモデルは通常実用上遅すぎます。
- データベース全体が英語で、すべてのユーザーが英語でチャットの質問をすることが期待されている場合を除き、多言語埋め込みモデルが必要です。これは、純粋な英語モデルよりも珍しいです。

モデルがローカルキャッシュに存在しない場合、新しい構成で初めてGramps Web APIが起動されるときにダウンロードされます。標準のDockerイメージを使用する場合、モデル`sentence-transformers/distiluse-base-multilingual-cased-v2`はすでにローカルに利用可能です。このモデルは良い出発点であり、多言語入力をサポートしています。

異なるモデルに関する学びをコミュニティと共有してください！

!!! info
    Sentence Transformersライブラリは、かなりのメモリを消費するため、ワーカープロセスが終了する可能性があります。一般的な目安として、セマンティックサーチが有効な場合、各Gunicornワーカーは約200MBのメモリを消費し、各Celeryワーカーはアイドル状態でも約500MBのメモリを消費し、埋め込みを計算しているときは最大1GBに達します。[CPUとメモリ使用量の制限](cpu-limited.md)を参照して、メモリ使用量を制限する設定を確認してください。また、一時的なメモリ使用量のスパイクによるOOMエラーを防ぐために、十分に大きなスワップパーティションを用意することをお勧めします。

## LLMプロバイダーの設定

LLMとの通信には、OpenAI互換APIをサポートするPydantic AIフレームワークを使用します。これにより、Ollamaを介してローカルにデプロイされたLLM（[Ollama OpenAI互換性](https://ollama.com/blog/openai-compatibility)を参照）や、OpenAI、Anthropic、Hugging Face TGI（テキスト生成推論）などのホスティングAPIを使用できます。LLMは、構成パラメータ`LLM_MODEL`および`LLM_BASE_URL`を介して設定されます。

### OpenAI APIを介したホスティングLLMの使用

OpenAI APIを使用する場合、`LLM_BASE_URL`は設定しなくてもよく、`LLM_MODEL`はOpenAIモデルの1つ（例：`gpt-4o-mini`）に設定する必要があります。LLMは、RAGとツール呼び出しの両方を使用して質問に答えます：セマンティックサーチ結果から関連情報を選択し、専門のツールを使用してデータベースに直接クエリを送信できます。深い系譜的または歴史的知識は必要ありません。したがって、小さな/安価なモデルが十分かどうかを試すことができます。

また、アカウントにサインアップし、APIキーを取得して`OPENAI_API_KEY`環境変数に保存する必要があります。

!!! info
    `LLM_MODEL`は構成パラメータです。環境変数を介して設定したい場合は、`GRAMPSWEB_LLM_MODEL`を使用してください（[構成](configuration.md)を参照）。`OPENAI_API_KEY`は構成パラメータではなく、Pydantic AIライブラリによって直接使用される環境変数であるため、プレフィックスを付けないでください。

### Mistral AIの使用

Mistral AIのホスティングモデルを使用するには、`LLM_MODEL`を設定する際にモデル名の前に`mistral:`を付けます。

Mistral AIのアカウントにサインアップし、APIキーを取得して`MISTRAL_API_KEY`環境変数に保存する必要があります。Pydantic AIは自動的に正しいMistral APIエンドポイントを使用するため、`LLM_BASE_URL`を設定する必要はありません。

環境変数を使用したDocker Composeの例設定：
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Ollamaを介したローカルLLMの使用

[Ollama](https://ollama.com/)は、LLMをローカルで実行する便利な方法です。詳細についてはOllamaのドキュメントを参照してください。LLMはかなりの計算リソースを必要とし、最小のモデルを除いて、GPUサポートなしではおそらく遅すぎることに注意してください。[`tinyllama`](https://ollama.com/library/tinyllama)がニーズを満たすかどうかを試してみてください。満たさない場合は、より大きなモデルを試してみてください。コミュニティと経験を共有してください！

Docker ComposeでGramps Webをデプロイする際には、Ollamaサービスを追加できます。

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

その後、`LLM_BASE_URL`構成パラメータを`http://ollama:11434/v1`に設定します。`LLM_MODEL`をOllamaがサポートするモデルに設定し、`ollama pull <model>`でコンテナ内にダウンロードします。最後に、`OPENAI_API_KEY`を`ollama`に設定します。

Ollamaに関する問題をトラブルシューティングするには、Ollamaサービス環境で環境変数`OLLAMA_DEBUG=1`を設定してデバッグログを有効にできます。

!!! info
    Gramps Web AIチャットにOllamaを使用している場合は、コミュニティをサポートするために、欠落している詳細をこのドキュメントで補完してください。

### その他のプロバイダーの使用

他のプロバイダーに関するドキュメントを提出し、コミュニティと経験を共有してください！
