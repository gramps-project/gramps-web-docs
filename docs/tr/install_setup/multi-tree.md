# Birden Fazla Ağaç Barındırma Kurulumu

Varsayılan olarak, Gramps Web yalnızca yapılandırma dosyasında belirtilen tek bir aile ağacı veritabanına (&ldquo;ağaç&rdquo;) erişime izin verir.

Ancak, Gramps Web API arka uçunun 0.7.0 sürümünden itibaren, tek bir kurulumdan birden fazla ağaç sunmak da mümkündür. Ancak, her kullanıcı (şu anda) tek bir ağaca bağlıdır, bu nedenle bu kurulum, ağaçları kullanıcılar arasında paylaşmak için değil, birden fazla izole Gramps Web örneği barındırmak için uygundur.

## Çoklu ağaç desteğini etkinleştirin

Çoklu ağaç desteğini etkinleştirmek için, `TREE` yapılandırma seçeneği tek bir yıldız `*` olarak ayarlanmalıdır, örneğin bir yapılandırma dosyasında:

```python
TREE = "*"
```

Bu, sunucunun Gramps veritabanı dizinindeki tüm ağaçların erişilebilir olmasını sağlar (yeterli kullanıcı izinleri verildiğinde). Ağacın kimliği, alt dizinin adıdır. Mevcut ağaçları (isimler ve kimlikler) listelemek için aşağıdaki komutu kullanabilirsiniz:

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Ayrıca, medya dosyalarının ayrı alt klasörlerde saklandığından emin olmak için `MEDIA_PREFIX_TREE` yapılandırma seçeneğini `True` olarak ayarlamalısınız. Aksi takdirde, kullanıcılar, izinleri olmayan bir ağaca ait medya dosyalarına erişebilir!

## Belirli bir ağaca kullanıcı hesabı ekleyin

Belirli bir ağaca bir kullanıcı eklemek için, kullanıcı ekleme komutuna `--tree TREEID` komut satırı seçeneğini ekleyin. Ayrıca, JSON yükünde `tree` özelliği ayarlanmış olarak `/users/` uç noktasına POST yapabilirsiniz.

Kullanıcı adları ve e-posta adreslerinin *tüm* ağaçlar arasında benzersiz olması gerekmektedir.

## Yeni bir ağaç oluşturun

Yeni bir ağaç oluşturmak için, Gramps CLI yerine `/trees/` uç noktasına POST yapmanız önerilir. Bu, ağaç kimliği olarak bir UUIDv4 kullanır ve bu da ismin tahmin edilememesi nedeniyle ek bir güvenlik sağlar. Şu anda yalnızca SQLite, yeni oluşturulan ağaçlar için desteklenmektedir.

## Yetkilendirme

Yetkilendirmek için (bir token almak), yalnızca kullanıcı adı ve şifre gereklidir, çünkü her kullanıcı için ağaç kimliği bilindiğinden, bunu sağlamaya gerek yoktur.

## Mevcut medya dosyalarını taşıyın

Mevcut bir Gramps Web örneğini çoklu ağaç desteğine geçirmek ve yerel medya dosyaları kullanıyorsanız, bunları ağaç kimliği adıyla orijinal konumun bir alt klasörüne taşıyabilirsiniz.

Eğer S3 üzerinde barındırılan medya dosyaları kullanıyorsanız, `gramps-web-api` deposunun `scripts` dizininde sağlanan scripti kullanabilirsiniz:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Bu, ilgili erişim anahtarlarının zaten ortam değişkenleri olarak ayarlandığını varsayar.

## Mevcut kullanıcı veritabanını taşıyın

Çoklu ağaç desteğini etkinleştirmek ve mevcut kullanıcıları yeniden kullanmak istiyorsanız, onları belirli bir ağaca atamanız gerekir. Bunun için sağlanan aşağıdaki komutu kullanabilirsiniz:

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Ön yüzü özelleştirin

Giriş sayfasından erişilebilen kayıt sayfası, çoklu ağaç kurulumunda çalışmaz, çünkü kayıt için bir ağaç belirtilmesi gerekir. Bu nedenle, [ön yüz yapılandırmasında](frontend-config.md) `hideRegisterLink` değerini `true` olarak ayarlamak tavsiye edilir.
