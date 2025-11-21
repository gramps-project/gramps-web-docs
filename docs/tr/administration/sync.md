# Gramps Web ve Gramps Masaüstünü Senkronize Et

*Gramps Web Sync*, Gramps için masaüstü bilgisayarınızdaki Gramps veritabanınızı Gramps Web ile senkronize etmenizi sağlayan bir eklentidir; medya dosyalarını da içerir.

!!! warning
    Herhangi bir senkronizasyon aracı gibi, lütfen bunu bir yedekleme aracı olarak düşünmeyin. Bir tarafta yapılan kazara bir silme işlemi diğer tarafa yansıtılacaktır. Aile ağacınızın düzenli yedeklerini (Gramps XML formatında) oluşturduğunuzdan emin olun.

!!! info
    Belgeler, Gramps Web Sync Eklentisi'nin en son sürümüne atıfta bulunmaktadır. Gerekirse eklentiyi en son sürüme güncellemek için Gramps eklenti yöneticisini kullanın.

## Kurulum

Eklenti, Python 3.10 veya daha yeni bir sürümde çalışan Gramps 6.0 gerektirir. Gramps Masaüstü'nde mevcuttur ve [alışıldık şekilde](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps) kurulabilir.

!!! warn
    Lütfen masaüstünüzdeki Gramps sürümünün, sunucunuzda çalışan sürümle aynı olduğundan emin olun. Hangi Gramps sürümünün sunucunuzda çalıştığını öğrenmek için [Yardım Alın](../help/help.md) bölümüne bakın. Gramps sürümü `MAJOR.MINOR.PATCH` biçimindedir ve `MAJOR` ve `MINOR` web ve masaüstünde aynı olmalıdır.

Opsiyonel adım:

