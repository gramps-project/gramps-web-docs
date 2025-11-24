バックエンドおよびフロントエンド開発のために、Gramps Web APIに手動でクエリを送信することが便利です。HTTPieとjqを使用すると、JWT認証を含めて簡単に実行できます。

## インストール

HTTPieは`pip`でインストールします：

```bash
python3 -m pip install httpie
```

HTTPieのバージョンは3.0.0以上が必要です。

jqはUbuntuで以下のコマンドを使用してインストールできます。

```bash
sudo apt install jq
```

## アクセストークンの取得

アクセストークンを取得するには、トークンエンドポイントにクエリを送信します。開発インスタンスが`localhost:5555`で実行されていると仮定すると、次のコマンドを使用できます。

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

出力としてJSONトークンが表示されます。

jqを使用すると、アクセストークンを環境変数に保存することもできます：

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

このトークンを認証が必要なすべてのAPI呼び出しに使用できます。例えば：

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

デフォルトでは、アクセストークンは15分後に期限切れになることに注意してください。
