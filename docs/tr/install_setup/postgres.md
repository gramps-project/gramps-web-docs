# PostgreSQL Veritabanı Kullanımı

Varsayılan olarak, Gramps aile ağacını depolamak için dosya tabanlı bir SQLite veritabanı kullanır. Bu, Gramps Web için mükemmel bir şekilde çalışır ve çoğu kullanıcı için önerilir. Ancak, Gramps Web API sürüm 0.3.0'dan itibaren, her veritabanında tek bir aile ağacını destekleyen bir PostgreSQL sunucusu da desteklenmektedir; bu, [Gramps PostgreSQL Eklentisi](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) ile güçlendirilmiştir. [sürüm 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0) itibarıyla, birden fazla aile ağacını tek bir veritabanında barındırmaya olanak tanıyan SharedPostgreSQL Eklentisi de desteklenmektedir; bu, özellikle Gramps Web API [çoklu-ağaç desteği](multi-tree.md) ile birlikte kullanıldığında faydalıdır.

## PostgreSQL Sunucusunu Kurma

PostgreSQLAddon ile kullanılmak üzere yeni bir veritabanı kurmak istiyorsanız, sunucuyu kurmak için [Gramps Wiki'deki talimatları](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) takip edebilirsiniz.

Alternatif olarak, PostgreSQL sunucusunu Gramps Web ile aynı docker ana bilgisayarında bir konteynerde çalıştırmak için Docker Compose'u da kullanabilirsiniz.

Gramps ile dockerize edilmiş bir PostgreSQL kullanmak, varsayılan PostgreSQL görüntülerinin herhangi bir yerel ayar içermemesi nedeniyle yalnızca karmaşık hale gelir; bu yerel ayarlar Gramps tarafından nesnelerin yerelleştirilmiş sıralaması için gereklidir. En kolay seçenek, [bu depoda](https://github.com/DavidMStraub/gramps-postgres-docker/) yayınlanan `gramps-postgres` görüntüsünü kullanmaktır. Bunu kullanmak için, `docker-compose.yml` dosyanıza aşağıdaki bölümü ekleyin:
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
ve ayrıca bu YAML dosyasının `volumes:` bölümüne `postgres_data:` anahtarını ekleyin. Bu görüntü, Gramps soybilgisel verileri için ayrı bir veritabanı ve Gramps kullanıcı veritabanı içerir; her birinin ayrı şifreleri olabilir.

## Gramps Aile Ağacını İçe Aktarma

Yine, PostgreSQL sunucusunu kendiniz kurduysanız, veritabanına bir aile ağacı aktarmak için [Gramps Wiki'deki talimatları](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) takip edebilirsiniz.

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

## Veritabanı ile Kullanım için Web API'yi Yapılandırma

PostgreSQL veritabanı ile kullanım için Web API'yi yapılandırmak için, `docker-compose.yml` dosyasındaki `grampsweb` hizmetinin `environment:` anahtarının altına aşağıdakileri ekleyin:

```yaml
      # PostgreSQL eklentisi, ağaç adının
      # veritabanı adıyla eşit olduğunu varsayar
      # ve burada PostgreSQL görüntüsünün varsayılan
      # veritabanı adı kullanılır
      GRAMPSWEB_TREE: postgres
      # Kimlik bilgileri, PostgreSQL konteyneri için
      # kullanılanlarla uyuşmalıdır
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

## Çoklu-ağaç Kurulumunda Paylaşılan PostgreSQL Veritabanı Kullanma

Bir [çoklu-ağaç kurulumu](multi-tree.md) kullanırken, SharedPostgreSQL eklentisi, tüm ağaçları, API aracılığıyla yeni oluşturulanlar da dahil olmak üzere, tek bir PostgreSQL veritabanında barındırmak için uygun bir seçenektir; bu, gizlilik veya güvenlikten ödün vermeden yapılabilir.

Bunu başarmak için, yukarıda açıklandığı gibi `gramps-postgres` görüntüsüne dayalı bir konteyner kurun ve yapılandırma seçeneği `NEW_DB_BACKEND`'i `sharedpostgresql` olarak ayarlayın; örneğin, `GRAMPSWEB_NEW_DB_BACKEND` ortam değişkeni aracılığıyla.

## Kullanıcı Veritabanı için PostgreSQL Veritabanı Kullanma

Soybilgisel veriler için hangi veritabanı arka ucunun kullanıldığına bakılmaksızın, kullanıcı veritabanı uygun bir veritabanı URL'si sağlayarak bir PostgreSQL veritabanında barındırılabilir. Yukarıda bahsedilen `gramps-postgres` docker görüntüsü, bu amaç için kullanılabilecek ayrı bir `grampswebuser` veritabanı içerir. Bu durumda, `USER_DB_URI` yapılandırma seçeneği için uygun değer
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Arama İndeksi için PostgreSQL Veritabanı Kullanma

Gramps Web API sürüm 2.4.0'dan itibaren, arama indeksi ya bir SQLite veritabanında (varsayılan) ya da bir PostgreSQL veritabanında barındırılmaktadır. Bu amaç için de `gramps-postgres` görüntüsü kullanılabilir. Arama indeksi için, soybilgisel verilerimizi PostgreSQL'de barındırıp barındırmadığımızdan bağımsız olarak, görüntü tarafından sağlanan `gramps` veritabanını kullanabiliriz (arama indeksi ve soybilgisel veriler aynı veritabanında bir arada bulunabilir). Bu, yukarıdaki örnekte, `SEARCH_INDEX_DB_URI` yapılandırma seçeneğini ayarlayarak gerçekleştirilebilir:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Sorunlar

Sorun durumunda, lütfen Gramps Web ve PostgreSQL sunucusunun günlük çıktısını izleyin. Docker durumunda, bu aşağıdaki komutlarla gerçekleştirilir:

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Eğer Gramps Web (veya belgeler) ile ilgili bir sorun olduğunu düşünüyorsanız, lütfen [Github'da](https://github.com/gramps-project/gramps-web-api/issues) bir sorun bildirin.
