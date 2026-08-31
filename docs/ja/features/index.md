---
hide:
  - toc
  - navigation
---

# 機能


![画像タイトル](screenshots/sync.png){ align=left width="300"}

## Gramps Desktopとの完全統合

Gramps Webは、[Gramps Desktop](https://gramps-project.org/)が系譜データを保存するために使用するのと同じ**モデル/データベース**構造を使用しています。Gramps Desktopで行うのと同様に、すべての[レコードタイプ](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)をブラウズできます: ***人々、家族、イベント、場所、リポジトリ、ソース、引用、メディアオブジェクト、ノート。***

[Gramps Web Sync Add-on](../administration/sync.md)を使用することで、Gramps WebとGramps Desktop間でデータを双方向に同期できます！Gramps Webや、あなたが知っているGramps Desktopアプリでデータを編集してみてください – それらはシームレスに連携します！

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/fan.png){ align=right width="400"}

## インタラクティブな家系図グラフ

高品質のインタラクティブグラフィックスと設定可能な世代数で、祖先ツリー、子孫ツリー、砂時計グラフ、関係グラフ、またはファンチャートとして家系図をナビゲートできます。

任意の人物にマウスをホバーすると、その人物の主要な事実を含むプレビューカードが表示され、チャートから詳細ページに直接ジャンプできます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/tree-edit.png){ align=left width="400"}

## チャート内で直接ツリーを構築

ツリービューを編集モードに切り替え、チャートを離れずに家系図を成長させることができます。すべての人物カードには、父、母、子、または配偶者を追加するための**+**ボタンがあり、データベース内の既存の人物をリンクするか、その場で新しい人物を作成できます。各変更は即座に保存されます。

[家系図の編集](../user-guide/tree-edit.md)を参照してください。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/timeline.png){ align=right width="400"}

## 年代順のタイムライン

家系図内のすべてのイベントを横向きのズーム可能なタイムラインに表示します。世紀をスクロールしてズームし、単一の人物、またはその祖先や子孫、あるいは特定の場所で起こったすべての出来事にフィルタリングできます。

[タイムライン](../user-guide/timeline.md)を参照してください。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/map.png){ align=left width="400"}

## 強力な地図

インタラクティブで検索可能な地図上に、家系図内のすべての場所を表示します。場所を作成する際にOpenStreetMapで新しい場所を直接検索し、データベース内の人物を地理的にプロットし、地図上でイベントを線で結ぶことで特定の人物の人生を追跡できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/ohm.png){ align=right width="400"}

## 歴史的地図

Grampsにメディアオブジェクトとして保存された歴史的地図をカスタムマップオーバーレイに変換します。

さらに、[OpenHistoricalMap](https://www.openhistoricalmap.org/)プロジェクトによって作成された歴史的ベクターマップは、系譜マッピングに最適な補完物です。時間スライダーを使用して、家族の歴史における場所の進化をスクロールし、祖先が住んでいた場所やイベントが発生した場所を表示します。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/search.png){ align=left width="400"}

## 何でも見つける

フルテキスト検索エンジンは、テキストノートの内容を含むすべてのGrampsオブジェクトタイプをカバーし、ワイルドカードと論理演算子をサポートします。

サーバーで有効になっている場合、**セマンティック検索**は「19世紀のバイエルンの農夫」のような自然言語クエリに対して、正確な単語ではなく意味で応答します。正確なクエリには、[Gramps Query Language](../user-guide/gql.md)に基づく高度なフィルターモードを提供するオブジェクトリストビューがあり、テキスト、タグ、プライバシーによるクイックフィルターも利用できます。

任意の人物のページから、[外部検索](../user-guide/external-search.md)は、FamilySearch、Ancestry、CompGenなどのサイトで事前に入力された検索を開きます – 自分自身の検索も追加できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/chat.png){ align=right width="400"}

## 統合されたAIアシスタント

AIによって動かされるGramps Webでは、あなたの家系図とチャットできます – 母国語で！

アシスタントは単に検索するだけではなく、データベースに直接クエリを実行し、人物、イベント、家族、場所をフィルタリングし、個人間の関係を計算します。アシスタントが回答を構築する際に使用しているツールを確認でき、長い質問はバックグラウンドタスクとして実行されるため、他の作業に移動して戻ってくることができます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/dna.png){ align=left width="400"}

## DNAマッチ、染色体ブラウザ & Y-DNA

DNA系譜プロバイダーからのDNAマッチデータがある場合、それをアップロードして将来にわたって保存し、インタラクティブな染色体ブラウザでマッチを表示できます。

生のY染色体SNPデータは、個人の最も可能性の高い[Y-DNAハプログループ](../user-guide/y-dna.md)を特定し、タイミングの推定を伴って人間のY染色体ツリーにおける父系の祖先を表示するために使用できます。分析は完全にあなた自身のサーバー上で実行されるため、データは第三者に送信されることはありません。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/tag.png){ align=right width="400"}

## 自動顔検出による写真内の人物タグ付け

