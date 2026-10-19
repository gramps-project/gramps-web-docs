# Использование базы данных PostgreSQL

По умолчанию Gramps Web хранит каждое семейное дерево в своем собственном файле базы данных SQLite. Это не требует дополнительных сервисов, резервное копирование так же просто, как копирование файлов, и это хорошо работает для большинства установок, включая те, которые [хостят несколько деревьев](multi-tree.md).

В качестве альтернативы семейные деревья могут быть размещены на сервере PostgreSQL с использованием дополнения SharedPostgreSQL, которое хранит все деревья в одной базе данных. Это может иметь смысл, если вы уже используете сервер PostgreSQL и хотите управлять резервным копированием и мониторингом там, или если вы ожидаете, что многие пользователи будут редактировать одновременно. PostgreSQL также может хостить [базу данных пользователей](#using-a-postgresql-database-for-the-user-database) и [индекс поиска](#using-a-postgresql-database-for-the-search-index), независимо от того, где хранятся семейные деревья.

!!! warning "Дополнение PostgreSQL устарело"
    Устаревшее дополнение PostgreSQL, которое хранит одно семейное дерево на базу данных, устарело с версии Gramps Web API 3.24 и больше не будет поддерживаться в Gramps Web API 4.0, потому что оно несовместимо с хостингом нескольких деревьев, что становится стандартом в этой версии. Если вы его используете, смотрите [Перемещение дерева из дополнения PostgreSQL в SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Настройка сервера PostgreSQL

Самый простой вариант — запустить сервер PostgreSQL в контейнере на том же хосте Docker, что и Gramps Web, используя Docker Compose.

Gramps требует, чтобы на сервере PostgreSQL были установлены локали для корректной сортировки объектов на разных языках, и стандартные образы PostgreSQL не включают их. Образ [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) добавляет их. Чтобы использовать его, добавьте следующий раздел в ваш `docker-compose.yml`:
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
и также добавьте `postgres_data:` в качестве ключа в разделе `volumes:` этого YAML-файла. Образ содержит две базы данных, каждая со своим пользователем и паролем: `gramps` для генеалогических данных и `grampswebuser` для базы данных пользователей Gramps Web.

Если вы используете свой собственный сервер PostgreSQL, создайте базу данных с именем `gramps`, в которой настроенный пользователь сможет создавать таблицы, и убедитесь, что установлены необходимые локали для ваших пользователей.

## Настройка Gramps Web

Новые семейные деревья создаются в базе данных SharedPostgreSQL, когда Gramps Web работает в [моде нескольких деревьев](multi-tree.md), и параметр конфигурации `NEW_DB_BACKEND` установлен на `sharedpostgresql`. С приведенной выше настройкой Docker Compose добавьте следующее под ключом `environment:` сервиса `grampsweb` в `docker-compose.yml`:

```yaml
      # включить режим нескольких деревьев
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # создавать новые деревья в базе данных SharedPostgreSQL
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # Хост и порт сервера PostgreSQL. Хост — это
      # имя сервиса PostgreSQL выше
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Учетные данные должны совпадать с теми, которые используются для
      # контейнера PostgreSQL
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Смотрите [Конфигурация](configuration.md) для описания всех этих параметров. Обратите внимание, что хост и порт сохраняются с каждым деревом при его создании, поэтому изменение их позже затрагивает только новые деревья.

## Создание дерева и импорт данных

Чтобы создать новое дерево, выполните POST-запрос к конечной точке `/trees/`, как описано в [Настройке для хостинга нескольких деревьев](multi-tree.md#create-a-new-tree). Ответ содержит ID нового дерева, который вам нужен для [создания учетной записи владельца дерева](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

После того как владелец дерева вошел в систему, он может [импортировать](../administration/import.md) существующее семейное дерево, например, файл XML Gramps, экспортированный из Gramps Desktop, через веб-интерфейс.

## Использование базы данных PostgreSQL для базы данных пользователей

База данных пользователей обычно является файлом SQLite, независимо от того, где хранятся семейные деревья. Чтобы использовать PostgreSQL вместо этого, установите параметр конфигурации `USER_DB_URI` на URL базы данных PostgreSQL. С образом `gramps-postgres` выше используйте его базу данных `grampswebuser`:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Использование базы данных PostgreSQL для индекса поиска

Индекс поиска также по умолчанию хранится в SQLite. Чтобы использовать PostgreSQL вместо этого, установите параметр конфигурации `SEARCH_INDEX_DB_URI` на URL базы данных PostgreSQL. С образом `gramps-postgres` выше вы можете использовать его базу данных `gramps`, независимо от того, хранятся ли ваши семейные деревья там:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Перемещение дерева из дополнения PostgreSQL в SharedPostgreSQL

Старые установки могут хостить свое семейное дерево с помощью дополнения PostgreSQL, которое хранит одно дерево на базу данных и устарело. Чтобы узнать, какое дополнение использует дерево, посмотрите файл `database.txt` в подкаталоге дерева в директории базы данных Gramps: он содержит `postgresql` для устаревшего дополнения PostgreSQL и `sharedpostgresql` для SharedPostgreSQL.

Чтобы переместить дерево из дополнения PostgreSQL в SharedPostgreSQL в рамках одной установки, сохраняя ваши учетные записи пользователей и медиафайлы:

1. [Создайте резервную копию вашего семейного дерева](../administration/export.md#back-up-your-family-tree) в виде файла Gramps XML (`.gramps`), используя учетную запись, которая может просматривать частные записи.
2. Измените вашу конфигурацию, как описано в [Настройке Gramps Web](#configuring-gramps-web). Вы можете продолжать использовать ваш существующий контейнер `gramps-postgres`.
3. [Создайте новое дерево](multi-tree.md#create-a-new-tree) и запомните его ID дерева.
4. Назначьте ваши существующие учетные записи пользователей новому дереву, как описано в [Миграции существующей базы данных пользователей](multi-tree.md#migrate-existing-user-database).
5. Переместите ваши медиафайлы в ожидаемое место для нового дерева, как описано в [Миграции существующих медиафайлов](multi-tree.md#migrate-existing-media-files).
6. Войдите в систему и [импортируйте](../administration/import.md) файл Gramps XML в новое дерево.

Сохраните файл Gramps XML, пока не убедитесь, что новое дерево завершено.

Если вы перемещаетесь в отдельную установку Gramps Web, следуйте шагам в [Перемещение в другую инстанцию Gramps Web](../administration/export.md#move-to-a-different-gramps-web-instance).

## Проблемы

В случае возникновения проблем, пожалуйста, следите за выводом журнала Gramps Web и сервера PostgreSQL. В случае использования Docker это достигается с помощью

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Если вы подозреваете, что есть проблема с Gramps Web (или документацией), пожалуйста, создайте проблему [на Github](https://github.com/gramps-project/gramps-web-api/issues).
