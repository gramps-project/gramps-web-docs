# Gramps Web ve Gramps Masaüstünü Senkronize Et

*Gramps Web Sync*, Gramps için bir eklentidir ve masaüstü bilgisayarınızdaki Gramps veritabanınızı Gramps Web ile senkronize etmenizi sağlar; medya dosyalarını da içerir.

!!! warning
    Herhangi bir senkronizasyon aracı gibi, bunu bir yedekleme aracı olarak düşünmeyin. Bir tarafta yapılan kazara bir silme işlemi diğer tarafa aktarılacaktır. Aile ağacınızın düzenli yedeklerini (Gramps XML formatında) oluşturduğunuzdan emin olun.

!!! info
    Dokümantasyon, Gramps Web Sync Eklentisi'nin en son sürümüne atıfta bulunmaktadır. Gerekirse eklentiyi en son sürüme güncellemek için Gramps eklenti yöneticisini kullanın.

!!! note "Sürüm 1.5'te ne değişti"
    Eklentinin arayüzü sürüm 1.5'te yeniden yazıldı. Adım adım sihirbaz kaldırıldı ve tek bir pencere ile değiştirildi; medya dosyaları artık nesne değişiklikleri ile birlikte onaylanıyor, ayrı bir sayfada değil. Senkronizasyon modu seçici arıyorsanız, artık değişiklikler listesinin **üstünde** yer alıyor, altında değil. **Birleştirme** senkronizasyon modu kaldırıldı; aşağıdaki [Senkronizasyon modu](#sync-mode) kısmına bakın.

## Kurulum

Eklenti, Python 3.10 veya daha yeni bir sürümde çalışan Gramps 6.0 gerektirir. Gramps Masaüstünde mevcuttur ve [alışıldık şekilde](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps) kurulabilir.

!!! warning
    Lütfen masaüstünüzdeki Gramps sürümünün, sunucunuzda çalışan sürümle aynı olduğundan emin olun. Hangi Gramps sürümünün sunucunuzda çalıştığını öğrenmek için [Yardım Al](../help/help.md) bölümüne bakın. Gramps sürümü `MAJOR.MINOR.PATCH` biçimindedir ve `MAJOR` ve `MINOR` web ve masaüstünde aynı olmalıdır.

### Sunucu gereksinimleri

Eklenti, bağlandığı anda sunucunuz hakkında iki şeyi kontrol eder ve herhangi biri karşılanmazsa devam etmeyi reddeder. Her iki kontrol de herhangi bir şey indirilmeden önce gerçekleşir.

- **Gramps Web API sürümü 3.x.** Bu eklenti sürümü, Gramps 6.0 için Gramps Web API 3 ile çalışır. Daha eski bir sunucunun güncellenmesi gerekir; *daha yeni* bir API ana sürümünde çalışan bir sunucu, daha yeni bir Gramps sürümüne ihtiyaç duyar, daha yeni bir eklentiye değil, çünkü her Gramps sürüm hattı bir API sürümü ile eşleşir. Sunucunuzun sürümünü Gramps Web'de *Ayarlar ▸ Sürüm bilgisi* altında bulabilirsiniz.
- **Bir arka plan görev kuyruğu.** Senkronizasyon, değişikliklerini bir arka plan görevi olarak gönderir. Yapılandırılmış bir görev kuyruğu olmayan bir sunucuda, değişikliklerin uygulanması senkronize olarak çalışır ve gerçek bir aile ağacında zaman aşımına uğrar, bu nedenle eklenti başlamayı reddeder ve yarıda kalmaz.

Ayrıca, uzaktaki veritabanına değişiklik uygulamak için en az editör ayrıcalıklarına sahip bir hesaba ihtiyacınız vardır.

Opsiyonel adım:

