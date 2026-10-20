# Налаштування фронтенду

Фронтенд Gramps Web є додатком на Javascript, який розгортається як набір статичних файлів HTML, CSS та Javascript. Зазвичай, спеціальна конфігурація для фронтенду не потрібна. Однак деяку поведінку можна змінити, встановивши відповідні параметри у файлі `config.js` в кореневій директорії дистрибуції.

Файл повинен мати таку структуру:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Існують такі ключі параметрів.

Ключ | Тип | Опис 
----|-----|-----------
`hideDNALink` | boolean | Якщо true, приховати посилання на ДНК у навігаційній панелі.
`hideRegisterLink` | boolean | Якщо true, приховати посилання на реєстрацію на сторінці входу. Це слід використовувати для розгортань з кількома деревами.
`loginRedirect` | string | URL для перенаправлення, коли не виконано вхід і навігація на будь-яку сторінку, окрім "login" або "register"
`mapBaseStyleLight` | string | URL стилю MapLibre для базової карти в світлій темі (за замовчуванням: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | URL стилю MapLibre для базової карти в темній темі (за замовчуванням: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | URL стилю MapLibre для накладення OpenHistoricalMap (за замовчуванням: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
`mapWikidata` | boolean | Якщо false, видалити шар [Wikidata buildings](../user-guide/map.md#wikidata-buildings) з карти (за замовчуванням: true)
