ローカルコンピュータ（Linux、Mac、またはWindows）でGramps Webを試すには、Gramps Desktopのインストールに干渉せずに、次のコマンドを使用してDockerを利用できます。

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new ghcr.io/gramps-project/grampsweb:latest
```

これにより、新しい空のGramps Webインスタンスが[http://localhost:5055](http://localhost:5055)でアクセス可能になり、ここで管理者ユーザーを作成し、Gramps XMLファイルをインポートできます。

!!! info
    この簡単なセットアップでは、長時間のタスクを別のプロセスで実行することができないため、大きなGramps XMLファイルのインポートは、初回実行アシスタントのタイムアウトにより失敗する可能性があります。


コンピュータからメディアファイルを使用するには、次のコマンドでGrampsメディアフォルダーをコンテナにマウントできます。

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

この操作は、コンテナを再起動したときにデータベースに加えた変更を保持しないことに注意してください。Gramps Webを適切に設定するには、[デプロイメント](deployment.md)についての説明を読み続けてください。
