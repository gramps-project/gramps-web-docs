# Использование базы данных PostgreSQL

По умолчанию Gramps использует файловую базу данных SQLite для хранения семейного дерева. Это отлично работает для Gramps Web и рекомендуется для большинства пользователей. Однако, начиная с версии 0.3.0 API Gramps Web, также поддерживается сервер PostgreSQL с одним семейным деревом на базу данных, работающий на основе [дополнения Gramps PostgreSQL](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). С [версии 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0) также поддерживается дополнение SharedPostgreSQL, которое позволяет размещать несколько семейных деревьев в одной базе данных, что особенно полезно при использовании вместе с поддержкой [мульти-деревьев API Gramps Web](multi-tree.md).

## Настройка сервера PostgreSQL

Если вы хотите настроить новую базу данных для использования с PostgreSQLAddon, вы можете следовать [инструкциям в вики Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) для настройки сервера.

Кроме того, вы также можете использовать Docker Compose для запуска сервера PostgreSQL в контейнере на том же хосте Docker, что и Gramps Web.

Использование контейнеризированного PostgreSQL с Gramps усложняется тем, что стандартные образы PostgreSQL не имеют установленных локалей, которые необходимы Gramps для локализованной сортировки объектов. Самый простой вариант — использовать образ `gramps-postgres`, выпущенный в [этом репозитории](https://github.com/DavidMStraub/gramps-postgres-docker/). Чтобы использовать его, добавьте следующий раздел в ваш `docker-compose.yml`:
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
и также добавьте `postgres_data:` как ключ в разделе `volumes:` этого YAML файла. Этот образ содержит отдельную базу данных для генеалогических данных Gramps и для базы данных пользователей Gramps; у каждой из них могут быть отдельные пароли.

## Импорт семейного дерева Gramps

Если вы настроили сервер PostgreSQL самостоятельно, вы можете следовать [инструкциям в вики Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) для импорта семейного дерева в базу данных.

Кроме того, если вы следовали инструкциям Docker Compose выше, вы можете использовать следующую команду для импорта XML-файла Gramps, расположенного на вашем хосте Docker:

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

## Настройка Web API для работы с базой данных

Чтобы настроить Web API для работы с базой данных PostgreSQL, добавьте следующее под ключом `environment:` сервиса `grampsweb` в `docker-compose.yml`:

```yaml
      # дополнение PostgreSQL предполагает, что имя дерева
      # равно имени базы данных, и здесь используется
      # имя базы данных по умолчанию образа PostgreSQL
      TREE: postgres
      # Учетные данные должны совпадать с теми, что используются для
      # контейнера PostgreSQL
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Использование общей базы данных PostgreSQL в установке с несколькими деревьями

При использовании [настройки с несколькими деревьями](multi-tree.md) дополнение SharedPostgreSQL является удобным вариантом для размещения всех деревьев, включая вновь созданные через API, в одной базе данных PostgreSQL без ущерба для конфиденциальности или безопасности.

Для этого настройте контейнер на основе образа `gramps-postgres`, как описано выше, и просто установите параметр конфигурации `NEW_DB_BACKEND` в `sharedpostgresql`, например, через переменную окружения `GRAMPSWEB_NEW_DB_BACKEND`.

## Использование базы данных PostgreSQL для базы данных пользователей

Независимо от того, какой бэкенд базы данных используется для генеалогических данных, база данных пользователей может быть размещена в базе данных PostgreSQL, предоставив соответствующий URL базы данных. Упомянутый выше образ `gramps-postgres` содержит отдельную базу данных `grampswebuser`, которая может быть использована для этой цели. В этом случае соответствующее значение для параметра конфигурации `USER_DB_URI` будет
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Использование базы данных PostgreSQL для индекса поиска

С версии 2.4.0 API Gramps Web индекс поиска размещается либо в базе данных SQLite (по умолчанию), либо в базе данных PostgreSQL. Также для этой цели можно использовать образ `gramps-postgres`. Для индекса поиска мы можем использовать базу данных `gramps`, предоставляемую образом, независимо от того, размещаем ли мы наши генеалогические данные в PostgreSQL или нет (индекс поиска и генеалогические данные могут сосуществовать в одной базе данных). Это можно сделать, в приведенном выше примере, установив параметр конфигурации `SEARCH_INDEX_DB_URI` в
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Проблемы

В случае возникновения проблем, пожалуйста, следите за выводом журнала Gramps Web и сервера PostgreSQL. В случае использования Docker это достигается с помощью

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Если вы подозреваете, что есть проблема с Gramps Web (или документацией), пожалуйста, создайте проблему [на Github](https://github.com/gramps-project/gramps-web-api/issues).
