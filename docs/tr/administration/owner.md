# Ağaç sahibi için bir hesap oluşturun

Gramps Web'i kullanmaya başlamadan önce, ağaç sahibi için bir hesap oluşturmanız gerekir. Belirli bir ağaç için kullanıcı hesabı yoksa, bir hesap oluşturmak için bir form gösterilecektir. Form, sunucunun tek ağaç veya çoklu ağaç için yapılandırılmasına bağlıdır.

## Tek ağaç yapılandırması: yönetici hesabı oluşturun

Tek ağaç yapılandırmasına sahip bir sunucuda, henüz hiçbir kullanıcı hesabı yoksa, Gramps Web'i açmak bir yönetici hesabı oluşturmak için bir form gösterir. Yönetici kullanıcı, (tek) ağacın sahibi ve kurulumun yöneticisi olacaktır. Form ayrıca e-posta bildirimleri için gerekli e-posta yapılandırmasını ayarlamaya da olanak tanır (örneğin, bir kullanıcı parolasını sıfırlama). E-posta yapılandırması, sunucuda bir yapılandırma dosyası veya ortam değişkenleri aracılığıyla zaten eklenmişse, formun bu kısmı boş bırakılabilir.

Parola iki kez girilmelidir; form yalnızca her iki giriş eşleştiğinde gönderilebilir.

Örnek zaten yapılandırılmışsa, formun adresini açmak, mevcut bir hesapla giriş yapmanızı isteyen bir mesaj gösterir.

## Çoklu ağaç yapılandırması: yönetici hesabı oluşturun

Çoklu ağaç yapılandırmasında, eğer *herhangi bir ağaçta* kullanıcı yoksa, yani sunucu yeni oluşturulmuşsa, yönetici hesabı oluşturmak için aynı form gösterilecektir.

## Çoklu ağaç yapılandırması: ağaç sahibi hesabı oluşturun

Çoklu ağaç yapılandırmasında, her kullanıcı tek bir ağaç ile ilişkilidir. Diğer ağaçlarda kullanıcılar mevcut olsa bile, eğer *bu ağaç için* henüz bir sahibi yoksa, web arayüzünde bir ağaç sahibi oluşturulabilir.

Ancak, ağaç sahibi oluşturma formu, tüm ağaçlar için aynı olan Gramps Web ana sayfasında otomatik olarak gösterilmeyecektir. Bunun yerine, `https://my-gramps-instance/firstrun/my-tree-id` adresinden erişilebilir; burada `https://my-gramps-instance`, Gramps Web kurulumunuzun temel adresi ve `my-tree-id` ağaç ID'nizdir.

Bir site yöneticisinin yeni bir ağaç oluşturmak için olası bir iş akışı şunlardır:

- REST API aracılığıyla bir ağaç oluşturun ve yeni ağacın ID'sini alın
- İlgili ağaç ID'si ile ağaç sahibi oluşturma formunun bağlantısını potansiyel ağaç sahibi ile paylaşın

Ağaç sahibi oluşturma formu, yukarıda açıklanan yönetici oluşturma formuna benzer, tek farkı e-posta yapılandırmasını değiştirmeye izin vermemesidir (bu yalnızca yöneticiler için mümkündür).
