# Gramps Web Güncellemesi

Docker Compose'a dayalı kurulum yöntemlerinden birini kullanıyorsanız, Gramps Web'i en son sürüme güncellemek basittir. `docker-compose.yml` dosyanızın bulunduğu klasörde, aşağıdaki komutları çalıştırın:

```bash
docker compose pull
docker compose up -d
```

[Gramps Web API](https://github.com/gramps-project/gramps-web-api) için küçük sürüm atlamaları için bu yeterlidir. Ancak, [Gramps Web API sürüm notlarını](https://github.com/gramps-project/gramps-web-api/releases) takip etmeyi unutmayın; çünkü ek dikkat veya yapılandırma değişiklikleri gerektiren kırıcı değişiklikler olabilir.

Varsayılan `grampsweb:latest` docker imajının her zaman API'nin en son sürümünü ve ön yüzün en son sürümünü birleştirdiğini unutmayın. İki bileşeni ayrı ayrı yükseltmek istiyorsanız - bu mümkündür - burada açıklananlardan daha karmaşık bir kurulum gereklidir.
