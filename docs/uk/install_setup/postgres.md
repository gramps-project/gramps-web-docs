# Використання бази даних PostgreSQL

За замовчуванням Gramps використовує файл-системну базу даних SQLite для зберігання родинного дерева. Це працює цілком добре для Gramps Web і рекомендується для більшості користувачів. Однак, починаючи з версії 0.3.0 API Gramps Web, також підтримується сервер PostgreSQL з одним родинним деревом на базу даних, що працює за допомогою [додатку Gramps PostgreSQL](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). З [версії 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0) також підтримується додаток SharedPostgreSQL, який дозволяє розміщувати кілька родинних дерев в одній базі даних, що особливо корисно при використанні разом з підтримкою [багатодерев](multi-tree.md) API Gramps Web.

## Налаштування сервера PostgreSQL

Якщо ви хочете налаштувати нову базу даних для використання з PostgreSQLAddon, ви можете слідувати [інструкціям у Вікі Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) для налаштування сервера.

Альтернативно, ви також можете використовувати Docker Compose для запуску сервера PostgreSQL в контейнері на тому ж хості Docker, що й Gramps Web.

Використання контейнеризованого PostgreSQL з Gramps ускладнюється лише тим фактом, що стандартні образи PostgreSQL не мають жодних локалей, які, однак, потрібні Gramps для локалізованої колації об'єктів. Найпростіший варіант - використовувати образ `gramps-postgres`, випущений у [цьому репозиторії](https://github.com/DavidMStraub/gramps-postgres-docker/). Щоб його використовувати, додайте наступний розділ до вашого `docker-compose.yml`:
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
також додайте `postgres_data:` як ключ під розділом `volumes:` цього YAML файлу. Цей образ містить окрему базу даних для генеалогічних даних Gramps і для бази даних користувачів Gramps; кожна з них може мати окремі паролі.

## Імпорт родинного дерева Gramps

Знову ж таки, якщо ви самостійно налаштували сервер PostgreSQL, ви можете слідувати [інструкціям у Вікі Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) для імпорту родинного дерева в базу даних.

Альтернативно, якщо ви виконали інструкції Docker Compose вище, ви можете використовувати наступну команду для імпорту XML-файлу Gramps, розташованого на вашому хості Docker:

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## Налаштування Web API для використання з базою даних

Щоб налаштувати Web API для використання з базою даних PostgreSQL, додайте наступне під ключем `environment:` сервісу `grampsweb` у `docker-compose.yml`:

```yaml
      # додаток PostgreSQL припускає, що ім'я дерева
      # дорівнює імені бази даних, і тут використовується
      # стандартне ім'я бази даних образу PostgreSQL
      TREE: postgres
      # Облікові дані повинні відповідати тим, що використовуються для
      # контейнера PostgreSQL
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Використання спільної бази даних PostgreSQL у багатодеревій установці

При використанні [багатодеревої конфігурації](multi-tree.md) додаток SharedPostgreSQL є зручним варіантом для розміщення всіх дерев, також новостворених через API, в одній базі даних PostgreSQL без компромісів у приватності чи безпеці.

Щоб досягти цього, налаштуйте контейнер на основі образу `gramps-postgres`, як описано вище, і просто встановіть параметр конфігурації `NEW_DB_BACKEND` на `sharedpostgresql`, наприклад, через змінну середовища `GRAMPSWEB_NEW_DB_BACKEND`.

## Використання бази даних PostgreSQL для бази даних користувачів

Незалежно від того, який бекенд бази даних використовується для генеалогічних даних, база даних користувачів може бути розміщена в базі даних PostgreSQL, надавши відповідний URL бази даних. Docker-образ `gramps-postgres`, згаданий вище, містить окрему базу даних `grampswebuser`, яка може бути використана для цієї мети. У цьому випадку відповідне значення для параметра конфігурації `USER_DB_URI` буде
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Використання бази даних PostgreSQL для індексу пошуку

Починаючи з версії 2.4.0 API Gramps Web, індекс пошуку розміщується або в базі даних SQLite (за замовчуванням), або в базі даних PostgreSQL. Також для цієї мети можна використовувати образ `gramps-postgres`. Для індексу пошуку ми можемо використовувати базу даних `gramps`, надану образом, незалежно від того, чи розміщуємо ми наші генеалогічні дані в PostgreSQL чи ні (індекс пошуку та генеалогічні дані можуть співіснувати в одній базі даних). Це можна досягти, у наведеному вище прикладі, встановивши параметр конфігурації `SEARCH_INDEX_DB_URI` на
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Проблеми

У разі виникнення проблем, будь ласка, слідкуйте за виходом журналу Gramps Web та сервера PostgreSQL. У випадку Docker це досягається за допомогою

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Якщо ви підозрюєте, що є проблема з Gramps Web (або документацією), будь ласка, подайте запит [на Github](https://github.com/gramps-project/gramps-web-api/issues).
