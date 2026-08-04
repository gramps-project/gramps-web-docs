# Настройка интерфейса

Интерфейс Gramps Web — это приложение на Javascript, которое развертывается как набор статических файлов HTML, CSS и Javascript. Обычно для интерфейса не требуется специальная конфигурация. Однако некоторые параметры можно изменить, установив соответствующие опции в файле `config.js` в корне дистрибутива.

Файл должен иметь следующую структуру:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Существуют следующие ключи опций.

Ключ | Тип | Описание 
----|-----|-----------
`hideDNALink` | boolean | Если true, скрыть ссылку на ДНК в навигационной панели.
`hideRegisterLink` | boolean | Если true, скрыть ссылку на регистрацию на странице входа. Это следует использовать для развертываний с несколькими деревьями.
`loginRedirect` | string | URL для перенаправления, когда пользователь не вошел в систему и переходит на любую страницу, кроме "входа" или "регистрации".
`mapBaseStyleLight` | string | URL стиля MapLibre для базовой карты в светлой теме (по умолчанию: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | URL стиля MapLibre для базовой карты в темной теме (по умолчанию: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | URL стиля MapLibre для наложения OpenHistoricalMap (по умолчанию: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
