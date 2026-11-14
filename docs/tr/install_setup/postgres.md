# PostgreSQL Veritabanı Kullanımı

Varsayılan olarak, Gramps Web her aile ağacını kendi SQLite veritabanı dosyasında saklar. Bu, ek bir hizmet gerektirmez, yedeklemeler dosyaları kopyalamaktan ibarettir ve çoğu kurulum için, birden fazla ağacı [barındıranlar](multi-tree.md) dahil olmak üzere, iyi çalışır.

Alternatif olarak, aile ağaçları SharedPostgreSQL eklentisi kullanılarak bir PostgreSQL sunucusunda barındırılabilir; bu, tüm ağaçları tek bir veritabanında tutar. Eğer zaten bir PostgreSQL sunucusu çalıştırıyorsanız ve yedeklemeleri ve izlemeyi orada yönetmek istiyorsanız veya aynı anda birçok kullanıcının düzenleme yapmasını bekliyorsanız bu mantıklı olabilir. PostgreSQL ayrıca aile ağaçlarının nerede saklandığından bağımsız olarak [kullanıcı veritabanını](#using-a-postgresql-database-for-the-user-database) ve [arama dizinini](#using-a-postgresql-database-for-the-search-index) barındırabilir.

!!! warning "PostgreSQL eklentisi kullanım dışı"
    Tek bir aile ağacını veritabanında saklayan eski PostgreSQL eklentisi, Gramps Web API 3.24'ten beri kullanım dışıdır ve Gramps Web API 4.0'da artık desteklenmeyecektir; çünkü bu sürümde varsayılan olarak birden fazla ağacı barındırmakla uyumlu değildir. Eğer bunu kullanıyorsanız, [PostgreSQL eklentisinden SharedPostgreSQL'e bir ağacı taşıma](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql) bölümüne bakın.

## PostgreSQL Sunucusunu Kurma

En kolay seçenek, PostgreSQL sunucusunu Gramps Web ile aynı Docker ana bilgisayarında bir konteynerde çalıştırmaktır; bunun için Docker Compose kullanılır.

Gramps, nesneleri farklı dillerde doğru bir şekilde sıralamak için PostgreSQL sunucusunda yerel ayarların kurulu olmasını gerektirir ve varsayılan PostgreSQL görüntüleri bunları içermez. [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) görüntüsü bunları ekler. Kullanmak için, `docker-compose.yml` dosyanıza aşağıdaki bölümü ekleyin:
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
Ayrıca bu YAML dosyasının `volumes:` bölümüne `postgres_data:` anahtarını ekleyin. Görüntü, her biri kendi kullanıcı ve şifresine sahip iki veritabanı içerir: genealogik veriler için `gramps` ve Gramps Web kullanıcı veritabanı için `grampswebuser`.

Eğer kendi PostgreSQL sunucunuzu kullanıyorsanız, yapılandırılan kullanıcının tablolar oluşturabileceği `gramps` adında bir veritabanı oluşturun ve kullanıcılarınızın ihtiyaç duyduğu yerel ayarların kurulu olduğundan emin olun.

## Gramps Web'i Yapılandırma

Yeni aile ağaçları, Gramps Web [çoklu ağaç modunda](multi-tree.md) çalıştığında ve `NEW_DB_BACKEND` yapılandırma seçeneği `sharedpostgresql` olarak ayarlandığında SharedPostgreSQL veritabanında oluşturulur. Yukarıdaki Docker Compose kurulumu ile, `docker-compose.yml` dosyasındaki `grampsweb` hizmetinin `environment:` anahtarının altına aşağıdakileri ekleyin:

```yaml
      # çoklu ağaç modunu etkinleştir
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # Yeni ağaçları SharedPostgreSQL veritabanında oluştur
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # PostgreSQL sunucusunun ana bilgisayarı ve portu. 
      # ana bilgisayar yukarıdaki PostgreSQL hizmetinin adıdır
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Kimlik bilgileri, PostgreSQL konteyneri için kullanılanlarla
      # uyumlu olmalıdır
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Tüm bu seçeneklerin açıklaması için [Yapılandırma](configuration.md) bölümüne bakın. Ana bilgisayar ve port, her ağaç oluşturulduğunda kaydedilir, bu nedenle daha sonra bunları değiştirmek yalnızca yeni ağaçları etkiler.

## Bir Ağaç Oluşturma ve Veri İçe Aktarma

Yeni bir ağaç oluşturmak için, [Birden Fazla Ağaç Barındırma İçin Kurulum](multi-tree.md#create-a-new-tree) bölümünde açıklandığı gibi `/trees/` uç noktasına POST yapın. Yanıt, yeni ağacın kimliğini içerir; bu kimlik, [ağaç sahibi hesabını oluşturmak](../administration/owner.md#multi-tree-setup-create-tree-owner-account) için gereklidir.

Ağaç sahibi giriş yaptıktan sonra, mevcut bir aile ağacını [içe aktarabilir](../administration/import.md); örneğin, Gramps Desktop'tan dışa aktarılan bir Gramps XML dosyasını web arayüzü üzerinden.

## Kullanıcı Veritabanı İçin PostgreSQL Veritabanı Kullanımı

Kullanıcı veritabanı genellikle aile ağaçlarının nerede barındırıldığına bakılmaksızın bir SQLite dosyasıdır. Bunun yerine PostgreSQL kullanmak için, `USER_DB_URI` yapılandırma seçeneğini bir PostgreSQL veritabanı URL'sine ayarlayın. Yukarıdaki `gramps-postgres` görüntüsü ile, `grampswebuser` veritabanını kullanın:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Arama İndeksi İçin PostgreSQL Veritabanı Kullanımı

Arama indeksi varsayılan olarak SQLite'da saklanır. Bunun yerine PostgreSQL kullanmak için, `SEARCH_INDEX_DB_URI` yapılandırma seçeneğini bir PostgreSQL veritabanı URL'sine ayarlayın. Yukarıdaki `gramps-postgres` görüntüsü ile, aile ağaçlarınız orada barındırılsın ya da barındırılmasın, `gramps` veritabanını kullanabilirsiniz:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

Arama indeksi PostgreSQL 12 veya daha yenisini gerektirir.

## PostgreSQL Eklentisinden SharedPostgreSQL'e Ağaç Taşıma

Eski kurulumlar, her veritabanında tek bir ağaç saklayan ve kullanım dışı olan PostgreSQL eklentisi ile aile ağaçlarını barındırıyor olabilir. Bir ağacın hangi eklentiyi kullandığını öğrenmek için, Gramps veritabanı dizininin ağacın alt dizinindeki `database.txt` dosyasına bakın: bu dosya, kullanım dışı PostgreSQL eklentisi için `postgresql` ve SharedPostgreSQL için `sharedpostgresql` içerir.

Kullanıcı hesaplarınızı ve medya dosyalarınızı koruyarak bir ağaç taşımak için, PostgreSQL eklentisinden SharedPostgreSQL'e aynı kurulum içinde:

1. [Aile ağacınızı dışa aktarın](../administration/export.md#export-the-family-tree-as-gramps-xml) ve özel kayıtları görüntüleyebilen bir hesap kullanın.
2. [Gramps Web'i Yapılandırma](#configuring-gramps-web) bölümünde açıklandığı gibi yapılandırmanızı değiştirin. Mevcut `gramps-postgres` konteynerinizi kullanmaya devam edebilirsiniz.
3. [Yeni bir ağaç oluşturun](multi-tree.md#create-a-new-tree) ve ağaç kimliğini not edin.
4. Mevcut kullanıcı hesaplarınızı yeni ağaca atayın; bu, [Mevcut Kullanıcı Veritabanını Taşıma](multi-tree.md#migrate-existing-user-database) bölümünde açıklanmıştır.
5. Medya dosyalarınızı yeni ağaç için beklenen konuma taşıyın; bu, [Mevcut Medya Dosyalarını Taşıma](multi-tree.md#migrate-existing-media-files) bölümünde açıklanmıştır.
6. Giriş yapın ve Gramps XML dosyasını yeni ağaca [içe aktarın](../administration/import.md).

Yeni ağacın tamamlandığını kontrol edene kadar Gramps XML dosyasını saklayın.

Eğer ayrı bir Gramps Web kurulumuna geçiyorsanız, [Farklı Bir Gramps Web Örneğine Taşınma](../administration/export.md#move-to-a-different-gramps-web-instance) bölümündeki adımları izleyin.

## Sorunlar

Sorun durumunda, lütfen Gramps Web ve PostgreSQL sunucusunun günlük çıktısını izleyin. Docker durumunda, bu aşağıdaki komutlarla gerçekleştirilir:

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Eğer Gramps Web (veya belgeler) ile ilgili bir sorun olduğunu düşünüyorsanız, lütfen [Github](https://github.com/gramps-project/gramps-web-api/issues) üzerinde bir sorun bildirin.
