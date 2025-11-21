ローカルコンピュータ（Linux、Mac、またはWindows）でGramps Webを試すために、Gramps Desktopのインストールに干渉せずに、以下のコマンドを使ってDockerを利用できます。

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

これにより、新しい空のGramps Webインスタンスが[http://localhost:5055](http://localhost:5055)でアクセス可能になり、そこで管理ユーザーを作成し、Gramps XMLファイルをインポートできます。

!!! info
    この簡単なセットアップでは、長いタスクを別のプロセスで実行することができないため、大きなGramps XMLファイルのインポートは初回実行アシスタントのタイムアウトにより失敗する可能性があります。

コンピュータからメディアファイルを使用するには、Grampsメディアフォルダをコンテナにマウントすることができます。

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

この操作では、コンテナを再起動した際にデータベースに加えた変更が保持されないことに注意してください。Gramps Webを適切にセットアップするには、[デプロイメント](deployment.md)についての説明を読み続けてください。