??? note inline end "Gnome anahtar zinciri hatası"
    Şu anda birçok Gnome masaüstü yapılandırmasını etkileyen bir [python anahtar zinciri hatası](https://github.com/jaraco/keyring/issues/496) bulunmaktadır. `~/.config/python_keyring/keyringrc.cfg` yapılandırma dosyasını oluşturmanız ve aşağıdaki gibi düzenlemeniz gerekebilir:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- API şifresini sisteminizin şifre yöneticisinde güvenli bir şekilde saklamak için `keyring`'i kurun (örneğin, `sudo apt install python3-keyring` veya `sudo dnf install python3-keyring`).

## Kullanım

Kurulduktan sonra, eklenti Gramps altında *Araçlar > Aile Ağacı İşleme > Gramps&nbsp;Web&nbsp;Sync* menüsünde mevcuttur. Başlatıldığında ve geri alma geçmişinin silineceğini onaylayan bir iletişim kutusunu onayladıktan sonra, bir sihirbaz senkronizasyon adımlarında size rehberlik edecektir. Değişikliklerinizi açıkça onaylayana kadar yerel ağacınıza veya sunucuya hiçbir değişiklik uygulanmayacağını unutmayın.

### Adım 1: sunucu kimlik bilgilerini girin

Araç, Gramps Web örneğinizin temel URL'sini (örnek: `https://mygrampsweb.com/`), kullanıcı adınızı ve şifrenizi isteyecektir. Değişiklikleri uzaktaki veritabanınıza senkronize etmek için en az editör yetkilerine sahip bir hesaba ihtiyacınız vardır. Kullanıcı adı ve URL, Gramps kullanıcı dizininizde düz metin olarak saklanacak, şifre yalnızca `keyring` yüklüyse saklanacaktır (yukarıya bakın).

### Adım 2: değişiklikleri gözden geçirin

Kimlik bilgilerinizi onayladıktan sonra, araç yerel ve uzaktaki veritabanlarını karşılaştırır ve herhangi bir fark olup olmadığını değerlendirir. Eğer varsa, aşağıdaki kategorilerden birine ait nesne değişikliklerinin bir listesini görüntüler (bir nesne bir kişi, aile, etkinlik, yer vb. olabilir):

- yerel olarak eklenen
- yerel olarak silinen
- yerel olarak değiştirilen
- uzaktan eklenen
- uzaktan silinen
- uzaktan değiştirilen
- aynı anda değiştirilen (yani, her iki tarafta da)

Araç, her nesne için hangi tarafın daha yeni olduğunu değerlendirmek için zaman damgalarını kullanır (detaylarla ilgileniyorsanız aşağıdaki "Arka Plan" bölümüne bakın).

Eğer değişiklikler beklediğiniz gibi görünüyorsa, gerekli değişiklikleri yerel ve uzaktaki veritabanlarına uygulamak için "Uygula" butonuna tıklayabilirsiniz.

!!! tip "Gelişmiş: Senkronizasyon modu"
    Değişiklikler listesinin altında, bir senkronizasyon modu seçebilirsiniz.
    
    Varsayılan, **iki yönlü senkronizasyon**, tespit edilen değişiklikleri (yerel olarak eklenen nesneler uzaktaki tarafa eklenecek vb.) çoğu tarafa uygulayacağı anlamına gelir. Her iki tarafta da değiştirilen nesneler birleştirilecek ve her iki tarafta da güncellenecektir.

    **uzaktan yerel olarak sıfırlama** seçeneği, uzaktaki Gramps veritabanının tam olarak yerel olan gibi görünmesini sağlar. "Uzaktan eklenen" olarak tespit edilen nesneler tekrar silinecek, "uzaktan silinen" olarak tespit edilen nesneler tekrar eklenecek vb. *Yerel Gramps veritabanına hiçbir değişiklik uygulanmayacaktır.*

    **yerelden uzaktaki sıfırlama** seçeneği ters yönde çalışır ve yerel durumu uzaktaki veritabanının durumu ile ayarlar. *Uzaktaki veritabanına hiçbir değişiklik uygulanmayacaktır.*

    Son olarak, **birleştirme** seçeneği, her iki veritabanını değiştirmesi açısından iki yönlü senkronizasyona benzer, ancak *hiçbir nesneyi silmez*, bunun yerine yalnızca bir tarafta silinen tüm nesneleri geri yükler.

### Adım 3: medya dosyalarını senkronize et

*Veritabanları senkronize edildikten sonra*, araç yeni veya güncellenmiş medya dosyalarını kontrol eder. Eğer bulursa, bir liste görüntüler ve gerekli dosyaları yüklemek/indirmek için onay ister.

Medya dosyası senkronizasyonunun aşağıdaki sınırlamalarını dikkate alın:

- Eğer yerel bir dosyanın, Gramps veritabanında saklanan dosyadan farklı bir kontrol toplamı varsa (bu, örneğin Gramps'a eklendikten sonra düzenlenen Word dosyaları için olabilir), yükleme bir hata mesajı ile başarısız olacaktır.
- Araç, tüm yerel dosyaların bütünlüğünü kontrol etmez, bu nedenle medya nesnesi için saklanan yolda bir yerel dosya varsa, ancak dosya sunucudaki dosyadan farklıysa, araç bunu tespit etmeyecektir. Yanlış kontrol toplamlarına sahip dosyaları tespit etmek için Medya Doğrulama Eklentisini kullanın.

## Sorun Giderme

### Hata ayıklama günlüğü

Eğer Senkronizasyon Eklentisi ile sorun yaşıyorsanız, lütfen Gramps'ı [komut satırından başlatarak](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) hata ayıklama günlüğü etkin olacak şekilde başlatın:

```bash
gramps --debug grampswebsync
```

Bu, sorunun nedenini belirlemenize yardımcı olacak birçok yararlı günlük ifadesini komut satırına yazdıracaktır.

### Sunucu kimlik bilgileri

Eğer ilk adım başarısız olursa, lütfen sunucu URL'sini, kullanıcı adınızı ve şifrenizi kontrol edin.

### İzin sorunları

Eğer izinlerle ilgili bir hata ile karşılaşırsanız, lütfen Gramps Web kullanıcı hesabınızın kullanıcı rolünü kontrol edin. Uzaktaki veritabanına yalnızca editör, sahibi veya yönetici rolüne sahip bir kullanıcıysanız değişiklik uygulayabilirsiniz.

### Beklenmedik veritabanı değişiklikleri

Eğer senkronizasyon aracı, olmadığını düşündüğünüz değişiklikleri tespit ederse, bu, veritabanlarından birinde Gramps'ı yanıltan tutarsızlıklar olduğu veya yerel bilgisayarınız ile sunucunuz arasındaki zamanın senkronize olmadığı anlamına gelebilir.

Her iki makinedeki saatlerin doğru ayarlandığından emin olun (not: zaman dilimi önemli değildir çünkü araç, zaman diliminden bağımsız olan Unix zaman damgalarını kullanır).

Yerel veritabanınızda kontrol etme ve onarma aracını çalıştırarak bunun yardımcı olup olmadığını görebilirsiniz.

Yerel veritabanınızdaki tutarsızlıkların yanlış pozitifler oluşturmadığından emin olmanın kaba ama etkili bir yöntemi, veritabanınızı Gramps XML formatında dışa aktarıp yeni, boş bir veritabanına yeniden içe aktarmaktır. Bu kayıpsız bir işlemdir ancak tüm verilerin tutarlı bir şekilde içe aktarılmasını sağlar.

### Zaman aşımı hataları

Eğer zaman aşımı hataları (örneğin, HTTP durumu 408 hatası veya "zaman aşımı" kelimesini içeren başka bir hata mesajı ile belirtilen) yaşıyorsanız, bu muhtemelen uzaktaki tarafa senkronize edilmesi gereken büyük bir değişiklik sayısının, sunucu yapılandırmanızla birleşiminden kaynaklanmaktadır.

Senkronizasyon eklentisinin v1.2.0'dan önceki sürümleri ve Gramps Web API'sinin v2.7.0'dan önceki sürümleri için (Gramps Web'deki sürüm bilgisi sekmesine bakın), sunucu tarafına senkronizasyon, sunucu yapılandırmasına bağlı olarak bir veya birkaç dakika içinde zaman aşımına uğrayacak tek bir istekte işlenmiştir. Büyük senkronizasyonlar (örneğin, yerel veritabanına binlerce nesne içe aktarıldıktan sonra veya tam yerel veritabanını boş bir sunucu tarafı veritabanına senkronize etmeye çalışırken) bu süre çok kısa olabilir.

Eğer senkronizasyon eklentisi v1.2.0 veya daha yeni ve Gramps Web API v2.7.0 veya daha yeni kullanıyorsanız, sunucu tarafı senkronizasyonu bir arka plan işçisi tarafından işlenir ve çok uzun süre çalışabilir (bir ilerleme çubuğu görüntülenecektir) ve zaman aşımı hataları meydana gelmemelidir.

### Beklenmedik medya dosyası hataları

Eğer bir medya dosyasını yükleme başarısız olursa, bu genellikle disk üzerindeki gerçek dosyanın kontrol toplamı ile yerel Gramps veritabanındaki kontrol toplamı arasındaki uyumsuzluktan kaynaklanır. Bu genellikle Gramps dışında düzenlenen ofis belgeleri gibi düzenlenebilir dosyalarla olur. Lütfen tüm medya dosyalarının kontrol toplamlarını düzeltmek için Gramps Medya Doğrulama Eklentisini kullanın.

### Yardım isteyin

Eğer yukarıdakilerin hiçbiri yardımcı olmuyorsa, topluluktan yardım isteyebilirsiniz. [Gramps forumunun Gramps Web kategorisinde](https://gramps.discourse.group/c/gramps-web/28) bir gönderi oluşturarak yardım isteyin. Lütfen aşağıdakileri sağladığınızdan emin olun:

- Gramps Web Sync eklentisinin sürümü (ve lütfen en son sürümü kullanın)
- Kullandığınız Gramps masaüstü sürümü
- Yukarıda açıklandığı gibi etkinleştirilen Gramps hata ayıklama günlüğünün çıktısı
- Gramps Web'in sürüm bilgisi (Ayarlar/Sürüm bilgisi altında bulabilirsiniz)
- Gramps Web kurulumunuz hakkında verebileceğiniz herhangi bir ayrıntı (kendi barındırdığınız, Grampshub, ...)
- Eğer erişiminiz varsa Gramps Web sunucu günlüklerinizin çıktısı (docker kullanıyorsanız: `docker compose logs --tail 100 grampsweb` ve `docker compose logs --tail 100 grampsweb-celery`)

## Arka Plan: eklentinin nasıl çalıştığı

Eğer eklentinin nasıl çalıştığı hakkında merak ediyorsanız, bu bölümde daha fazla detay bulabilirsiniz.

Eklenti, yerel bir Gramps veritabanını uzaktaki bir Gramps Web veritabanı ile senkronize tutmak için tasarlanmıştır; hem yerel hem de uzaktaki değişikliklere (işbirlikçi düzenleme) izin verir.

**Şu durumlar için uygun değildir:**

- Yerel veritabanının doğrudan bir türevi olmayan bir veritabanı ile senkronize etmek (yerel veritabanının kopyasından veya Gramps XML dışa aktarma/içeri aktarma ile başlamak)
- Her iki tarafta da büyük sayıda değişiklik olan iki veritabanını birleştirmek. Bu amaç için mükemmel [İçeri Aktarma Birleştirme Aracı](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) kullanın.

Aracın çalışma prensipleri oldukça basittir:

- Yerel ve uzaktaki veritabanlarını karşılaştırır
- Eğer herhangi bir fark varsa, en son aynı nesnenin zaman damgasını kontrol eder, buna **t** diyelim
- Eğer bir nesne **t**'den daha yakın bir tarihte değiştiyse ve bir veritabanında mevcutsa ancak diğerinde yoksa, her iki tarafa senkronize edilir (yeni nesne varsayalım)
- Eğer bir nesne **t**'den önce son kez değiştiyse ve bir veritabanında yoksa, her iki taraftan da silinir (silinmiş nesne varsayalım)
- Eğer bir nesne farklıysa ancak yalnızca bir veritabanında **t**'den sonra değiştiyse, diğerine senkronize edilir (değiştirilmiş nesne varsayalım)
- Eğer bir nesne farklıysa ancak her iki veritabanında da **t**'den sonra değiştiyse, birleştirilir (çelişkili değişiklik varsayalım)

Bu algoritma basit ve sağlamdır çünkü senkronizasyon geçmişini takip etmeyi gerektirmez. Ancak, en iyi şekilde *sık sık senkronize ettiğinizde* çalışır.
