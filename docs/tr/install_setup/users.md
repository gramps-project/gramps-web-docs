# Kullanıcı sistemi

Gramps Web, kamu erişimi için internete açılmak üzere tasarlanmamıştır, yalnızca kimlik doğrulaması yapılmış kullanıcılar tarafından erişilebilir. Kullanıcı hesapları, site sahibi tarafından komut satırı veya web arayüzü aracılığıyla veya kendi kendine kayıt olup sonrasında site sahibi tarafından onaylanarak oluşturulabilir.

## Kullanıcı rolleri

Aşağıdaki kullanıcı rolleri şu anda tanımlanmıştır.

Rol | Rol ID | İzinler
-----|---------|------------
Misafir | 0 | Özel olmayan nesneleri görüntüle
Üye | 1 | Misafir + özel nesneleri görüntüle
Katkıda Bulunan* | 2 | Üye + nesne ekle
Editör | 3 | Katkıda Bulunan + nesneleri düzenle ve sil
Sahip | 4 | Editör + kullanıcıları yönet
Yönetici | 5 | Sahip + çoklu ağaç kurulumunda diğer ağaçları düzenle

Bir kaydın özel olup olmadığı, kayıt başına ayarlanır, bkz. [Özel kayıtlar](../user-guide/privacy.md). Varsayılan olarak hiçbir şey özel değildir, hatta yaşayan insanlar bile.

\* "Katkıda Bulunan" rolünün şu anda yalnızca kısmen desteklendiğini unutmayın; örneğin, aile nesneleri eklenemez çünkü bunlar aile üyelerinin temel Gramps kişi nesnelerinin değiştirilmesini gerektirir. Mümkün olduğunca diğer rolleri kullanmanız önerilir.

## AI sohbetini kimlerin kullanabileceğini yapılandırma

Eğer [AI sohbetini yapılandırdıysanız](chat.md), burada sohbet özelliğini kullanmasına izin verilen kullanıcı gruplarını seçmek için bir seçenek göreceksiniz.

## Kullanıcıları yönetme

Kullanıcıları yönetmenin iki yolu vardır:

- Web arayüzü kullanarak sahip izinleri ile
- Sunucuda komut satırında

Web uygulamasına ilk erişim için gereken sahip hesabı, boş bir kullanıcı veritabanı ile Gramps Web'e erişildiğinde otomatik olarak başlatılan onboarding sihirbazında eklenebilir.

### Komut satırında kullanıcıları yönetme

[Eğer Docker Compose](deployment.md) kullanıyorsanız, temel komut şudur:

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

`COMMAND` `add`, `set-password` veya `delete` olabilir. `[ARGS]` için `--help` kullanarak sözdizimini ve olası yapılandırma seçeneklerini görüntüleyebilirsiniz.

`set-password NAME`, mevcut bir kullanıcı için eski şifreye ihtiyaç duymadan yeni bir şifre ayarlar; örneğin, kimsenin artık giriş yapamadığı ve e-posta şifre sıfırlamaları için ayarlanmadığı durumlarda (Gramps Web API 3.26+). Şifreyi iki kez girmesi istenir ve gösterilmez, böylece şifre shell geçmişine geçmez. Kullanıcının tüm oturumları sonlandırılır.

### Kendi kendine kayıtlı kullanıcıları onaylama

Bir kullanıcı kendi kendine kayıt olduğunda, hemen erişim verilmez. Yeni kullanıcı kaydı hakkında ağaç sahibine bir e-posta gönderilir ve kullanıcıya e-posta adresini onaylaması için bir e-posta isteği gönderilir. E-posta adresini başarıyla onaylamak, kullanıcının rolünü `onaylanmamış`'tan `devre dışı`'ya değiştirir. Kullanıcı hesabı bu iki rolden birindeyken, kullanıcı giriş yapamaz. Ağaç sahibi, kullanıcının talebini gözden geçirmeli ve giriş yapmasına izin verilmeden önce kullanıcıya uygun bir rol atamalıdır.
