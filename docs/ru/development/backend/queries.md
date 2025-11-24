Для разработки бэкенда и фронтенда может быть полезно отправлять ручные запросы к Gramps Web API. С помощью HTTPie и jq это можно сделать удобно, включая аутентификацию JWT.

## Установка

HTTPie устанавливается с помощью `pip`:

```bash
python3 -m pip install httpie
```

Вам потребуется версия HTTPie 3.0.0 или новее.

jq можно установить в Ubuntu с помощью

```bash
sudo apt install jq
```

## Получение токена доступа

Чтобы получить токен доступа, выполните запрос к конечной точке токена. Предполагая, что ваша экземпляр разработки работает на `localhost:5555`, вы можете использовать команду

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Вы увидите JSON токены в выводе.

С помощью jq вы также можете сохранить токен доступа в переменной окружения:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Теперь вы можете использовать этот токен во всех API вызовах, которые требуют аутентификации, например:

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Обратите внимание, что по умолчанию токены доступа истекают через 15 минут.
