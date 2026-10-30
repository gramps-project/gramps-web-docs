# Gramps Web DigitalOcean 1-Click App

Замість того, щоб [налаштовувати Gramps Web самостійно](deployment.md), ви також можете скористатися [Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean хостить демонстраційну версію Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

У рамках процедури налаштування вам потрібно буде зареєструвати обліковий запис у DigitalOcean і вибрати платний план для "дроплета" (віртуальної машини), яку ви будете використовувати.

Можна стверджувати, що це наразі найпростіший спосіб розгорнути власну, самохостингову інстанцію Gramps Web, захищену SSL, без використання власного обладнання.

!!! info
    Зверніть увагу, що ви будете платити DigitalOcean за хостингові послуги. Проект Gramps з відкритим кодом не надає платної підтримки.

## Крок 1: Створіть обліковий запис DigitalOcean

Створіть обліковий запис на [DigitalOcean](https://www.digitalocean.com/), якщо у вас його ще немає.

## Крок 2: Створіть дроплет

- Перейдіть до [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) і натисніть "Створити дроплет Gramps Web".
- Виберіть план з принаймні 2 ГБ оперативної пам'яті.
- Налаштуйте автентифікацію для вашого дроплета.
- Натисніть "Створити дроплет".

## Крок 3: Налаштуйте доменне ім'я

Вам потрібно доменне ім'я (або піддомен). Якщо ви володієте доменом, вкажіть його на IP-адресу вашого дроплета. В іншому випадку ви можете скористатися безкоштовною послугою, такою як [DuckDNS](https://www.duckdns.org/).

## Крок 4: Увійдіть у ваш дроплет

SSH до вашого дроплета. Ви повинні побачити повідомлення "Ласкаво просимо до налаштування Gramps Web DigitalOcean 1-click app!". Якщо це не так, почекайте кілька хвилин і спробуйте ще раз (інсталяція ще не завершена).

Скрипт налаштування запитає у вас доменне ім'я (наприклад, `mygrampswebinstance.duckdns.org`) та електронну адресу (необхідну для сертифіката Let's Encrypt). Додатково він також запитає налаштування SMTP, які Gramps Web використовує для надсилання електронних листів, наприклад, для скидання паролів; залиште хост SMTP порожнім, щоб пропустити це.

Коли це буде зроблено, чекайте, поки налаштування завершиться у фоновому режимі.

## Крок 5: Запустіть Gramps Web

Ваша інстанція Gramps Web тепер повинна бути доступною за коренем вашого домену, з дійсним SSL-сертифікатом, і вона повинна показувати помічник першого запуску.

## Зміна конфігурації пізніше

Скрипт налаштування зберігає базову URL-адресу та налаштування електронної пошти у файлі `/root/letsencrypt.env` як [опції конфігурації](configuration.md), що починаються з `GRAMPSWEB_`, наприклад:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Щоб додати або змінити налаштування, відредагуйте цей файл на дроплеті та застосуйте зміни за допомогою

```bash
cd /opt/grampsweb && docker compose up -d
