# フロントエンドのカスタマイズ

Gramps Web フロントエンドは、静的な HTML、CSS、および Javascript ファイルのセットとして展開される Javascript アプリケーションです。通常、フロントエンドには特別な設定は必要ありません。ただし、`config.js` ファイルの適切なオプションを設定することで、いくつかの動作を変更できます。このファイルは配布のルートにあります。

ファイルは以下の構造を持つ必要があります。

```javascript
window.grampsjsConfig = {
    option: value
}
```

以下のオプションキーが存在します。

キー | タイプ | 説明 
----|-----|-----------
`hideDNALink` | boolean | true の場合、ナビゲーションバーの DNA リンクを非表示にします。
`hideRegisterLink` | boolean | true の場合、ログインページの登録リンクを非表示にします。これはマルチツリー展開に使用されるべきです。
`loginRedirect` | string | ログインしていない状態で「login」または「register」以外のページに移動した場合にリダイレクトする URL
`mapBaseStyleLight` | string | ライトテーマのベースマップ用の MapLibre スタイル URL (デフォルト: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | ダークテーマのベースマップ用の MapLibre スタイル URL (デフォルト: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | OpenHistoricalMap オーバーレイ用の MapLibre スタイル URL (デフォルト: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
`mapWikidata` | boolean | false の場合、地図から [Wikidata buildings](../user-guide/map.md#wikidata-buildings) レイヤーを削除します (デフォルト: true)
