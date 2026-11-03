# CPU ve bellek kullanımını sınırlama

Önerilen docker tabanlı kurulumda, Gramps Web arka uç hizmetini sunmak için [Gunicorn](https://gunicorn.org/) ve arka plan görevleri için [Celery](https://docs.celeryq.dev) kullanır. Her iki durumda da, birden fazla işçi süreci paralel olarak çalıştırılabilir, bu da uygulamanın kullanıcı perspektifinden daha duyarlı olmasını sağlar. Ancak, işçi sayısını artırmak, kullanılan RAM miktarını da artırır (uygulama boşta olduğunda bile) ve isteklerin paralel olarak işlenmesine izin vermek, yüksek CPU kullanımına yol açabilir (özellikle birçok kullanıcı uygulamayı aynı anda kullanıyorsa). Hem Gunicorn hem de Celery, paralel işçi sayısını sınırlamaya izin verir.

## Sisteminiz hakkında bilgi alın

Linux'ta, sisteminizde mevcut olan çekirdek sayısını aşağıdaki komut ile kontrol edebilirsiniz:

```bash
lscpu | grep CPU
```

Ne kadar bellek ve takas alanınızın mevcut olduğunu görmek için, aşağıdaki komutu kullanın:

```bash
free -h
```

## Gunicorn işçi sayısını sınırlama

Varsayılan Gramps Web docker görüntüsünü kullanırken Gunicorn işçi sayısını ayarlamanın en kolay yolu, `GUNICORN_NUM_WORKERS` ortam değişkenini ayarlamaktır; örneğin, bunu `docker-compose.yml` dosyasında "environment" altında tanımlayarak yapabilirsiniz.

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

İdeal işçi sayısını belirlemek için [Gunicorn belgelerine](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) bakın.

!!! info
    Docker görüntüsü, işçilerin yüklenmiş uygulamanın belleğini paylaştığı için `--preload` seçeneği ile Gunicorn'u başlatır ve her ek işçi daha az bellek gerektirir. Gunicorn komutunu geçersiz kılarsanız, bundan faydalanmak için `--preload` seçeneğini koruyun.

## Celery işçi sayısını sınırlama

Celery işçi sayısını ayarlamak için, Docker compose dosyasındaki `concurrency` ayarını uyarlayın:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

İdeal işçi sayısını belirlemek için [Celery belgelerine](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) bakın.

!!! info
    `concurrency` bayrağı atlanırsa (bu, Gramps Web belgelerinde v2.5.0'a kadar böyleydi), sistemde mevcut olan CPU çekirdek sayısına varsayılan olarak ayarlanır; bu da önemli miktarda bellek tüketebilir.
