# Gramps Webの更新

Docker Composeに基づくインストール方法のいずれかを使用している場合、Gramps Webを最新バージョンに更新するのは簡単です。`docker-compose.yml`があるフォルダで、以下のコマンドを実行してください。

```bash
docker compose pull
docker compose up -d
```

[Gramps Web API](https://github.com/gramps-project/gramps-web-api)のマイナーバージョンのアップデートについては、これだけで十分です。ただし、[Gramps Web APIのリリースノート](https://github.com/gramps-project/gramps-web-api/releases)も確認してください。破壊的変更があり、追加の注意や設定変更が必要な場合があります。

デフォルトの`grampsweb:latest` Dockerイメージは、常にAPIの最新バージョンとフロントエンドの最新バージョンを組み合わせています。2つのコンポーネントを別々にアップグレードしたい場合（可能です）、ここで説明されているよりも複雑なセットアップが必要です。
