Yerel bilgisayarınızda (Linux, Mac veya Windows) Gramps Web'i Gramps Desktop kurulumunuza müdahale etmeden denemek için, aşağıdaki komutla Docker kullanabilirsiniz:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Bu, [http://localhost:5055](http://localhost:5055) adresinde yeni, boş bir Gramps Web örneği oluşturacak; burada bir yönetici kullanıcısı oluşturabilir ve bir Gramps XML dosyası içe aktarabilirsiniz.

!!! info
    Bu basit kurulum, uzun görevleri ayrı bir süreçte çalıştırmaya izin vermediğinden, büyük bir Gramps XML dosyasını içe aktarmak ilk çalıştırma asistanındaki bir zaman aşımından dolayı başarısız olabilir.


Bilgisayarınızdaki medya dosyalarını kullanmak için Gramps medya klasörünü konteynıra monte edebilirsiniz:

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Bu, konteynırı yeniden başlattığınızda veritabanında yaptığınız değişiklikleri kalıcı hale getirmeyecektir. Gramps Web'i düzgün bir şekilde kurmak için [Dağıtım](deployment.md) hakkında okumaya devam edin.
