# Ağaç sahibi için bir hesap oluşturun

Gramps Web'i kullanmaya başlamadan önce, ağaç sahibi için bir hesap oluşturmanız gerekir. Belirli bir ağaç için kullanıcı hesabı yoksa, bir hesap oluşturmak için bir form gösterilecektir. Form, sunucunun tek bir ağaç veya birden fazla ağaç için yapılandırılmasına bağlıdır.

## Tek ağaç yapılandırması: yönetici hesabı oluşturun

Tek ağaç yapılandırmasına sahip bir sunucuda, henüz kullanıcı hesabı yoksa, Gramps Web'i açmak bir yönetici hesabı oluşturmak için bir form gösterir. Yönetici kullanıcı, (tek) ağacın sahibi ve kurulumun yöneticisi olacaktır. Form ayrıca, e-posta bildirimleri için gereken e-posta yapılandırmasını ayarlamaya da olanak tanır (örneğin, bir kullanıcı şifresini sıfırlamak için). E-posta yapılandırması sunucuda bir yapılandırma dosyası veya ortam değişkenleri aracılığıyla zaten eklenmişse, formun bu kısmı boş bırakılabilir.

## Çoklu ağaç yapılandırması: yönetici hesabı oluşturun

Çoklu ağaç yapılandırmasında, eğer *herhangi bir ağaçta* kullanıcı yoksa, yani sunucu yeni oluşturulmuşsa, aynı yönetici hesabı oluşturma formu gösterilecektir.

## Çoklu ağaç yapılandırması: ağaç sahibi hesabı oluşturun

Çoklu ağaç yapılandırmasında, her kullanıcı tek bir ağaçla ilişkilidir. Diğer ağaçlarda kullanıcılar mevcut olsa bile, eğer *bu ağaç için* henüz bir sahibi yoksa, web arayüzünde bir ağaç sahibi oluşturulabilir.

Ancak, ağaç sahibi oluşturma formu, tüm ağaçlar için aynı olan Gramps Web ana sayfasında otomatik olarak gösterilmeyecektir. Bunun yerine, `https://my-gramps-instance/firstrun/my-tree-id` adresinden erişilebilir; burada `https://my-gramps-instance`, Gramps Web kurulumunuzun temel adresidir ve `my-tree-id` ağacınızın kimliğidir.

Bir site yöneticisinin yeni bir ağaç oluşturmak için olası bir iş akışı şunlardır:

- REST API aracılığıyla bir ağaç oluşturun, yeni ağacın kimliğini alın
- Potansiyel ağaç sahibi ile uygun ağaç kimliği ile ağaç sahibi oluşturma formunun bağlantısını paylaşın

Ağaç sahibi oluşturma formu, yukarıda tanımlanan yönetici oluşturma formuna benzer, tek farkı e-posta yapılandırmasını değiştirmeye izin vermemesidir (bu yalnızca yöneticiler için mümkündür).
