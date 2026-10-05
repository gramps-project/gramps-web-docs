# Autenticação OIDC

Gramps Web suporta autenticação OpenID Connect (OIDC), permitindo que os usuários façam login usando provedores de identidade externos. Isso inclui os provedores integrados Google e Microsoft, bem como provedores OIDC personalizados como Keycloak, Authentik e Authelia.

!!! warning "GitHub como provedor OIDC não é mais suportado"
    Se você tiver `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` configurados de uma versão anterior, remova-os – eles agora são ignorados, e os usuários que anteriormente fizeram login via GitHub não podem mais fazer login dessa forma. O GitHub é um provedor OAuth 2.0, não um provedor OpenID Connect, e nunca retornou a reivindicação da qual o Gramps Web depende para identidade, portanto, nunca foi totalmente confiável.

## Visão Geral

A autenticação OIDC permite que você:

- Use provedores de identidade externos para autenticação de usuários
- Suporte múltiplos provedores de autenticação simultaneamente
- Mapeie grupos/papéis OIDC para papéis de usuário do Gramps Web
- Implemente Single Sign-On (SSO) e Single Sign-Out
- Opcionalmente desative a autenticação local por nome de usuário/senha

## Configuração

Para habilitar a autenticação OIDC, você precisa configurar as configurações apropriadas no seu arquivo de configuração do Gramps Web ou em variáveis de ambiente. Veja a página de [Configuração do Servidor](configuration.md#settings-for-oidc-authentication) para uma lista completa das configurações OIDC disponíveis.

!!! info
    Ao usar variáveis de ambiente, lembre-se de prefixar cada nome de configuração com `GRAMPSWEB_` (por exemplo, `GRAMPSWEB_OIDC_ENABLED`). Veja [Arquivo de configuração vs. variáveis de ambiente](configuration.md#configuration-file-vs-environment-variables) para detalhes.

### Provedores Integrados

Gramps Web tem suporte integrado para provedores de identidade populares. Para usá-los, você só precisa fornecer o ID do cliente e o segredo do cliente:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` e `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` e `OIDC_MICROSOFT_CLIENT_SECRET`

Você pode configurar múltiplos provedores simultaneamente. O sistema detectará automaticamente quais provedores estão disponíveis com base nos valores de configuração.

!!! tip "Microsoft: implantações de inquilino único"
    O provedor Microsoft integrado usa o endpoint multi-inquilino `/common` e aceita logins de qualquer conta Microsoft por design. Se você deseja permitir apenas usuários do seu próprio inquilino, use o [provedor OIDC personalizado](#custom-oidc-providers) com a URL do emissor específica do seu inquilino, o que mantém a validação do emissor ativa e restringe os logins a esse inquilino.

### Provedores OIDC Personalizados

Para provedores OIDC personalizados (como Keycloak, Authentik, Authelia ou um inquilino Microsoft Entra de inquilino único), use estas configurações:

Chave | Descrição
----|-------------
`OIDC_ENABLED` | Booleano, se deve habilitar a autenticação OIDC. Defina como `True`.
`OIDC_ISSUER` | URL do emissor do seu provedor. A descoberta é obtida de `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID do cliente para seu provedor OIDC
`OIDC_CLIENT_SECRET` | Segredo do cliente para seu provedor OIDC
`OIDC_NAME` | Nome de exibição personalizado (opcional, padrão é "OIDC")
`OIDC_SCOPES` | Escopos OAuth (opcional, padrão é "openid email profile")
`OIDC_USERNAME_CLAIM` | Reivindicação usada para gerar o nome de usuário (opcional, padrão é "preferred_username")
`OIDC_PKCE` | Se deve usar PKCE, veja [PKCE](#pkce) (opcional, habilitado automaticamente se o provedor suportá-lo)

### PKCE

Desde a API Gramps Web 3.23, o Gramps Web suporta [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, método `S256`) para o fluxo de código de autorização. Alguns provedores de identidade, como Pocket ID, podem ser configurados para *exigir* PKCE para um cliente e recusar logins que não o utilizem. Versões mais antigas da API Gramps Web nunca usam PKCE, então logins com tal cliente falham.

Se o PKCE é usado é decidido no login da seguinte forma:

- Se `OIDC_PKCE` está definido como `True`, o PKCE é usado.
- Se `OIDC_PKCE` está definido como `False`, o PKCE não é usado, mesmo que o provedor o suporte.
- Se `OIDC_PKCE` não está definido, ou está definido mas vazio, o PKCE é usado se o documento de descoberta do provedor (`/.well-known/openid-configuration`) listar `S256` em `code_challenge_methods_supported`, e não é usado de outra forma.

Para a maioria das configurações, você não precisa definir nada. Defina `OIDC_PKCE` como `True` se seu provedor exigir PKCE, mas não anunciar `S256` em seu documento de descoberta, e como `False` se seu provedor anunciar `S256`, mas tratá-lo incorretamente. Como variáveis de ambiente, booleanos devem estar em minúsculas (`GRAMPSWEB_OIDC_PKCE=true`), veja [Configuração](configuration.md).

Para os provedores integrados, as opções correspondentes são `OIDC_GOOGLE_PKCE` e `OIDC_MICROSOFT_PKCE`.

O verificador de código PKCE é mantido na sessão do usuário entre o redirecionamento para o provedor e o callback, portanto, isso não requer alteração nas URIs de redirecionamento.

### Configurações Multi-Árvore

Em um servidor multi-árvore, a árvore na qual o usuário está fazendo login deve ser conhecida antes que o Gramps Web redirecione para o provedor de identidade, portanto, o login começa com:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` é obrigatório em configurações multi-árvore; omiti-lo ou passar o ID de uma árvore que não existe falha no login. Em um servidor de árvore única, `tree` é opcional, mas se fornecido, deve corresponder à `TREE` configurada.

Uma identidade OIDC está vinculada exatamente a uma conta Gramps Web, que por sua vez pertence a exatamente uma árvore – fazer login contra uma árvore diferente falha em vez de mover a conta. Não há como vincular uma única identidade no provedor a contas em várias árvores; usuários que precisam de acesso a várias árvores precisam de identidades separadas no provedor (por exemplo, nomes de usuário ou contas distintas).

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

A árvore nunca faz parte da URI de redirecionamento, mesmo em servidores multi-árvore – ela viaja separadamente na sessão, uma vez que os provedores exigem que a URI de redirecionamento corresponda exatamente à registrada.

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

Se nenhuma configuração `OIDC_GROUP_*` estiver configurada, o mapeamento de papéis está desativado e os papéis são gerenciados manualmente no Gramps Web; novas contas OIDC são então criadas desativadas e precisam ser aprovadas por um proprietário ou administrador existente (veja [Primeiro Login e Inicialização](#first-login-and-bootstrapping) abaixo).

Uma vez que o mapeamento de papéis esteja configurado, a cada login:

- Se a reivindicação de papel estiver presente e o usuário pertencer a um grupo mapeado, ele recebe o papel correspondente.
- Se a reivindicação de papel estiver presente, mas o usuário não pertencer a nenhum grupo mapeado, seu papel é definido como desativado. Este é um padrão de falha fechada, não um bug – o Gramps Web não pode inferir um papel para um grupo que não reconhece.
- Se a reivindicação de papel estiver ausente do token completamente, o papel existente permanece inalterado; uma nova conta ainda tem como padrão o estado desativado.

!!! warning "O Google não envia uma reivindicação de grupos"
    Os tokens do Google nunca incluem uma reivindicação `groups`, então com o mapeamento de papéis habilitado, logins do Google caem sob "reivindicação ausente" acima: usuários existentes mantêm seu papel, mas novos usuários do Google são criados desativados e precisam de aprovação manual. Tenha isso em mente antes de habilitar o mapeamento de papéis apenas para outro provedor – isso não desativa, por si só, usuários existentes do Google.

O Microsoft Entra retorna papéis de aplicativo e associações de grupos apenas no token de ID, não do endpoint de userinfo. O Gramps Web mescla as reivindicações do token de ID na resposta de userinfo para que `OIDC_ROLE_CLAIM` funcione da mesma forma que para outros provedores; onde ambos contêm uma reivindicação, o valor de userinfo tem precedência.

## Primeiro Login e Inicialização

Novas contas criadas através do OIDC começam desativadas, a menos que o mapeamento de papéis atribua um papel a elas (veja acima). Em uma instância completamente nova, ninguém pode aprovar uma conta desativada, e se `OIDC_DISABLE_LOCAL_AUTH` também estiver habilitado, não há login por senha para recorrer.

!!! warning "Configure um grupo de proprietário/admin antes do primeiro login"
    Antes que alguém faça login via OIDC pela primeira vez, defina `OIDC_GROUP_OWNER` (ou `OIDC_GROUP_ADMIN`) e certifique-se de que o primeiro usuário pertença a esse grupo no provedor. Caso contrário, a instância não pode ser inicializada através do OIDC.

## Contas e Nomes de Usuário

Contas criadas através do OIDC recebem um nome de usuário gerado, atribuído uma vez na criação da conta e nunca alterado em logins posteriores:

- Provedores integrados: `<provider>_<claim value>`, por exemplo, `microsoft_alice@contoso.com`
- Provedor personalizado: o valor da reivindicação simples, por exemplo, `alice`

Um sufixo numérico é adicionado em caso de colisão. Não há como renomear o nome de usuário de uma conta criada pelo OIDC posteriormente; o nome completo e o endereço de e-mail, por outro lado, são atualizados em cada login.

Um login OIDC nunca se anexa a uma conta local existente que compartilha seu endereço de e-mail – isso é deliberado, uma vez que vincular contas por e-mail é um vetor de tomada de conta. Um usuário que já possui uma conta local recebe uma segunda conta separada na primeira vez que faz login via OIDC.

Endereços de e-mail do provedor são armazenados apenas se o provedor os marcar como verificados (ou omitir completamente a reivindicação `email_verified`); caso contrário, o login prossegue sem armazenar um endereço de e-mail. Como os endereços de e-mail não precisam ser exclusivos (desde a API Gramps Web 3.22), um endereço é armazenado mesmo que outra conta já o utilize.

## Logout OIDC

Gramps Web suporta Single Sign-Out (logout SSO) para provedores OIDC. `GET /api/oidc/logout/` procura o `end_session_endpoint` do provedor e o retorna como `logout_url` na resposta; é o frontend do Gramps Web que navega o navegador até lá para realmente encerrar a sessão no provedor de identidade. `logout_url` é `null` quando o provedor não tem um `end_session_endpoint`.

!!! warning "Tokens não são revogados no logout"
    Fazer logout apenas encerra a sessão do navegador; atualmente não há como revogar um token do Gramps Web que já foi emitido. Os tokens permanecem válidos até expirarem (`JWT_ACCESS_TOKEN_EXPIRES`, padrão de 15 minutos para tokens de acesso), independentemente de o usuário ter feito logout no Gramps Web ou no provedor de identidade.

## Solução de Problemas

Comece no ponto onde o login para e siga o ramo. O Gramps Web registra a razão para um callback falhado (procure por `OIDC callback error for provider` no log do servidor), que geralmente é mais específico do que a mensagem exibida no navegador.

**1. O botão de login está faltando?**

- Verifique `<BASE_URL>/api/oidc/config/`. Se `enabled` for `false` ou `providers` estiver vazio, OIDC não está configurado: `OIDC_ENABLED` deve ser `True`, e um provedor personalizado precisa de `OIDC_ISSUER` e `OIDC_CLIENT_ID`.
- Um provedor integrado (Google, Microsoft) só está registrado se tanto seu ID do cliente quanto seu segredo do cliente estiverem definidos.
- Verifique no log do servidor na inicialização por `Could not load discovery document`. Isso significa que o servidor não conseguiu acessar `<issuer>/.well-known/openid-configuration` (ou `OIDC_OPENID_CONFIG_URL`). Ele tenta novamente na primeira utilização, mas o contêiner Gramps Web deve ser capaz de resolver e acessar a URL do emissor por conta própria, não apenas seu navegador.

**2. O navegador recebe um erro logo após ser enviado ao provedor?**

O erro é mostrado pelo provedor de identidade, antes de você fazer login.

- *"redirect URI mismatch"* (ou similar): a URI de redirecionamento registrada no provedor deve corresponder exatamente, incluindo esquema, host, porta e ID do provedor. Veja [URIs de Redirecionamento Necessárias](#required-redirect-uris). Note que ela é construída a partir de `BASE_URL`, então um `BASE_URL` errado gera uma URI de redirecionamento errada.
- *Um erro de PKCE* (por exemplo `invalid_request`, "code challenge required", ou um parâmetro `code_challenge` ausente): o provedor exige PKCE, mas o Gramps Web não o enviou. Vá para [o ramo PKCE](#pkce-branch) abaixo.

**3. O provedor aceita o login, mas o Gramps Web então mostra um erro?**

- *`mismatching_state`, ou o erro menciona a sessão ou estado*: o navegador não enviou de volta o cookie de sessão que o Gramps Web definiu quando o login começou. Este cookie também carrega o verificador de código PKCE. Certifique-se de que o endereço no navegador corresponda a `BASE_URL` (mesmo esquema e host), que um proxy reverso passe cookies e o host original, e que o login seja iniciado e concluído na mesma aba ou janela do navegador.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: verifique o log do servidor para a razão subjacente. Causas comuns são um segredo de cliente errado, uma URL de emissor que não corresponde à reivindicação `iss` dos tokens, e o provedor retornando um erro para o callback (por exemplo, PKCE, veja abaixo).
- *Tentativas excessivas*: os endpoints de login e callback têm limite de taxa (5 solicitações por minuto). Aguarde um minuto e tente novamente.

**4. O login é bem-sucedido, mas você vê "Conta em Revisão", ou não pode fazer nada?**

Novas contas são criadas desativadas, a menos que o mapeamento de papéis atribua um papel. Veja [Primeiro Login e Inicialização](#first-login-and-bootstrapping) e [Comportamento do Mapeamento de Papéis](#role-mapping-behavior). Um administrador também pode ativar a conta em Configurações > Administração > Gerenciar usuários.

### Ramo PKCE

Gramps Web decide se deve usar PKCE quando um login começa (veja [PKCE](#pkce)). Para descobrir o que aconteceu na sua configuração, trabalhe através dessas perguntas em ordem:

1. **`OIDC_PKCE` está definido?** (Para provedores integrados, `OIDC_GOOGLE_PKCE` ou `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE é usado. Pule para a pergunta 3.
    - `False`: PKCE está deliberadamente desativado, e o documento de descoberta do provedor é ignorado. Se seu provedor exigir PKCE, remova a configuração ou defina como `True`.
    - Não definido, ou vazio: continue com a pergunta 2.
2. **O documento de descoberta lista `S256`?** Abra `<issuer>/.well-known/openid-configuration` e procure por `S256` em `code_challenge_methods_supported`.
    - Sim: PKCE é usado automaticamente. Continue com a pergunta 3.
    - Não, ou o campo está ausente: PKCE **não** é usado. Defina `OIDC_PKCE` como `True` se seu provedor exigir. Também verifique o log do servidor para `Could not check the provider for PKCE support`, o que significa que o documento de descoberta não pôde ser buscado e o PKCE foi, portanto, deixado de fora.
3. **O PKCE foi realmente enviado?** Inicie um login e olhe o endereço da página de login do provedor (ou o primeiro redirecionamento na aba de rede do seu navegador). Ele deve conter `code_challenge=` e `code_challenge_method=S256`.
    - Presente, mas o login ainda falha no callback: o provedor rejeitou o verificador de código. O cookie de sessão pode ter sido perdido entre o redirecionamento e o callback (veja o ramo 3 acima), ou o provedor não suporta `S256`, caso em que defina `OIDC_PKCE` como `False` se o provedor não exigir PKCE.
    - Ausente: as configurações acima não foram aplicadas. Verifique se a variável de ambiente tem o prefixo correto e um valor em minúsculas (por exemplo, `GRAMPSWEB_OIDC_PKCE=true` no Docker; `True` não é lido como um booleano), reinicie o servidor e verifique a configuração novamente.

!!! note
    Com PKCE habilitado no provedor como *opcional*, ou não habilitado de forma alguma, os logins funcionam se o Gramps Web envia ou não um desafio. Apenas provedores (ou clientes) configurados para *exigir* PKCE fazem essa configuração importar.

## Configurações de Exemplo

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
OIDC_NAME="SSO da Família"
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
EMAIL_USE_SSL=True  # Usar SSL implícito para a porta 465
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

### Pocket ID

Crie um cliente OIDC no Pocket ID com a URI de redirecionamento `<BASE_URL>/api/oidc/callback/custom` (veja [URIs de Redirecionamento Necessárias](#required-redirect-uris)). Se você habilitar "Requerer PKCE" para o cliente, nenhuma configuração adicional do Gramps Web é necessária, uma vez que o Pocket ID anuncia suporte a PKCE em seu documento de descoberta. Em seguida, configure:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Um guia de configuração OIDC feito pela comunidade para Gramps Web está disponível no [site oficial da documentação da Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

A maior parte da configuração para o Keycloak pode ser deixada em seus padrões (*Cliente → Criar cliente → Autenticação do cliente ATIVADA*).
Existem algumas exceções:

1. **Escopo OpenID** – O escopo `openid` não está incluído por padrão em todas as versões do Keycloak. Para evitar problemas, adicione-o manualmente: *Cliente → [Cliente Gramps] → Escopos do cliente → Adicionar escopo → Nome: `openid` → Definir como padrão.*
2. **Papéis** – Papéis podem ser atribuídos no nível do cliente ou globalmente por reino.

    * Se você estiver usando papéis de cliente, defina a opção de configuração `OIDC_ROLE_CLAIM` como: `resource_access.[nome-do-cliente-gramps].roles`
    * Para tornar os papéis visíveis para o Gramps, navegue até *Escopos do Cliente* (a seção de nível superior, não sob o cliente específico), então: *Papéis → Mapeadores → papéis do cliente → Adicionar ao userinfo → ATIVADO.*
