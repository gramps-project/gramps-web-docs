# Autenticação OIDC

Gramps Web suporta autenticação OpenID Connect (OIDC), permitindo que os usuários façam login usando provedores de identidade externos. Isso inclui tanto provedores populares como Google, Microsoft e GitHub, quanto provedores OIDC personalizados como Keycloak, Authentik e outros.

## Visão Geral

A autenticação OIDC permite que você:

- Use provedores de identidade externos para autenticação de usuários
- Suporte múltiplos provedores de autenticação simultaneamente
- Mapeie grupos/papéis OIDC para papéis de usuário do Gramps Web
- Implemente Single Sign-On (SSO) e Single Sign-Out
- Opcionalmente desative a autenticação local por nome de usuário/senha

## Configuração

Para habilitar a autenticação OIDC, você precisa configurar as configurações apropriadas no seu arquivo de configuração do Gramps Web ou em variáveis de ambiente. Consulte a página de [Configuração do Servidor](configuration.md#settings-for-oidc-authentication) para uma lista completa das configurações OIDC disponíveis.

!!! info
    Ao usar variáveis de ambiente, lembre-se de prefixar cada nome de configuração com `GRAMPSWEB_` (por exemplo, `GRAMPSWEB_OIDC_ENABLED`). Consulte [Arquivo de configuração vs. variáveis de ambiente](configuration.md#configuration-file-vs-environment-variables) para detalhes.

### Provedores Integrados

Gramps Web tem suporte integrado para provedores de identidade populares. Para usá-los, você só precisa fornecer o ID do cliente e o segredo do cliente:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` e `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` e `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` e `OIDC_GITHUB_CLIENT_SECRET`

Você pode configurar múltiplos provedores simultaneamente. O sistema detectará automaticamente quais provedores estão disponíveis com base nos valores de configuração.

### Provedores OIDC Personalizados

Para provedores OIDC personalizados (como Keycloak, Authentik ou qualquer provedor compatível com OIDC padrão), use estas configurações:

Chave | Descrição
----|-------------
`OIDC_ENABLED` | Booleano, se deve habilitar a autenticação OIDC. Defina como `True`.
`OIDC_ISSUER` | URL do emissor do seu provedor
`OIDC_CLIENT_ID` | ID do cliente para o seu provedor OIDC
`OIDC_CLIENT_SECRET` | Segredo do cliente para o seu provedor OIDC
`OIDC_NAME` | Nome de exibição personalizado (opcional, padrão é "OIDC")
`OIDC_SCOPES` | Escopos OAuth (opcional, padrão é "openid email profile")

## URIs de Redirecionamento Requeridos

Ao configurar seu provedor OIDC, você deve registrar a seguinte URI de redirecionamento:

**Para provedores OIDC que suportam curingas: (por exemplo, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Onde `*` é um curinga regex. Dependendo do interpretador regex do seu provedor, isso também pode ser um `.*` ou similar. 
Certifique-se de que o regex está habilitado se o seu provedor exigir (por exemplo, Authentik).

**Para provedores OIDC que não suportam curingas: (por exemplo, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

## Mapeamento de Papéis

Gramps Web pode mapear automaticamente grupos ou papéis OIDC do seu provedor de identidade para papéis de usuário do Gramps Web. Isso permite que você gerencie permissões de usuários centralmente em seu provedor de identidade.

### Configuração

Use estas configurações para configurar o mapeamento de papéis:

Chave | Descrição
----|-------------
`OIDC_ROLE_CLAIM` | O nome da reivindicação no token OIDC que contém os grupos/papéis do usuário. Padrão é "groups"
`OIDC_GROUP_ADMIN` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Admin" do Gramps
`OIDC_GROUP_OWNER` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Owner" do Gramps
`OIDC_GROUP_EDITOR` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Editor" do Gramps
`OIDC_GROUP_CONTRIBUTOR` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Contributor" do Gramps
`OIDC_GROUP_MEMBER` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Member" do Gramps
`OIDC_GROUP_GUEST` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Guest" do Gramps

### Comportamento do Mapeamento de Papéis

- Se nenhum mapeamento de papel estiver configurado (nenhuma variável `OIDC_GROUP_*` definida), os papéis de usuário existentes são preservados
- Os usuários são atribuídos ao papel mais alto ao qual têm direito com base na filiação a grupos
- O mapeamento de papéis é sensível a maiúsculas e minúsculas por padrão (depende do seu provedor OIDC)

## Logout OIDC

Gramps Web suporta Single Sign-Out (logout SSO) para provedores OIDC. Quando um usuário faz logout do Gramps Web após se autenticar via OIDC, ele será automaticamente redirecionado para a página de logout do provedor de identidade se o provedor suportar o `end_session_endpoint`.

### Logout de Backchannel

Gramps Web implementa a especificação de Logout de Back-Channel do OpenID Connect. Isso permite que provedores de identidade notifiquem o Gramps Web quando um usuário faz logout de outro aplicativo ou do próprio provedor de identidade.

#### Configuração

Para configurar o logout de backchannel com seu provedor de identidade:

1. **Registre o endpoint de logout de backchannel** na configuração do cliente do seu provedor de identidade:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Configure seu provedor** para enviar notificações de logout. Os passos exatos dependem do seu provedor:

   **Keycloak:**

   - Na configuração do seu cliente, navegue até "Configurações"
   - Defina "URL de Logout de Backchannel" como `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Habilite "Logout de Backchannel Requer Sessão" se você quiser logout baseado em sessão

   **Authentik:**

   - Na configuração do seu provedor, adicione a URL de logout de backchannel
   - Certifique-se de que o provedor está configurado para enviar tokens de logout

!!! warning "Expiração do Token"
    Devido à natureza sem estado dos tokens JWT, o logout de backchannel atualmente registra o evento de logout, mas não pode revogar imediatamente os tokens JWT já emitidos. Os tokens permanecerão válidos até expirarem (padrão: 15 minutos para tokens de acesso).

    Para maior segurança, considere:

    - Reduzir o tempo de expiração do token JWT (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Educar os usuários a fazer logout manualmente do Gramps Web ao fazer logout do seu provedor de identidade

!!! tip "Como Funciona"
    Quando um usuário faz logout do seu provedor de identidade ou de outro aplicativo:

    1. O provedor envia um `logout_token` JWT para o endpoint de logout de backchannel do Gramps Web
    2. Gramps Web valida o token e registra o evento de logout
    3. O JTI do token de logout é adicionado a uma lista de bloqueio para prevenir ataques de repetição
    4. Quaisquer novas solicitações de API com o JWT do usuário serão negadas uma vez que os tokens expirem

## Exemplos de Configurações

### Provedor OIDC Personalizado (Keycloak)

```python
TREE="Minha Árvore Genealógica"
BASE_URL="https://minhatree.exemplo.com"
SECRET_KEY="..."  # sua chave secreta
USER_DB_URI="sqlite:////caminho/para/usuarios.sqlite"

# Configuração OIDC Personalizada
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.exemplo.com/realms/meurealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="seu-segredo-do-cliente"
OIDC_NAME="SSO da Família"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Opcional: redirecionar automaticamente para o login SSO
OIDC_DISABLE_LOCAL_AUTH=True  # Opcional: desativar login por nome de usuário/senha

# Opcional: Mapeamento de papéis de grupos OIDC para papéis do Gramps
OIDC_ROLE_CLAIM="groups"  # ou "roles" dependendo do seu provedor
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.exemplo.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@exemplo.com"
EMAIL_HOST_PASSWORD="..." # sua senha SMTP
DEFAULT_FROM_EMAIL="gramps@exemplo.com"
```

### Provedor Integrado (Google)

```python
TREE="Minha Árvore Genealógica"
BASE_URL="https://minhatree.exemplo.com"
SECRET_KEY="..."  # sua chave secreta
USER_DB_URI="sqlite:////caminho/para/usuarios.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="seu-id-do-cliente-google"
OIDC_GOOGLE_CLIENT_SECRET="seu-segredo-do-cliente-google"
```

### Múltiplos Provedores

Você pode habilitar múltiplos provedores OIDC simultaneamente:

```python
TREE="Minha Árvore Genealógica"
BASE_URL="https://minhatree.exemplo.com"
SECRET_KEY="..."  # sua chave secreta
USER_DB_URI="sqlite:////caminho/para/usuarios.sqlite"

# Provedor personalizado
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.exemplo.com/realms/meurealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="seu-segredo-do-cliente"
OIDC_NAME="SSO da Empresa"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="seu-id-do-cliente-google"
OIDC_GOOGLE_CLIENT_SECRET="seu-segredo-do-cliente-google"

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="seu-id-do-cliente-github"
OIDC_GITHUB_CLIENT_SECRET="seu-segredo-do-cliente-github"
```

### Authelia

Um guia de configuração OIDC feito pela comunidade para Gramps Web está disponível no [site oficial da documentação do Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

A maior parte da configuração para o Keycloak pode ser deixada em seus padrões (*Cliente → Criar cliente → Autenticação do cliente ATIVADA*).
Existem algumas exceções:

1. **Escopo OpenID** – O escopo `openid` não está incluído por padrão em todas as versões do Keycloak. Para evitar problemas, adicione-o manualmente: *Cliente → [Cliente Gramps] → Escopos do cliente → Adicionar escopo → Nome: `openid` → Definir como padrão.*
2. **Papéis** – Os papéis podem ser atribuídos no nível do cliente ou globalmente por realm.

    * Se você estiver usando papéis de cliente, defina a opção de configuração `OIDC_ROLE_CLAIM` como: `resource_access.[nome-do-cliente-gramps].roles`
    * Para tornar os papéis visíveis para o Gramps, navegue até *Escopos do Cliente* (a seção de nível superior, não sob o cliente específico), então: *Papéis → Mapeadores → papéis de cliente → Adicionar a userinfo → ATIVADO.*
