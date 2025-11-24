Для розробки бекенду та фронтенду може бути корисно надсилати ручні запити до Gramps Web API. Використовуючи HTTPie та jq, це можна зручно зробити, включаючи аутентифікацію JWT.

## Встановлення

HTTPie встановлюється за допомогою `pip`:

```bash
python3 -m pip install httpie
```

Вам потрібна версія HTTPie 3.0.0 або новіша.

jq можна встановити в Ubuntu за допомогою

```bash
sudo apt install jq
```

## Отримання токена доступу

Щоб отримати токен доступу, запитайте кінцеву точку токена. Припустимо, що ваша розробницька інстанція працює на `localhost:5555`, ви можете використати команду

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Ви побачите JSON токени у виході.

Використовуючи jq, ви також можете зберегти токен доступу в змінній середовища:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Тепер ви можете використовувати цей токен у всіх викликах API, які потребують аутентифікації, наприклад:

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Зверніть увагу, що за замовчуванням токени доступу закінчуються через 15 хвилин.
