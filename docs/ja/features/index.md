---
hide:
  - toc
  - navigation
---

# 機能


![画像タイトル](screenshots/sync.png){ align=left width="300"}

## Gramps Desktopとの完全統合

Gramps Webは、系譜データを保存するために[Gramps Desktop](https://gramps-project.org/)が使用するのと同じ**モデル/データベース**構造を使用しています。Gramps Desktopで行うのと同様に、すべての[レコードタイプ](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)を閲覧できます：***人々、家族、イベント、場所、リポジトリ、ソース、引用、メディアオブジェクト、ノート。***

[Gramps Web Sync Add-on](../administration/sync.md)を使用することで、Gramps WebとGramps Desktopの間でデータを双方向に同期できます！Gramps Webまたは愛用のGramps Desktopアプリでデータを編集してみてください – 両者はシームレスに連携します！

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/fan.png){ align=right width="400"}

## インタラクティブな家系図グラフ

高品質のインタラクティブグラフィックスと設定可能な世代数を使用して、先祖ツリー、子孫ツリー、砂時計グラフ、関係グラフ、またはファンチャートとして家系図をナビゲートできます。

任意の人物にマウスをホバーすると、その人物の重要な事実を含むプレビューカードが表示され、チャートから詳細ページに直接ジャンプできます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/tree-edit.png){ align=left width="400"}

## チャート内でツリーを構築

ツリービューを編集モードに切り替え、チャートを離れずに家系図を成長させます。各人物カードには、父、母、子、または配偶者を追加するための**+**ボタンがあり、すでにデータベースにいる誰かをリンクするか、その場で新しい人物を作成できます。各変更は即座に保存されます。

[家系図の編集](../user-guide/tree-edit.md)を参照してください。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/timeline.png){ align=right width="400"}

## 年代順タイムライン

家系図内のすべてのイベントを水平でズーム可能なタイムラインに表示します。世紀をスクロールしてズームし、特定の人物にフィルタリングすることも、すべての先祖や子孫にフィルタリングすることも、特定の場所で起こったすべてのことにフィルタリングすることもできます。

[タイムライン](../user-guide/timeline.md)を参照してください。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/map.png){ align=left width="400"}

## 強力な地図

インタラクティブで検索可能な地図上に家系図内のすべての場所を表示します。場所を作成する際にOpenStreetMapで新しい場所を直接検索し、データベース内の人物を地理的にプロットし、イベントを地図上の線で結ぶことで特定の人物の人生を追跡します。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/ohm.png){ align=right width="400"}

## 歴史的地図

Grampsにメディアオブジェクトとして保存された歴史的地図をカスタムマップオーバーレイに変換します。

さらに、[OpenHistoricalMap](https://www.openhistoricalmap.org/)プロジェクトによって作成された歴史的ベクターマップは、系譜マッピングに最適な補完物です。タイムスライダーを使用して家族の歴史における場所の進化をスクロールし、先祖が住んでいた場所やイベントが発生した場所を表示します。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/search.png){ align=left width="400"}

## 何でも見つける

フルテキスト検索エンジンは、テキストノートの内容を含むすべてのGrampsオブジェクトタイプをカバーし、ワイルドカードと論理演算子をサポートします。

正確なクエリのために、オブジェクトリストビューは[Grampsクエリ言語](../user-guide/gql.md)に基づく高度なフィルターモードを提供し、テキスト、タグ、およびプライバシーによるクイックフィルターも提供します。

任意の人物のページから、[外部検索](../user-guide/external-search.md)を開くと、FamilySearch、Ancestry、CompGenなどのサイトで事前に入力された検索が開きます – 自分のサイトを追加することもできます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/chat.png){ align=right width="400"}

## 統合されたAIアシスタント

AIによって動かされるGramps Webでは、家系図とチャットできます – 母国語で！

アシスタントは単に検索するだけでなく、ツールのセットを使用してデータベースに直接クエリを実行し、人物、イベント、家族、場所をフィルタリングし、個人間の関係を計算します。アンサーを構築する際に使用しているツールを確認でき、長い質問はバックグラウンドタスクとして実行されるため、他のページに移動して戻ることができます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/dna.png){ align=left width="400"}

## DNAマッチ、染色体ブラウザ＆Y-DNA

DNA系譜プロバイダーからのDNAマッチデータがある場合は、それをアップロードして将来にわたって保存し、インタラクティブな染色体ブラウザでマッチを表示します。

生のY染色体SNPデータを使用して、個人の最も可能性の高い[Y-DNAハプログループ](../user-guide/y-dna.md)を特定し、父系の祖先を人間のY染色体ツリーに表示し、タイミングの推定を行います。分析は完全に自分のサーバー上で実行されるため、データは第三者に送信されることはありません。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/tag.png){ align=right width="400"}

## 自動顔検出による写真の人物タグ付け

親戚と協力して古い家族写真の先祖を特定します。自動顔検出のおかげで、人物のタグ付けはわずか2クリックで完了します。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/revisions.png){ align=left width="400"}

