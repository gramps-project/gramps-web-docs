---
hide:
  - toc
---

# Gramps Web geliştirme: genel bakış

Gramps Web, ayrı ayrı geliştirilen iki bileşenden oluşan bir web uygulamasıdır:

- **Gramps Web API**, Python ile yazılmış ve Flask tabanlı bir RESTful API'dir. Kaynak kodu [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/) adresinde barındırılmaktadır. Veritabanı erişimini ve soybilimsel işlevleri doğrudan Gramps Python kütüphanesini kullanarak yönetir. Gramps Web'in arka ucunu oluşturur. Geliştirme belgeleri için [Backend](backend/index.md) sayfasına bakın.
- **Gramps Web Frontend**, Gramps Web'in ön yüzü olarak hizmet veren bir Javascript web uygulamasıdır. Kaynak kodu [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/) adresinde barındırılmaktadır. Geliştirme belgeleri için [Frontend](frontend/index.md) sayfasına bakın.

Sürümleme hakkında bir not: Gramps Web API ve Gramps Web ön yüzü bağımsız olarak sürümlenir. Şu anda, "Gramps Web" – birleştirilmiş uygulama – ayrı bir sürüm numarasına sahip değildir. Her iki proje de [SemVer](https://semver.org/) standartlarına uymaktadır.

Eğer bir Python veya Javascript geliştiricisi değilseniz ancak yine de Gramps Web'e katkıda bulunmak istiyorsanız, [Contribute](../contribute/contribute.md) sayfasına göz atın.
