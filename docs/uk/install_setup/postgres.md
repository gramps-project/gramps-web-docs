# Використання бази даних PostgreSQL

За замовчуванням Gramps Web зберігає кожне родинне дерево у власному файлі бази даних SQLite. Це не потребує додаткового сервісу, резервні копії так само прості, як копіювання файлів, і це добре працює для більшості установок, включаючи ті, що [хостять кілька дерев](multi-tree.md).

Альтернативно, родинні дерева можуть бути розміщені на сервері PostgreSQL за допомогою аддона SharedPostgreSQL, який зберігає всі дерева в одній базі даних. Це може мати сенс, якщо ви вже запускаєте сервер PostgreSQL і хочете керувати резервними копіями та моніторингом там, або якщо ви очікуєте, що багато користувачів редагуватимуть одночасно. PostgreSQL також може хостити [базу даних користувачів](#using-a-postgresql-database-for-the-user-database) та [індекс пошуку](#using-a-postgresql-database-for-the-search-index), незалежно від того, де зберігаються родинні дерева.

!!! warning "Аддон PostgreSQL застарів"
    Старий аддон PostgreSQL, який зберігає одне родинне дерево на базу даних, застарів і більше не буде підтримуватися в майбутніх версіях Gramps Web API. Якщо ви його використовуєте, дивіться [Переміщення дерева з аддона PostgreSQL до SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Налаштування сервера PostgreSQL

Найпростіший варіант — запустити сервер PostgreSQL у контейнері на тому ж хості Docker, що й Gramps Web, використовуючи Docker Compose.

Gramps потребує встановлених локалей на сервері PostgreSQL, щоб правильно сортувати об'єкти різними мовами, а стандартні образи PostgreSQL не включають жодної з них. Образ [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) додає їх. Щоб його використовувати, додайте наступний розділ до вашого `docker-compose.yml`:
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
а також додайте `postgres_data:` як ключ під секцією `volumes:` цього YAML файлу. Образ містить дві бази даних, кожна з власним користувачем і паролем: `gramps` для генеалогічних даних і `grampswebuser` для бази даних користувачів Gramps Web.

Якщо ви використовуєте свій власний сервер PostgreSQL, створіть базу даних з назвою `gramps`, в якій налаштований користувач може створювати таблиці, і переконайтеся, що встановлені локалі, які потрібні вашим користувачам.

## Налаштування Gramps Web

Нові родинні дерева створюються в базі даних SharedPostgreSQL, коли Gramps Web працює в [режимі кількох дерев](multi-tree.md) і параметр конфігурації `NEW_DB_BACKEND` встановлений на `sharedpostgresql`. З налаштуванням Docker Compose вище, додайте наступне під ключем `environment:` сервісу `grampsweb` у `docker-compose.yml`:

```yaml
      # увімкнути режим кількох дерев
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # створити нові дерева в базі даних SharedPostgreSQL
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # Хост і порт сервера PostgreSQL. 
      # Хост — це назва сервісу PostgreSQL вище
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Облікові дані повинні відповідати тим, що використовуються для
      # контейнера PostgreSQL
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Дивіться [Конфігурація](configuration.md) для опису всіх цих параметрів. Зверніть увагу, що хост і порт зберігаються з кожним деревом, коли воно створюється, тому зміна їх пізніше вплине лише на нові дерева.

## Створення дерева та імпорт даних

Щоб створити нове дерево, надішліть POST запит на кінцеву точку `/trees/`, як описано в [Налаштування для хостингу кількох дерев](multi-tree.md#create-a-new-tree). Відповідь містить ID нового дерева, який вам потрібно для [створення облікового запису власника дерева](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Після того, як власник дерева увійде в систему, він може [імпортувати](../administration/import.md) існуюче родинне дерево, наприклад, файл Gramps XML, експортований з Gramps Desktop, через веб-інтерфейс.

## Використання бази даних PostgreSQL для бази даних користувачів

База даних користувачів зазвичай є файлом SQLite, незалежно від того, де розміщуються родинні дерева. Щоб використовувати PostgreSQL замість цього, встановіть параметр конфігурації `USER_DB_URI` на URL бази даних PostgreSQL. З образом `gramps-postgres`, наведеним вище, використовуйте його базу даних `grampswebuser`:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Використання бази даних PostgreSQL для індексу пошуку

Індекс пошуку також за замовчуванням зберігається в SQLite. Щоб використовувати PostgreSQL замість цього, встановіть параметр конфігурації `SEARCH_INDEX_DB_URI` на URL бази даних PostgreSQL. З образом `gramps-postgres`, наведеним вище, ви можете використовувати його базу даних `gramps`, незалежно від того, чи розміщуються ваші родинні дерева там:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Переміщення дерева з аддона PostgreSQL до SharedPostgreSQL

Старі установки можуть хостити своє родинне дерево за допомогою аддона PostgreSQL, який зберігає одне дерево на базу даних і застарів. Щоб дізнатися, який аддон використовує дерево, подивіться на файл `database.txt` у підкаталозі дерева в каталозі бази даних Gramps: він містить `postgresql` для застарілого аддона PostgreSQL і `sharedpostgresql` для SharedPostgreSQL.

Щоб перемістити дерево з аддона PostgreSQL до SharedPostgreSQL в межах однієї установки, зберігаючи ваші облікові записи користувачів і медіафайли:

1. [Зробіть резервну копію вашого родинного дерева](../administration/export.md#back-up-your-family-tree) у вигляді файлу Gramps XML (`.gramps`), використовуючи обліковий запис, який може переглядати приватні записи.
2. Змініть вашу конфігурацію, як описано в [Налаштуванні Gramps Web](#configuring-gramps-web). Ви можете продовжувати використовувати свій існуючий контейнер `gramps-postgres`.
3. [Створіть нове дерево](multi-tree.md#create-a-new-tree) і запишіть його ID дерева.
4. Призначте свої існуючі облікові записи користувачів новому дереву, як описано в [Міграція існуючої бази даних користувачів](multi-tree.md#migrate-existing-user-database).
5. Перемістіть свої медіафайли до місця, яке очікується для нового дерева, як описано в [Міграція існуючих медіафайлів](multi-tree.md#migrate-existing-media-files).
6. Увійдіть в систему та [імпортуйте](../administration/import.md) файл Gramps XML у нове дерево.

Зберігайте файл Gramps XML, поки не перевірите, що нове дерево завершене.

Якщо ви переміщаєтеся до окремої установки Gramps Web, дотримуйтесь кроків у [Переміщення до іншої інстанції Gramps Web](../administration/export.md#move-to-a-different-gramps-web-instance).

## Проблеми

У разі проблем, будь ласка, слідкуйте за виходом журналу Gramps Web та сервера PostgreSQL. У випадку з Docker це досягається за допомогою

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Якщо ви підозрюєте, що є проблема з Gramps Web (або документацією), будь ласка, подайте проблему [на Github](https://github.com/gramps-project/gramps-web-api/issues).
