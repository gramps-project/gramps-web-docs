# 1-Click App Gramps Web у DigitalOcean

Замість [самостійного налаштування Gramps Web](deployment.md) ви також можете скористатися [1-Click App Gramps Web у DigitalOcean](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean розміщує демонстраційну версію Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="Реферальний значок DigitalOcean" /></a>

У межах процедури налаштування вам потрібно буде зареєструвати обліковий запис у DigitalOcean і вибрати платний план для «droplet» (віртуальної машини), який використовуватиметься.

Можна стверджувати, що наразі це найпростіший спосіб розгорнути власний екземпляр Gramps Web на власному хостингу, захищений за допомогою SSL, без використання власного обладнання.

!!! info
    Зверніть увагу, що ви платитимете DigitalOcean за послуги хостингу. Проєкт Gramps із відкритим кодом не надає платної підтримки.

## Крок 1: Створіть обліковий запис DigitalOcean

Створіть обліковий запис у [DigitalOcean](https://www.digitalocean.com/), якщо ви ще цього не зробили.

## Крок 2: Створіть droplet

- Перейдіть до [1-Click App Gramps Web](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) і натисніть «Create Gramps Web Droplet».
- Виберіть план щонайменше з 2 ГБ оперативної пам’яті.
- Налаштуйте автентифікацію для вашого droplet
- Натисніть «Create Droplet»

## Крок 3: Налаштуйте доменне ім’я

Вам знадобиться доменне ім’я (або субдомен). Якщо ви володієте доменом, спрямуйте його на IP-адресу вашого droplet. В іншому разі ви можете скористатися безкоштовним сервісом, наприклад [DuckDNS](https://www.duckdns.org/).

## Крок 4: Увійдіть до вашого droplet

Підключіться до вашого droplet через SSH. Ви повинні побачити повідомлення «Welcome to the Gramps Web DigitalOcean 1-click app setup!». Якщо це не так, зачекайте кілька хвилин і спробуйте ще раз (інсталяцію ще не завершено).

Скрипт налаштування попросить вас указати доменне ім’я (наприклад, `mygrampswebinstance.duckdns.org`) та адресу електронної пошти (потрібну для сертифіката Let's Encrypt). За бажанням він також попросить указати параметри SMTP, які Gramps Web використовує для надсилання електронних листів, наприклад для скидання паролів; залиште поле SMTP-хоста порожнім, щоб пропустити цей крок.

Після цього зачекайте, доки налаштування завершиться у фоновому режимі

## Крок 5: Запустіть Gramps Web

Тепер ваш екземпляр Gramps Web має бути доступний у корені вашого домену з чинним сертифікатом SSL, і ви повинні побачити помічник першого запуску.

## Подальша зміна конфігурації

Скрипт налаштування зберігає базову URL-адресу та параметри електронної пошти у файлі `/root/letsencrypt.env` як [параметри конфігурації](configuration.md) з префіксом `GRAMPSWEB_`, наприклад:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Щоб додати або змінити параметри, відредагуйте цей файл на droplet і застосуйте зміни за допомогою

```bash
cd /opt/grampsweb && docker compose up -d
```