親戚と協力して古い家族写真の祖先を特定します。自動顔検出のおかげで、人物のタグ付けはわずか2クリックで完了します。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/revisions.png){ align=left width="400"}

## 完全な改訂履歴 – 元に戻す機能

家系図へのすべての編集が記録されます。トランザクションごとにグループ化された完全な履歴をブラウズし、どのフィールドが追加、削除、または変更されたかを正確に確認するために任意の個別の変更を掘り下げ、間違いであることが判明した場合はトランザクションを元に戻すことができます。

[改訂履歴](../user-guide/revisions.md)を参照してください。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/list.png){ align=right width="400"}

## プライバシーレベル & ユーザーアクセス

多くの人々は一部の詳細を非公開にしたいと考えており、私たちはそれを尊重します！レコードをプライベートとしてマークし、どのユーザーがプライベートレコードを表示できるかを制御できます。プライベートレコードは、最大のセキュリティのためにデータベース層でフィルタリングされます。さらに、ユーザーが追加および編集できる内容を制御できます。

ユーザーはパスワードでサインインするか、[OpenID Connect](../install_setup/oidc.md)を使用して外部アイデンティティプロバイダーを介してサインインできます – GoogleとMicrosoftは標準で、Keycloak、Authentik、Autheliaなどのカスタムプロバイダーも利用可能です。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/blog.png){ align=left width="400"}

## 含まれる系譜ブログ

研究をブログストーリーの形で要約し、親戚と共有します。専用のエディタにより、新しい投稿の作成が簡単になります。すべてのデータはGrampsデータベースに保存されます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/tasks.png){ align=right width="400"}

## 統合されたタスク管理アプリ

Gramps Webには、系譜研究を整理し計画するための統合されたタスク管理アプリが付属しています。各タスクにステータス、優先度、タグを付け、進捗をリッチテキストの説明で文書化し、途中で収集したメディアを添付します。

タスクはGrampsデータベース内のソースとして保存されるため、系譜データの一部となり、Gramps Desktopでもアクセスおよび編集できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/report.png){ align=left width="400"}

## 印刷可能なレポートを生成

Gramps Desktopを支えるコアに直接構築されているため、ブラウザから直接、デスクトップアプリがサポートするほぼすべての[レポート](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Reports)を生成できます。関係グラフや書籍レポートをPDFとして含みます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/export.png){ align=right width="300"}

## ロックインなし – データのインポートとエクスポート

Gramps XMLやGEDCOMを含むさまざまな形式でデータをインポートできるだけでなく、Gramps Webはユーザーがいつでもすべてのデータ（家系図データ、メディアファイル、ユーザーアカウント）をダウンロードできるようにし、バックアップや別のサーバーへの移動が可能です。あなたのデータはあなたのものです！

インポートは、何も書き込む前にドライランとしてプレビューでき、完全なバックアップをツリーに復元できます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/mobile.png){ align=left width="400"}

## すべてのデバイスで動作

任意のウェブ対応デバイスからGramps Webにアクセスできます。写真をアップロードしたり、レコードを作成または編集したり、他の人に家系図を見せたり、次の家族の集まりで思い出せない家族の名前を調べたりできます！

Gramps Webはプログレッシブウェブアプリです: ホーム画面やデスクトップにインストールすると、ネイティブアプリのように動作します。デスクトップでは、[キーボードショートカット](../user-guide/shortcuts.md)を使って数回のキー操作でどこにでも移動できます – `?`を押すとすべてのショートカットが表示されます。

<div style="clear:both;"></div>

---

![画像タイトル](screenshots/lang.png){ align=right width="300"}

## 完全に国際化

Grampsコミュニティによって翻訳された50以上の言語の中から、インターフェースの言語を切り替えられます。

<div style="clear:both;"></div>

---

## さらに多くの機能

- **通知とバックグラウンドタスク** – インポート、エクスポート、レポート、インデックスの再構築がバックグラウンドで実行され、進捗とエラーが一箇所に集約されます
- **カレンダーの記念日** – どのカレンダーアプリからでも家族の誕生日や記念日を購読できます
- **タグ、ブックマーク、履歴** – 色分けされたタグでオブジェクトを整理し、作業していたものに戻ることができます
- **一括編集** – リストビューで複数のオブジェクトを選択して一度に削除したり、重複オブジェクトをマージしたりできます
- **カスタマイズ可能なリストビュー** – 表示する列を選択し、テキスト、タグ、プライバシーでフィルタリングできます
- **テキスト認識（OCR）** – メディアギャラリー内のスキャンした文書からテキストを抽出します
- **データ検証** – 不自然な日付やその他のデータの問題をチェックします
- **あなた自身のものにする** – サイトに独自の名前、テーマカラー、ホームページのテキストと画像を付けます

<p>&nbsp;</p>

## デモ

デモにログインするには、以下のいずれかの***ユーザー/パス***のログイン資格情報を使用してください。各ユーザータイプはGramps Webユーザーに割り当てられる可能性があります。

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`


[デモログインに移動](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}


### 感謝

デモはDigitalOceanのご支援により実現しました。

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
