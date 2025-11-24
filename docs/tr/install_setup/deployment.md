# Gramps Web'i Docker ile Dağıtma

Gramps Web'i kendi sunucunuzda (veya sanal sunucuda) barındırmanın en uygun seçeneği Docker Compose ile gerçekleştirmektir.

Docker ve Docker Compose'un sisteminizde zaten yüklü olduğunu varsayıyoruz. Windows, Mac OS veya Linux'u ana sistem olarak kullanabilirsiniz. Desteklenen mimariler yalnızca x86-64 (masaüstü sistemler) ile sınırlı değildir, aynı zamanda düşük maliyetli ama yeterince güçlü bir web sunucusu olarak hizmet verebilen Raspberry Pi gibi ARM sistemlerini de içerir.

!!! note
    Sunucuda Gramps'ı yüklemenize gerek yoktur, çünkü bu docker imajında bulunmaktadır.


## Adım 1: Docker yapılandırması

Sunucuda `docker-compose.yml` adında yeni bir dosya oluşturun ve aşağıdaki içeriği ekleyin: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

Bu, konteyner yeniden başlatıldığında tüm ilgili verilerin kalıcı olmasını sağlamak için altı adlandırılmış hacim oluşturacaktır.

!!! warning
    Yukarıdaki işlem, API'yi ana makinenin 80 numaralı portunda **SSL/TLS koruması olmadan** kullanılabilir hale getirecektir. Bunu yerel testler için kullanabilirsiniz, ancak bunu doğrudan internete açmayın, tamamen güvensizdir!

## Adım 2: SSL/TLS ile güvenli erişim

Web API'si **mutlaka** kamu internetine HTTPS üzerinden sunulmalıdır. Birkaç seçenek vardır, örneğin:

- SSL/TLS'yi otomatik olarak içeren bir docker barındırma kullanmak
- Let's Encrypt sertifikası ile bir Nginx Ters Proxy kullanmak

İlk seçenek için [Let's Encrypt ile Docker](lets_encrypt.md) sayfasına bakın.

Eğer Gramps Web'i yalnızca yerel ağınızda kullanmayı planlıyorsanız, bu adımı atlayabilirsiniz.

## Adım 3: Sunucuyu başlatma

Aşağıdaki komutu çalıştırın:

```
docker compose up -d
```

İlk çalıştırmada, uygulama size aşağıdakileri yapmanıza olanak tanıyan bir ilk çalışma sihirbazı gösterecektir:

- Sahip (admin) kullanıcı için bir hesap oluşturma
- Bazı gerekli yapılandırma seçeneklerini ayarlama
- Gramps XML (`.gramps`) formatında bir aile ağacı içe aktarma

## Adım 4: Medya dosyalarını yükleme

Medya dosyalarını yüklemek için birkaç seçenek vardır.

- Gramps Web ile aynı sunucuda depolanan dosyaları kullanırken, adlandırılmış bir hacim yerine Docker konteynerine bir dizin bağlayabilirsiniz, yani `gramps_media:/app/media` yerine `/home/server_user/gramps_media/:/app/media` kullanarak medya dosyalarınızı buraya yükleyebilirsiniz.
- [S3'te barındırılan](s3.md) medya dosyalarını kullanırken, S3 Medya Yükleyici Eklentisi'ni kullanabilirsiniz.
- Tartışmasız en uygun seçenek [Gramps Web Senkronizasyonu](../administration/sync.md) kullanmaktır.
