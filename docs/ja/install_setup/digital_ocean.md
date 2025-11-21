# Gramps Web DigitalOcean 1-Click App

[Gramps Webを自分で設定する](deployment.md)代わりに、[Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)を使用することもできます。Digital OceanはGramps Webのデモ版をホストしています。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

セットアップ手順の一環として、DigitalOceanのアカウントにサインアップし、「ドロップレット」（仮想マシン）用の有料プランを選択する必要があります。

現在、これは自分のハードウェアを使用せずに、SSLで保護された独自の自己ホスト型Gramps Webインスタンスをデプロイする最も簡単な方法と言えるでしょう。

!!! info
    DigitalOceanにホスティングサービスの料金を支払うことになります。Grampsオープンソースプロジェクトは有料サポートを提供していません。

## ステップ 1: DigitalOceanアカウントを作成する

まだアカウントを持っていない場合は、[DigitalOcean](https://www.digitalocean.com/)でアカウントを作成してください。

## ステップ 2: ドロップレットを作成する

- [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)に移動し、「Gramps Web Dropletを作成」をクリックします。
- 最低2 GBのRAMを持つプランを選択します。
- ドロップレットへの認証を設定します。
- 「ドロップレットを作成」をクリックします。

!!! info
    1-Click Appが最新の`docker-compose`バージョンをインストールするまで、最大10分待つ必要がある場合があります。
    最新の`docker-compose`バージョンを使用することで、`firstlogin.sh`に関連するエラーを軽減できます。

## ステップ 3: ドメイン名を設定する

ドメイン名（またはサブドメイン）が必要です。ドメインを所有している場合は、それをドロップレットのIPアドレスにポイントします。そうでない場合は、[DuckDNS](https://www.duckdns.org/)のような無料サービスを使用できます。

## ステップ 4: ドロップレットにログインする

ドロップレットにSSHで接続します。「Gramps Web DigitalOcean 1-click app setup!へようこそ」というメッセージが表示されるはずです。これが表示されない場合は、数分待ってから再試行してください（インストールはまだ完了していません）。

セットアップスクリプトは、ドメイン名（例: `mygrampswebinstance.duckdns.org`）とメールアドレス（Let's Encrypt証明書に必要）を尋ねてきます。

これが完了したら、バックグラウンドでのセットアップが完了するのを待ちます。

## ステップ 5: Gramps Webを起動する

あなたのGramps Webインスタンスは、ドメインのルートでアクセス可能になり、有効なSSL証明書が設定され、初回実行アシスタントが表示されるはずです。
