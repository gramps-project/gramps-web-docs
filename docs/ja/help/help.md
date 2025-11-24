---
hide:
  - navigation
---

Gramps Webに関して問題が発生したり、助けが必要な場合は、以下のオプションのいずれかを選択してください。

[フォーラム :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[バックエンドの問題 :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[フロントエンドの問題 :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

最初にどこに行くべきかについてのガイダンスは以下をご覧ください。

## 質問する

公式のGramps Discourseフォーラムには、[Gramps Web専用のカテゴリ](https://gramps.discourse.group/c/gramps-web/)があります。Gramps Webに関する質問がある場合は、こちらを利用してください。例えば、

- Gramps Webの使用に関する質問
- Gramps Webの設定に関する質問
- Gramps Webのデプロイメントのトラブルシューティング
- Gramps Webの改善に関するアイデア
- ...

## 問題を報告する

Gramps Webにバグがあると思われる問題に遭遇した場合は、Githubを通じてサポートしてください。

Gramps Webで使用されるコードには、ユーザーインターフェース（「フロントエンド」）用とサーバーコード（「バックエンド」）用の2つの別々のGithubリポジトリがあります：

- [フロントエンドの問題](https://github.com/gramps-project/gramps-web/issues)
- [バックエンドの問題](https://github.com/gramps-project/gramps-web-api/issues)

どちらに問題を報告すればよいか不明な場合は、心配せずにどちらかを選択してください。メンテナは必要に応じて問題を移動できるでしょう。

いずれの場合でも、報告には必ず以下の情報を含めてください：

- セットアップに関する詳細（例：機密値を隠したdocker-composeファイル、またはGrampshubのようなホスティングされたバージョンを使用しているか、DigitalOceanのような事前設定されたイメージを使用しているか）
- バージョン情報。これを取得するには、Gramps Webの設定ページの「システム情報」タブに移動し、ボックス内の値をコピー＆ペーストしてください。値は以下のようになります：

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## 改善を提案する

将来の改善に関する一般的なアイデアや議論については、[フォーラム](https://gramps.discourse.group/c/gramps-web/)でディスカッションを開くことを自由に行ってください。また、特定の機能がすでに計画されているか、作業中であるかを確認するために、問題ページ（上記のリンク参照）をチェックすることもお勧めします。

限られた範囲の具体的な改善については、適切なフロントエンドまたはバックエンドのGithubリポジトリに機能リクエストとして直接問題を開くことを自由に行ってください。
