# Configuração do servidor

Usando a imagem Docker padrão, toda a configuração necessária pode ser feita pelo navegador. No entanto, dependendo da implantação, pode ser necessário personalizar a configuração do servidor.

Esta página lista todos os métodos para alterar a configuração e todas as opções de configuração existentes.


## Arquivo de configuração versus variáveis de ambiente

Para as configurações, você pode usar um arquivo de configuração ou variáveis de ambiente.

Ao usar a [configuração baseada no Docker Compose](deployment.md), você pode incluir um arquivo de configuração adicionando o seguinte item de lista à chave `volumes:` no bloco `grampsweb:`:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
onde `/path/to/config.cfg` é o caminho para o arquivo de configuração no sistema de arquivos do seu servidor (o lado direito refere-se ao caminho no contêiner e não deve ser alterado).

Ao usar variáveis de ambiente,

- prefixe cada nome de configuração com `GRAMPSWEB_` para obter o nome da variável de ambiente
- use dois sublinhados para configurações de dicionários aninhados; por exemplo, `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` definirá o valor da opção de configuração `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Observe que as opções de configuração definidas pelo ambiente têm precedência sobre as do arquivo de configuração. Se ambas estiverem presentes, a variável de ambiente terá precedência.

!!! warning "Variáveis de ambiente sem prefixo estão obsoletas"
    Por razões históricas, algumas configurações — `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` e `STATIC_PATH` — ainda podem ser definidas por meio de uma variável de ambiente *sem* o prefixo `GRAMPSWEB_`. Isso está obsoleto, gera um aviso nos registros durante a inicialização e deixará de funcionar em uma versão futura. Sempre use a forma com prefixo, por exemplo, `GRAMPSWEB_TREE` em vez de `TREE`.

    Observe que isso diz respeito apenas às variáveis de ambiente. Em um arquivo de configuração, os nomes das configurações são sempre usados sem prefixo.

!!! tip "Verificar opções obsoletas"
    As opções de configuração obsoletas das quais o seu servidor ainda depende — como variáveis de ambiente sem prefixo, `SEARCH_INDEX_DIR` ou `EMAIL_USE_TLS` — são registradas como avisos durante a inicialização. Desde o Gramps Web API 3.22, elas também são listadas, juntamente com sua substituição e a versão na qual o suporte será removido, no topo da página **Informações do sistema** (acessível pelo ícone de usuário na barra superior do aplicativo) quando você estiver conectado como administrador.

    As configurações de e-mail e a URL base que o assistente de primeira execução de versões anteriores armazenava no banco de dados também são listadas ali. Defina-as na sua configuração com os valores armazenados; o aviso desaparecerá quando eles coincidirem.

## Configurações existentes
As seguintes opções de configuração existem.

### Configurações obrigatórias

Chave | Descrição
----|-------------
`TREE` | O nome do banco de dados da árvore genealógica a ser usado. Mostre as árvores disponíveis com `gramps -l`. Se não existir uma árvore com esse nome, uma nova árvore vazia será criada.
`SECRET_KEY` | A chave secreta do flask. O segredo não deve ser compartilhado publicamente. Alterá-lo invalidará todos os tokens de acesso.
`USER_DB_URI` | A URL do banco de dados de usuários. Qualquer URL compatível com SQLAlchemy é permitida.

!!! info
    Você pode gerar uma chave secreta segura, por exemplo, com o comando

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Configurações opcionais

Chave | Descrição
----|-------------
`MEDIA_BASE_DIR` | Caminho a ser usado como diretório base para arquivos de mídia, substituindo o diretório base de mídia definido no Gramps. Ao usar [S3](s3.md), deve ter o formato `s3://<bucket_name>`
`TREE_ID` | Nome do diretório do banco de dados da árvore genealógica a ser usado no modo de árvore única (quando `TREE` não está definido como `*`). Quando definido, o servidor identifica a árvore pelo nome do diretório, em vez do nome exibido, o que é mais robusto em caso de renomeações. Obrigatório se você quiser renomear a árvore pela API. O nome do diretório pode ser encontrado por meio de `GET /api/trees/-` (o campo `id`).
`SEARCH_INDEX_DB_URI` | URL do banco de dados para o índice de pesquisa. Apenas `sqlite` ou `postgresql` são permitidos como backends. O padrão é `sqlite:///indexdir/search_index.db`, criando um arquivo SQLite na pasta `indexdir`, relativa ao caminho em que o script é executado
`SEARCH_INDEX_DIR` | **Obsoleto** (use `SEARCH_INDEX_DB_URI`). Diretório que contém o índice de pesquisa. Se definido enquanto `SEARCH_INDEX_DB_URI` não estiver definido, a URL do índice de pesquisa será derivada como `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Caminho a partir do qual servir arquivos estáticos (por exemplo, um frontend web estático)
`BASE_URL` | URL base na qual a API pode ser acessada (por exemplo, `https://mygramps.mydomain.com/`). Isso é necessário, por exemplo, para criar links corretos de redefinição de senha. O Web Push também exige uma URL HTTPS acessível publicamente; o padrão `http://localhost/` desativa o Web Push. Ao configurar essa opção pelo ambiente, use `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Origens das quais as solicitações CORS são permitidas. Por padrão, todas são proibidas. Use `"*"` para permitir solicitações de qualquer domínio.
`EMAIL_HOST` | Host do servidor SMTP (por exemplo, para enviar e-mails de redefinição de senha)
`EMAIL_PORT` | Porta do servidor SMTP. O padrão é 465
`EMAIL_HOST_USER` | Nome de usuário do servidor SMTP
`EMAIL_HOST_PASSWORD` | Senha do servidor SMTP
`EMAIL_USE_TLS` | **Obsoleto** (use `EMAIL_USE_SSL` ou `EMAIL_USE_STARTTLS`). Booleano que indica se TLS deve ser usado para enviar e-mails. O padrão é `True`. Ao usar STARTTLS, defina como `False` e use uma porta diferente de 25.
`EMAIL_USE_SSL` | Booleano que indica se SSL/TLS implícito deve ser usado para SMTP (v3.6.0+). O padrão é `True` se `EMAIL_USE_TLS` não estiver explicitamente definido. Normalmente usado com a porta 465.
`EMAIL_USE_STARTTLS` | Booleano que indica se STARTTLS explícito deve ser usado para SMTP (v3.6.0+). O padrão é `False`. Normalmente usado com a porta 587 ou 25.
`DEFAULT_FROM_EMAIL` | Endereço "De" para e-mails automatizados
`THUMBNAIL_CACHE_CONFIG` | Dicionário com configurações para o cache de miniaturas. Consulte [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para ver as configurações possíveis.
`REQUEST_CACHE_CONFIG` | Dicionário com configurações para o cache de solicitações. Consulte [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para ver as configurações possíveis.
`PERSISTENT_CACHE_CONFIG` | Dicionário com configurações para o cache persistente, usado, por exemplo, para telemetria. Consulte [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para ver as configurações possíveis.
`CELERY_CONFIG` | Configurações da fila de tarefas em segundo plano do Celery. Consulte [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) para ver as configurações possíveis.
`REPORT_DIR` | Diretório temporário onde será armazenada a saída da execução dos relatórios do Gramps
`EXPORT_DIR` | Diretório temporário onde será armazenada a saída da exportação do banco de dados do Gramps
`BACKUP_DIR` | Diretório onde os [backups](../administration/backups.md) são armazenados, em um subdiretório por árvore (v3.24.0+). Se não definido (o padrão), os backups não poderão ser armazenados no servidor, mas ainda poderão ser restaurados a partir de um arquivo enviado. Use um local persistente, por exemplo, um volume Docker, e preferencialmente um local que também tenha backup ou seja sincronizado em outro lugar.
`BACKUP_KEEP` | Número de backups armazenados mantidos por árvore; os mais antigos são excluídos quando um novo backup é criado (v3.24.0+). O padrão é `5`
`RATE_LIMIT_BACKUP` | Limite de frequência para criação de backups, por árvore (v3.24.0+). O padrão é `"10 per day"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Limite de frequência para criação de arquivos de mídia na página Exportar. O padrão é `"1 per hour"`
`REGISTRATION_DISABLED` | Se `True`, impede o registro de novos usuários (o padrão é `False`). Desde o Gramps Web API 3.26, a página de login também oculta o link de registro.
`PROXY_FIX_X_FOR` | Número de proxies reversos confiáveis à frente do Gramps Web (v3.26.0+). Defina como `1` atrás de um único proxy reverso para que os limites de frequência sejam aplicados por cliente, em vez de a todos os usuários em conjunto. O padrão é `0`. Defina-o somente se o servidor for acessível exclusivamente por meio desses proxies.
`DISABLE_TELEMETRY` | Se `True`, desativa a telemetria de estatísticas (o padrão é `False`). Consulte [telemetria](telemetry.md) para obter detalhes.
`PILLOW_MAX_IMAGE_PIXELS` | Define o parâmetro `PIL.Image.MAX_IMAGE_PIXELS`, que indica o número de pixels que a imagem processada pode conter. Consulte a [documentação](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) para obter detalhes.
`MAX_THUMBNAIL_FILE_BYTES` | Define um tamanho máximo rígido para arquivos de miniaturas. O padrão é `50 * 1024 * 1024` (50 MB). Aumentá-lo pode elevar muito o uso de memória e causar falhas por falta de memória ou perda de dados se arquivos grandes forem descompactados na memória.


!!! info
    Ao usar variáveis de ambiente para a configuração, as opções booleanas, como `EMAIL_USE_SSL`, devem ser a string `true` ou `false` (com distinção entre maiúsculas e minúsculas!).


### Configurações para bancos de dados PostgreSQL

Essas configurações são obrigatórias se as suas árvores genealógicas estiverem hospedadas em um [banco de dados PostgreSQL](postgres.md) usando o complemento SharedPostgreSQL.

Chave | Descrição
----|-------------
`POSTGRES_USER` | Nome de usuário para a conexão com o banco de dados
`POSTGRES_PASSWORD` | Senha do usuário do banco de dados


### Configurações relevantes para hospedar várias árvores

As seguintes configurações são relevantes ao [hospedar várias árvores](multi-tree.md).


Chave | Descrição
----|-------------
`MEDIA_PREFIX_TREE` | Booleano que indica se deve ser usada uma subpasta separada para os arquivos de mídia de cada árvore. O padrão é `False`, mas é altamente recomendável usar `True` em uma configuração com várias árvores
`NEW_DB_BACKEND` | Backend de banco de dados a ser usado para árvores genealógicas recém-criadas. Deve ser `sqlite` ou `sharedpostgresql`. O padrão é `sqlite`. O valor `postgresql` ainda é aceito, mas está obsoleto, pois o backend PostgreSQL será removido no Gramps Web API 4.0.
`POSTGRES_HOST` | Nome do host do servidor PostgreSQL usado para criar novas árvores ao usar uma configuração com várias árvores e o backend SharedPostgreSQL
`POSTGRES_PORT` | Porta do servidor PostgreSQL usada para criar novas árvores ao usar uma configuração com várias árvores e o backend SharedPostgreSQL


### Configurações para autenticação OIDC

Essas configurações são necessárias se você quiser usar a autenticação OpenID Connect (OIDC) com provedores externos. Para obter instruções detalhadas de configuração e exemplos, consulte [Autenticação OIDC](oidc.md).

Chave | Descrição
----|-------------
`OIDC_ENABLED` | Booleano que indica se a autenticação OIDC deve ser ativada. O padrão é `False`.
`OIDC_ISSUER` | URL do emissor do provedor OIDC (para provedores OIDC personalizados)
`OIDC_CLIENT_ID` | ID do cliente OAuth (para provedores OIDC personalizados)
`OIDC_CLIENT_SECRET` | Segredo do cliente OAuth (para provedores OIDC personalizados)
`OIDC_NAME` | Nome de exibição personalizado do provedor. O padrão é "OIDC"
`OIDC_SCOPES` | Escopos OAuth. O padrão é "openid email profile"
`OIDC_USERNAME_CLAIM` | Claim a ser usado para o nome de usuário. O padrão é "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Opcional: URL do endpoint de configuração do OpenID Connect (se não estiver usando o padrão `/.well-known/openid-configuration`)
`OIDC_PKCE` | Booleano que indica se PKCE deve ser usado. Se não definido, PKCE será usado quando o documento de descoberta do provedor listar `S256`. Consulte [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Booleano que indica se a autenticação local por nome de usuário/senha deve ser desativada. O padrão é `False`
`OIDC_AUTO_REDIRECT` | Booleano que indica se deve haver redirecionamento automático para OIDC quando apenas um provedor estiver configurado. O padrão é `False`
`OIDC_ALLOWED_REDIRECT_URIS` | Lista de URIs `https` nas quais aplicativos nativos podem receber o resultado do login (v3.26.0+), definida como uma lista JSON em uma variável de ambiente. Vazia por padrão. Necessária somente se a documentação de um aplicativo nativo solicitar isso. Consulte [Aplicativos nativos](oidc.md#native-apps)

#### Provedores OIDC integrados

Para provedores integrados (Google, Microsoft), use estas configurações:

Chave | Descrição
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID do cliente para o OAuth do Google
`OIDC_GOOGLE_CLIENT_SECRET` | Segredo do cliente para o OAuth do Google
`OIDC_MICROSOFT_CLIENT_ID` | ID do cliente para o OAuth da Microsoft
`OIDC_MICROSOFT_CLIENT_SECRET` | Segredo do cliente para o OAuth da Microsoft
`OIDC_GOOGLE_PKCE` | Booleano, configuração de PKCE para o Google; consulte [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Booleano, configuração de PKCE para a Microsoft; consulte [PKCE](oidc.md#pkce)

#### Mapeamento de funções OIDC

Essas configurações permitem mapear grupos/funções OIDC do seu provedor de identidade para funções de usuário do Gramps Web:

Chave | Descrição
----|-------------
`OIDC_ROLE_CLAIM` | Nome do claim no token OIDC que contém os grupos/funções do usuário. O padrão é "groups"
`OIDC_GROUP_ADMIN` | Nome do grupo/função do seu provedor OIDC que corresponde à função "Admin" do Gramps
`OIDC_GROUP_OWNER` | Nome do grupo/função do seu provedor OIDC que corresponde à função "Owner" do Gramps
`OIDC_GROUP_EDITOR` | Nome do grupo/função do seu provedor OIDC que corresponde à função "Editor" do Gramps
`OIDC_GROUP_CONTRIBUTOR` | Nome do grupo/função do seu provedor OIDC que corresponde à função "Contributor" do Gramps
`OIDC_GROUP_MEMBER` | Nome do grupo/função do seu provedor OIDC que corresponde à função "Member" do Gramps
`OIDC_GROUP_GUEST` | Nome do grupo/função do seu provedor OIDC que corresponde à função "Guest" do Gramps

### Configurações somente para recursos de IA

Essas configurações são necessárias se você quiser usar o chat de IA. Consulte [Configuração do chat de IA](chat.md) para obter detalhes.

!!! note
    As configurações `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` e `VECTOR_EMBEDDING_API_KEY` para pesquisa semântica são ignoradas desde o Gramps Web API 3.25, que removeu a pesquisa semântica. O chat de IA precisa apenas de `LLM_MODEL`.

Chave | Descrição
----|-------------
`LLM_BASE_URL` | URL base para a API de chat compatível com OpenAI. O padrão é `None`, que usa a API da OpenAI.
`LLM_MODEL` | Modelo a ser usado para a API de chat compatível com OpenAI. Se não definido (o padrão), o chat é desativado. A partir da v3.6.0, o assistente de IA usa Pydantic AI com recursos de chamada de ferramentas.
`LLM_MAX_OUTPUT_TOKENS` | Número máximo de tokens que o modelo pode gerar em uma única resposta. Não definido por padrão, deixando o limite a cargo do servidor do modelo. Útil para servidores de modelos sem limite próprio, nos quais uma resposta poderia continuar indefinidamente.
`LLM_MAX_CONTEXT_LENGTH` | Limite de caracteres para o contexto da árvore genealógica fornecido ao LLM. O padrão é 50000.
`LLM_SYSTEM_PROMPT` | Prompt de sistema personalizado para o assistente de chat do LLM (v3.6.0+). Se não definido, usa o prompt padrão otimizado para genealogia.
`LLM_VISION` | Booleano que indica se os usuários podem anexar imagens às suas perguntas (v3.26.0+). Ative-o somente se o modelo aceitar imagens. O padrão é `False`. Consulte [Imagens nas perguntas](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | Booleano que indica se o assistente pode propor alterações na árvore para que os usuários as revisem e apliquem (v3.26.0+). O padrão é `False`. Consulte [Permitir que o assistente proponha alterações](chat.md#letting-the-assistant-propose-changes)


## Exemplo de arquivo de configuração

Um arquivo de configuração mínimo para produção poderia ser assim:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # sua chave secreta
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Use SSL implícito para a porta 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # sua senha SMTP
DEFAULT_FROM_EMAIL="gramps@example.com"
```
