---
hide:
  - toc
  - navigation
---

# 機能


![画像タイトル](screenshots/sync.png){ align=left width="300"}

## Gramps Desktopとの完全統合

Gramps Webは、[Gramps Desktop](https://gramps-project.org/)が系譜データを保存するために使用するのと同じ**モデル/データベース**構造を使用しています。Gramps Desktopで行うのと同じ[レコードタイプ](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)をすべて閲覧できます: ***人々、家族、イベント、場所、リポジトリ、ソース、引用、メディアオブジェクト、およびノート。***

[Gramps Web Sync Add-on](../administration/sync.md)を使用することで、Gramps WebとGramps Desktop間でデータを双方向に同期できます！Gramps Webまたは愛用のGramps Desktopアプリでデータを編集してみてください – それらはシームレスに連携します！

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/fan.png){ align=right width="400"}

## インタラクティブな家系図グラフ

高品質なインタラクティブグラフィックスと設定可能な世代数を使用して、先祖ツリー、子孫ツリー、砂時計グラフ、関係グラフ、またはファンチャートとして家系図をナビゲートできます。

任意の人物にカーソルを合わせると、その人物の重要な事実を表示するプレビューカードが表示され、チャートから詳細ページに直接ジャンプできます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/tree-edit.png){ align=left width="400"}

## チャート内で直接ツリーを構築

ツリービューを編集モードに切り替え、チャートを離れずに家系図を成長させることができます。各人物カードには、父、母、子供、または配偶者を追加するための**+**ボタンがあります – データベースに既にいる誰かをリンクするか、その場で新しい人物を作成できます。各変更は即座に保存されます。

[家系図の編集](../user-guide/tree-edit.md)を参照してください。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/timeline.png){ align=right width="400"}

## 年代順タイムライン

家系図のすべてのイベントが横向きのズーム可能なタイムラインに表示されます。世紀をスクロールしてズームし、特定の人物に絞り込むことができます – あるいはその人のすべての先祖や子孫に – または特定の場所で起こったすべてのことに絞り込むこともできます。

[タイムライン](../user-guide/timeline.md)を参照してください。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/map.png){ align=left width="400"}

## 強力な地図

インタラクティブで検索可能な地図上に、家系図のすべての場所を表示します。場所を作成する際にOpenStreetMapで新しい場所を直接検索し、データベース内の人物を地理的にプロットし、イベントを地図上の線でつなぐことで特定の人物の人生を追跡できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/ohm.png){ align=right width="400"}

## 歴史的地図

Grampsにメディアオブジェクトとして保存された歴史的地図をカスタムマップオーバーレイに変換します。

さらに、[OpenHistoricalMap](https://www.openhistoricalmap.org/)プロジェクトによって作成された歴史的ベクターマップは、系譜マッピングの完璧な補完物です。時間スライダーを使用して、家族の歴史における場所の進化をスクロールし、先祖が住んでいた場所やイベントが発生した場所を表示します。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/search.png){ align=left width="400"}

## 何でも検索

フルテキスト検索エンジンは、テキストノートの内容を含むすべてのGrampsオブジェクトタイプをカバーし、ワイルドカードや論理演算子をサポートします。

サーバーで有効にされている場合、**セマンティック検索**は「19世紀のバイエルンの農夫」のような自然言語クエリに対して、正確な言葉ではなく意味によって応答します。正確なクエリの場合、オブジェクトリストビューは[Grampsクエリ言語](../user-guide/gql.md)に基づく高度なフィルターモードを提供し、テキスト、タグ、プライバシーによるクイックフィルターも提供します。

任意の人物のページから、[外部検索](../user-guide/external-search.md)を開くと、FamilySearch、Ancestry、CompGenなどのサイトで事前に入力された検索が開きます – 自分自身の検索も追加できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/chat.png){ align=right width="400"}

## 統合されたAIアシスタント

AIによって駆動されるGramps Webでは、家系図とチャットできます – 母国語で！

アシスタントは単に検索するだけでなく、データベースに直接クエリを実行し、人物、イベント、家族、場所をフィルタリングし、個人間の関係を計算します。アンサーを構築する際に使用しているツールを確認でき、長い質問はバックグラウンドタスクとして実行されるため、他のページに移動して戻ってくることができます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/dna.png){ align=left width="400"}

## DNAマッチ、染色体ブラウザ＆Y-DNA

DNA系譜プロバイダーからのDNAマッチデータがある場合、それをアップロードして将来にわたって保存し、インタラクティブな染色体ブラウザでマッチを表示できます。

生のY染色体SNPデータを使用して、人物の最も可能性の高い[Y-DNAハプログループ](../user-guide/y-dna.md)を特定し、時期の推定とともに人間のY染色体ツリーにおける父系の先祖を表示できます。分析は完全に自分のサーバー上で実行されるため、データは第三者に送信されることはありません。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/tag.png){ align=right width="400"}

## 自動顔検出による写真の人物タグ付け

親戚と協力して古い家族写真の先祖を特定します。自動顔検出のおかげで、人物のタグ付けはわずか2クリックで行えます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/revisions.png){ align=left width="400"}

