# PostgreSQL Veritabanı Kullanımı

Varsayılan olarak, Gramps aile ağacını depolamak için dosya tabanlı bir SQLite veritabanı kullanır. Bu, Gramps Web için mükemmel bir şekilde çalışır ve çoğu kullanıcı için önerilir. Ancak, Gramps Web API sürüm 0.3.0'dan itibaren, her veritabanında tek bir aile ağacı bulunan bir PostgreSQL sunucusu da desteklenmektedir; bu, [Gramps PostgreSQL Eklentisi](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) ile sağlanmaktadır. [Sürüm 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0) itibarıyla, birden fazla aile ağacını tek bir veritabanında barındırmaya olanak tanıyan SharedPostgreSQL Eklentisi de desteklenmektedir; bu, özellikle Gramps Web API [çoklu-ağaç desteği](multi-tree.md) ile birlikte kullanıldığında yararlıdır.

## PostgreSQL Sunucusunu Kurma

PostgreSQLAddon ile kullanılmak üzere yeni bir veritabanı kurmak istiyorsanız, sunucuyu kurmak için [Gramps Wiki'deki talimatları](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) takip edebilirsiniz.

Alternatif olarak, PostgreSQL sunucusunu Gramps Web ile aynı docker ana bilgisayarında bir konteynerde çalıştırmak için Docker Compose kullanabilirsiniz.

Gramps ile dockerize edilmiş bir PostgreSQL kullanmak, varsayılan PostgreSQL görüntülerinin herhangi bir yerel ayar içermemesi nedeniyle karmaşık hale gelmektedir; ancak Gramps, nesnelerin yerelleştirilmiş sıralaması için bunlara ihtiyaç duyar. En kolay seçenek, [bu depoda](https://github.com/DavidMStraub/gramps-postgres-docker/) yayınlanan `gramps-postgres` görüntüsünü kullanmaktır. Bunu kullanmak için, `docker-compose.yml` dosyanıza aşağıdaki bölümü ekleyin:
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
ve ayrıca bu YAML dosyasının `volumes:` bölümüne `postgres_data:` anahtarını ekleyin. Bu görüntü, Gramps soydan gelen verileri ve Gramps kullanıcı veritabanı için ayrı bir veritabanı içerir; her biri ayrı şifreler alabilir.

## Gramps Aile Ağacını İçe Aktarma

Yine, PostgreSQL sunucusunu kendiniz kurduysanız, veritabanına bir aile ağacını içe aktarmak için [Gramps Wiki'deki talimatları](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) takip edebilirsiniz.

Alternatif olarak, yukarıdaki Docker Compose talimatlarını takip ettiyseniz, docker ana bilgisayarınızda bulunan bir Gramps XML dosyasını içe aktarmak için aşağıdaki komutu kullanabilirsiniz:

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## Veritabanı ile Kullanım İçin Web API'yi Yapılandırma

Web API'yi PostgreSQL veritabanı ile kullanmak için, `docker-compose.yml` dosyasındaki `grampsweb` hizmetinin `environment:` anahtarının altına aşağıdakileri ekleyin:

```yaml
      # PostgreSQL eklentisi, ağaç adının
      # veritabanı adıyla eşit olduğunu varsayar
      # ve burada PostgreSQL görüntüsünün varsayılan
      # veritabanı adı kullanılır
      TREE: postgres
      # Kimlik bilgileri, PostgreSQL konteyneri için
      # kullanılanlarla uyuşmalıdır
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Çoklu Ağaç Kurulumunda Paylaşılan PostgreSQL Veritabanı Kullanımı

Bir [çoklu-ağaç kurulumu](multi-tree.md) kullanırken, SharedPostgreSQL eklentisi, tüm ağaçları, API aracılığıyla yeni oluşturulanlar dahil, tek bir PostgreSQL veritabanında barındırmak için pratik bir seçenektir; bu, gizlilik veya güvenlikten ödün vermeden yapılabilir.

Bunu başarmak için, yukarıda açıklandığı gibi `gramps-postgres` görüntüsüne dayalı bir konteyner kurun ve yapılandırma seçeneği `NEW_DB_BACKEND` değerini `sharedpostgresql` olarak ayarlayın; örneğin, `GRAMPSWEB_NEW_DB_BACKEND` ortam değişkeni aracılığıyla.

## Kullanıcı Veritabanı İçin PostgreSQL Veritabanı Kullanımı

Soy verileri için hangi veritabanı arka ucunun kullanıldığına bakılmaksızın, kullanıcı veritabanı uygun bir veritabanı URL'si sağlayarak bir PostgreSQL veritabanında barındırılabilir. Yukarıda bahsedilen `gramps-postgres` docker görüntüsü, bu amaç için kullanılabilecek ayrı bir `grampswebuser` veritabanı içerir. Bu durumda, `USER_DB_URI` yapılandırma seçeneği için uygun değer
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Arama İndeksi İçin PostgreSQL Veritabanı Kullanımı

Gramps Web API sürüm 2.4.0'dan itibaren, arama indeksi ya bir SQLite veritabanında (varsayılan) ya da bir PostgreSQL veritabanında barındırılmaktadır. Bu amaç için de `gramps-postgres` görüntüsü kullanılabilir. Arama indeksi için, soy verilerimizi PostgreSQL'de barındırıp barındırmadığımızdan bağımsız olarak, görüntü tarafından sağlanan `gramps` veritabanını kullanabiliriz (arama indeksi ve soy verileri aynı veritabanında bir arada var olabilir). Bu, yukarıdaki örnekte, `SEARCH_INDEX_DB_URI` yapılandırma seçeneğini ayarlayarak gerçekleştirilebilir:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Sorunlar

Sorun durumunda, lütfen Gramps Web ve PostgreSQL sunucusunun günlük çıktısını izleyin. Docker durumunda, bu aşağıdaki komutlarla gerçekleştirilir:

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Eğer Gramps Web (veya belgeler) ile ilgili bir sorun olduğundan şüpheleniyorsanız, lütfen [Github'da](https://github.com/gramps-project/gramps-web-api/issues) bir sorun bildirin.
