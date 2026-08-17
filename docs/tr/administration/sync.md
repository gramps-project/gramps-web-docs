# Gramps Web ve Gramps Masaüstünü Senkronize Et

*Gramps Web Senkronizasyonu*, Gramps'ın masaüstü bilgisayarınızdaki Gramps veritabanını Gramps Web ile senkronize eden bir eklentidir; medya dosyalarını da içerir. Her iki tarafta yapılan değişiklikler diğer tarafa aktarılır, böylece aynı aile ağacı üzerinde hem yerel olarak hem de web üzerinde çalışabilirsiniz.

Herhangi bir senkronizasyon aracı gibi, bu bir yedekleme değildir: bir tarafta bir şeyi silerseniz, diğer tarafta da silinir. Aile ağacınızın düzenli yedeklerini Gramps XML formatında tutun.

## Kurulum

Eklenti, Python 3.10 veya daha yeni bir sürümde çalışan Gramps 6.0 gerektirir. Gramps Masaüstünde mevcuttur ve [alışıldık şekilde](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps) kurulabilir. Bu belgeler, eklentinin en son sürümünü tanımlar; gerekirse güncellemek için Gramps eklenti yöneticisini kullanın.

Masaüstünüz ve sunucunuz aynı Gramps sürümünü çalıştırmalıdır. Sürüm `MAJOR.MINOR.PATCH` biçimindedir ve `MAJOR` ile `MINOR` eşleşmelidir. Sunucunuzun hangi Gramps sürümünü çalıştırdığını öğrenmek için [Yardım Alın](../help/help.md) bölümüne bakın.

### Sunucu gereksinimleri

Eklenti, bağlandığı anda sunucunuz hakkında iki şeyi kontrol eder, herhangi bir şey indirilmeden önce ve herhangi biri karşılanmazsa bir mesajla durur:

- **Gramps Web API sürümü 3.x.** Bu eklenti sürümü, Gramps 6.0 için Gramps Web API 3 ile çalışır. Daha eski bir sunucunun güncellenmesi gerekir; *daha yeni* bir API ana sürümünü çalıştıran bir sunucu, daha yeni bir Gramps sürümüne ihtiyaç duyar, daha yeni bir eklentiye değil, çünkü her Gramps sürüm hattı bir API sürümü ile eşleşir. Sunucunuzun sürümünü Gramps Web'deki *Ayarlar ▸ Sürüm bilgisi* altında bulabilirsiniz.
- **Arka plan görev kuyruğu.** Değişiklikler sunucuda bir arka plan görevi olarak uygulanır. Bir görev kuyruğu olmadan, bu senkronize bir şekilde çalışır ve gerçek bir aile ağacında zaman aşımına uğrar.

Uzak veritabanına değişiklik uygulamak için, editör, sahibi veya yönetici rolüne sahip bir hesaba ihtiyacınız vardır.

### Şifrenizi Saklamak (isteğe bağlı)

API şifresini sisteminizin şifre yöneticisinde saklamak için `keyring`'i kurun (örneğin, `sudo apt install python3-keyring` veya `sudo dnf install python3-keyring`). Anahtar zinciri kullanılamıyorsa, eklenti bunu belirtir ve onun olmadan devam eder – her seferinde şifreniz istenecektir.

Gramps **Snap** paketinde, sistem anahtar zinciri, bir kez arayüzü bağlayana kadar kısıtlama tarafından engellenmiştir. Eklenti, durumu algıladığında bu komutu gösterir:

```bash
snap connect gramps:password-manager-service
```

