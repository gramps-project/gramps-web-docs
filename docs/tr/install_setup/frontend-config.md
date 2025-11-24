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
-------|-----|-----------
`hideDNALink` | boolean | Doğruysa, navigasyon çubuğundaki DNA bağlantısını gizle.
`hideRegisterLink` | boolean | Doğruysa, giriş sayfasındaki kayıt bağlantısını gizle. Bu, çoklu ağaç dağıtımları için kullanılmalıdır.
`loginRedirect` | string | Giriş yapılmadığında "giriş" veya "kayıt" sayfası dışındaki herhangi bir sayfaya gidildiğinde yönlendirilecek URL
`leafletTileUrl` | string | Leaflet haritaları için özel karolar URL'si
`leafletTileSize` | number | Leaflet haritaları için özel karo boyutu
`leafletZoomOffset` | number | Leaflet haritaları için özel yakınlaştırma ofseti
`leafletTileAttribution` | string | Leaflet haritaları için özel atıf
