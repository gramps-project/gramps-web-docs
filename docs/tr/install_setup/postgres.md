# PostgreSQL Veritabanı Kullanımı

Varsayılan olarak, Gramps Web her aile ağacını kendi SQLite veritabanı dosyasında saklar. Bu, ek bir hizmet gerektirmez, yedeklemeler dosyaları kopyalamaktan ibarettir ve çoğu kurulum için iyi çalışır, çoklu ağaçları [barındıran](multi-tree.md) kurulumlar da dahil.

Alternatif olarak, aile ağaçları SharedPostgreSQL eklentisi kullanılarak bir PostgreSQL sunucusunda barındırılabilir; bu, tüm ağaçları tek bir veritabanında tutar. Eğer zaten bir PostgreSQL sunucusu çalıştırıyorsanız ve yedeklemeleri ve izlemeyi orada yönetmek istiyorsanız veya aynı anda birçok kullanıcının düzenleme yapmasını bekliyorsanız bu mantıklı olabilir. PostgreSQL ayrıca aile ağaçlarının nerede saklandığından bağımsız olarak [kullanıcı veritabanını](#using-a-postgresql-database-for-the-user-database) ve [arama dizinini](#using-a-postgresql-database-for-the-search-index) barındırabilir.

!!! warning "PostgreSQL eklentisi kullanımdan kaldırıldı"
    Tek bir aile ağacını veritabanında saklayan eski PostgreSQL eklentisi kullanımdan kaldırılmıştır ve gelecekteki Gramps Web API sürümlerinde desteklenmeyecektir. Eğer bunu kullanıyorsanız, [PostgreSQL eklentisinden SharedPostgreSQL'e bir ağacı taşıma](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql) konusuna bakın.

## PostgreSQL Sunucusunu Ayarlama

En kolay seçenek, PostgreSQL sunucusunu Gramps Web ile aynı Docker ana bilgisayarında bir konteynerde çalıştırmaktır; bunun için Docker Compose kullanılır.

Gramps, PostgreSQL sunucusunda nesneleri farklı dillerde doğru bir şekilde sıralamak için yerelleştirmelerin kurulu olmasını gerektirir ve varsayılan PostgreSQL görüntüleri bunları içermez. [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) görüntüsü bunları ekler. Bunu kullanmak için `docker-compose.yml` dosyanıza aşağıdaki bölümü ekleyin:
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
Ayrıca bu YAML dosyasının `volumes:` bölümüne `postgres_data:` anahtarını ekleyin. Görüntü, her biri kendi kullanıcı ve şifresine sahip iki veritabanı içerir: `gramps` genealogik veriler için ve `grampswebuser` Gramps Web kullanıcı veritabanı için.

Eğer kendi PostgreSQL sunucunuzu kullanıyorsanız, yapılandırılmış kullanıcının tablolar oluşturabileceği `gramps` adında bir veritabanı oluşturun ve kullanıcılarınızın ihtiyaç duyduğu yerelleştirmelerin kurulu olduğundan emin olun.

## Gramps Web'i Yapılandırma

Yeni aile ağaçları, Gramps Web [çoklu ağaç modunda](multi-tree.md) çalıştığında ve `NEW_DB_BACKEND` yapılandırma seçeneği `sharedpostgresql` olarak ayarlandığında SharedPostgreSQL veritabanında oluşturulur. Yukarıdaki Docker Compose kurulumu ile `docker-compose.yml` dosyasındaki `grampsweb` hizmetinin `environment:` anahtarının altına aşağıdakileri ekleyin:

```yaml
      # çoklu ağaç modunu etkinleştir
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # SharedPostgreSQL veritabanında yeni ağaçlar oluştur
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # PostgreSQL sunucusunun ana bilgisayarı ve portu. 
      # ana bilgisayar yukarıdaki PostgreSQL hizmetinin adıdır
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Kimlik bilgileri, PostgreSQL konteyneri için kullanılanlarla
      # uyuşmalıdır
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Tüm bu seçeneklerin açıklaması için [Yapılandırma](configuration.md) sayfasına bakın. Ana bilgisayar ve port, her ağaç oluşturulduğunda kaydedilir, bu nedenle bunların değiştirilmesi yalnızca yeni ağaçları etkiler.

## Bir Ağaç Oluşturma ve Veri İçe Aktarma

Yeni bir ağaç oluşturmak için, [Birden Fazla Ağaç Barındırma Kurulumu](multi-tree.md#create-a-new-tree) bölümünde açıklandığı gibi `/trees/` uç noktasına POST isteği gönderin. Yanıt, yeni ağacın kimliğini içerir; bu kimlik, [ağaç sahibi hesabını oluşturmak](../administration/owner.md#multi-tree-setup-create-tree-owner-account) için gereklidir.

Ağaç sahibi giriş yaptıktan sonra, mevcut bir aile ağacını [içe aktarabilir](../administration/import.md); örneğin, Gramps Desktop'tan dışa aktarılan bir Gramps XML dosyasını web arayüzü aracılığıyla.

## Kullanıcı Veritabanı için PostgreSQL Veritabanı Kullanma

Kullanıcı veritabanı genellikle aile ağaçlarının nerede barındırıldığına bakılmaksızın bir SQLite dosyasıdır. Bunun yerine PostgreSQL kullanmak için, `USER_DB_URI` yapılandırma seçeneğini bir PostgreSQL veritabanı URL'sine ayarlayın. Yukarıdaki `gramps-postgres` görüntüsü ile `grampswebuser` veritabanını kullanın:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Arama İndeksi için PostgreSQL Veritabanı Kullanma

Arama indeksi de varsayılan olarak SQLite'ta saklanır. Bunun yerine PostgreSQL kullanmak için, `SEARCH_INDEX_DB_URI` yapılandırma seçeneğini bir PostgreSQL veritabanı URL'sine ayarlayın. Yukarıdaki `gramps-postgres` görüntüsü ile, aile ağaçlarınız orada barındırılsın ya da barındırılmasın `gramps` veritabanını kullanabilirsiniz:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## PostgreSQL Eklentisinden SharedPostgreSQL'e Ağaç Taşıma

Eski kurulumlar, her veritabanında tek bir ağaç saklayan PostgreSQL eklentisi ile aile ağaçlarını barındırıyor olabilir ve bu eklenti kullanımdan kaldırılmıştır. Bir ağacın hangi eklentiyi kullandığını öğrenmek için, Gramps veritabanı dizininin ağacın alt dizinindeki `database.txt` dosyasına bakın: bu dosya, kullanımdan kaldırılan PostgreSQL eklentisi için `postgresql` ve SharedPostgreSQL için `sharedpostgresql` içerir.

Kullanıcı hesaplarınızı ve medya dosyalarınızı koruyarak bir ağacı PostgreSQL eklentisinden SharedPostgreSQL'e taşımak için:

1. [Aile ağacınızı yedekleyin](../administration/export.md#back-up-your-family-tree) ve özel kayıtları görüntüleyebilen bir hesap kullanarak bir Gramps XML (`.gramps`) dosyası oluşturun.
2. [Gramps Web'i Yapılandırma](#configuring-gramps-web) bölümünde açıklandığı gibi yapılandırmanızı değiştirin. Mevcut `gramps-postgres` konteynerinizi kullanmaya devam edebilirsiniz.
3. [Yeni bir ağaç oluşturun](multi-tree.md#create-a-new-tree) ve ağaç kimliğini not edin.
4. Mevcut kullanıcı hesaplarınızı yeni ağaca atayın; bu [Mevcut Kullanıcı Veritabanını Taşıma](multi-tree.md#migrate-existing-user-database) bölümünde açıklanmıştır.
5. Medya dosyalarınızı yeni ağaç için beklenen konuma taşıyın; bu [Mevcut Medya Dosyalarını Taşıma](multi-tree.md#migrate-existing-media-files) bölümünde açıklanmıştır.
6. Giriş yapın ve Gramps XML dosyasını yeni ağaca [içe aktarın](../administration/import.md).

Yeni ağacın tamamlandığını kontrol edene kadar Gramps XML dosyasını saklayın.

Eğer ayrı bir Gramps Web kurulumuna taşıyorsanız, [Farklı Bir Gramps Web Örneğine Taşıma](../administration/export.md#move-to-a-different-gramps-web-instance) adımlarını izleyin.

## Sorunlar

Sorunlarla karşılaşırsanız, lütfen Gramps Web ve PostgreSQL sunucusunun günlük çıktısını izleyin. Docker durumunda, bu aşağıdaki komutlarla gerçekleştirilir:

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Eğer Gramps Web (veya belgeler) ile ilgili bir sorun olduğundan şüpheleniyorsanız, lütfen [Github'ta](https://github.com/gramps-project/gramps-web-api/issues) bir sorun bildirin.
