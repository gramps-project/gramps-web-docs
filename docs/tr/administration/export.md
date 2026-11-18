# Veri Dışa Aktarma

Dışa Aktarma sayfası, aile ağacı verilerini çeşitli formatlarda indirmenizi ve tüm medya dosyalarının bir arşivini indirmenizi sağlar.

## Aile ağacını Gramps XML olarak dışa aktar

Aile ağacı verilerinin bir kopyasını almak için Gramps Web'de Dışa Aktarma sayfasını açın ve Gramps XML formatını seçin. Dosyayı oluşturmak için **Oluştur** butonuna tıklayın ve dosya hazır olduğunda **İndir** butonuna tıklayın. Büyük bir ağaç için dosyanın oluşturulması biraz zaman alabilir; bu süre zarfında sayfayı terk edebilir ve dosyayı daha sonra [bildirimler](../user-guide/notifications.md) bölümünden indirebilirsiniz.

Eğer Gramps Web kullanıcınızın özel kayıtlara erişim izni yoksa, dışa aktarma özel kayıtları içermeyecektir.

## Aile ağacınızı yedekleyin

Ağacın tamamı için – ayarları ve kullanıcıları dahil – [Yedekleme ve geri yükleme](backups.md) bölümüne bakın. Gramps XML dışa aktarımı yalnızca aile ağacı verilerinin bir yedeği olarak hizmet edebilir ve [Yedekten Geri Yükle](backups.md#restore-from-backup) aracılığıyla geri yüklenebilir.

## Aile ağacınızı diğer soybilim programı kullanıcılarıyla paylaşın

Gramps XML olarak soybilim verilerini paylaşmak bir seçenek değilse, bir GEDCOM dosyası da dışa aktarabilirsiniz. Bunun, Gramps Web ağacınızın yedeği olarak uygun olmadığını unutmayın.

## Medya dosyalarınızı yedekleyin

Medya dosyalarınızı yedeklemek için Dışa Aktarma sayfasında tüm medya dosyalarının bir ZIP arşivini oluşturabilir ve indirebilirsiniz.

Özellikle büyük ağaçlar için, bu işlemin sunucu için maliyetli olabileceğini ve yalnızca kesinlikle gerekli olduğunda yapılması gerektiğini unutmayın. Bu nedenle, oluşturulabilecek medya arşivlerinin sayısı sınırlıdır (varsayılan olarak saatte bir). Sınırı aştığınızda, hata mesajı bunu gösterir.

Medya dosyalarınızı düzenli olarak yedeklemek için daha iyi bir seçenek, [Gramps Web Senkronizasyon eklentisi](sync.md) (kendisi bir yedekleme çözümü değildir) kullanmak ve yerel bilgisayarınızda artımlı yedeklemeler oluşturmaktır.

Her iki durumda da, eğer Gramps Web kullanıcınızın özel kayıtlara erişim izni yoksa, dışa aktarma özel medya nesnelerinin dosyalarını içermeyecektir.

## Farklı bir Gramps Web örneğine geçin

Gramps Web, sizi belirli bir sağlayıcıya kilitlemez ve herhangi bir veri kaybetmeden, sunuculara doğrudan erişim olmadan farklı bir Gramps Web örneğine geçebilirsiniz.

Tam bir geçiş sağlamak için bu adımları izleyin (ağaç sahibi izinleriniz olduğunu varsayarak):

1. Dışa Aktarma sayfasına gidin ve ağacınızı Gramps XML (`.gramps`) dosyası olarak dışa aktarın. [Senkronizasyon eklentisini](sync.md) kullanıyorsanız, dışa aktarımı Gramps masaüstünde de oluşturabilirsiniz.
2. Dışa Aktarma sayfasında, bir medya arşivi oluşturun ve indirin. [Senkronizasyon eklentisini](sync.md) kullanıyorsanız, yerel Gramps medya klasörünüzü de ZIP'leyebilirsiniz.
3. Ayarlar > Yönetim > Kullanıcıları Yönet bölümüne gidin ve "Kullanıcı ayrıntılarını dışa aktar" butonuna tıklayın. Bu, bir JSON dosyası indirecektir.
4. Yeni Gramps Web örneğinde, [İçe Aktarma sayfasını](import.md) açın. 1. adımda dışa aktarılan `.gramps` dosyasını içe aktarın.
5. Yeni Gramps Web örneğinin İçe Aktarma sayfasında, [Medya Dosyalarını İçe Aktar](import-media.md) bölümünde medya arşivini (ZIP) yükleyin.
6. Yeni Gramps Web örneğinin Ayarlar > Yönetim > Kullanıcıları Yönet bölümüne gidin. "Kullanıcı hesaplarını içe aktar" butonuna tıklayın ve 3. adımda indirilen JSON dosyasını yükleyin.

Kullanıcı hesaplarınızın taşınacağını unutmayın, ancak tüm kullanıcılarınızın "şifreyi unuttum" bağlantısını kullanarak yeni şifreler belirlemesi gerekecektir, çünkü şifreler şifreli biçimde saklanır ve dışa aktarılamaz.