??? note inline end "Gnome anahtarlık hatası"
    Şu anda birçok Gnome masaüstü yapılandırmasını etkileyen bir [python anahtarlık hatası](https://github.com/jaraco/keyring/issues/496) bulunmaktadır. `~/.config/python_keyring/keyringrc.cfg` yapılandırma dosyasını oluşturmanız ve aşağıdaki gibi düzenlemeniz gerekebilir:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- API şifresini sisteminizin şifre yöneticisinde güvenli bir şekilde saklamak için `keyring` yükleyin (örneğin, `sudo apt install python3-keyring` veya `sudo dnf install python3-keyring`).

Anahtarlık kullanılamıyorsa, eklenti bunu bildirir ve bununla devam eder — her seferinde şifreniz istenecektir. Gramps **Snap** paketinde, sistem anahtarlığı, bir kez arayüzü bağlayana kadar kısıtlama nedeniyle engellenmiştir:

```bash
snap connect gramps:password-manager-service
```

Eklenti, durumu tespit ettiğinde bu komutu gösterir.

## Kullanım

Kurulduktan sonra, eklenti Gramps'te *Araçlar ▸ Aile Ağacı İşleme ▸ Gramps&nbsp;Web&nbsp;Sync* altında mevcuttur. Geri alma geçmişinin silineceğini belirten diyalog uyarısını onayladıktan sonra, senkronizasyon penceresi açılır.

**Yerel ağacınıza veya sunucuya herhangi bir değişiklik uygulanmaz, ta ki açıkça onaylamadığınız sürece.**

Pencerenin üst kısmında, senkronize ettiğiniz aile ağacının adı, ait olduğu hesap ve adres ile en son ne zaman senkronize edildiği bilgileri yer alır. Alt kısımda, eklentinin ve sunucunun Web API'sinin sürümü gösterilir — sorun bildirdiğinizde faydalıdır.

### Bağlantı

Bu aile ağacını daha önce senkronize ettiyseniz ve şifreniz saklanıyorsa, eklenti açıldığı anda bağlanır ve doğrudan karşılaştırmaya geçer. Aksi takdirde, Gramps Web örneğinizin temel URL'sini (örnek: `https://mygrampsweb.com/`), kullanıcı adınızı ve şifrenizi ister.

URL ve kullanıcı adı, Gramps kullanıcı dizininizde düz metin olarak saklanır. Şifre yalnızca **Şifreyi hatırla** seçeneğini işaretlediğinizde sistem şifre yöneticinizde saklanır; bu seçeneği kaldırmak, o sunucu için daha önce saklanan herhangi bir şifreyi kaldırır.

!!! tip "Birden fazla aile ağacı, birden fazla sunucu"
    Senkronize ettiğiniz her sunucu ayrı olarak saklanır ve en son ne zaman senkronize edildiğine dair kendi kaydı ile birlikte tutulur. İki sunucu arasında geçiş yapmak artık birbirini rahatsız etmez.

    Her kayıt, **hangi yerel aile ağacından** en son senkronize edildiğini de kaydeder. Eklenti yalnızca bu, açık olan ağaçla eşleştiğinde kendi kendine bağlanır; aksi takdirde bağlantı ayrıntılarını gösterir ve *Bağlan* butonuna basmanızı bekler, saklanan kimlik bilgileri farklı bir ağaçla ilişkilendiyse bir uyarı verir. Bu önemlidir çünkü farklı bir ağaç tutan bir sunucuya karşı senkronize etmek, her iki tarafın içeriğini silmeyi önerecektir.

Yazma işlemi yapılmadığı sürece iki eylem mevcuttur:

- **Sunucuyu değiştir…**, üst çubukta, bu ağacı farklı bir sunucuya yönlendirmek için bağlantı ayrıntılarına geri döner. Devam eden bir karşılaştırmayı kesintiye uğratır, bitmesini beklemenizi gerektirmez.
- **Bu sunucuyu unut**, bağlantı panelinde, saklanan adresi, kullanıcı adını ve şifreyi kaldırır, ayrıca bu ağacın en son ne zaman senkronize edildiği kaydını da siler. Bir sonraki senkronizasyon, iki ağacı sıfırdan karşılaştırır.

`http://` ile başlayan bir adres girerseniz, yazarken bir uyarı görünür. Şifreniz düz metin olarak gönderilecektir, bu nedenle yalnızca yerel testler için kullanın.

### Değişiklikleri Gözden Geçirme

Eklenti, yerel ve uzaktaki veritabanlarını karşılaştırır ve ne yapmayı önerdiğini gösterir. Önceki sürümlerden farklı olarak, iki ağaç arasındaki ham farklılıkları listelemek yerine, liste artık hangi veritabanlarının değiştirileceğine göre gruplandırılmış **hareketleri** gösterir:

```
▾ Bu bilgisayarda değiştirilecek (7 nesne)
    ▾ 3 nesne ekle
        Kişi   John Smith        I0123
    ▾ 4 nesneyi güncelle
        …
▾ Sunucuda değiştirilecek (5 nesne)
    …
```

Her satır, nesnenin adını belirtir, böylece kimin veya neyin etkilendiğini anlayabilirsiniz, yalnızca bir Gramps ID'si görmekle kalmazsınız.

Herhangi bir şey silinecekse, listenin üzerindeki bir uyarı, kaç nesnenin ve hangi tarafta olduğunu belirtir. Bu, silmelerin dahil olduğu her durumda görünür, ayrıca kendi yaptığınız bir silmeyi yaymakta olan sıradan iki yönlü bir senkronizasyon sırasında da görünür.

Listeyi tanımlayan işlemi gerçekleştirmek için **Uygula** butonuna basın.

!!! warning "Gözden geçirirken düzenleme yapmayın"
    Senkronizasyon penceresi Gramps'in geri kalanını engellemez, bu nedenle liste açıkken çalışmaya devam edebilirsiniz. Eğer etkilenen bir nesneyi düzenlerseniz, eklenti bunu Uygula butonuna bastığınızda tespit eder, hiçbir şeyi değiştirmeden durur ve tekrar karşılaştırmanızı ister. Hiçbir şey kaybolmaz, ancak karşılaştırmanın tekrarlanması gerekir.

#### Senkronizasyon modu

Senkronizasyon modu, değişiklikler listesinin **üstünde** seçilir. Değiştirmek, listeyi yeniden oluşturur, çünkü mod her bir farkın neye dönüşeceğini belirler.

- **İki yönlü senkronizasyon** (varsayılan) — her iki taraftan gelen değişiklikler birleştirilir. Her iki yerde de düzenlenen nesneler birleştirilir.
- **Sunucuyu bu bilgisayara uyacak şekilde sıfırla** — sunucu, bu bilgisayara uydurulur. Sadece sunucuda değiştirilen her şey silinir.
- **Bu bilgisayarı sunucuya uyacak şekilde sıfırla** — bu bilgisayar, sunucuya uyacak şekilde ayarlanır. Burada yalnızca değiştirilen her şey silinir.

!!! note
    Önceki sürümlerde mevcut olan **birleştirme** modu kaldırılmıştır. Bu, yalnızca bir tarafta silinen nesneleri geri yüklemekle iki yönlü senkronizasyondan farklıydı, bu da arayüzün faydalı bir şekilde açıklayabileceği bir ayrım değildi. Eğer buna güveniyorsanız, iki yönlü senkronizasyonu kullanın ve yedekten saklamak istediğiniz her şeyi geri yükleyin.

### Medya dosyaları

Medya dosyaları, ayrı bir adım olarak değil, aynı onaylamanın bir parçası olarak işlenir. Herhangi bir dosyanın aktarılması gerekiyorsa, listenin altında bunları taşımayı öneren bir onay kutusu bulunur:

```
[x] Ayrıca 12 medya dosyasını aktar (4 indirmek, 8 yüklemek için)
```

Dosyaları etkilemeden nesne değişikliklerini senkronize etmek için bu kutuyu işaretlemeyi kaldırın.

*Her iki* tarafta da eksik olan dosyalar ayrı olarak listelenir, çünkü bunlarla ilgili hiçbir şey yapılamaz:

```
Her iki tarafta da eksik 2 medya dosyası var ve aktarılamaz.
```

Medya dosyası senkronizasyonunun aşağıdaki sınırlamalarına dikkat edin:

- Eğer yerel bir dosya, Gramps veritabanında saklanan dosyadan farklı bir kontrol toplamına sahipse (bu, Gramps'a eklendikten sonra düzenlenen Word dosyaları için olabilir), yükleme bir hata mesajı ile başarısız olur.
- Araç, tüm yerel dosyaların bütünlüğünü kontrol etmez, bu nedenle medya nesnesi için saklanan yol altında bir yerel dosya varsa, ancak dosya sunucudaki dosyadan farklıysa, araç bunu tespit edemez. Yanlış kontrol toplamlarına sahip dosyaları tespit etmek için Medya Doğrulama Eklentisini kullanın.

### Bir şeyler yanlış gittiğinde

Eğer bir senkronizasyon yarıda kalırsa — örneğin, bir bağlantı kesilirse — eklenti daha önce uyguladığı değişiklikleri bildirir ve **Tekrar Dene** seçeneği sunar; bu, başarısız olan adımda devam eder, sıfırdan başlamaz. Uzak ağaçtaki indirilen kopya saklanır, bu nedenle tekrar denemek ikinci kez indirilip karşılaştırılmaz.

Başarısızlığın teknik ayrıntıları, bir *Ayrıntılar* genişletici altında mevcuttur ve hata raporu için kopyalamak üzere bir buton içerir.

## Sorun Giderme

### Hata ayıklama günlüğü

Eğer Senkronizasyon Eklentisi ile ilgili sorunlar yaşıyorsanız, lütfen Gramps'i [komut satırından başlatarak](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) hata ayıklama günlüğü etkinleştirin ve aşağıdaki seçeneği kullanın:

```bash
gramps --debug grampswebsync
```

Bu, sorunun nedenini belirlemenize yardımcı olacak birçok yararlı günlük ifadesini komut satırına yazdıracaktır.

### Sunucu kimlik bilgileri

Bağlantı başarısız olursa, lütfen sunucu URL'sini, kullanıcı adınızı ve şifrenizi kontrol edin.

### Eklenti bağlanmayı reddediyor

Eklenti, sunucunun Gramps Web API sürümünün çok eski veya çok yeni olduğunu veya bir arka plan görev kuyruğunun yapılandırılmadığını bildiriyorsa, yukarıdaki [Sunucu gereksinimleri](#server-requirements) kısmına bakın. Bunlar, başka bir şeyden önce kontrol edilir, bu nedenle mesaj doğrudan sorunu belirtir.

### İzin sorunları

Eğer izinlerle ilgili bir hata ile karşılaşırsanız, lütfen Gramps Web kullanıcı hesabınızın kullanıcı rolünü kontrol edin. Uzaktaki veritabanına yalnızca editör, sahibi veya yönetici rolüne sahip bir kullanıcı olarak değişiklik uygulayabilirsiniz.

### Beklenmedik veritabanı değişiklikleri

Eğer senkronizasyon aracı, olmadığını düşündüğünüz değişiklikleri tespit ederse, bu, Gramps'ın bir fark tespit etmesine neden olan bir veritabanındaki tutarsızlıklar veya yerel bilgisayarınız ile sunucunuz arasındaki zamanın senkronize olmaması olabilir.

Her iki makinenin saatlerinin doğru ayarlandığından emin olun (not, zaman dilimi önemli değildir çünkü araç Unix zaman damgalarını kullanır, bu da zaman diliminden bağımsızdır).

Ayrıca, yerel veritabanınızda kontrol ve onarım aracını çalıştırmayı deneyebilir ve bunun yardımcı olup olmadığını görebilirsiniz.

Yerel veritabanınızdaki tutarsızlıkların yanlış pozitiflere neden olmadığından emin olmak için, veritabanınızı Gramps XML formatında dışa aktarabilir ve yeni, boş bir veritabanına yeniden içe aktarabilirsiniz. Bu kayıpsız bir işlemdir ancak tüm verilerin tutarlı bir şekilde içe aktarılmasını sağlar.

!!! tip
    Eğer eklenti korkutucu bir sayıda silme öneriyorsa, önce üst çubuğu kontrol edin: bu, yazmak üzere olduğunuz sunucudaki aile ağacının adını belirtir. Farklı bir ağaç tutan bir sunucuya karşı senkronize etmek, tam olarak bu semptomu üretir.

### Zaman aşımı hataları

Sunucuya yapılan senkronizasyon, bir arka plan işçisi tarafından işlenir, bu nedenle uzun süren senkronizasyonların zaman aşımına uğramaması gerekir. Bu nedenle, yapılandırılmış bir görev kuyruğu olmayan bir sunucu, bağlantı zamanında reddedilir — [Sunucu gereksinimleri](#server-requirements) kısmına bakın.

Eklentiden sunucuya yapılan istekler, yanıt alınmadan 60 saniye sonra zaman aşımına uğrar, bu nedenle ulaşılamayan bir sunucu, sonsuza kadar askıda kalmak yerine bir bağlantı hatası bildirir.

### Beklenmedik medya dosyası hataları

Eğer bir medya dosyasının yüklenmesi başarısız olursa, bu genellikle disk üzerindeki gerçek dosya ile yerel Gramps veritabanındaki kontrol toplamı arasındaki uyumsuzluktan kaynaklanır. Bu, Gramps dışında düzenlenen ofis belgeleri gibi düzenlenebilir dosyalarla sıkça olur. Lütfen tüm medya dosyalarının kontrol toplamlarını düzeltmek için Gramps Medya Doğrulama Eklentisini kullanın.

### Yardım isteyin

Eğer yukarıdakilerin hiçbiri yardımcı olmuyorsa, topluluktan yardım isteyebilirsiniz; [Gramps forumunun Gramps Web kategorisinde](https://gramps.discourse.group/c/gramps-web/28) bir gönderi paylaşarak. Lütfen şunları sağlamayı unutmayın:

- Gramps Web Sync eklentisinin sürümü (ve lütfen en son yayımlanan sürümü kullanın) — senkronizasyon penceresinin altında, sunucunun Web API sürümünün yanında gösterilir
- Kullandığınız Gramps masaüstü sürümü
- Yukarıda açıklandığı gibi etkinleştirilen Gramps hata ayıklama günlüğünün çıktısı
- Gramps Web'in sürüm bilgisi (Ayarlar/Sürüm bilgisi altında bulabilirsiniz)
- Gramps Web kurulumunuz hakkında verebileceğiniz herhangi bir ayrıntı (kendi barındırdığınız, Grampshub, ...)
- Gramps Web sunucu günlüklerinizin çıktısı, eğer bunlara erişiminiz varsa (docker kullanıyorsanız: `docker compose logs --tail 100 grampsweb` ve `docker compose logs --tail 100 grampsweb-celery`)

## Arka Plan: Eklentinin Çalışma Şekli

Eklentinin nasıl çalıştığına dair merak ediyorsanız, bu bölümde daha fazla ayrıntı bulabilirsiniz.

Eklenti, yerel bir Gramps veritabanını uzaktaki bir Gramps Web veritabanı ile senkronize tutmak için tasarlanmıştır, böylece hem yerel hem de uzaktan değişikliklere (işbirlikçi düzenleme) izin verir.

Bu, **uygun değildir**

- Yerel veritabanının doğrudan türevi olmayan bir veritabanı ile senkronize etmek (yerel veritabanının bir kopyasından veya Gramps XML dışa aktarma/içe aktarma ile)
- Her iki tarafta da büyük sayıda değişiklik olan iki veritabanını birleştirmek için. Bu amaçla mükemmel [İçe Aktarma Birleştirme Aracı](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) kullanılmalıdır.

Aracın çalışma prensipleri oldukça basittir:

- Yerel ve uzaktaki veritabanlarını karşılaştırır
- Herhangi bir fark varsa, en son aynı nesnenin zaman damgasını kontrol eder, buna **t** diyelim
- Eğer bir veritabanında **t**'den daha yakın bir tarihte değişmiş bir nesne varsa ancak diğerinde yoksa, her iki tarafa senkronize edilir (yeni nesne varsayalım)
- Eğer **t**'den daha önce değişmiş bir nesne bir veritabanında yoksa, her iki tarafta da silinir (silinmiş nesne varsayalım)
- Eğer bir nesne farklıysa ancak yalnızca bir veritabanında **t**'den sonra değişmişse, diğerine senkronize edilir (değiştirilmiş nesne varsayalım)
- Eğer bir nesne farklıysa ancak her iki veritabanında da **t**'den sonra değişmişse, birleştirilir (çelişkili değişiklik varsayalım)

En son başarılı senkronizasyonun zamanı da kaydedilir, her sunucu için ayrı olarak ve en son aynı nesne daha yeni olduğunda **t** olarak kullanılır.

Bu algoritma basit ve sağlamdır çünkü senkronizasyon geçmişini takip etmeyi gerektirmez. Ancak, en iyi şekilde *sık sık senkronize ettiğinizde* çalışır.
