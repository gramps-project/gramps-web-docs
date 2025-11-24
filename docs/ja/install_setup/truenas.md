# TrueNAS セットアップ

このガイドでは、TrueNAS Community Edition 25.04 で Gramps Web をセットアップする方法を説明します。

!!! warning
    このガイドは、Docker Compose ベースの新しいアプリシステムを導入した TrueNAS Community Edition 25.04 以降を対象としています。以前のバージョンの TrueNAS には適用されません。

## 前提条件

- TrueNAS Community Edition 25.04 以降
- TrueNAS ウェブインターフェースの基本的な理解
- Gramps Web データを保存するためのデータセット

## 概要

TrueNAS Community Edition 25.04 では、以前の Helm チャートベースのアプローチに代わって、新しい Docker Compose ベースのアプリシステムが導入されました。このガイドでは、Docker Compose を使用して Gramps Web のカスタムアプリを作成する手順を説明します。

## ステップ 1: ストレージの準備

1. TrueNAS ウェブインターフェースで **Datasets** に移動します。
2. Gramps Web 用の新しいデータセットを作成します（例: `grampsweb`）。このデータセットのフルパス（例: `/mnt/storage/grampsweb`）をメモしておいてください。後で必要になります。

さまざまなコンポーネントのためにサブディレクトリを作成します：
- `users` - ユーザーデータベース
- `database` - Gramps データベースファイル
- `media` - メディアファイル

## ステップ 2: Docker Compose アプリの作成

1. TrueNAS ウェブインターフェースで **Apps** に移動します。
2. **Discover Apps** をクリックします。
3. "Gramps Web" を検索してクリックします。
4. "Install" をクリックします。

これにより、アプリの設定ページに移動します。

## ステップ 3: アプリの設定

### Gramps Web 設定

- **Timezone:** あなたのローカルタイムゾーンに設定します（例: `Europe/Berlin`）
- **Redis password:** Redis のパスワードを設定します。これはアプリ内部でのみ使用されます。
- **Disable telemetry:** このボックスはチェックを外しておいてください – 詳細は [こちらを参照](telemetry.md)。
- **Secret key:** これは強力でユニークな値に設定することが重要です。ランダムキーを生成する方法については [サーバー設定](configuration.md#existing-configuration-settings) を参照してください。
- **Additional Environment Variables:** すべての追加の [設定オプション](configuration.md) を `GRAMPSWEB_` プレフィックス付きの環境変数として設定する必要があります。ブール値は環境変数の場合、`true` または `false`（すべて小文字）として設定する必要があることなど、[設定ドキュメント](configuration.md)を詳細に確認してください。これは一般的な落とし穴です。

少なくとも `GRAMPSWEB_BASE_URL` を Gramps Web インスタンスにアクセスできる URL に設定してください。これは適切な動作に必要です。

この段階でメール設定を行うこともできます。行う場合は、オンボーディングウィザードのメール設定ステップをスキップできます。関連する環境変数は次のとおりです：

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

すべての設定は、TrueNAS Apps インターフェースで "Edit" をクリックすることで後で変更できます。

### ストレージ設定

- **Users Storage:** 先に作成した `users` ディレクトリへのパスを選択します。
- **Index Storage:** デフォルト設定の "ixVolume (Dataset created automatically by the system)" のままで大丈夫です。
- **Thumbnail Cache Storage:** デフォルト設定の "ixVolume (Dataset created automatically by the system)" のままで大丈夫です。
- **Cache Storage:** デフォルト設定の "ixVolume (Dataset created automatically by the system)" のままで大丈夫です。
- **Media Storage:** 先に作成した `media` ディレクトリへのパスを選択します。
- **Gramps Database Storage:** 先に作成した `database` ディレクトリへのパスを選択します。

### リソース設定

スムーズな動作を確保するために、少なくとも 2 CPU と 4096 MB の RAM を割り当てることをお勧めします。

## ステップ 4: Gramps Web へのアクセス

アプリがデプロイされると、TrueNAS Apps インターフェースの "Web UI" ボタンをクリックして Gramps Web にアクセスできます。オンボーディングウィザード "Welcome to Gramps Web" が表示されるはずです。

ユーザーが Gramps Web インターフェースにアクセスできるようにする場合は、**アプリをインターネットに直接公開しないでください**。次のステップに進んでください。

## ステップ 5: リバースプロキシの設定

ユーザーに Gramps Web インスタンスを安全に公開するために、リバースプロキシを設定することをお勧めします。これにより、SSL/TLS 証明書を管理し、アクセスを制御できます。

最も簡単なオプションは、公式の TrueNAS Nginx Proxy Manager アプリを使用することです。TrueNAS Apps インターフェースでアプリを検索してインストールします。すべての設定をデフォルトのままにしておくことができますが、1 つの追加の環境変数 `DISABLE_IPV6` を `true` に設定して、潜在的な IPv6 関連の問題を回避することをお勧めします。

デプロイが完了したら、Nginx Proxy Manager ウェブインターフェースを開き、次の設定で新しいプロキシホストを作成します：

- Scheme: `http`
- Forward Hostname / IP: あなたの TrueNAS サーバーのホスト名（例: `truenas`）
- Forward Port: Gramps Web アプリに割り当てられたポート（正確なポートは TrueNAS Apps インターフェースで確認してください）
- "SSL" タブで "Force SSL" にチェックを入れます。
- "SSL Certificates" の下で "Add SSL Certificate" > "Let's Encrypt" を選択して、あなたのドメイン用の新しい Let's Encrypt 証明書を作成します。

ルーターの設定や SSL 証明書の取得に関する詳細については、[Nginx Proxy Manager ドキュメント](https://nginxproxymanager.com/guide/) を参照してください。
