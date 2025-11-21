# フロントエンドのカスタマイズ

Gramps Web フロントエンドは、静的な HTML、CSS、および Javascript ファイルのセットとしてデプロイされる Javascript アプリケーションです。通常、フロントエンドに特別な設定は必要ありません。ただし、`config.js` ファイルで適切なオプションを設定することで、一部の動作を変更できます。このファイルは、配布のルートに配置されます。

ファイルは以下の構造を持つ必要があります：

```javascript
window.grampsjsConfig = {
    option: value
}
```

以下のオプションキーが存在します。

Key | Type | Description 
----|-----|-----------
`hideDNALink` | boolean | true の場合、ナビゲーションバーの DNA リンクを非表示にします。
`hideRegisterLink` | boolean | true の場合、ログインページの登録リンクを非表示にします。これはマルチツリーのデプロイメントで使用する必要があります。
`loginRedirect` | string | ログインしていない状態で「login」または「register」以外のページに移動したときにリダイレクトする URL
`leafletTileUrl` | string | Leaflet マップ用のカスタムタイル URL
`leafletTileSize` | number | Leaflet マップ用のカスタムタイルサイズ
`leafletZoomOffset` | number | Leaflet マップ用のカスタムズームオフセット
`leafletTileAttribution` | string | Leaflet マップ用のカスタム帰属
