# OIDC Аутентификация

Gramps Web поддерживает аутентификацию OpenID Connect (OIDC), позволяя пользователям входить в систему, используя внешние поставщики идентификации. Это включает как популярных поставщиков, таких как Google, Microsoft и GitHub, так и кастомные OIDC-поставщики, такие как Keycloak, Authentik и другие.

## Обзор

Аутентификация OIDC позволяет вам:

- Использовать внешние поставщики идентификации для аутентификации пользователей
- Поддерживать несколько поставщиков аутентификации одновременно
- Соответствовать OIDC группам/ролям ролям пользователей Gramps Web
- Реализовать единую аутентификацию (SSO) и единую выход (Single Sign-Out)
- При необходимости отключить локальную аутентификацию по имени пользователя/паролю

## Конфигурация

Чтобы включить аутентификацию OIDC, вам нужно настроить соответствующие параметры в вашем файле конфигурации Gramps Web или переменных окружения. См. страницу [Конфигурация сервера](configuration.md#settings-for-oidc-authentication) для полного списка доступных параметров OIDC.

!!! info
    При использовании переменных окружения не забудьте добавить префикс `GRAMPSWEB_` к каждому имени параметра (например, `GRAMPSWEB_OIDC_ENABLED`). См. [Файл конфигурации против переменных окружения](configuration.md#configuration-file-vs-environment-variables) для получения подробной информации.

### Встроенные Поставщики

Gramps Web имеет встроенную поддержку популярных поставщиков идентификации. Чтобы использовать их, вам нужно только указать идентификатор клиента и секрет клиента:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` и `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` и `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` и `OIDC_GITHUB_CLIENT_SECRET`

Вы можете настроить несколько поставщиков одновременно. Система автоматически определит, какие поставщики доступны на основе значений конфигурации.

### Кастомные OIDC Поставщики

Для кастомных OIDC поставщиков (таких как Keycloak, Authentik или любой стандартный OIDC-совместимый поставщик) используйте следующие параметры:

Ключ | Описание
----|-------------
`OIDC_ENABLED` | Логическое значение, указывающее, включена ли аутентификация OIDC. Установите в `True`.
`OIDC_ISSUER` | URL-адрес вашего поставщика
`OIDC_CLIENT_ID` | Идентификатор клиента для вашего OIDC-поставщика
`OIDC_CLIENT_SECRET` | Секрет клиента для вашего OIDC-поставщика
`OIDC_NAME` | Кастомное отображаемое имя (необязательно, по умолчанию "OIDC")
`OIDC_SCOPES` | OAuth области (необязательно, по умолчанию "openid email profile")

## Обязательные URL-адреса перенаправления

При настройке вашего OIDC-поставщика вы должны зарегистрировать следующий URL-адрес перенаправления:

**Для OIDC-поставщиков, поддерживающих подстановочные знаки: (например, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Где `*` является подстановочным знаком regex. В зависимости от интерпретатора regex вашего поставщика это также может быть `.*` или подобное.
Убедитесь, что regex включен, если ваш поставщик этого требует (например, Authentik).

**Для OIDC-поставщиков, которые не поддерживают подстановочные знаки: (например, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Сопоставление Ролей

Gramps Web может автоматически сопоставлять OIDC группы или роли от вашего поставщика идентификации с ролями пользователей Gramps Web. Это позволяет вам централизованно управлять разрешениями пользователей в вашем поставщике идентификации.

### Конфигурация

Используйте эти параметры для настройки сопоставления ролей:

Ключ | Описание
----|-------------
`OIDC_ROLE_CLAIM` | Имя утверждения в OIDC токене, которое содержит группы/роли пользователя. По умолчанию "groups"
`OIDC_GROUP_ADMIN` | Имя группы/роли от вашего OIDC-поставщика, которое соответствует роли "Admin" в Gramps
`OIDC_GROUP_OWNER` | Имя группы/роли от вашего OIDC-поставщика, которое соответствует роли "Owner" в Gramps
`OIDC_GROUP_EDITOR` | Имя группы/роли от вашего OIDC-поставщика, которое соответствует роли "Editor" в Gramps
`OIDC_GROUP_CONTRIBUTOR` | Имя группы/роли от вашего OIDC-поставщика, которое соответствует роли "Contributor" в Gramps
`OIDC_GROUP_MEMBER` | Имя группы/роли от вашего OIDC-поставщика, которое соответствует роли "Member" в Gramps
`OIDC_GROUP_GUEST` | Имя группы/роли от вашего OIDC-поставщика, которое соответствует роли "Guest" в Gramps

### Поведение Сопоставления Ролей

- Если сопоставление ролей не настроено (нет установленных переменных `OIDC_GROUP_*`), существующие роли пользователей сохраняются
- Пользователям назначается самая высокая роль, на которую они имеют право на основе их членства в группе
- Сопоставление ролей по умолчанию чувствительно к регистру (зависит от вашего OIDC-поставщика)

## Выход из OIDC

Gramps Web поддерживает единую выход (SSO logout) для OIDC-поставщиков. Когда пользователь выходит из Gramps Web после аутентификации через OIDC, он будет автоматически перенаправлен на страницу выхода поставщика идентификации, если поставщик поддерживает `end_session_endpoint`.

### Выход через Backchannel

Gramps Web реализует спецификацию OpenID Connect Back-Channel Logout. Это позволяет поставщикам идентификации уведомлять Gramps Web, когда пользователь выходит из другой программы или самого поставщика идентификации.

#### Конфигурация

Чтобы настроить выход через backchannel с вашим поставщиком идентификации:

1. **Зарегистрируйте конечную точку выхода через backchannel** в конфигурации клиента вашего поставщика идентификации:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Настройте вашего поставщика** для отправки уведомлений о выходе. Конкретные шаги зависят от вашего поставщика:

   **Keycloak:**

   - В конфигурации вашего клиента перейдите в "Настройки"
   - Установите "Backchannel Logout URL" на `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Включите "Backchannel Logout Session Required", если хотите выход на основе сессии

   **Authentik:**

   - В конфигурации вашего поставщика добавьте URL-адрес выхода через backchannel
   - Убедитесь, что поставщик настроен на отправку токенов выхода

!!! warning "Истечение Токена"
    Из-за безгосударственной природы JWT токенов, выход через backchannel в настоящее время регистрирует событие выхода, но не может немедленно отозвать уже выданные JWT токены. Токены останутся действительными до истечения срока (по умолчанию: 15 минут для токенов доступа).

    Для повышения безопасности рассмотрите возможность:

    - Сокращения времени истечения срока действия JWT токена (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Обучения пользователей вручную выходить из Gramps Web при выходе из вашего поставщика идентификации

!!! tip "Как Это Работает"
    Когда пользователь выходит из вашего поставщика идентификации или другой программы:

    1. Поставщик отправляет JWT `logout_token` на конечную точку выхода через backchannel Gramps Web
    2. Gramps Web проверяет токен и регистрирует событие выхода
    3. JTI токена выхода добавляется в черный список, чтобы предотвратить атаки повторного воспроизведения
    4. Любые новые API-запросы с JWT пользователя будут отклонены после истечения токенов

## Примеры Конфигураций

### Кастомный OIDC Поставщик (Keycloak)

```python
TREE="Мое Древо Семьи"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # ваш секретный ключ
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Кастомная OIDC Конфигурация
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="ваш-секрет-клиента"
OIDC_NAME="Семейный SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Необязательно: автоматически перенаправлять на SSO вход
OIDC_DISABLE_LOCAL_AUTH=True  # Необязательно: отключить вход по имени пользователя/паролю

# Необязательно: Сопоставление ролей от OIDC групп к ролям Gramps
OIDC_ROLE_CLAIM="groups"  # или "roles" в зависимости от вашего поставщика
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # ваш SMTP пароль
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Встроенный Поставщик (Google)

```python
TREE="Мое Древо Семьи"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # ваш секретный ключ
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="ваш-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="ваш-google-client-secret"
```

### Несколько Поставщиков

Вы можете одновременно включить несколько OIDC-поставщиков:

```python
TREE="Мое Древо Семьи"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # ваш секретный ключ
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Кастомный поставщик
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="ваш-секрет-клиента"
OIDC_NAME="Компания SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="ваш-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="ваш-google-client-secret"

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="ваш-github-client-id"
OIDC_GITHUB_CLIENT_SECRET="ваш-github-client-secret"
```

### Authelia

Руководство по настройке OIDC для Gramps Web, созданное сообществом, доступно на [официальном сайте документации Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).
