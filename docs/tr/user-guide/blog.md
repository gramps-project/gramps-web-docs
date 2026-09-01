# Yerleşik Blogu Kullanma

Blog, ailenizin tarih araştırmaları hakkında hikayeler sunmak için tasarlanmıştır.

Gramps veritabanında, blog gönderileri not eklenmiş kaynaklar olarak temsil edilir; bu not, blogun metnini içerir ve isteğe bağlı olarak blog gönderisinin resimleri için medya dosyaları içerebilir. Gramps Web, `Blog` etiketi olan her kaynağı blog makalesi olarak değerlendirir.

## Bir blog gönderisi ekleme

Bir gönderi yazmanın en hızlı yolu, Gramps Web'deki özel **Yeni Blog Gönderisi** formudur. Bunu, Blog sayfasındaki mavi **+** düğmesinden veya üst uygulama çubuğundaki **Ekle** menüsünden (artı simgesi) **Blog Gönderisi** seçeneğini seçerek açabilirsiniz.

Formda aşağıdaki alanlar bulunmaktadır:

- **Başlık** – gönderinin başlığı (gerekli)
- **Yazar** – kimin yazdığı
- **İçerik** – gönderinin kendisi için zengin metin editörü
- **Medya** – bir veya daha fazla medya nesnesi. İlk medya nesnesi, metnin üzerinde gösterilen önizleme resmi olur; hepsi altında bir galeri olarak görünür.
- **Etiketler** ve diğer nesneler için olduğu gibi bir **özel** anahtarı

Formu kaydetmek, sizin için temel kaynak, not ve `Blog` etiketini oluşturur; bu, [aşağıda](#relation-between-blog-and-sources) açıklanmıştır.

### Gönderiyi manuel olarak ekleme

Ayrıca, temel nesneleri kendiniz oluşturarak bir gönderi oluşturabilirsiniz. Bu, Gramps Desktop'ta ([Gramps Web ile senkronize](../administration/sync.md)) yapmanın tek yoludur ve adımlar her iki uygulamada da aynıdır:

- Yeni bir kaynak ekleyin. Kaynağın başlığı, blog gönderinizin başlığı olacak, kaynağın yazarı ise gönderinin yazarı olacaktır.
- İsteğe bağlı olarak, kaynağı Gramps Web blogunuza karşılık gelen bir depo ile ilişkilendirin.
- Kaynağa yeni bir not ekleyin. Blog gönderinizi yazın ve metni notun içine kopyalayın.
- İsteğe bağlı olarak, kaynağınıza bir veya daha fazla medya dosyası ekleyin. İlk medya dosyası, metnin üzerinde gösterilen gönderi önizleme resmi olarak alınacaktır. Tüm medya dosyaları, metnin altında bir galeri olarak gösterilecektir.
- Kaynağa `Blog` etiketini ekleyin (varsa oluşturun).

## Blog ve kaynaklar arasındaki ilişki

Blog gönderileri sadece kaynaklar olduğundan, tüm blog makaleleri de kaynaklar listesinde görünür ve aramalarda kaynaklar olarak yer alır. Kaynak görünümünde, o blog gönderisi için blog görünümüne götüren "blogda göster" düğmesi vardır. Blog gönderisinin URL'si, ilgili kaynağın Gramps ID'sini de içerir, bu nedenle `yourdomain.com/blog/S0123` adresindeki bir makale, `yourdomain.com/source/S0123` adresindeki kaynağa karşılık gelir.

Her blog gönderisinin altında, sizi kaynak görünümüne götüren "detaylar" düğmesi bulunmaktadır.
