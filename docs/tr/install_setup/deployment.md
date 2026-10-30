# Gramps Web'i Docker ile Dağıtma

Gramps Web'i kendi sunucunuzda (veya sanal sunucuda) barındırmanın en uygun seçeneği Docker Compose kullanmaktır.

Docker ve Docker Compose'un sisteminizde zaten yüklü olduğunu varsayacağız. Windows, Mac OS veya Linux'u ana sistem olarak kullanabilirsiniz. Desteklenen mimariler yalnızca x86-64 (masaüstü sistemler) değil, aynı zamanda düşük maliyetli ama yeterince güçlü bir web sunucusu olarak hizmet verebilecek Raspberry Pi gibi ARM sistemlerini de içerir.

!!! note
    Sunucuda Gramps'ı yüklemenize gerek yoktur, çünkü docker imajında bulunmaktadır.


## Adım 1: Docker yapılandırması

Sunucuda `docker-compose.yml` adında yeni bir dosya oluşturun ve aşağıdaki içeriği ekleyin: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

Bu, konteyner yeniden başlatıldığında tüm ilgili verilerin kalıcı olmasını sağlamak için altı adlandırılmış hacim oluşturacaktır.

`GRAMPSWEB_BASE_URL`'yi Gramps Web'e ulaşılacak adres olarak ayarlayın, örneğin `https://gramps.mydomain.com`. Bu, şifre sıfırlama gibi e-postalarda bağlantılar oluşturmak için kullanılır. E-posta göndermek için, ayrıca [yapılandırma](configuration.md) bölümünde açıklanan e-posta ayarlarını ekleyin.

!!! warning
    Yukarıdaki ayar, API'yi ana makinenin 80 numaralı portunda **SSL/TLS koruması olmadan** kullanılabilir hale getirecektir. Bunu yerel testler için kullanabilirsiniz, ancak bunu doğrudan internete açmayın, tamamen güvensizdir!

## Adım 2: SSL/TLS ile güvenli erişim

Web API'si **mutlaka** kamu internetine HTTPS üzerinden sunulmalıdır. Birkaç seçenek vardır, örneğin:

- SSL/TLS'yi otomatik olarak içeren bir docker barındırma kullanmak
- Let's Encrypt sertifikası ile bir Nginx Ters Proxy kullanmak

İlk seçenek için [Let's Encrypt ile Docker](lets_encrypt.md) sayfasına bakın.

Gramps Web'i yalnızca yerel ağınızda kullanmayı planlıyorsanız, bu adımı atlayabilirsiniz.

## Adım 3: Sunucuyu başlatma

Aşağıdaki komutu çalıştırın:

```
docker compose up -d
```

İlk çalıştırmada, uygulama size aşağıdakileri yapma imkanı veren bir ilk çalıştırma sihirbazı gösterecektir:

- Sahip (admin) kullanıcı için bir hesap oluşturma
- Gramps XML (`.gramps`) formatında bir aile ağacı içe aktarma

## Adım 4: Medya dosyalarını yükleme

Medya dosyalarını yüklemek için birkaç seçenek vardır.

- Gramps Web ile aynı sunucuda depolanan dosyaları kullanırken, adlandırılmış bir hacim yerine Docker konteynerine bir dizin bağlayabilirsiniz, yani `/home/server_user/gramps_media/:/app/media` yerine `gramps_media:/app/media` kullanarak, medya dosyalarınızı oraya yükleyebilirsiniz.
- [S3 üzerinde barındırılan](s3.md) medya dosyalarını kullanıyorsanız, S3 Medya Yükleyici Eklentisini kullanabilirsiniz.
- Tartışmasız en uygun seçenek, [Gramps Web Senkronizasyonu](../administration/sync.md) kullanmaktır.
