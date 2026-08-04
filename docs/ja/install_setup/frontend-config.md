# フロントエンドのカスタマイズ

Gramps Web フロントエンドは、静的な HTML、CSS、および Javascript ファイルのセットとしてデプロイされる Javascript アプリケーションです。通常、フロントエンドに特別な設定は必要ありません。ただし、`config.js` ファイルに適切なオプションを設定することで、いくつかの動作を変更できます。このファイルは配布のルートにあります。

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
`hideRegisterLink` | boolean | true の場合、ログインページの登録リンクを非表示にします。これはマルチツリーのデプロイメントに使用するべきです。
`loginRedirect` | string | ログインしていない状態で「login」または「register」以外のページに移動したときにリダイレクトする URL
`mapBaseStyleLight` | string | ライトテーマのベースマップ用の MapLibre スタイル URL (デフォルト: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | ダークテーマのベースマップ用の MapLibre スタイル URL (デフォルト: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | OpenHistoricalMap オーバーレイ用の MapLibre スタイル URL (デフォルト: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
