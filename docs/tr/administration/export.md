## Aile ağacınızı yedekleyin

Aile ağacınızın yedeğini oluşturmak için, Gramps Web'de Dışa Aktarma sayfasını açın ve Gramps XML formatını seçin.

"Export" butonuna tıklamak dosyayı oluşturacak ve hazır olduğunda indirmeye başlayacaktır.

Eğer Gramps Web kullanıcınızın özel kayıtlara erişim izni yoksa, dışa aktarma tam bir yedekleme olmayacaktır, çünkü özel kayıtları içermeyecektir.

## Aile ağacınızı diğer soybilim programı kullanıcılarıyla paylaşın

Soybilim verilerini Gramps XML olarak paylaşmak bir seçenek değilse, bir GEDCOM dosyası da dışa aktarabilirsiniz. Bunun Gramps Web ağacınızın yedeği olarak uygun olmadığını unutmayın.

## Medya dosyalarınızı yedekleyin

Medya dosyalarınızı yedeklemek için, Dışa Aktarma sayfasında tüm medya dosyalarının bir ZIP arşivini oluşturabilir ve indirebilirsiniz.

Özellikle büyük ağaçlar için, bu işlemin sunucu için maliyetli olabileceğini ve yalnızca kesinlikle gerekli olduğunda yapılması gerektiğini unutmayın.

Medya dosyalarınızı düzenli olarak yedeklemek için daha iyi bir seçenek, [Gramps Web Sync eklentisini](sync.md) kullanmak (bu kendisi bir yedekleme çözümü değildir) ve yerel bilgisayarınızda artımlı yedeklemeler oluşturmaktır.

Her iki durumda da, eğer Gramps Web kullanıcınızın özel kayıtlara erişim izni yoksa, dışa aktarma özel medya nesnelerinin dosyalarını içermeyecektir.

## Farklı bir Gramps Web örneğine geçin

Gramps Web sizi belirli bir sağlayıcıya kilitlemez ve verilerinizi kaybetmeden, sunuculara doğrudan erişim olmadan her zaman farklı bir Gramps Web örneğine geçebilirsiniz.

Tam bir geçiş sağlamak için bu adımları izleyin (ağaç sahibi izinleriniz olduğunu varsayarak):

1. Dışa Aktarma sayfasına gidin ve ağacınızı Gramps XML (`.gramps`) dosyası olarak dışa aktarın. [Sync eklentisini](sync.md) kullanıyorsanız, dışa aktarmayı Gramps masaüstünde de oluşturabilirsiniz.
2. Dışa Aktarma sayfasında, bir medya arşivi oluşturun ve indirin. [Sync eklentisini](sync.md) kullanıyorsanız, yerel Gramps medya klasörünüzü basitçe ZIP'leyebilirsiniz.
3. Ayarlar > Yönetim > Kullanıcıları Yönet bölümüne gidin ve "Kullanıcı detaylarını dışa aktar" butonuna tıklayın. Bu, bir JSON dosyası indirecektir.
4. Yeni Gramps Web örneğinde, İçe Aktarma sayfasını açın. 1. adımda dışa aktarılan `.gramps` dosyasını içe aktarın.
5. Yeni Gramps Web örneğinin İçe Aktarma sayfasında, medya arşivini (ZIP) yükleyin.
6. Yeni Gramps Web örneğinin Ayarlar > Yönetim > Kullanıcıları Yönet bölümüne gidin. "Kullanıcı hesaplarını içe aktar" butonuna tıklayın ve 3. adımda indirilen JSON dosyasını yükleyin.

Kullanıcı hesaplarınızın taşınacak olmasına rağmen, tüm kullanıcılarınızın "şifremi unuttum" bağlantısını kullanarak yeni şifreler belirlemesi gerekecektir, çünkü şifreler şifrelenmiş biçimde saklanır ve dışa aktarılamaz.
