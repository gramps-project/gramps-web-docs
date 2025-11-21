# バックエンド開発セットアップ

このページでは、Gramps Webのバックエンド（サーバーコンポーネント）である[Gramps Web API](https://github.com/gramps-project/gramps-web-api/)の開発を開始するために必要な手順をリストアップします。


## 前提条件

推奨される開発セットアップは、devcontainersを使用したVisual Studio Codeです。このアプローチにより、必要なすべてのツールを備えた事前構成された開発環境が作成されます。始めるには、次の要素が必要です：

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) と [Dev Containers拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) がインストールされていること
- [Git](https://git-scm.com)

Linux、macOS、またはWindowsをオペレーティングシステムとして使用できます。


## 始め方

1. [Gramps Web APIリポジトリ](https://github.com/gramps-project/gramps-web-api)を開き、「fork」をクリックします。
2. Gitを使用して、フォークしたリポジトリをローカルマシンにクローンします。
3. クローンしたリポジトリをVisual Studio Codeで開きます。プロンプトが表示されたら「Containerで再オープン」を選択するか、コマンドパレットを手動で開き（Ctrl+Shift+PまたはCmd+Shift+P）、"Dev Containers: Rebuild and Reopen in Container"を選択します。
4. devコンテナがビルドされて起動するのを待ちます。特に初回は数分かかる場合があります。


## タスク

バックエンドコードのみを修正する場合、Webサーバーを立ち上げる必要はありません - ユニットテストは、実行中のサーバーを必要とせずにAPIへのリクエストをシミュレートできるFlaskテストクライアントを使用します。

ただし、サーバーを実行することは、次のような場合に便利です：

- 実際のHTTPリクエストで変更を試したい場合（[手動クエリ](queries.md)を参照）
- 変更がGramps Webアプリケーション全体に与える影響をプレビューしたい場合、または
- フロントエンドにも同時に変更を加えたい場合（[フロントエンド開発セットアップ](../frontend/setup.md)を参照）。

サーバーの実行は、devコンテナ内で事前定義されたタスクによって簡素化されています。コマンドパレット（Ctrl+Shift+PまたはCmd+Shift+P）から「Tasks: Run Task」を選択し、次のいずれかを選ぶことでこれらのタスクを実行できます：
- "Serve Web API" - デバッグログを有効にしてポート5555でFlask開発サーバーを起動します
- "Start Celery worker" - バックグラウンドタスクを処理するCeleryワーカーを起動します。


## デバッグ

デバッグは時に難しいことがあります。特に複雑な動作を追跡したり微妙な問題を特定したりする際にそうです。これを容易にするために、実行中のAPIインスタンスと個々のテストケースをVisual Studio Code内で直接デバッグできます。

### Gramps Web APIのデバッグ

実行中のAPIをデバッグするには：

1. Visual Studio Codeを開き、**実行とデバッグ**ビューに移動します。  
2. ドロップダウンメニューから**"Web API"**構成を選択します。  
3. デバッグを開始します。  
4. バックエンドにリクエストを送信すると（手動またはGramps Web GUIを通じて）、コード内に設定したブレークポイントで実行が一時停止します。  
   これにより、変数、制御フロー、およびその他の実行時の詳細を検査できます。

### テストケースのデバッグ

特定のテストケースをデバッグするには：

1. デバッグしたいテストファイルを開きます（例えば、`test_people.py`）。  
2. Visual Studio Codeで**実行とデバッグ**ビューを開きます。  
3. **"Current Test File"**構成を選択します。  
4. デバッグを開始します — 実行は、そのテストファイル内に設定されたブレークポイントで停止します。  

このセットアップにより、テストロジックをステップ実行し、変数の値を調べ、テストの失敗や予期しない結果をよりよく理解できます。
