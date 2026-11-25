# Gramps Web DigitalOcean 1-Click App

[Gramps Web を自分でセットアップする](deployment.md)代わりに、[Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)も使用できます。Digital Ocean は Gramps Web のデモ版をホストしています。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

セットアップ手順の一環として、DigitalOcean のアカウントを作成し、使用する「droplet」（仮想マシン）の有料プランを選択する必要があります。

これは、現在のところ、自分のハードウェアを使用せずに、SSL で保護された独自のセルフホスト型 Gramps Web インスタンスをデプロイする最も簡単な方法と言えるでしょう。

!!! info
    DigitalOcean のホスティングサービスに対して料金を支払う必要があることに注意してください。Gramps オープンソースプロジェクトでは、有料サポートを提供していません。

## 手順 1: DigitalOcean アカウントを作成する

まだアカウントをお持ちでない場合は、[DigitalOcean](https://www.digitalocean.com/) でアカウントを作成してください。

## 手順 2: droplet を作成する

- [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) に移動し、「Create Gramps Web Droplet」をクリックしてください。
- RAM が 2 GB 以上のプランを選択してください。
- droplet の認証を設定してください。
- 「Create Droplet」をクリックしてください。

## 手順 3: ドメイン名を設定する

ドメイン名（またはサブドメイン）が必要です。ドメインを所有している場合は、そのドメインを droplet の IP アドレスに向けてください。それ以外の場合は、[DuckDNS](https://www.duckdns.org/) などの無料サービスを使用できます。

## 手順 4: droplet にログインする

droplet に SSH 接続してください。「Welcome to the Gramps Web DigitalOcean 1-click app setup!」というメッセージが表示されるはずです。表示されない場合は、数分待ってからもう一度試してください（インストールがまだ完了していない可能性があります）。

セットアップスクリプトで、ドメイン名（例: `mygrampswebinstance.duckdns.org`）とメールアドレス（Let's Encrypt 証明書に必要です）の入力を求められます。必要に応じて、パスワードのリセットなど、Gramps Web がメール送信に使用する SMTP 設定の入力も求められます。これを省略するには、SMTP ホストを空のままにしてください。

完了したら、バックグラウンドでセットアップが完了するまで待ってください。

## 手順 5: Gramps Web を起動する

これで、Gramps Web インスタンスが有効な SSL 証明書とともにドメインのルートでアクセス可能になり、初回実行アシスタントが表示されるはずです。

## 後から設定を変更する

セットアップスクリプトは、ベース URL とメール設定を、`GRAMPSWEB_` をプレフィックスとする[設定オプション](configuration.md)としてファイル `/root/letsencrypt.env` に保存します。例:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

設定を追加または変更するには、droplet 上でこのファイルを編集し、次のコマンドで変更を適用してください。

```bash
cd /opt/grampsweb && docker compose up -d
```
