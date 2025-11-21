# Ön Uç Geliştirme Kurulumu

Bu sayfa, ön uç geliştirmeye başlamak için gereken adımları açıklar.

## Ön Koşullar

Önerilen geliştirme kurulumu, devcontainer'lar ile Visual Studio Code kullanır. Bu yaklaşım, ihtiyaç duyduğunuz tüm araçlarla önceden yapılandırılmış bir geliştirme ortamı oluşturur.

Gerekli ön koşullar için [Arka Uç Geliştirme Kurulumu](../backend/setup.md#prerequisites) sayfasına bakın.

## Başlarken

1. [Gramps Web ön uç deposunu](https://github.com/gramps-project/gramps-web) açın ve "fork" butonuna tıklayın.
2. Forkladığınız depoyu Git kullanarak yerel makinenize klonlayın.
3. Klonlanan depoyu Visual Studio Code'da açın. İstendiğinde "Konteynerde Yeniden Aç" seçeneğini seçin veya komut paletini manuel olarak açın (Ctrl+Shift+P veya Cmd+Shift+P) ve "Dev Containers: Yeniden Oluştur ve Konteynerde Yeniden Aç" seçeneğini seçin.
4. Geliştirici konteynerinin oluşturulmasını ve başlamasını bekleyin. Bu, özellikle ilk seferde birkaç dakika sürebilir.

## Ön Uç Geliştirme Sunucusunu Çalıştırma

Ön uç geliştirme sunucusunu çalıştırmak ve değişikliklerinizin tarayıcıda etkisini önizlemek için, dev konteynerdeki önceden tanımlı görevleri kullanabilirsiniz.

Bunun çalışması için, önce [Gramps Web API arka uç](../backend/setup.md#tasks) örneğini başlatmanız gerekir. Bunu yapmanın en kolay yolu, arka uç dev konteynerini kullanmak ve ayrı bir VS Code penceresinde [“Web API'yi Sun” görevini](../backend/setup.md#tasks) çalıştırmaktır.

Arka uç çalışmaya başladıktan sonra, komut paletinden (Ctrl+Shift+P veya Cmd+Shift+P) "Görevler: Görev Çalıştır" seçeneğini seçerek ve ardından "Gramps Web ön uçunu Sun" seçeneğini seçerek ön uç geliştirme sunucusunu çalıştırabilirsiniz.

Bu, ön uç geliştirme sunucusunu 8001 numaralı portta başlatır; tarayıcınızda `http://localhost:8001` adresine giderek erişebilirsiniz. Ön uç kodunda değişiklik yaptığınızda, tarayıcı otomatik olarak yeniden yüklenir ve değişikliklerinizin etkisini hemen görmenizi sağlar.