## 完全な改訂履歴 – 元に戻す機能付き

家系図へのすべての編集が記録されます。トランザクションごとにグループ化された完全な履歴を閲覧し、個々の変更を掘り下げて、どのフィールドが追加、削除、または変更されたかを正確に確認し、間違いが判明した場合はトランザクションを元に戻すことができます。すべてのオブジェクトのページには、誰がいつ変更したかを示す改訂タブもあります。

[改訂履歴](../user-guide/revisions.md)を参照してください。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/list.png){ align=right width="400"}

## プライバシーレベルとユーザーアクセス

多くの人々は、いくつかの詳細を非公開にしたいと考えており、私たちはそれを尊重します！レコードをプライベートとしてマークし、どのユーザーがプライベートレコードを表示できるかを制御できます。プライベートレコードは、最大のセキュリティのためにデータベース層でフィルタリングされます。さらに、ユーザーが追加および編集できる内容を制御できます。

ユーザーはパスワードでサインインするか、[OpenID Connect](../install_setup/oidc.md)を使用して外部アイデンティティプロバイダーを介してサインインできます – GoogleやMicrosoftが標準で、Keycloak、Authentik、Autheliaなどのカスタムプロバイダーも利用可能です。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/blog.png){ align=left width="400"}

## 系譜ブログが含まれています

研究をブログストーリーの形式で要約し、親戚と共有します。専用のエディタにより、新しい投稿を書くのが簡単になります。すべてのデータはGrampsデータベースに保存されます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/tasks.png){ align=right width="400"}

## 統合されたタスク管理アプリ

Gramps Webには、系譜研究を整理し計画するための統合されたタスク管理アプリが付属しています。各タスクにステータス、優先度、タグを付け、進捗をリッチテキストの説明で文書化し、収集したメディアを添付します。

タスクはGrampsデータベース内のソースとして保存されるため、系譜データの一部となり、Gramps Desktopでもアクセスおよび編集できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/report.png){ align=left width="400"}

## 印刷可能なレポートを生成

Gramps Desktopを支えるコアの上に直接構築されているため、ブラウザから直接、デスクトップアプリがサポートするほぼすべての[レポート](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Reports)を生成できます。関係グラフやブックレポートをPDFとして生成することが可能です。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/export.png){ align=right width="300"}

## ロックインなし – データのインポートとエクスポート

Gramps XMLやGEDCOMを含むさまざまな形式でデータをインポートできるだけでなく、Gramps Webはユーザーがすべてのデータ（家系図データ、メディアファイル、ユーザーアカウント）をいつでもダウンロードできるようにします。バックアップ目的や別のサーバーに移動するために。あなたのデータはあなたのものです！

インポートは、何も書き込む前にドライランとしてプレビューでき、完全なバックアップをツリーに復元できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/mobile.png){ align=left width="400"}

## すべてのデバイスで動作

ウェブ対応デバイスからGramps Webにアクセスできます。写真をアップロードしたり、レコードを作成または編集したり、家系図を他の人に見せたり、次の家族の再会で思い出せない家族の名前を調べたりできます！

Gramps Webはプログレッシブウェブアプリです：ホーム画面やデスクトップにインストールすると、ネイティブアプリのように動作します。デスクトップでは、[キーボードショートカット](../user-guide/shortcuts.md)を使用して数回のキー操作でどこにでも移動できます – `?`を押すとすべてが表示されます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/lang.png){ align=right width="300"}

## 完全に国際化

Grampsコミュニティによって翻訳された50以上の言語の中からインターフェースの言語を切り替えられます。

<div style="clear:both;"></div>

---

## さらに多くの機能

- **通知とバックグラウンドタスク** – インポート、エクスポート、レポート、インデックス再構築はバックグラウンドで実行され、進捗とエラーが一箇所に集約されます
- **タグ、ブックマーク、履歴** – 色分けされたタグでオブジェクトを整理し、作業中のものに戻ります
- **一括編集** – リストビューで複数のオブジェクトを選択して一度に削除したり、重複オブジェクトをマージしたりできます
- **カスタマイズ可能なリストビュー** – 表示する列を選択し、テキスト、タグ、またはプライバシーでフィルタリングします
- **テキスト認識（OCR）** – メディアギャラリー内のスキャンした文書からテキストを抽出します
- **データ検証** – 不合理な日付やその他のデータの問題がないかツリーをチェックします
- **カレンダー** – グレゴリオ暦、ユリウス暦、ヘブライ暦、フランス革命暦、ペルシャ暦、イスラム暦、またはスウェーデン暦で日付を入力します
- **自分のものにする** – サイトに独自の名前、テーマカラー、ホームページのテキストと画像を付けます

<p>&nbsp;</p>

## デモ

デモにログインするには、以下のいずれかの***ユーザー/パス***のログイン資格情報を使用してください。各ユーザータイプはGramps Webユーザーに割り当てられる可能性があります。

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`


[デモログインに移動](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}


### 感謝

デモはDigitalOceanによって親切にサポートされています。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
