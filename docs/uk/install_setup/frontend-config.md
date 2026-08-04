# Налаштування фронтенду

Фронтенд Gramps Web є JavaScript-додатком, який розгортається як набір статичних файлів HTML, CSS та JavaScript. Зазвичай, для фронтенду не потрібна спеціальна конфігурація. Однак деяка поведінка може бути змінена шляхом встановлення відповідних параметрів у файлі `config.js` в корені дистрибуції.

Файл повинен мати таку структуру:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Існують наступні ключі параметрів.

Ключ | Тип | Опис 
----|-----|-----------
`hideDNALink` | boolean | Якщо true, приховати посилання на ДНК в навігаційній панелі.
`hideRegisterLink` | boolean | Якщо true, приховати посилання на реєстрацію на сторінці входу. Це слід використовувати для розгортань з кількома деревами.
`loginRedirect` | string | URL для перенаправлення, коли не увійшли в систему і переходять на будь-яку сторінку, крім "вхід" або "реєстрація"
`mapBaseStyleLight` | string | URL стилю MapLibre для базової карти в світлій темі (за замовчуванням: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | URL стилю MapLibre для базової карти в темній темі (за замовчуванням: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | URL стилю MapLibre для накладення OpenHistoricalMap (за замовчуванням: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
