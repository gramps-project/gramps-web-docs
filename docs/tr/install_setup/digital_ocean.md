# Gramps Web DigitalOcean 1-Tıklama Uygulaması

[Gramps Web'i kendiniz kurmak](deployment.md) yerine, [Gramps Web DigitalOcean 1-Tıklama Uygulaması](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy)'nı da kullanabilirsiniz. Digital Ocean, Gramps Web'in Demo sürümünü barındırmaktadır.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Kurulum prosedürü kapsamında, DigitalOcean'da bir hesap oluşturmanız ve kullanmak için "droplet" (sanallaştırılmış makine) için ücretli bir plan seçmeniz gerekecektir.

Bu, şu anda kendi, kendine barındırılan Gramps Web örneğinizi SSL ile güvenli bir şekilde, kendi donanımınızı kullanmadan dağıtmanın en basit yolu olarak değerlendirilebilir.

!!! info
    DigitalOcean'a barındırma hizmetleri için ödeme yapacağınızı unutmayın. Gramps açık kaynak projesi ücretli destek sağlamaz.

## Adım 1: DigitalOcean hesabı oluşturun

Henüz bir hesabınız yoksa [DigitalOcean](https://www.digitalocean.com/) adresinde bir hesap oluşturun.

## Adım 2: Droplet oluşturun

- [Gramps Web 1-Tıklama Uygulaması](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) sayfasına gidin ve "Gramps Web Droplet Oluştur" butonuna tıklayın.
- En az 2 GB RAM'e sahip bir plan seçin.
- Droplet'inize kimlik doğrulama ayarlarını yapın.
- "Droplet Oluştur" butonuna tıklayın.

## Adım 3: Alan adı ayarlayın

Bir alan adına (veya alt alan adına) ihtiyacınız olacak. Eğer bir alan adınız varsa, bunu droplet'inizin IP adresine yönlendirin. Aksi takdirde, [DuckDNS](https://www.duckdns.org/) gibi ücretsiz bir hizmet kullanabilirsiniz.

## Adım 4: Droplet'inize giriş yapın

Droplet'inize SSH ile bağlanın. "Gramps Web DigitalOcean 1-tıklama uygulaması kurulumuna hoş geldiniz!" mesajını görmelisiniz. Eğer böyle bir mesaj görmüyorsanız, birkaç dakika bekleyin ve tekrar deneyin (kurulum henüz tamamlanmamış olabilir).

Kurulum betiği sizden alan adını (örneğin, `mygrampswebinstance.duckdns.org`) ve bir e-posta adresini (Let's Encrypt sertifikası için gereklidir) isteyecektir. İsteğe bağlı olarak, Gramps Web'in e-posta göndermek için kullandığı SMTP ayarlarını da isteyebilir; şifre sıfırlama gibi işlemler için; bu kısmı atlamak için SMTP sunucusunu boş bırakabilirsiniz.

Bu işlem tamamlandıktan sonra, arka planda kurulumun tamamlanmasını bekleyin.

## Adım 5: Gramps Web'i başlatın

Gramps Web örneğiniz artık alan adınızın kökünde, geçerli bir SSL sertifikası ile erişilebilir olmalı ve ilk çalıştırma asistanını göstermelidir.

## Daha sonra yapılandırmayı değiştirme

Kurulum betiği, temel URL'yi ve e-posta ayarlarını `/root/letsencrypt.env` dosyasında `GRAMPSWEB_` ile başlayan [yapılandırma seçenekleri](configuration.md) olarak saklar, örneğin:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Ayar eklemek veya değiştirmek için, bu dosyayı droplet üzerinde düzenleyin ve değişikliği uygulamak için

```bash
cd /opt/grampsweb && docker compose up -d
