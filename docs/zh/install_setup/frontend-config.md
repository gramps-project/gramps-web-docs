# 自定义前端

Gramps Web 前端是一个 JavaScript 应用程序，作为一组静态 HTML、CSS 和 JavaScript 文件进行部署。通常，前端不需要特殊配置。然而，通过在发行版根目录下的 `config.js` 文件中设置适当的选项，可以更改某些行为。

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
`hideRegisterLink` | boolean | 如果为 true，则在登录页面上隐藏注册链接。此选项应在多树部署中使用。
`loginRedirect` | string | 当未登录并导航到除“登录”或“注册”以外的任何页面时，重定向到的 URL。
`mapBaseStyleLight` | string | 轻主题下基础地图的 MapLibre 样式 URL（默认：`https://tiles.openfreemap.org/styles/liberty`）
`mapBaseStyleDark` | string | 深色主题下基础地图的 MapLibre 样式 URL（默认：`https://tiles.openfreemap.org/styles/dark`）
`mapOhmStyle` | string | OpenHistoricalMap 覆盖层的 MapLibre 样式 URL（默认：`https://www.openhistoricalmap.org/map-styles/main/main.json`）