## 完全な改訂履歴 – 元に戻す機能付き

家系図へのすべての編集が記録されます。トランザクションごとにグループ化された完全な履歴を閲覧し、個々の変更を詳しく見て、どのフィールドが追加、削除、または変更されたかを正確に確認し、間違いであることが判明した場合はトランザクションを元に戻すことができます。すべてのオブジェクトのページには、誰がいつ変更したかを示す改訂タブもあります。

[改訂履歴](../user-guide/revisions.md)を参照してください。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/list.png){ align=right width="400"}

## プライバシーレベルとユーザーアクセス

多くの人々は、いくつかの詳細を非公開にしておきたいと考えており、私たちはそれを尊重します！レコードをプライベートとしてマークし、どのユーザーがプライベートレコードを表示できるかを制御できます。プライベートレコードは、最大のセキュリティのためにデータベース層でフィルタリングされます。さらに、ユーザーが追加および編集できる内容を制御できます。

ユーザーはパスワードでサインインするか、[OpenID Connect](../install_setup/oidc.md)を使用して外部アイデンティティプロバイダーを介してサインインできます – GoogleやMicrosoftが標準で、Keycloak、Authentik、Autheliaなどのカスタムプロバイダーも利用可能です。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/blog.png){ align=left width="400"}

## 含まれている系譜ブログ

研究をブログストーリーの形で要約し、親戚と共有します。専用のエディタが新しい投稿の作成を簡単にします。すべてのデータはGrampsデータベースに保存されます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/tasks.png){ align=right width="400"}

## 統合されたタスク管理アプリ

Gramps Webには、系譜研究を整理し計画するための統合タスク管理アプリが付属しています。各タスクにステータス、優先度、タグを付け、リッチテキストの説明で進捗を文書化し、収集したメディアを添付します。

タスクはGrampsデータベース内のソースとして保存されるため、系譜データの一部となり、Gramps Desktopでもアクセスおよび編集できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/report.png){ align=left width="400"}

## 印刷可能なレポートを生成

Gramps Desktopを支えるコアの上に直接構築されているため、ブラウザから直接、デスクトップアプリがサポートするほぼすべての[レポート](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Reports)を生成できます。関係グラフや書籍レポートをPDFとして生成できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/export.png){ align=right width="300"}

## ロックインなし – データのインポートとエクスポート

Gramps XMLやGEDCOMを含むさまざまな形式でデータをインポートできるだけでなく、Gramps Webはユーザーがいつでもすべてのデータ（家系図データ、メディアファイル、ユーザーアカウント）をダウンロードできるようにします。バックアップ目的や別のサーバーに移動するために。あなたのデータはあなたのものです！

インポートは、何も書き込まれる前にドライランとしてプレビューでき、完全なバックアップをツリーに復元できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/mobile.png){ align=left width="400"}

## すべてのデバイスで動作

ウェブ対応デバイスからGramps Webにアクセスできます。写真をアップロードしたり、レコードを作成または編集したり、他の人に家系図を見せたり、次の家族の集まりで思い出せない家族の名前を調べたりできます！

Gramps Webはプログレッシブウェブアプリです: ホーム画面やデスクトップにインストールすると、ネイティブアプリのように動作します。デスクトップでは、[キーボードショートカット](../user-guide/shortcuts.md)を使用して数回のキー入力でどこにでも移動できます – `?`を押すとすべてのショートカットが表示されます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/lang.png){ align=right width="300"}

## 完全に国際化

Grampsコミュニティによって翻訳された50以上の言語の中から、インターフェースの言語を切り替えられます。

<div style="clear:both;"></div>

---

## その他

- **通知とバックグラウンドタスク** – インポート、エクスポート、レポート、インデックス再構築がバックグラウンドで実行され、進捗とエラーが一か所に集約されます
- **タグ、ブックマーク、履歴** – 色分けされたタグでオブジェクトを整理し、作業中の内容に戻ることができます
- **一括編集** – リストビューで複数のオブジェクトを選択して一度に削除したり、重複オブジェクトをマージしたりできます
- **カスタマイズ可能なリストビュー** – 表示する列を選択し、テキスト、タグ、プライバシーでフィルタリングできます
- **テキスト認識 (OCR)** – メディアギャラリー内のスキャンした文書からテキストを抽出します
- **データ検証** – 不適切な日付やその他のデータ問題についてツリーをチェックします
- **カレンダー** – グレゴリオ暦、ユリウス暦、ヘブライ暦、フランス革命暦、ペルシャ暦、イスラム暦、またはスウェーデン暦で日付を入力します
- **自分のものにする** – サイトに独自の名前、テーマカラー、ホームページのテキストと画像を設定します

<p>&nbsp;</p>

## デモ

デモにログインするには、以下のいずれかの***ユーザー/パス***のログイン資格情報を使用してください。それぞれはGramps Webユーザーに割り当てられる可能性のあるユーザータイプを表しています。

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`


[デモログインに移動](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}


### 感謝

デモはDigitalOceanのご支援により実現しています。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
