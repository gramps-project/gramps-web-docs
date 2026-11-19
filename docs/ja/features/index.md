---
hide:
  - toc
  - navigation
---

# 機能

Gramps Webは、共同系譜のためのウェブアプリです。オープンソースの系譜プログラムである[Gramps](https://gramps-project.org/)に基づいており、同じデータで動作します。自分のサーバーで実行することも、ホスティングプロバイダーを利用することもできます。

[デモを試す](#demo){ .md-button .md-button--primary } [始める](../install_setup/setup.md){ .md-button }

## 家系図を探る { .feature-group }

![先祖の七世代を示すファンチャート](screenshots/fan.png){ align=right width="400"}

### インタラクティブな家系図グラフ

高品質なインタラクティブグラフィックスと設定可能な世代数で、先祖ツリー、子孫ツリー、砂時計グラフ、関係グラフ、またはファンチャートとして家系図をナビゲートできます。

任意の人物にマウスを合わせると、その人物の重要な事実が記載されたプレビューカードが表示され、チャートから詳細ページに直接ジャンプできます。

<div style="clear:both;"></div>

---

![1940年代から1970年代の家族イベントのタイムライン](screenshots/timeline.png){ align=left width="400"}

### 年代順のタイムライン

あなたの家系図にあるすべてのイベントを横向きのズーム可能なタイムラインに表示します。世紀をスクロールし、ズームした後、特定の人物に絞り込むことができます - またはその人物のすべての先祖や子孫、または特定の場所で起こったすべてのことに絞り込むことができます。

[タイムライン](../user-guide/timeline.md)を参照してください。

<div style="clear:both;"></div>

---

![場所が選択されたロンドンの地図、写真とイベントを表示](screenshots/map.png){ align=right width="400"}

### インタラクティブマップ

あなたの家系図にあるすべての場所をインタラクティブで検索可能な地図に表示します。場所を作成する際にOpenStreetMapで新しい場所を直接検索し、データベース内の人物を地理的にプロットし、イベントを地図上の線でつなげて特定の人物の人生をたどることができます。

<div style="clear:both;"></div>

---

![1707年に設定された時間スライダーを持つOpenHistoricalMapレイヤーのロンドン](screenshots/ohm.png){ align=left width="400"}

### 歴史的地図

Grampsにメディアオブジェクトとして保存された歴史的地図をカスタムマップオーバーレイに変換します。

また、[OpenHistoricalMap](https://www.openhistoricalmap.org/)プロジェクトの歴史的ベクターマップに切り替えることもできます。時間スライダーを使用して家族の歴史における場所の進化をスクロールし、先祖が住んでいた場所やイベントが発生した場所を表示します。

<div style="clear:both;"></div>

---

![人物、イベント、メディアに対する「アルバート」の検索結果](screenshots/search.png){ align=right width="400"}

### 何でも見つける

フルテキスト検索エンジンは、テキストノートの内容を含むすべてのGrampsオブジェクトタイプをカバーし、ワイルドカードや論理演算子をサポートします。

正確なクエリのために、オブジェクトリストビューは[Grampsオブジェクトクエリ言語](../user-guide/goql.md)に基づく高度なフィルターモードを提供し、テキスト、タグ、プライバシーによるクイックフィルターも利用できます。

任意の人物のページから、[外部検索](../user-guide/external-search.md)を開くと、FamilySearch、Ancestry、CompGenなどのサイトで事前に入力された検索が行われます - 自分のサイトを追加することもできます。

<div style="clear:both;"></div>

## 構築と研究 { .feature-group }

![家族のメンバーを追加するためのダイアログを持つ編集モードの先祖ツリー](screenshots/tree-edit.png){ align=left width="400"}

### チャート内で直接家系図を構築

ツリービューを編集モードに切り替え、チャートを離れずに家系図を成長させます。すべての人物カードには、父、母、子、または配偶者を追加するための**+**ボタンがあります - すでにデータベースにいる誰かをリンクするか、その場で新しい人物を作成することができます。各変更は即座に保存されます。

[家系図の編集](../user-guide/tree-edit.md)を参照してください。

<div style="clear:both;"></div>

---

![出生証明書を読み取り、新しい記録を提案するAIアシスタント](screenshots/chat.png){ align=right width="400"}

### 統合されたAIアシスタント

自分の言語で家系図に関する質問をし、データに基づいた回答を得ることができます。

アシスタントは単に検索するだけでなく、ツールのセットを使用してデータベースに直接クエリを実行し、人物、イベント、家族、場所をフィルタリングし、個人間の関係を計算します。回答を構築する際に使用しているツールを観察でき、長い質問はバックグラウンドタスクとして実行されるため、他のページに移動して戻ってくることができます。

アシスタントはオプションであり、[サーバー管理者によって設定される必要があります](../install_setup/chat.md)が、AIモデルプロバイダーが必要です。

<div style="clear:both;"></div>

---

![11人のマッチの共有DNAセグメントを示す染色体ブラウザ](screenshots/dna.png){ align=left width="400"}

### DNAマッチ、染色体ブラウザ & Y-DNA

DNAテストプロバイダーからDNAマッチデータをアップロードし、家系図と一緒に保存し、インタラクティブな染色体ブラウザでマッチを表示します。

生のY染色体SNPデータは、個人の最も可能性の高い[Y-DNAハプログループ](../user-guide/y-dna.md)を特定し、推定タイミングを伴って人間のY染色体ツリーにおける父系の先祖を表示するために使用できます。分析は完全に自分のサーバー上で実行されるため、データは第三者に送信されることはありません。

<div style="clear:both;"></div>

---

![2人がタグ付けされ、他の検出された顔がアウトライン表示された絵画](screenshots/tag.png){ align=right width="400"}

### 自動顔検出による写真の人物タグ付け

古い家族写真の先祖を親戚と一緒に特定します。顔は自動的に検出されるため、人物にタグ付けするのは2クリックで済みます。

<div style="clear:both;"></div>

---

![ステータス、優先度、タグを持つ研究タスクのリスト](screenshots/tasks.png){ align=left width="400"}

### 統合されたタスク管理アプリ

Gramps Webには、系譜研究を整理し計画するための統合されたタスク管理アプリが付属しています。各タスクにステータス、優先度、タグを付け、進捗をリッチテキストの説明で文書化し、収集したメディアを添付します。

タスクはGrampsデータベース内のソースとして保存されるため、系譜データの一部となり、Gramps Desktopでもアクセスおよび編集が可能です。

<div style="clear:both;"></div>

---

![家族写真の人物を特定することに関するブログ投稿](screenshots/blog.png){ align=right width="400"}

### 系譜ブログが含まれています

研究を写真付きのブログストーリーの形で要約し、親戚と共有します。専用のエディタにより、新しい投稿を書くのが簡単です。すべてのデータはGrampsデータベースに保存されます。

<div style="clear:both;"></div>

## 一緒に作業する { .feature-group }

![家系図の人物リスト](screenshots/list.png){ align=left width="400"}

### プライバシーレベルとユーザーアクセス

[レコードをプライベートとしてマークする](../user-guide/privacy.md)ことができ、個々の名前、イベントリンク、またはDNAマッチまで制御し、どのユーザーがプライベートレコードを表示できるかを制御します。プライベートレコードは最大のセキュリティのためにデータベース層でフィルタリングされます。さらに、ユーザーが追加および編集できる内容を制御することもできます。

ユーザーはパスワードでサインインするか、[OpenID Connect](../install_setup/oidc.md)を使用して外部アイデンティティプロバイダーを通じてサインインできます - GoogleやMicrosoftは標準で、Keycloak、Authentik、Autheliaなどのカスタムプロバイダーも利用可能です。

<div style="clear:both;"></div>

---

![人物レコードの変更されたフィールドを示すリビジョン](screenshots/revisions.png){ align=right width="400"}

### 完全なリビジョン履歴 - 元に戻す機能付き

家系図のすべての編集が記録されます。トランザクションごとにグループ化された完全な履歴を閲覧し、個々の変更を詳しく見て、どのフィールドが追加、削除、または変更されたかを正確に確認し、間違いが判明した場合はトランザクションを元に戻すことができます。すべてのオブジェクトのページにも、誰がいつ変更したかを示すリビジョンタブがあります。

[リビジョン履歴](../user-guide/revisions.md)を参照してください。

<div style="clear:both;"></div>

---

![Gramps DesktopのツールメニューにあるGramps Web Syncエントリ](screenshots/sync.png){ align=left width="300"}

### Gramps Desktopとの完全な統合

Gramps Webは、[Gramps Desktop](https://gramps-project.org/)と同じデータモデルとデータベースを使用しています。すべての同じ[レコードタイプ](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)：人物、家族、イベント、場所、リポジトリ、ソース、引用、メディアオブジェクト、ノートをブラウズおよび編集できます。

[Gramps Web Syncアドオン](../administration/sync.md)を使用すると、データを双方向で同期できるため、Gramps DesktopとGramps Webで並行して作業を続けることができます。

<div style="clear:both;"></div>

## レポートとデータエクスポート { .feature-group }

![PDFとして生成された先祖レポート](screenshots/report.png){ align=right width="400"}

### 印刷可能なレポートを生成

Gramps WebはGramps Desktopと同じコアに基づいているため、ブラウザから直接、デスクトップアプリがサポートするほぼすべての[レポート](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports)を生成できます。関係グラフや書籍レポートをPDFとして生成できます。

<div style="clear:both;"></div>

---

![利用可能なファイル形式のリストを持つエクスポートページ](screenshots/export.png){ align=left width="300"}

### ロックインなし - データのインポートとエクスポート

Gramps XMLやGEDCOMなど、さまざまな形式でデータをインポートし、バックアップや別のサーバーに移動するために、いつでもすべてのデータ - 家系図データ、メディアファイル、ユーザーアカウント - をダウンロードできます。

インポートは、何も書き込む前にドライランとしてプレビューでき、完全なバックアップをツリーに復元できます。

<div style="clear:both;"></div>

## どこでも使用できる { .feature-group }

![デスクトップと電話の同じ人物ページ](screenshots/mobile.png){ align=right width="400"}

### すべてのデバイスで動作

Gramps Webをウェブブラウザを搭載した任意のデバイスで使用できます：写真をアップロードしたり、レコードを作成または編集したり、次の家族の再会で親戚に家系図を見せたりできます。

Gramps Webはプログレッシブウェブアプリです：ホームスクリーンやデスクトップにインストールすると、ネイティブアプリのように動作します。デスクトップでは、[キーボードショートカット](../user-guide/shortcuts.md)を使用して数回のキー入力でどこにでも移動できます - `?`を押すとすべてのショートカットが表示されます。

<div style="clear:both;"></div>

---

![言語選択メニュー](screenshots/lang.png){ align=left width="300"}

### 完全に国際化

Grampsコミュニティによって翻訳された50以上の言語のいずれかでインターフェースを使用できます。

<div style="clear:both;"></div>

## さらに多くの機能

- **通知とバックグラウンドタスク** - インポート、エクスポート、レポート、インデックス再構築はバックグラウンドで実行され、進捗とエラーは1か所に集約されます
- **タグ、ブックマーク、履歴** - 色分けされたタグでオブジェクトを整理し、作業していたものに戻ることができます
- **一括編集** - リストビューで複数のオブジェクトを選択して一度に削除したり、重複オブジェクトをマージしたりできます
- **カスタマイズ可能なリストビュー** - 表示する列を選択し、テキスト、タグ、プライバシーでフィルタリングできます
- **テキスト認識（OCR）** - メディアギャラリー内のスキャンされた文書からテキストを抽出します
- **データ検証** - 不適切な日付やその他のデータ問題についてツリーをチェックします
- **カレンダー** - グレゴリオ暦、ユリウス暦、ヘブライ暦、フランス革命暦、ペルシャ暦、イスラム暦、またはスウェーデン暦で日付を入力します
- **自分のものにする** - サイトに独自の名前、テーマカラー、ホームページのテキストと画像を設定します

## デモ

デモにログインするには、以下のユーザー名/パスワードのペアのいずれかを使用してください。各ペアはGramps Webのユーザーロールの1つを表しています。

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

デモは2時間ごとにリセットされるため、行った変更は一時的です。

[デモログインに移動](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### 感謝

デモはDigitalOceanのご支援により提供されています。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
