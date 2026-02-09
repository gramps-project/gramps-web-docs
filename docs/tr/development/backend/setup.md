# Backend geliştirme kurulumu

Bu sayfa, [Gramps Web API](https://github.com/gramps-project/gramps-web-api/) geliştirmeye başlamak için gereken adımları listelemektedir; Gramps Web'in arka uç (sunucu bileşeni) kısmıdır.

## Ön koşullar

Önerilen geliştirme kurulumu, devcontainer'lar ile Visual Studio Code kullanmaktadır. Bu yaklaşım, ihtiyacınız olan tüm araçlarla önceden yapılandırılmış bir geliştirme ortamı oluşturacaktır. Başlamak için aşağıdaki bileşenlere ihtiyacınız olacak:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) ve [Dev Containers eklentisi](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) yüklü
- [Git](https://git-scm.com)

İşletim sistemi olarak Linux, macOS veya Windows kullanabilirsiniz.

## Başlarken

1. [Gramps Web API deposunu](https://github.com/gramps-project/gramps-web-api) açın ve "fork" butonuna tıklayın.
2. Forkladığınız depoyu Git kullanarak yerel makinenize klonlayın.
3. Klonlanan depoyu Visual Studio Code'da açın. İstendiğinde "Container'da Yeniden Aç" seçeneğini seçin veya komut paletini manuel olarak açın (Ctrl+Shift+P veya Cmd+Shift+P) ve "Dev Containers: Yeniden Oluştur ve Container'da Yeniden Aç" seçeneğini seçin.
4. Dev container'ın inşa edilmesini ve başlamasını bekleyin. Bu, özellikle ilk seferde birkaç dakika sürebilir.

    **Dev Container inşası başarılı olduğunda, komut şu şekilde dönecektir:**

    `Başarıyla gramps-webapi-x.x.x yüklendi.`

    !!! bilgi
        Visual Studio Code'da Container'ı Yeniden Oluşturmak için:

        - Eğer container'daysanız, "Container'da Yeniden Oluştur" palet komutunu kullanın.

        - Eğer klasör görünümündeyseniz (yani container'da değilseniz) "Yeniden Oluştur ve Container'da Yeniden Aç" palet komutunu kullanın.

## Görevler

Eğer sadece arka uç kodunu değiştiriyorsanız, bir web sunucusu başlatmanıza gerek yoktur - birim testleri, çalışan bir sunucuya ihtiyaç duymadan API'ye istek simüle etmeye olanak tanıyan bir Flask test istemcisi kullanır.

Ancak, bir sunucu çalıştırmak faydalıdır eğer

- değişikliklerinizi gerçek HTTP istekleri ile denemek istiyorsanız (bkz. [manuel sorgular](queries.md)),
- değişikliklerin tam Gramps Web uygulaması üzerindeki etkisini önizlemek istiyorsanız veya
- ayrıca ön uçta eş zamanlı değişiklikler yapmak istiyorsanız (bkz. [ön uç geliştirme kurulumu](../frontend/setup.md)).

Sunucuyu çalıştırmak, dev container'da önceden tanımlanmış görevlerle basitleştirilmiştir. Bu görevleri komut paletinden (Ctrl+Shift+P veya Cmd+Shift+P) "Görevler: Görev Çalıştır" seçeneğini seçerek ve ardından aşağıdakilerden birini seçerek çalıştırabilirsiniz:
- "Web API'yi Sun" - Flask geliştirme sunucusunu 5555 numaralı portta hata ayıklama günlüğü etkin olarak başlatır.
- "Celery işçisini Başlat" - arka plan görevlerini işlemek için bir Celery işçisi başlatır.

## Hata Ayıklama

Hata ayıklama bazen zorlayıcı olabilir, özellikle karmaşık davranışları izlemeye veya ince sorunları tanımlamaya çalışırken. Bunu kolaylaştırmak için, hem çalışan bir API örneğini hem de bireysel test durumlarını doğrudan Visual Studio Code içinde hata ayıklayabilirsiniz.

### Gramps Web API'yi Hata Ayıklama

Çalışan API'yi hata ayıklamak için:

1. Visual Studio Code'u açın ve **Çalıştır ve Hata Ayıkla** görünümüne gidin.  
2. Aşağı açılır menüden **"Web API"** yapılandırmasını seçin.  
3. Hata ayıklamayı başlatın.  
4. Arka uca istek gönderdiğinizde (ister manuel olarak ister Gramps Web GUI aracılığıyla), kodda ayarladığınız herhangi bir kesme noktasında yürütme duracaktır.  
   Bu, değişkenleri, kontrol akışını ve diğer çalışma zamanı ayrıntılarını incelemenizi sağlar.

### Test Durumlarını Hata Ayıklama

Belirli bir test durumunu hata ayıklamak için:

1. Hata ayıklamak istediğiniz test dosyasını açın (örneğin, `test_people.py`).  
2. Visual Studio Code'da **Çalıştır ve Hata Ayıkla** görünümünü açın.  
3. **"Mevcut Test Dosyası"** yapılandırmasını seçin.  
4. Hata ayıklamayı başlatın — yürütme, o test dosyası içinde ayarlanan herhangi bir kesme noktasında duracaktır.  

Bu kurulum, test mantığını adım adım incelemenizi, değişken değerlerini gözlemlemenizi ve test hatalarını veya beklenmedik sonuçları daha iyi anlamanızı sağlar.