Birçok Gnome masaüstü yapılandırmasında, [python keyring'de bir hata](https://github.com/jaraco/keyring/issues/496) nedeniyle `~/.config/python_keyring/keyringrc.cfg` adlı yapılandırma dosyasını aşağıdaki içerikle oluşturmanız gerekir:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Kullanım

Eklenti, Gramps'ta *Araçlar ▸ Aile Ağacı İşleme ▸ Gramps&nbsp;Web&nbsp;Senkr.* altında mevcuttur. Geri alma geçmişinin silineceğini belirten diyalog uyarısını onayladıktan sonra, senkronizasyon penceresi açılır. Açıkça onaylamadığınız sürece yerel ağacınıza veya sunucuya hiçbir değişiklik uygulanmaz.

Pencerenin üst kısmında, senkronize ettiğiniz aile ağacının adı, ait olduğu hesap ve adres ile en son ne zaman senkronize edildiği bilgisi yer alır. Alt kısımda, eklentinin ve sunucunun Web API'sinin sürümü gösterilir; bu, bir sorun bildirirken faydalıdır.

### Bağlanma

Eğer daha önce bu aile ağacını senkronize ettiyseniz ve şifreniz saklanmışsa, eklenti açılır açılmaz bağlanır ve doğrudan karşılaştırmaya geçer. Aksi takdirde, Gramps Web örneğinizin temel URL'sini (örnek: `https://mygrampsweb.com/`), kullanıcı adınızı ve şifrenizi ister.

URL ve kullanıcı adı, Gramps kullanıcı dizininizde düz metin olarak saklanır. Şifreniz yalnızca **Şifreyi Hatırla** seçeneğini işaretli bırakırsanız sistem şifre yöneticinizde saklanır; bu seçeneği kaldırmak, o sunucu için zaten saklanan herhangi bir şifreyi kaldırır. `http://` ile başlayan bir adres girerseniz, eklenti yazarken sizi uyarır, çünkü şifreniz düz metin olarak gönderilecektir.

Senkrone ettiğiniz her sunucu ayrı olarak saklanır ve en son ne zaman senkronize edildiğine dair kendi kaydı ile birlikte tutulur, böylece iki sunucu arasında geçiş yapabilirsiniz. Her giriş ayrıca hangi yerel aile ağacından en son senkronize edildiğini kaydeder. Eklenti, yalnızca açık olan ağaçla eşleştiğinde kendi başına bağlanır; aksi takdirde bağlantı ayrıntılarını gösterir ve *Bağlan* butonuna basmanızı bekler.

Hiçbir şey yazılmadığı sürede iki işlem mevcuttur:

- **Sunucuyu Değiştir…**, üst çubukta, bağlantı ayrıntılarına geri döner, böylece bu ağacı farklı bir sunucuya yönlendirebilirsiniz. Devam eden bir karşılaştırmayı kesintiye uğratır, böylece bitmesini beklemek zorunda kalmazsınız.
- **Bu sunucuyu unut**, bağlantı panelinde, saklanan adresi, kullanıcı adını ve şifreyi, bu ağacın en son ne zaman senkronize edildiği kaydı ile birlikte kaldırır. Bir sonraki senkronizasyon, iki ağacı sıfırdan karşılaştırır.

### Değişiklikleri Gözden Geçirme

Eklenti, yerel ve uzak veritabanlarını karşılaştırır ve hangi veritabanlarını değiştireceğini önerdiği eylemleri gösterir:

```
▾ Bu bilgisayarda değişiklik yapılacak (7 nesne)
    ▾ 3 nesne ekle
        Kişi   John Smith        I0123
    ▾ 4 nesneyi güncelle
        …
▾ Sunucuda değişiklik yapılacak (5 nesne)
    …
```

Her satır, nesnenin adını belirtir, böylece kimin veya neyin etkilendiğini Gramps ID'sini görmekten daha iyi anlayabilirsiniz. Eğer herhangi bir şey silinecekse, listenin üstünde kaç nesnenin ve hangi tarafta olduğunu belirten bir not yer alır.

Listede belirtilenleri gerçekleştirmek için **Uygula** butonuna basın.

Senkronizasyon penceresi, Gramps'ın geri kalanını engellemez, böylece liste açıkken çalışmaya devam edebilirsiniz. Bu arada etkilenen bir nesneyi düzenlerseniz, eklenti Uygula'ya bastığınızda bunu fark eder, hiçbir şeyi değiştirmeden durur ve tekrar karşılaştırmanızı ister.

#### Senkronizasyon Modu

Senkronizasyon modu, değişiklikler listesinin üstünde seçilir. Değiştirmek, listeyi yeniden oluşturur, çünkü mod her farkın ne olacağını belirler.

- **İki Yönlü Senkronizasyon** (varsayılan) – her iki taraftan gelen değişiklikler birleştirilir. Her iki yerde de düzenlenen nesneler birleştirilir.
- **Sunucuyu bu bilgisayara eşleştir** – sunucu, bu bilgisayara eşleştirilir. Sadece sunucuda değiştirilen her şey atılır.
- **Bu bilgisayarı sunucuya eşleştir** – bu bilgisayar, sunucuya eşleştirilir. Burada yalnızca değiştirilen her şey atılır.

1.5 sürümünden önce mevcut olan **birleştirme** modu kaldırılmıştır. Bu, yalnızca bir tarafta silinen nesneleri geri yüklemekle, silme işlemini yaymak yerine farklıydı. Eğer buna güveniyorsanız, iki yönlü senkronizasyonu kullanın ve yedekten saklamak istediğiniz her şeyi geri yükleyin.

### Medya Dosyaları

Medya dosyaları, ayrı bir adım olarak değil, aynı onay sürecinin bir parçası olarak işlenir. Herhangi bir dosyanın aktarılması gerekiyorsa, listenin altında bunları taşımak için bir onay kutusu sunulur:

```
[x] Ayrıca 12 medya dosyasını aktar (4 indirilmek üzere, 8 yüklenmek üzere)
```

Dosyaları etkilemeden nesne değişikliklerini senkronize etmek için kutuyu işaretini kaldırın.

*Her iki* tarafta da eksik olan dosyalar ayrı olarak listelenir, çünkü bunlar hakkında hiçbir şey yapılamaz:

```
Her iki tarafta da eksik 2 medya dosyası var ve aktarılamaz.
```

Medya dosyası senkronizasyonunun iki sınırlaması vardır:

- Eğer yerel bir dosyanın, Gramps veritabanında saklananla farklı bir kontrol toplamı varsa (bu, Gramps'a eklendikten sonra düzenlenen Word dosyaları gibi durumlarda olabilir), yükleme bir hata mesajı ile başarısız olur.
- Araç, tüm yerel dosyaların bütünlüğünü doğrulamaz. Medya nesnesi için saklanan yol altında bir dosya varsa ancak sunucudaki dosyadan farklıysa, araç bunu tespit edemez. Yanlış kontrol toplamlarına sahip dosyaları bulmak için Medya Doğrulama Eklentisini kullanın.

### Senkronizasyon başarısız olursa

Eğer bir senkronizasyon yarıda kalırsa – örneğin bir bağlantı kesilirse – eklenti, daha önce uyguladığı şeyleri rapor eder ve **Tekrar Dene** seçeneğini sunar; bu, başarısız olan adımda devam eder, sıfırdan başlamaz. Uzak ağacın indirilmiş kopyası saklanır, bu nedenle yeniden denemek ikinci kez indirilip karşılaştırılmaz.

Başarısızlığın teknik ayrıntıları, bir *Ayrıntılar* genişletici altında mevcuttur ve bir hata raporu için kopyalamak üzere bir düğme içerir.

## Sorun Giderme

**Beklenmedik değişiklikler.** Eğer eklenti korkutucu bir silme sayısı öneriyorsa, önce üst çubuğu kontrol edin: bu, yazmak üzere olduğunuz sunucudaki aile ağacının adını belirtir. Farklı bir ağacı tutan bir sunucuya karşı bir ağacı senkronize etmek, tam olarak bu semptomu üretir.

Aksi takdirde, beklemediğiniz farklılıklar, veritabanlarından birindeki tutarsızlıklardan veya bilgisayarınız ile sunucunuz arasındaki saatlerin senkronize olmamasından kaynaklanabilir. Her iki saatin de doğru ayarlandığından emin olun (zaman dilimi önemli değildir, çünkü araç Unix zaman damgalarını kullanır) ve yerel veritabanınızda kontrol etme ve onarma aracını çalıştırın. Son çare olarak, yerel veritabanınızı Gramps XML formatında dışa aktarın ve yeni, boş bir veritabanına yeniden içe aktarın. Bu kayıpsız bir işlemdir, ancak tüm verilerin tutarlı bir şekilde saklandığından emin olur.

**Medya dosyası hataları.** Başarısız bir yükleme genellikle disk üzerindeki dosyanın kontrol toplamı ile yerel Gramps veritabanındaki kontrol toplamı arasındaki uyumsuzluktan kaynaklanır; bu, Gramps dışında düzenlenen ofis belgeleri gibi düzenlenebilir dosyalarla olur. Kontrol toplamlarını düzeltmek için Gramps Medya Doğrulama Eklentisini kullanın.

**İzin hataları.** Gramps Web kullanıcı hesabınızın rolünü kontrol edin: yalnızca editörler, sahipler ve yöneticiler uzak veritabanında değişiklik uygulayabilir.

### Yardım İsteyin

Eğer yukarıdakilerin hiçbiri yardımcı olmuyorsa, topluluktan yardım isteyin ve [Gramps forumunun Gramps Web kategorisinde](https://gramps.discourse.group/c/gramps-web/28) bir gönderi paylaşın. Lütfen aşağıdakileri sağlayın:

- Senkronizasyon penceresinin alt kısmında sunucunun Web API sürümü ile birlikte gösterilen Gramps Web Senkronizasyonu eklentisinin sürümü (ve lütfen en son yayımlanan sürümü kullanın)
- Kullandığınız Gramps masaüstü sürümü
- Gramps Web'in sürüm bilgisi, *Ayarlar ▸ Sürüm bilgisi* altında bulunur
- Gramps Web kurulumunuz hakkında herhangi bir ayrıntı (kendinize ait, Grampshub, ...)
- Eğer erişiminiz varsa, Gramps Web sunucu günlüklerinizin çıktısı (Docker kullanıyorsanız: `docker compose logs --tail 100 grampsweb` ve `docker compose logs --tail 100 grampsweb-celery`)

Eğer sizden bir hata ayıklama günlüğü istenirse, Gramps'ı [komut satırından](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) hata ayıklama günlüğü etkinleştirilmiş olarak başlatın ve sorunu yeniden oluşturun:

```bash
gramps --debug grampswebsync
```

## Arka Plan: Eklentinin Çalışma Şekli

Eklenti, yerel bir Gramps veritabanını uzaktaki bir Gramps Web veritabanı ile senkronize tutmak için tasarlanmıştır ve hem yerel hem de uzak değişikliklere izin verir (işbirlikçi düzenleme).

Bu, **uygun değildir**

- yerel veritabanının doğrudan bir türevi olmayan bir veritabanı ile senkronize etmek için (yerel veritabanının bir kopyasından veya Gramps XML dışa aktarma/içe aktarma ile başlamak),
- her iki tarafta da büyük sayıda değişiklik olan iki veritabanını birleştirmek için, bu tür birleştirme için mükemmel [İçe Aktarma Birleştirme Aracını](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) kullanın.

Çalışma prensipleri basittir:

- Yerel ve uzak veritabanlarını karşılaştırır.
- Herhangi bir farklılık varsa, en son aynı nesnenin zaman damgasını kontrol eder, buna **t** diyelim.
- Eğer bir nesne, **t**'den daha yakın bir zamanda değiştiyse bir veritabanında ama diğerinde yoksa, her iki tarafa senkronize edilir (yeni nesne varsayalım).
- Eğer bir nesne, **t**'den önce en son değiştiyse bir veritabanında yoksa, her iki taraftan da silinir (silinmiş nesne varsayalım).
- Eğer bir nesne farklıysa ama yalnızca bir veritabanında **t**'den sonra değiştiyse, diğerine senkronize edilir (değiştirilmiş nesne varsayalım).
- Eğer bir nesne farklıysa ama her iki veritabanında da **t**'den sonra değiştiyse, birleştirilir (çelişkili değişiklik varsayalım).

En son başarılı senkronizasyonun zamanı da kaydedilir, her sunucu için ayrı olarak ve en son aynı nesneden daha yakın olduğunda **t** olarak kullanılır.

Bu algoritma basit ve sağlamdır çünkü senkronizasyon geçmişini takip etmeyi gerektirmez. Ancak, en iyi şekilde *sık sık senkronize ettiğinizde* çalışır.
