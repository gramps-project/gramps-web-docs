Gramps Web'i yerel bilgisayarınızda (Linux, Mac veya Windows) Gramps Desktop kurulumunuza müdahale etmeden denemek için, aşağıdaki komut ile Docker kullanabilirsiniz:

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Bu, [http://localhost:5055](http://localhost:5055) adresinde erişilebilir yeni, boş bir Gramps Web örneği oluşturur; burada bir admin kullanıcı oluşturabilir ve bir Gramps XML dosyası içe aktarabilirsiniz.

!!! info
    Bu basit kurulum uzun görevleri ayrı bir süreçte çalıştırmaya izin vermediğinden, büyük bir Gramps XML dosyasını içe aktarmak, ilk çalıştırma asistanında zaman aşımından dolayı başarısız olabilir.


Bilgisayarınızdaki medya dosyalarını kullanmak için Gramps medya klasörünü konteynıra monte edebilirsiniz:

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Bu, konteynırı yeniden başlattığınızda veritabanında yaptığınız değişikliklerin kalıcı olmayacağını unutmayın. Gramps Web'i doğru bir şekilde kurmak için [Deployment](deployment.md) hakkında okumaya devam edin.
