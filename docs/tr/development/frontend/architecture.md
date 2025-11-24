# Mimari

## Bileşenler

Ön yüz, web bileşenlerinden oluşturulmuştur. Bunlar, `src` dizinindeki Javascript dosyalarında tanımlanmıştır.

Tipik olarak, her dosya bir bileşeni tanımlar ve şu şekilde başlar:
```javascript
class GrampsjsSomeElement extends LitElement
```
ve şu şekilde biter:
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
bu, başka yerlerde kullanılabilecek yeni HTML öğesi `grampsjs-some-element`'i tanımlar.

Ana giriş noktası, `index.html` içinde yer alan `gramps-js` öğesidir ve `GrampsJs.js` dosyasında tanımlanmıştır. Bu, tüm bireysel sayfaların tanımını (basitçe, rota/URL'ye göre gösterilen veya gizlenen öğelere karşılık gelir), menüyü ve yönlendirmeyi içerir.

`src/views` dizinindeki bileşenler genellikle arka uçtan veri çeken tam sayfa bileşenlerine karşılık gelir (örneğin, insanlar listesi görünümü), `src/components` dizinindeki bileşenler ise genellikle görünüm içinde kullanılan daha küçük yapı taşlarıdır ve verilerini üst öğeden sağlanan niteliklerden alır. Ancak, bu ayrım katı değildir.

## Veri akışı

Veri, `src/api.js` içindeki `apiGet`, `apiPut` ve `apiPost` yöntemleri aracılığıyla Arka Uç/API ile değiştirilir; bu yöntemler otomatik olarak kimlik doğrulama işlemlerini yönetir.

Veri, üst bileşenlerden alt bileşenlere özellikler aracılığıyla aktarılır (örneğin, [Lit belgelerine](https://lit.dev/docs/components/properties/) bakınız).

Verinin bir alt bileşenden bir üst bileşene geri iletilmesi gerektiğinde, `src/api.js` içindeki `fireEvent` fonksiyonu ile tetiklenebilen özel olaylar kullanılır ve Lit'in `@` sözdizimi ile dinlenir [(belgeler)](https://lit.dev/docs/components/events/).

## Kimlik Doğrulama

Yenileme jetonu ve kimlik doğrulama jetonu, tarayıcının yerel depolamasında saklanır. Herhangi bir API çağrısı yapıldığında ve jeton süresi dolduğunda, saklanan yenileme jetonu yeni bir erişim jetonu almak için kullanılır ve API çağrısı tekrarlanır.

Kullanıcının yetkilendirme kapsamı, erişim jetonunun taleplerinde saklanır ve `getPermissions` fonksiyonu ile elde edilir; bu, üst düzey `GrampsJs` öğesinde `canAdd`, `canEdit`, `canManageUsers` boolean özelliklerini ayarlamak için kullanılır ve bu özellikler, yetkilendirme ile ilgili işlevselliği uygulamak için alt öğelere aktarılır.
