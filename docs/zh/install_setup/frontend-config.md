# 自定义前端

Gramps Web 前端是一个 JavaScript 应用程序，作为一组静态 HTML、CSS 和 JavaScript 文件进行部署。通常，前端不需要特殊配置。然而，可以通过在发行版根目录下的 `config.js` 文件中设置适当的选项来改变某些行为。

该文件应具有以下结构：

```javascript
window.grampsjsConfig = {
    option: value
}
```

以下选项键存在。

键 | 类型 | 描述 
----|-----|-----------
`hideDNALink` | boolean | 如果为 true，则在导航栏上隐藏 DNA 链接。
`hideRegisterLink` | boolean | 如果为 true，则在登录页面上隐藏注册链接。这应在多树部署中使用。
`loginRedirect` | string | 当未登录并导航到除“登录”或“注册”以外的任何页面时，重定向到的 URL
`leafletTileUrl` | string | Leaflet 地图的自定义图块 URL
`leafletTileSize` | number | Leaflet 地图的自定义图块大小
`leafletZoomOffset` | number | Leaflet 地图的自定义缩放偏移
`leafletTileAttribution` | string | Leaflet 地图的自定义归属
