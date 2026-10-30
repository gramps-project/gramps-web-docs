# Gramps Web DigitalOcean 1-Click App

[Gramps Webを自分で設定する](deployment.md)のではなく、[Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)を使用することもできます。Digital OceanはGramps Webのデモ版をホストしています。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

セットアップ手順の一環として、DigitalOceanのアカウントにサインアップし、使用する「ドロップレット」（仮想マシン）の有料プランを選択する必要があります。

現在、これは自分のハードウェアを使用せずに、SSLで保護された自ホストのGramps Webインスタンスをデプロイする最も簡単な方法であると言えます。

!!! info
    DigitalOceanにホスティングサービスの料金を支払うことになります。Grampsオープンソースプロジェクトは有料サポートを提供していません。

## ステップ 1: DigitalOceanアカウントを作成する

まだアカウントを持っていない場合は、[DigitalOcean](https://www.digitalocean.com/)でアカウントを作成してください。

## ステップ 2: ドロップレットを作成する

- [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)に移動し、「Gramps Web Dropletを作成」をクリックします。
- 最低2GBのRAMを持つプランを選択します。
- ドロップレットへの認証を設定します。
- 「Dropletを作成」をクリックします。

!!! info
    1-Click Appが最新の`docker-compose`バージョンをインストールするまで、最大10分待つ必要がある場合があります。
    最新の`docker-compose`バージョンを使用することで、`firstlogin.sh`に関連するエラーを軽減できます。
    
## ステップ 3: ドメイン名を設定する

ドメイン名（またはサブドメイン）が必要です。ドメインを所有している場合は、それをドロップレットのIPアドレスにポイントしてください。そうでない場合は、[DuckDNS](https://www.duckdns.org/)のような無料サービスを使用できます。

## ステップ 4: ドロップレットにログインする

ドロップレットにSSH接続します。「Gramps Web DigitalOcean 1-click app setup!へようこそ」というメッセージが表示されるはずです。表示されない場合は、数分待って再試行してください（インストールはまだ完了していません）。

セットアップスクリプトは、ドメイン名（例: `mygrampswebinstance.duckdns.org`）とメールアドレス（Let's Encrypt証明書に必要）を尋ねます。オプションとして、Gramps Webがパスワードリセットなどのためにメールを送信するために使用するSMTP設定も尋ねられます。SMTPホストを空白のままにしておくと、これをスキップできます。

これが完了したら、バックグラウンドでセットアップが完了するのを待ちます。

## ステップ 5: Gramps Webを起動する

あなたのGramps Webインスタンスは、ドメインのルートでアクセス可能になり、有効なSSL証明書があり、初回実行アシスタントが表示されるはずです。

## 後で設定を変更する

セットアップスクリプトは、基本URLとメール設定を`/root/letsencrypt.env`ファイルに`GRAMPSWEB_`で始まる[設定オプション](configuration.md)として保存します。例:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

設定を追加または変更するには、ドロップレット上でこのファイルを編集し、次のコマンドで変更を適用します。

```bash
cd /opt/grampsweb && docker compose up -d
