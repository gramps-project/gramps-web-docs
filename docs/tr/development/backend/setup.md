# Backend geliştirme kurulumu

Bu sayfa, Gramps Web'in backend'ini (sunucu bileşeni) geliştirmeye başlamak için gereken adımları listeler: [Gramps Web API](https://github.com/gramps-project/gramps-web-api/).

## Ön koşullar

Önerilen geliştirme kurulumu, devcontainers ile Visual Studio Code kullanmaktadır. Bu yaklaşım, ihtiyaç duyduğunuz tüm araçlarla önceden yapılandırılmış bir geliştirme ortamı oluşturacaktır. Başlamak için aşağıdaki bileşenlere ihtiyacınız olacak:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) ve [Dev Containers uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) yüklü
- [Git](https://git-scm.com)

İşletim sistemi olarak Linux, macOS veya Windows kullanabilirsiniz.

## Başlarken

1. [Gramps Web API deposunu](https://github.com/gramps-project/gramps-web-api) açın ve "fork" butonuna tıklayın.
2. Forkladığınız depoyu yerel makinenize Git kullanarak klonlayın.
3. Klonlanan depoyu Visual Studio Code'da açın. İstendiğinde "Container'da Yeniden Aç" seçeneğini seçin veya komut paletini manuel olarak açın (Ctrl+Shift+P veya Cmd+Shift+P) ve "Dev Containers: Yeniden Oluştur ve Container'da Yeniden Aç" seçeneğini seçin.
4. Geliştirici konteynerinin oluşturulmasını ve başlamasını bekleyin. Bu, özellikle ilk kez birkaç dakika sürebilir.

## Görevler

Eğer yalnızca backend kodunu değiştiriyorsanız, bir web sunucusu başlatmanıza gerek yoktur - birim testleri, çalışır durumda bir sunucuya ihtiyaç duymadan API'ye istek simüle etmeye olanak tanıyan bir Flask test istemcisi kullanır.

Ancak, bir sunucu çalıştırmak faydalıdır eğer

- Değişikliklerinizi gerçek HTTP istekleri ile denemek istiyorsanız (bkz. [manuel sorgular](queries.md)),
- Değişikliklerin etkisini tam Gramps Web uygulamasında önizlemek istiyorsanız veya
- Aynı zamanda frontend'de de değişiklikler yapmak istiyorsanız (bkz. [frontend geliştirme kurulumu](../frontend/setup.md)).

Sunucunun çalıştırılması, önceden tanımlanmış görevlerle geliştirici konteynerinde basitleştirilmiştir. Bu görevleri komut paletinden (Ctrl+Shift+P veya Cmd+Shift+P) "Görevler: Görev Çalıştır" seçeneğini seçerek ve ardından aşağıdakilerden birini seçerek çalıştırabilirsiniz:
- "Web API'yi Sun" - Flask geliştirme sunucusunu 5555 numaralı portta hata ayıklama günlüğü etkin olarak başlatır.
- "Celery işçisini Başlat" - arka plan görevlerini işlemek için bir Celery işçisi başlatır.

## Hata Ayıklama

Hata ayıklama bazen zorlu olabilir, özellikle karmaşık davranışları izlemeye veya ince sorunları tanımlamaya çalışırken. Bunu kolaylaştırmak için, hem çalışan bir API örneğini hem de bireysel test durumlarını doğrudan Visual Studio Code içinde hata ayıklayabilirsiniz.

### Gramps Web API'yi Hata Ayıklama

Çalışan API'yi hata ayıklamak için:

1. Visual Studio Code'u açın ve **Çalıştır ve Hata Ayıkla** görünümüne gidin.  
2. Açılır menüden **"Web API"** yapılandırmasını seçin.  
3. Hata ayıklamayı başlatın.  
4. Backend'e istek gönderdiğinizde (ister manuel olarak ister Gramps Web GUI aracılığıyla), kodda ayarladığınız herhangi bir kesme noktasında yürütme duracaktır.  
   Bu, değişkenleri, kontrol akışını ve diğer çalışma zamanı ayrıntılarını incelemenizi sağlar.

### Test Durumlarını Hata Ayıklama

Belirli bir test durumunu hata ayıklamak için:

1. Hata ayıklamak istediğiniz test dosyasını açın (örneğin, `test_people.py`).  
2. Visual Studio Code'da **Çalıştır ve Hata Ayıkla** görünümünü açın.  
3. **"Mevcut Test Dosyası"** yapılandırmasını seçin.  
4. Hata ayıklamayı başlatın — yürütme, o test dosyasında ayarlanan herhangi bir kesme noktasında duracaktır.  

Bu kurulum, test mantığını adım adım incelemenizi, değişken değerlerini gözlemlemenizi ve test hatalarını veya beklenmedik sonuçları daha iyi anlamanızı sağlar.
