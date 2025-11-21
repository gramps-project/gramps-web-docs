Arka uç ve ön uç geliştirme için, Gramps Web API'sine manuel sorgular göndermek faydalı olabilir. HTTPie ve jq kullanarak, bu JWT kimlik doğrulaması dahil olmak üzere rahat bir şekilde yapılabilir.

## Kurulum

HTTPie `pip` ile kurulur:

```bash
python3 -m pip install httpie
```

HTTPie'nin 3.0.0 veya daha yeni bir sürümüne ihtiyacınız olacak.

jq, Ubuntu'da şu şekilde kurulabilir:

```bash
sudo apt install jq
```

## Erişim token'ı alma

Erişim token'ı almak için token uç noktasına sorgu yapın. Geliştirme örneğinizin `localhost:5555` üzerinde çalıştığını varsayarsak, şu komutu kullanabilirsiniz:

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Çıktı olarak JSON token'larını göreceksiniz.

jq kullanarak, erişim token'ını bir ortam değişkeninde de saklayabilirsiniz:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Artık bu token'ı kimlik doğrulaması gerektiren tüm API çağrılarında kullanabilirsiniz, örneğin:

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Varsayılan olarak, erişim token'larının 15 dakika sonra süresi dolacağını unutmayın.
