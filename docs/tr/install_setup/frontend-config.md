# Ön Uç Özelleştirme

Gramps Web ön ucu, statik HTML, CSS ve Javascript dosyaları seti olarak dağıtılan bir Javascript uygulamasıdır. Normalde, ön uç için özel bir yapılandırma gerekli değildir. Ancak, bazı davranışlar, dağıtımın kökündeki `config.js` dosyasında uygun seçenekler ayarlanarak değiştirilebilir.

Dosyanın aşağıdaki yapıya sahip olması gerekir:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Aşağıdaki seçenek anahtarları mevcuttur.

Anahtar | Tür | Açıklama 
----|-----|-----------
`hideDNALink` | boolean | Eğer doğruysa, gezinme çubuğundaki DNA bağlantısını gizle.
`hideRegisterLink` | boolean | Eğer doğruysa, giriş sayfasındaki kayıt bağlantısını gizle. Bu, çoklu ağaç dağıtımları için kullanılmalıdır.
`loginRedirect` | string | Giriş yapılmadığında "giriş" veya "kayıt" sayfası dışındaki herhangi bir sayfaya gidildiğinde yönlendirilecek URL
`mapBaseStyleLight` | string | Açık tema için temel harita MapLibre stil URL'si (varsayılan: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | Koyu tema için temel harita MapLibre stil URL'si (varsayılan: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | OpenHistoricalMap örtüsü için MapLibre stil URL'si (varsayılan: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
`mapWikidata` | boolean | Eğer yanlışsa, haritadan [Wikidata binalarını](../user-guide/map.md#wikidata-buildings) kaldır (varsayılan: doğru)
