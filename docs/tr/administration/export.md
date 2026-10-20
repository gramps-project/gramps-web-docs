## Aile ağacınızı yedekleyin

Ağaç sahipleri, [Yedeklemeler](settings.md#backups) bölümünde ağaçlarının ayarları ve kullanıcıları da dahil olmak üzere tam yedeklerini oluşturabilir, indirebilir ve geri yükleyebilir.

Alternatif olarak, yalnızca aile ağacı verilerinin yedeğini oluşturmak için Gramps Web'deki Dışa Aktarma sayfasını açın ve Gramps XML formatını seçin.

"İhraç et" butonuna tıklamak, dosyayı oluşturacak ve hazır olduğunda indirmeye başlayacaktır.

Eğer Gramps Web kullanıcınızın özel kayıtlara erişim izni yoksa, dışa aktarma tam bir yedek olmayacaktır, çünkü özel kayıtları içermeyecektir.

Bu Gramps XML dosyası daha sonra [Yedekten Geri Yükle](settings.md#restore-from-backup) aracılığıyla ağacı tam olarak bu duruma geri yüklemek için kullanılabilir.

## Aile ağacınızı diğer soybilim programlarının kullanıcılarıyla paylaşın

Soybilim verilerini Gramps XML olarak paylaşmak bir seçenek değilse, bir GEDCOM dosyası da dışa aktarabilirsiniz. Bunun Gramps Web ağacınız için bir yedekleme olarak uygun olmadığını unutmayın.

## Medya dosyalarınızı yedekleyin

Medya dosyalarınızı yedeklemek için, Dışa Aktarma sayfasında tüm medya dosyalarının bir ZIP arşivini oluşturabilir ve indirebilirsiniz.

Özellikle büyük ağaçlar için, bu işlemin sunucu için maliyetli olabileceğini ve yalnızca gerçekten gerekli olduğunda yapılması gerektiğini unutmayın. Bu nedenle, oluşturulabilecek medya arşivlerinin sayısı sınırlıdır (varsayılan olarak saatte bir). Sınırı aştığınızda, hata mesajı bunu gösterir.

Medya dosyalarınızı düzenli olarak yedeklemek için daha iyi bir seçenek, [Gramps Web Senkronizasyon eklentisi](sync.md) (kendisi bir yedekleme çözümü değildir) kullanmak ve yerel bilgisayarınızda artımlı yedeklemeler oluşturmaktır.

Her iki durumda da, eğer Gramps Web kullanıcınızın özel kayıtlara erişim izni yoksa, dışa aktarma özel medya nesnelerinin dosyalarını içermeyecektir.

## Farklı bir Gramps Web örneğine geçin

Gramps Web, sizi belirli bir sağlayıcı ile kilitlemez ve verilerinizi kaybetmeden, sunuculara doğrudan erişim olmadan farklı bir Gramps Web örneğine her zaman geçebilirsiniz.

Tam bir geçiş sağlamak için bu adımları izleyin (ağaç sahibi izinleriniz olduğunu varsayarak):

1. Dışa Aktarma sayfasına gidin ve ağacınızı Gramps XML (`.gramps`) dosyası olarak dışa aktarın. [Senkronizasyon eklentisini](sync.md) kullanıyorsanız, dışa aktarmayı Gramps masaüstünde de oluşturabilirsiniz.
2. Dışa Aktarma sayfasında, bir medya arşivi oluşturun ve indirin. [Senkronizasyon eklentisini](sync.md) kullanıyorsanız, yerel Gramps medya klasörünüzü de basitçe ZIP'leyebilirsiniz.
3. Ayarlar > Yönetim > Kullanıcıları Yönet bölümüne gidin ve "Kullanıcı detaylarını dışa aktar" butonuna tıklayın. Bu, bir JSON dosyası indirecektir.
4. Yeni Gramps Web örneğinde, İçe Aktarma sayfasını açın. 1. adımda dışa aktarılan `.gramps` dosyasını içe aktarın.
5. Yeni Gramps Web örneğinin İçe Aktarma sayfasında, medya arşivini (ZIP) yükleyin.
6. Yeni Gramps Web örneğinin Ayarlar > Yönetim > Kullanıcıları Yönet bölümüne gidin. "Kullanıcı hesaplarını içe aktar" butonuna tıklayın ve 3. adımda indirilen JSON dosyasını yükleyin.

Kullanıcı hesaplarınızın taşınacağını unutmayın, ancak tüm kullanıcılarınızın "şifremi unuttum" bağlantısını kullanarak yeni şifreler belirlemesi gerekecektir, çünkü şifreler şifreli biçimde saklanır ve dışa aktarılamaz.
