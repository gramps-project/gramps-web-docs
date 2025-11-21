# Telemetri

Gramps Web API sürüm 3.2.0'dan itibaren, Gramps Web varsayılan olarak her 24 saatte bir Gramps Web ekibi tarafından kontrol edilen bir analiz uç noktasına tamamen anonimleştirilmiş telemetri verileri gönderir. Bu sayfa toplanan telemetri verileri, bunların nasıl kullanıldığı ve istenirse nasıl devre dışı bırakılacağı hakkında bilgi içermektedir.

## Hangi veriler toplanıyor?

Telemetri verileri aşağıdaki biçimde küçük bir JSON yüküdür:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Kendiniz de [kaynak kodunda](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87) kontrol edebileceğiniz gibi, sunucu ve ağaç tanımlayıcıları sunucu ve ağaç için benzersizdir, ancak herhangi bir kişisel olarak tanımlanabilir bilgi içermez. `timestamp`, Unix zaman damgası olarak mevcut zamanı temsil eder.

## Veriler neden toplanıyor?

Günde bir kez benzersiz bir tanımlayıcı göndermek, Gramps Web ekibinin kaç tane benzersiz sunucunun Gramps Web çalıştırdığını ve kaç tane benzersiz ağacın kullanıldığını takip etmesine olanak tanır.

Bu, Gramps Web tarafından kullanılan harita döşemeleri gibi dış hizmetler üzerindeki etkiyi anlamak için önemlidir.

## Veriler nasıl toplanıyor?

Gramps Web API sunucunuza bir istek yapıldığında, son 24 saatte telemetri verilerinin gönderilip gönderilmediğini kontrol eder (yerel önbellekteki bir anahtarı kontrol ederek). Eğer gönderilmemişse, yukarıdaki yük bir veriyi kaydeden uç noktaya gönderilir.

Kaydetme uç noktası Google Cloud Run üzerinde barındırılmakta olup, doğrudan bir [açık kaynak deposundan](https://github.com/DavidMStraub/cloud-run-telemetry) dağıtılmaktadır, bu nedenle verilerin nasıl işlendiğini inceleyebilirsiniz.

## Verilerle ne yapılacak?

Her şeyden önce, Gramps Web ekibi tarafından kullanılacak, varsayımsal olarak toplanabilecek (örneğin sunucunun IP adresi gibi) anonimleştirilmiş yükün ötesinde hiçbir veri kullanılmayacaktır.

Toplanan anonimleştirilmiş kimlikler ve zaman damgası, aşağıdaki gibi grafikler üretmek için birleştirilecektir:

- Zaman fonksiyonu olarak aktif Gramps Web kurulumlarının sayısı
- Zaman fonksiyonu olarak aktif Gramps Web ağaçlarının sayısı

Bu grafikler Gramps Web dokümantasyon sitesinde yayınlanacaktır.

## Telemetri nasıl devre dışı bırakılır?

İstatistik verileri Gramps Web ekibi için faydalı olduğundan ve kişisel olarak tanımlanabilir verilerin gönderilmediğini garanti ettiğimizden, **telemetriyi devre dışı bırakmamanızdan memnuniyet duyarız!**

Yine de, Gramps Web kullanıcıları tam kontrol sağlar, bu nedenle isterseniz bu özelliği devre dışı bırakmayı seçebilirsiniz.

Bunu yapmak için, `DISABLE_TELEMETRY` yapılandırma seçeneğini `True` olarak ayarlamanız yeterlidir (örneğin, `GRAMPSWEB_DISABLE_TELEMETRY` ortam değişkenini `true` olarak ayarlayarak &ndash; ayrıntılar için [yapılandırma belgelerine](configuration.md) bakın).
