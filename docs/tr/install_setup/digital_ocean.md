# Gramps Web DigitalOcean 1-Tık Uygulaması

[Gramps Web'i kendiniz kurmak](deployment.md) yerine [Gramps Web DigitalOcean 1-Tık Uygulaması](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) uygulamasını da kullanabilirsiniz. Digital Ocean, Gramps Web'in Demo sürümünü barındırır.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Kurulum prosedürünün bir parçası olarak DigitalOcean'da bir hesap oluşturmanız ve kullanacağınız “droplet” (sanal makine) için ücretli bir plan seçmeniz gerekir.

Bu yöntem, kendi donanımınızı kullanmadan, SSL ile güvence altına alınmış, kendi barındırdığınız Gramps Web örneğinizi dağıtmanın şu anda en basit yolu sayılabilir.

!!! info
    Barındırma hizmetleri için DigitalOcean'a ödeme yapacağınızı unutmayın. Gramps açık kaynak projesi ücretli destek sağlamaz.

## 1. Adım: DigitalOcean hesabı oluşturma

Henüz bir hesabınız yoksa [DigitalOcean](https://www.digitalocean.com/) üzerinde bir hesap oluşturun.

## 2. Adım: Droplet oluşturma

- [Gramps Web 1-Tık Uygulaması](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) sayfasına gidin ve “Create Gramps Web Droplet” seçeneğine tıklayın.
- En az 2 GB RAM içeren bir plan seçin.
- Droplet'ınız için kimlik doğrulamayı ayarlayın
- “Create Droplet” seçeneğine tıklayın

## 3. Adım: Alan adı ayarlama

Bir alan adına (veya alt alan adına) ihtiyacınız olacaktır. Bir alan adınız varsa alan adınızı droplet'ınızın IP adresine yönlendirin. Aksi takdirde [DuckDNS](https://www.duckdns.org/) gibi ücretsiz bir hizmet kullanabilirsiniz.

## 4. Adım: Droplet'ınıza giriş yapma

Droplet'ınıza SSH ile bağlanın. “Welcome to the Gramps Web DigitalOcean 1-click app setup!” mesajını görmeniz gerekir. Mesajı görmüyorsanız birkaç dakika bekleyip tekrar deneyin (kurulum henüz tamamlanmamış olabilir).

Kurulum betiği sizden alan adını (ör. `mygrampswebinstance.duckdns.org`) ve bir e-posta adresini (Let's Encrypt sertifikası için gereklidir) girmenizi isteyecektir. İsteğe bağlı olarak Gramps Web'in e-posta göndermek için kullandığı SMTP ayarlarını da (ör. parola sıfırlama işlemleri için) isteyecektir; bunu atlamak için SMTP sunucusu alanını boş bırakın.

Bu işlem tamamlandığında kurulumun arka planda tamamlanmasını bekleyin

## 5. Adım: Gramps Web'i başlatma

Gramps Web örneğinize artık alan adınızın kökünden geçerli bir SSL sertifikasıyla erişilebilmesi ve ilk çalıştırma yardımcısının görüntülenmesi gerekir.

## Yapılandırmayı daha sonra değiştirme

Kurulum betiği, temel URL'yi ve e-posta ayarlarını [yapılandırma seçenekleri](configuration.md) olarak `GRAMPSWEB_` ön ekiyle `/root/letsencrypt.env` dosyasında depolar; örneğin:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Ayar eklemek veya değiştirmek için droplet üzerindeki bu dosyayı düzenleyin ve değişikliği şu komutla uygulayın:

```bash
cd /opt/grampsweb && docker compose up -d
```
