# Ağaç Özelleştirme

Ağaç sahipleri ve yöneticileri, ağacın adını ve görünümünü, ayrıca ana sayfasını tüm kullanıcılar için uyarlayabilir. Bu ayarlar, [Yönetim ayarları](settings.md) bölümündeki **Ağaç ayarları** ve **Özelleştirme** kısımlarında bulunur.

## Aile Ağacı Adı

!!! note
    Ağacın adını değiştirmek yalnızca bir [çoklu-ağaç kurulumunda](../install_setup/multi-tree.md) veya `TREE_ID` açıkça [sunucu yapılandırmasında](../install_setup/configuration.md) ayarlandığında çalışır. `TREE_ID` ayarlanmamış varsayılan tek ağaç kurulumunda bu bir hata verecektir.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeye olanak tanır. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

!!! tip
    Veritabanını yeniden adlandırmadan yalnızca uygulama çubuğunda gösterilen adı değiştirmek istiyorsanız, bunun yerine [Uygulama başlığı](#app-title) ayarını kullanın.

## Araştırmacı Bilgileri

Ana araştırmacının adını, adresini ve iletişim bilgilerini ayarlayın. Bu bilgiler, dışa aktarımlarda (örneğin, GEDCOM dosyalarında) yer alır.

## Tema Renkleri

Gramps Web arayüzü için özel bir **birincil renk** ve **vurgulayıcı renk** ayarlayın. Bu renkler, bu ağacın tüm kullanıcılarına uygulanır ve kaydedildikten hemen sonra etkili olur.

Renk seçicileri kullanarak renkleri seçin, ardından **Kaydet** butonuna tıklayın. Varsayılan ayarlara geri dönmek için **Sıfırla** butonuna tıklayın.

## Uygulama Başlığı

Uygulama için özel bir başlık ayarlayın. Ayarlandığında, bu, tarayıcı başlık çubuğundaki aile ağacı adını ve üst uygulama çubuğunu geçersiz kılar.

Bir başlık girin ve **Kaydet** butonuna tıklayın. Varsayılan (aile ağacı adı) kullanmak için boş bırakın.

## Ana Sayfa Notu

Gösterilecek bir Gramps **Notu** nesnesi seçin. Not içeriği, ana gösterge panosu sütunlarının altında görüntülenir ve ağaca erişimi olan tüm kullanıcılar tarafından görünür.

Bir not aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa notasını silmek için **Kaldır** butonuna tıklayın.

## Ana Sayfa Görseli

Gösterge panosu ana sayfasında görüntülenecek bir Gramps **Medya** nesnesi seçin. Ana sayfa notu ile birleştirildiğinde, görsel not metninin yanında görünür. Bir not olmadan yalnızca görsel gösterilir.

Bir medya nesnesi aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa görselini silmek için **Kaldır** butonuna tıklayın.

## Dışa Aktarma/İçe Aktarma Ayarları

Ağaç düzeyindeki ayarlar (uygulama başlığı, tema renkleri, ana sayfa notu/görseli vb.) yedekleme amacıyla veya başka bir Gramps Web örneğine kopyalamak için bir JSON dosyası olarak dışa aktarılabilir.

- Mevcut ayarları JSON dosyası olarak indirmek için **Ayarları Dışa Aktar** butonuna tıklayın.
- Önceden dışa aktarılmış bir JSON dosyasını yüklemek ve ayarları uygulamak için **Ağaç ayarlarını İçe Aktar** butonuna tıklayın.
