# Gramps Web Kurulum / Ayar

Bu bölüm, Gramps Web'in kurulumu ve ayarları ile başlamanın diğer seçeneklerini ele alır.

## Gramps Web ile Başlarken

Gramps Web, bir sunucuda çalışan ve web tarayıcısı aracılığıyla erişilen bir web uygulamasıdır. İnternet üzerinden kimlik doğrulaması yapılmış kullanıcılara erişilebilir hale getirilmesi amaçlanmıştır.

Eğer Gramps Web'i soybilimsel araştırma verileriniz için kullanmak istiyorsanız, aşağıdaki seçeneklerden birini seçmeniz gerekmektedir:

1. Kendi donanımınızda barındırma
2. Bulutta barındırma
3. Barındırılan bir örnek için kaydolma

Birinci seçenek size maksimum esneklik ve kontrol sağlarken, teknik olarak da zorlu olabilir.

!!! ipucu
    Gramps Web'in ana prensiplerinden biri, kullanıcıların kendi verileri üzerinde her zaman kontrol sahibi olmalarını sağlamaktır, bu nedenle bir örnekten diğerine veri taşımak basittir. Bir seçenek seçtikten sonra kilitlenmek konusunda endişelenmeyin!

## Kendi Donanımınızda Barındırma

Gramps Web'i kendi donanımınızda barındırmanın en pratik yolu Docker Compose kullanmaktır. Ayrıca, Gramps Web'i bodrumunuzdaki bir Raspberry Pi'de çalıştırabilmeniz için ARM mimarisi için Docker görüntüleri de sağlıyoruz.

Kurulum talimatları için [Docker ile Dağıtım](deployment.md) sayfasına bakın.

## Bulutta Barındırma

Gramps Web'i kurmak, diğer basit web uygulamalarına göre daha zorlayıcı olabilir ve sıradan "paylaşımlı barındırma" sağlayıcıları ile uyumlu değildir. Sanal bir sunucu için kaydolabilir ve Gramps Web'i [manuel](deployment.md) olarak kurabilirsiniz.

Daha basit bir seçenek, önceden kurulmuş bir bulut görüntüsü kullanmaktır. Bir örnek, [DigitalOcean 1-tıklama uygulamamızdır](digital_ocean.md).

## Barındırılan Bir Örnek İçin Kayıt Olma

Barındırılan Gramps Web, Gramps Web ile başlamanın en kolay yoludur, çünkü herhangi bir kurulum veya yapılandırma gerektirmez.

Gramps Web için özel barındırma sağlayıcılarının bir listesi burada bulunmaktadır (Gramps açık kaynak topluluğu, bu hizmetlerin sorumluluğunu üstlenmez):

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), Gramps Web'in ana katkı sağlayıcılarından biri tarafından sunulmaktadır.

Eğer Gramps Web için barındırılan bir seçenek kullanıyorsanız, bu bölümün geri kalanını atlayabilir ve doğrudan [Yönetim](../administration/admin.md) bölümüne geçebilirsiniz.
