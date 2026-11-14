# Yedekleme ve geri yükleme

Ağaç sahipleri, [Yönetim ayarları](settings.md) bölümündeki **Yedeklemeler** kısmında aile ağacının yedeklerini oluşturabilir, indirebilir ve geri yükleyebilir.

Bir yedek, aile ağacı verilerini, özel kayıtlar dahil, ağaç ayarlarını ve ağacın kullanıcılarını içerir. Medya dosyaları dahil değildir; [Medya dosyalarınızı yedekleyin](export.md#back-up-your-media-files) kısmına bakın.

## Saklanan yedekler

Eğer sunucu yöneticisi bir yedekleme dizini (`BACKUP_DIR`, bkz. [Sunucu yapılandırması](../install_setup/configuration.md)) ayarladıysa, yedekler sunucuda saklanabilir. Aksi takdirde, bölümde yedeklerin saklanmasının yapılandırılmadığını belirten bir bildirim gösterilir ve yalnızca yüklenen bir dosyadan geri yükleme yapılabilir.

Bir yedek oluşturmak için **Yedek Oluştur...** butonuna tıklayın. Yedek, arka planda bir görev olarak oluşturulur ve ardından saklanan yedekler listesinde, tarihi, kişi sayısını ve boyutunu göstererek görünür. Sunucu yalnızca en yeni yedekleri (varsayılan olarak beş) saklar ve daha eski olanları otomatik olarak siler. Günlük olarak oluşturulabilecek yedek sayısı da sınırlıdır.

Her saklanan yedek için şunları yapabilirsiniz:

- **İndir**: Başka bir yerde bir kopyasını saklamak için `.tar` dosyası olarak indirin.
- **Geri Yükle**: Aşağıda açıklandığı gibi geri yükleyin.
- **Sil**: Onayladıktan sonra silin.

Sunucuda çalışan Gramps Web sürümünden daha yeni bir sürümle yapılmış bir yedek, bir uyarı simgesi ile işaretlenir ve geri yüklenemez.

## Yedekten Geri Yükle

Ağacı saklanan bir yedekten veya yüklenen bir dosyadan geri yükler. Saklanan bir yedeği geri yüklemek için, yanındaki geri yükleme butonuna tıklayın. Bir dosyadan geri yüklemek için, bir Gramps Web yedeği (`.tar`) veya bir Gramps XML dosyası (`.gramps`) seçin ve **Geri Yükle** butonuna tıklayın.

!!! danger
    Verilerin geri yüklenmesi yıkıcı bir değiştirme işlemidir, bir birleştirme değil. Yedekte mevcut olmayan herhangi bir nesne silinir.

Bir Gramps Web yedeği için, yedeğin ne zaman yapıldığı, hangi ağaç için yapıldığı ve hangi sürümle yapıldığı hakkında bir diyalog gösterilir ve hangi bölümlerin geri yükleneceğini seçmenize olanak tanır:

- **Veri** – aile ağacının nesneleri
- **Ağaç ayarları** – tema renkleri, uygulama başlığı ve ana sayfa notu gibi Yönetim sayfasının ayarları
- **Kullanıcılar** – ağacın kullanıcıları

Geri yüklemenin neyi değiştireceğini görmek için **Önizleme** butonuna tıklayın. Bir Gramps XML dosyası yalnızca veri içerdiğinden, böyle bir dosya için önizleme hemen başlar. Oturumunuz yeterince taze değilse, yeniden kimlik doğrulamanız istenecektir. Önizleme, arka planda bir görev olarak çalışır ve tamamlandığında, nesne türüne göre (kişiler, aileler, olaylar, yerler, alıntılar, kaynaklar, depolar, medya nesneleri, notlar, etiketler) ve seçilmişse ağaç ayarları ve kullanıcılar için değişiklikleri özetleyen bir diyalog açar:

- **Ekle** – yedekte mevcut ancak mevcut ağaçta eksik olan nesneler
- **Güncelle** – her ikisinde de mevcut olan ancak farklı olan nesneler
- **Sil** – mevcut ağaçta yedekte bulunmayan nesneler
- **Değişmemiş** – her ikisinde de özdeş olan nesneler

Herhangi bir nesne silinecekse, diyalog kaç tane olduğunu uyarır. Özeti gözden geçirin, ardından değişiklikleri uygulamak için **Geri Yükle** butonuna tıklayın veya iptal etmek için **İptal** butonuna tıklayın.

Geri yüklemeden sonra, yedekten eklenen kullanıcılar listelenir. Rastgele bir şifre alırlar, bu nedenle oturum açmadan önce şifrelerini sıfırlamaları gerekir. Sunucuda zaten mevcut olan kullanıcılar asla değiştirilmez. Sunucuda dosyaları eksik olan medya nesneleri de listelenir; bunları [Medya dosyalarını içe aktar](import-media.md) kısmından yükleyin.

!!! note
    Verilerin geri yüklenmesi yalnızca nesne verilerini ve medya referanslarını geri yükler. İkili medya dosyaları ve ağaç meta verileri (varsayılan kişi, yer işaretleri, ad grupları) etkilenmez.

!!! tip
    Bunu, kötü bir içe aktarma veya istenmeyen bir toplu düzenleme sonrasında, bir ağacı bilinen iyi bir yedeğe geri almak için kullanın.

## Gramps XML yedeği olarak

Eğer yedeklerin saklanması mümkün değilse veya yalnızca aile ağacı verilerinin bir kopyasını saklamak istiyorsanız, ağacı Gramps XML olarak [dışa aktarın](export.md). Böyle bir dosya, [Yedekten Geri Yükle](#restore-from-backup) kısmından da geri yüklenebilir.

Gramps Web kullanıcınızın özel kayıtlara erişim izni yoksa, dışa aktarma tam bir yedek olmayacaktır, çünkü özel kayıtları içermeyecektir.
