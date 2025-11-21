# Gramps Web DigitalOcean 1-Tık Uygulaması

[Gramps Web'i kendiniz kurmak](deployment.md) yerine, [Gramps Web DigitalOcean 1-Tık Uygulamasını](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) kullanabilirsiniz. Digital Ocean, Gramps Web'in Demo sürümünü barındırmaktadır.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Kurulum prosedürünün bir parçası olarak, DigitalOcean'da bir hesap oluşturmanız ve kullanmak için "droplet" (sanallaştırılmış makine) için bir ücretli plan seçmeniz gerekecektir.

Bu, kendi donanımınızı kullanmadan, SSL ile güvence altına alınmış kendi kendine barındırılan Gramps Web örneğinizi dağıtmanın şu anda en basit yolu olarak değerlendirilebilir.

!!! info
    DigitalOcean'a barındırma hizmetleri için ödeme yapacağınızı unutmayın. Gramps açık kaynak projesi ücretli destek sağlamamaktadır.

## Adım 1: DigitalOcean hesabı oluşturun

Henüz bir hesabınız yoksa [DigitalOcean](https://www.digitalocean.com/) adresinde bir hesap oluşturun.

## Adım 2: Droplet oluşturun

- [Gramps Web 1-Tık Uygulamasına](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) gidin ve "Gramps Web Droplet Oluştur" butonuna tıklayın.
- En az 2 GB RAM içeren bir plan seçin.
- Droplet'inize kimlik doğrulaması ayarlayın.
- "Droplet Oluştur" butonuna tıklayın.

!!! info
    1-Tık Uygulamasının en son `docker-compose` sürümünü yüklemesi için on dakikaya kadar beklemeniz gerekebilir.
    En son `docker-compose` sürümünü kullanmak, `firstlogin.sh` ile ilgili hataları azaltabilir.

## Adım 3: Bir alan adı ayarlayın

Bir alan adına (veya alt alan adına) ihtiyacınız olacak. Eğer bir alan adınız varsa, onu droplet'inizin IP adresine yönlendirin. Aksi takdirde, [DuckDNS](https://www.duckdns.org/) gibi ücretsiz bir hizmet kullanabilirsiniz.

## Adım 4: Droplet'inize giriş yapın

Droplet'inize SSH ile bağlanın. "Gramps Web DigitalOcean 1-tık uygulama kurulumu hoş geldiniz!" mesajını görmelisiniz. Eğer bu mesajı görmüyorsanız, birkaç dakika bekleyin ve tekrar deneyin (kurulum henüz tamamlanmamış olabilir).

Kurulum betiği sizden alan adını (örneğin `mygrampswebinstance.duckdns.org`) ve Let's Encrypt sertifikası için gerekli olan bir e-posta adresini isteyecektir.

Bu işlem tamamlandığında, arka planda kurulumun tamamlanmasını bekleyin.

## Adım 5: Gramps Web'i başlatın

Gramps Web örneğiniz artık alan adınızın kökünde, geçerli bir SSL sertifikası ile erişilebilir olmalı ve ilk çalıştırma asistanını göstermelidir.
