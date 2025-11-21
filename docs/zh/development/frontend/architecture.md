# 架构

## 组件

前端由 Web 组件构建。这些组件在 `src` 目录中的 Javascript 文件中定义。

通常，每个文件定义一个组件，开始于
```javascript
class GrampsjsSomeElement extends LitElement
```
并以
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
结束，这定义了可以在其他地方使用的新 HTML 元素 `grampsjs-some-element`。

主要入口点包含在 `index.html` 中，是在 `GrampsJs.js` 中定义的 `gramps-js` 元素。这包含所有单独页面的定义（这些页面简单对应于根据路由/URL 显示或隐藏的元素）、菜单和路由。

`src/views` 目录中的组件通常对应于从后端获取数据的全页面组件（例如，人员列表视图），而 `src/components` 中的组件通常是用于视图内部的小型构建块，它们从父元素提供的属性中获取数据。然而，这种分离并不严格。

## 数据流

数据通过 `src/api.js` 中的 `apiGet`、`apiPut` 和 `apiPost` 方法与后端/API 交换，这些方法自动处理身份验证。

数据通过属性从父组件传递到子组件（参见例如 [Lit 文档](https://lit.dev/docs/components/properties/)）。

当需要将数据从子组件反馈到父组件时，使用自定义事件，这些事件可以通过 `src/api.js` 中的 `fireEvent` 函数触发，并使用 Lit 的 `@` 语法进行监听 [(文档)](https://lit.dev/docs/components/events/)。

## 身份验证

刷新令牌和身份验证令牌存储在浏览器的本地存储中。每当进行 API 调用且令牌过期时，存储的刷新令牌将用于获取新的访问令牌，并重复 API 调用。

用户的授权范围存储在访问令牌的声明中，通过 `getPermissions` 函数获取，并在顶层 `GrampsJs` 元素中使用，以设置布尔属性 `canAdd`、`canEdit`、`canManageUsers`，这些属性被传递给子元素以实现特定于授权的功能。
