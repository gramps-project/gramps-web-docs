# Autenticação OIDC

Gramps Web suporta autenticação OpenID Connect (OIDC), permitindo que os usuários façam login usando provedores de identidade externos. Isso inclui os provedores integrados Google e Microsoft, bem como provedores OIDC personalizados como Keycloak, Authentik e Authelia.

!!! warning "GitHub como um provedor OIDC não é mais suportado"
    Se você tiver `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` configurados de uma versão anterior, remova-os – eles agora são ignorados, e os usuários que anteriormente fizeram login via GitHub não podem mais fazer login dessa forma. O GitHub é um provedor OAuth 2.0, não um provedor OpenID Connect, e nunca retornou a reivindicação da qual o Gramps Web depende para identidade, portanto, nunca foi totalmente confiável.

## Visão Geral

A autenticação OIDC permite que você:

- Use provedores de identidade externos para autenticação de usuários
- Suporte múltiplos provedores de autenticação simultaneamente
- Mapeie grupos/papéis OIDC para papéis de usuário do Gramps Web
- Implemente Single Sign-On (SSO) e Single Sign-Out
- Opcionalmente desative a autenticação local por nome de usuário/senha

## Configuração

Para habilitar a autenticação OIDC, você precisa configurar as definições apropriadas no seu arquivo de configuração do Gramps Web ou nas variáveis de ambiente. Consulte a página de [Configuração do Servidor](configuration.md#settings-for-oidc-authentication) para uma lista completa das configurações OIDC disponíveis.

!!! info
    Ao usar variáveis de ambiente, lembre-se de prefixar cada nome de configuração com `GRAMPSWEB_` (por exemplo, `GRAMPSWEB_OIDC_ENABLED`). Consulte [Arquivo de configuração vs. variáveis de ambiente](configuration.md#configuration-file-vs-environment-variables) para mais detalhes.

### Provedores Integrados

Gramps Web tem suporte integrado para provedores de identidade populares. Para usá-los, você só precisa fornecer o ID do cliente e o segredo do cliente:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` e `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` e `OIDC_MICROSOFT_CLIENT_SECRET`

Você pode configurar múltiplos provedores simultaneamente. O sistema detectará automaticamente quais provedores estão disponíveis com base nos valores de configuração.

!!! tip "Microsoft: implantações de inquilino único"
    O provedor Microsoft integrado usa o endpoint multi-inquilino `/common` e aceita logins de qualquer conta Microsoft por design. Se você deseja permitir apenas usuários do seu próprio inquilino, use o [provedor OIDC personalizado](#custom-oidc-providers) com a URL do emissor específica do seu inquilino, o que mantém a validação do emissor ativa e restringe logins a esse inquilino.

### Provedores OIDC Personalizados

Para provedores OIDC personalizados (como Keycloak, Authentik, Authelia ou um inquilino único do Microsoft Entra), use estas configurações:

Chave | Descrição
----|-------------
`OIDC_ENABLED` | Booleano, se deve habilitar a autenticação OIDC. Defina como `True`.
`OIDC_ISSUER` | URL do emissor do seu provedor. A descoberta é buscada em `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID do cliente para seu provedor OIDC
`OIDC_CLIENT_SECRET` | Segredo do cliente para seu provedor OIDC
`OIDC_NAME` | Nome de exibição personalizado (opcional, padrão é "OIDC")
`OIDC_SCOPES` | Escopos OAuth (opcional, padrão é "openid email profile")
`OIDC_USERNAME_CLAIM` | Reivindicação usada para gerar o nome de usuário (opcional, padrão é "preferred_username")

### Configurações de Múltiplas Árvores

Em um servidor de múltiplas árvores, a árvore na qual o usuário está fazendo login deve ser conhecida antes que o Gramps Web redirecione para o provedor de identidade, então o login começa com:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` é obrigatório em configurações de múltiplas árvores; omiti-lo ou passar o ID de uma árvore que não existe falha no login. Em um servidor de árvore única, `tree` é opcional, mas se fornecido, deve corresponder ao `TREE` configurado.

Uma identidade OIDC está vinculada a exatamente uma conta do Gramps Web, que por sua vez pertence a exatamente uma árvore – fazer login em uma árvore diferente falha em vez de mover a conta. Não há como vincular uma única identidade no provedor a contas em várias árvores; usuários que precisam de acesso a várias árvores precisam de identidades separadas no provedor (por exemplo, nomes de usuário ou contas distintas).

!!! warning
    Uma conta de administrador do site sem árvore associada (veja [criando uma conta de administrador](../administration/owner.md)) não pode fazer login via OIDC, uma vez que o login OIDC sempre requer uma árvore. Essas contas devem ser criadas e autenticadas com um nome de usuário/senha local.

## URIs de Redirecionamento Necessárias

Ao configurar seu provedor OIDC, você deve registrar a seguinte URI de redirecionamento:

**Para provedores OIDC que suportam curingas: (por exemplo, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Onde `*` é um curinga regex. Dependendo do interpretador regex do seu provedor, isso também pode ser um `.*` ou similar.
Certifique-se de que o regex esteja habilitado se o seu provedor exigir (por exemplo, Authentik).

**Para provedores OIDC que não suportam curingas: (por exemplo, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

A árvore nunca faz parte da URI de redirecionamento, mesmo em servidores de múltiplas árvores – ela viaja separadamente na sessão, uma vez que os provedores exigem que a URI de redirecionamento corresponda exatamente à registrada.

## Mapeamento de Papéis

Gramps Web pode mapear automaticamente grupos ou papéis OIDC do seu provedor de identidade para papéis de usuário do Gramps Web. Isso permite que você gerencie permissões de usuários centralmente em seu provedor de identidade. O mapeamento de papéis funciona da mesma forma para todos os provedores, integrados ou personalizados.

### Configuração

Use estas configurações para configurar o mapeamento de papéis:

Chave | Descrição
----|-------------
`OIDC_ROLE_CLAIM` | O nome da reivindicação no token OIDC que contém os grupos/papéis do usuário. O padrão é "groups". Caminhos com pontos são suportados, por exemplo, `realm_access.roles`.
`OIDC_GROUP_ADMIN` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Admin" do Gramps
`OIDC_GROUP_OWNER` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Owner" do Gramps
`OIDC_GROUP_EDITOR` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Editor" do Gramps
`OIDC_GROUP_CONTRIBUTOR` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Contributor" do Gramps
`OIDC_GROUP_MEMBER` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Member" do Gramps
`OIDC_GROUP_GUEST` | O nome do grupo/papel do seu provedor OIDC que mapeia para o papel "Guest" do Gramps

### Comportamento do Mapeamento de Papéis

Se nenhuma configuração `OIDC_GROUP_*` for configurada, o mapeamento de papéis está desativado e os papéis são gerenciados manualmente no Gramps Web; novas contas OIDC são então criadas desativadas e precisam ser aprovadas por um proprietário ou administrador existente (veja [Primeiro Login e Inicialização](#first-login-and-bootstrapping) abaixo).

Uma vez que o mapeamento de papéis está configurado, a cada login:

- Se a reivindicação de papel estiver presente e o usuário pertencer a um grupo mapeado, ele recebe o papel correspondente.
- Se a reivindicação de papel estiver presente, mas o usuário não pertencer a nenhum grupo mapeado, seu papel é definido como desativado. Este é um padrão fail-closed, não um bug – o Gramps Web não pode inferir um papel para um grupo que não reconhece.
- Se a reivindicação de papel estiver ausente do token completamente, o papel existente permanece inalterado; uma nova conta ainda é criada desativada.

!!! warning "O Google não envia uma reivindicação de grupos"
    Os tokens do Google nunca incluem uma reivindicação de `groups`, então, com o mapeamento de papéis habilitado, os logins do Google caem sob "reivindicação ausente" acima: usuários existentes mantêm seu papel, mas novos usuários do Google são criados desativados e precisam de aprovação manual. Tenha isso em mente antes de habilitar o mapeamento de papéis apenas para outro provedor – isso não desativa, por si só, usuários existentes do Google.

O Microsoft Entra retorna papéis de aplicativo e associações de grupo apenas no token de ID, não do endpoint de userinfo. O Gramps Web mescla as reivindicações do token de ID na resposta de userinfo para que `OIDC_ROLE_CLAIM` funcione da mesma forma que para outros provedores; onde ambos contêm uma reivindicação, o valor de userinfo tem precedência.

## Primeiro Login e Inicialização

Novas contas criadas através do OIDC começam desativadas, a menos que o mapeamento de papéis atribua um papel a elas (veja acima). Em uma nova instância, ninguém pode aprovar uma conta desativada, e se `OIDC_DISABLE_LOCAL_AUTH` também estiver habilitado, não há login por senha para recorrer.

!!! warning "Configure um grupo de proprietário/admin antes do primeiro login"
    Antes que alguém faça login via OIDC pela primeira vez, defina `OIDC_GROUP_OWNER` (ou `OIDC_GROUP_ADMIN`) e certifique-se de que o primeiro usuário pertença a esse grupo no provedor. Caso contrário, a instância não pode ser inicializada através do OIDC.

## Contas e Nomes de Usuário

Contas criadas através do OIDC recebem um nome de usuário gerado, atribuído uma vez na criação da conta e nunca alterado em logins posteriores:

- Provedores integrados: `<provider>_<valor da reivindicação>`, por exemplo, `microsoft_alice@contoso.com`
- Provedor personalizado: o valor da reivindicação simples, por exemplo, `alice`

Um sufixo numérico é adicionado em caso de colisão. Não há como renomear o nome de usuário de uma conta criada pelo OIDC posteriormente; o nome completo e o endereço de e-mail, por outro lado, são atualizados em cada login.

Um login OIDC nunca se anexa a uma conta local existente que compartilha seu endereço de e-mail – isso é deliberado, uma vez que vincular contas por e-mail é um vetor de tomada de conta. Um usuário que já possui uma conta local recebe uma segunda conta separada na primeira vez que faz login via OIDC.

Endereços de e-mail do provedor são armazenados apenas se o provedor os marcar como verificados (ou omitir completamente a reivindicação `email_verified`) e se o endereço não estiver já em uso por outra conta; caso contrário, o login prossegue sem armazenar um endereço de e-mail.

## Logout OIDC

Gramps Web suporta Single Sign-Out (logout SSO) para provedores OIDC. `GET /api/oidc/logout/` procura o `end_session_endpoint` do provedor e o retorna como `logout_url` na resposta; é o frontend do Gramps Web que navega o navegador até lá para realmente encerrar a sessão no provedor de identidade. `logout_url` é `null` quando o provedor não tem um `end_session_endpoint`.

!!! warning "Tokens não são revogados no logout"
    Fazer logout apenas encerra a sessão do navegador; atualmente não há como revogar um token do Gramps Web que já foi emitido. Os tokens permanecem válidos até expirarem (`JWT_ACCESS_TOKEN_EXPIRES`, padrão de 15 minutos para tokens de acesso), independentemente de o usuário ter feito logout no Gramps Web ou no provedor de identidade.

## Exemplos de Configurações

### Provedor OIDC Personalizado (Keycloak)

```python
TREE="Minha Árvore Familiar"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # sua chave secreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Configuração OIDC Personalizada
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="seu-segredo-do-cliente"
OIDC_NAME="SSO Familiar"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Opcional: redirecionar automaticamente para o login SSO
OIDC_DISABLE_LOCAL_AUTH=True  # Opcional: desativar login por nome de usuário/senha

# Opcional: Mapeamento de papéis de grupos OIDC para papéis do Gramps
OIDC_ROLE_CLAIM="groups"  # ou "roles" dependendo do seu provedor
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # sua senha SMTP
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Provedor Integrado (Google)

```python
TREE="Minha Árvore Familiar"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # sua chave secreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="seu-id-do-cliente-google"
OIDC_GOOGLE_CLIENT_SECRET="seu-segredo-do-cliente-google"
```

### Múltiplos Provedores

Você pode habilitar múltiplos provedores OIDC simultaneamente:

```python
TREE="Minha Árvore Familiar"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # sua chave secreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Provedor personalizado
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="seu-segredo-do-cliente"
OIDC_NAME="SSO da Empresa"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="seu-id-do-cliente-google"
OIDC_GOOGLE_CLIENT_SECRET="seu-segredo-do-cliente-google"

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="seu-id-do-cliente-microsoft"
OIDC_MICROSOFT_CLIENT_SECRET="seu-segredo-do-cliente-microsoft"
```

### Authelia

Um guia de configuração OIDC feito pela comunidade para Gramps Web está disponível no [site oficial da documentação do Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

A maior parte da configuração para o Keycloak pode ser deixada em seus padrões (*Cliente → Criar cliente → Autenticação do cliente ATIVADA*).
Existem algumas exceções:

1. **Escopo OpenID** – O escopo `openid` não está incluído por padrão em todas as versões do Keycloak. Para evitar problemas, adicione-o manualmente: *Cliente → [cliente Gramps] → Escopos do cliente → Adicionar escopo → Nome: `openid` → Definir como padrão.*
2. **Papéis** – Os papéis podem ser atribuídos tanto no nível do cliente quanto globalmente por reino.

    * Se você estiver usando papéis de cliente, defina a opção de configuração `OIDC_ROLE_CLAIM` como: `resource_access.[nome-do-cliente-gramps].roles`
    * Para tornar os papéis visíveis para o Gramps, navegue até *Escopos do Cliente* (a seção de nível superior, não sob o cliente específico), então: *Papéis → Mapeadores → papéis de cliente → Adicionar a userinfo → ATIVADO.*
