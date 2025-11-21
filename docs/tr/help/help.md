---
hide:
  - navigation
---

Gramps Web ile ilgili sorunlarla karşılaşırsanız veya yardıma ihtiyacınız olursa, lütfen aşağıdaki seçeneklerden birini seçin.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Arka uç sorunları :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Ön uç sorunları :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

İlk olarak nereye yönelmeniz gerektiği konusunda bazı rehberlikler aşağıda verilmiştir.

## Soru sorma

Resmi Gramps Discourse forumunda [Gramps Web için ayrı bir kategori](https://gramps.discourse.group/c/gramps-web/) bulunmaktadır. Gramps Web ile ilgili herhangi bir sorunuz varsa bunu kullanabilirsiniz, örneğin

- Gramps Web'in kullanımıyla ilgili sorular
- Gramps Web'in yapılandırmasıyla ilgili sorular
- Gramps Web'in dağıtımında sorun giderme
- Gramps Web ile ilgili iyileştirme fikirleri
- ...

## Sorun bildirme

Gramps Web'de bir hata olduğunu düşündüğünüz bir sorunla karşılaşırsanız, lütfen bunu Github üzerinden bildirin.

Gramps Web'de kullanılan kod için iki ayrı Github deposu bulunmaktadır, biri kullanıcı arayüzü (“ön uç”) ve diğeri sunucu kodu (“arka uç”) içindir:

- [Ön uç sorunları](https://github.com/gramps-project/gramps-web/issues)
- [Arka uç sorunları](https://github.com/gramps-project/gramps-web-api/issues)

Eğer bir sorunu nereye bildireceğinizden emin değilseniz, endişelenmeyin ve iki seçenekten birini seçin - bakımcılar gerekirse sorunu aktarabilecektir.

Her durumda, lütfen raporunuzda her zaman aşağıdaki bilgileri ekleyin:

- Kurulumunuz hakkında detaylar (örneğin, hassas değerlerin gizlendiği bir docker-compose dosyası veya Grampshub gibi barındırılan bir versiyon mu kullandığınız, ya da DigitalOcean gibi önceden yapılandırılmış bir görüntü mü kullandığınız)
- Sürüm bilgileri. Bunu almak için, Gramps Web'deki Ayarlar sayfasında "Sistem bilgileri" sekmesine gidin ve kutudaki değerleri kopyalayıp yapıştırın; bu değerler aşağıdaki gibi görünmelidir:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## İyileştirme önerileri

Gelecek iyileştirmeler hakkında genel fikirler ve tartışmalar için, [forumda](https://gramps.discourse.group/c/gramps-web/) bir tartışma açmaktan çekinmeyin. Belirli bir özelliğin zaten planlanıp planlanmadığını veya üzerinde çalışılıp çalışılmadığını kontrol etmek için sorun sayfalarını (yukarıdaki bağlantılara bakın) da incelemek isteyebilirsiniz.

Sınırlı kapsamda belirli iyileştirmeler için, uygun ön uç veya arka uç Github deposunda doğrudan bir özellik isteği ile bir sorun açmaktan çekinmeyin.
