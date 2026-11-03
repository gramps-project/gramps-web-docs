# CPUとメモリ使用量の制限

推奨されるDockerベースのセットアップでは、Gramps Webは[Gunicorn](https://gunicorn.org/)を使用してバックエンドを提供し、[Celery](https://docs.celeryq.dev)を使用してバックグラウンドタスクを処理します。いずれの場合も、複数のワーカープロセスを並行して実行できるため、ユーザーの視点からアプリケーションがより応答性を持つようになります。しかし、ワーカーの数を増やすと、使用されるRAMの量も増加します（アプリケーションがアイドル状態のときでも）し、リクエストを並行して処理できるようにすると、高いCPU使用率につながる可能性があります（特に多くのユーザーが同時にアプリケーションを使用している場合）。GunicornとCeleryの両方は、並行ワーカーの数を制限することを許可します。

## システム情報の取得

Linuxでは、次のコマンドを使用してシステムで利用可能なコアの数を確認できます。

```bash
lscpu | grep CPU
```

利用可能なメモリとスワップスペースを確認するには、次のコマンドを使用します。

```bash
free -h
```

## Gunicornワーカーの数の制限

デフォルトのGramps Web Dockerイメージを使用する場合、Gunicornワーカーの数を設定する最も簡単な方法は、環境変数`GUNICORN_NUM_WORKERS`を設定することです。例えば、`docker-compose.yml`ファイルの「environment」セクションで宣言します。

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

理想的なワーカーの数を決定するには、[Gunicornのドキュメント](https://docs.gunicorn.org/en/stable/design.html#how-many-workers)を参照してください。

!!! info
    Dockerイメージは`--preload`オプションを使用してGunicornを起動するため、ワーカーは読み込まれたアプリケーションのメモリを共有し、各追加ワーカーは少ないメモリを必要とします。Gunicornコマンドをオーバーライドする場合は、この利点を享受するために`--preload`を維持してください。

## Celeryワーカーの数の制限

Celeryワーカーの数を設定するには、Docker Composeファイルの`concurrency`設定を調整します。

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

理想的なワーカーの数を決定するには、[Celeryのドキュメント](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency)を参照してください。

!!! info
    `concurrency`フラグが省略されると（これはv2.5.0までのGramps Webドキュメントでのケースでした）、システムで利用可能なCPUコアの数にデフォルト設定され、かなりの量のメモリを消費する可能性があります。
