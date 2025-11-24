# Configuração do Servidor

Usando a imagem padrão do Docker, toda a configuração necessária pode ser feita a partir do navegador. No entanto, dependendo da implantação, pode ser necessário personalizar a configuração do servidor.

Esta página lista todos os métodos para alterar a configuração e todas as opções de configuração existentes.

## Arquivo de configuração vs. variáveis de ambiente

Para as configurações, você pode usar um arquivo de configuração ou variáveis de ambiente.

Quando você usa a [configuração baseada em Docker Compose](deployment.md), pode incluir um arquivo de configuração adicionando o seguinte item à lista sob a chave `volumes:` no bloco `grampsweb:`:

```yaml
      - /caminho/para/config.cfg:/app/config/config.cfg
```
onde `/caminho/para/config.cfg` é o caminho para o arquivo de configuração no sistema de arquivos do seu servidor (o lado direito refere-se ao caminho no contêiner e não deve ser alterado).

Ao usar variáveis de ambiente,

- prefixe cada nome de configuração com `GRAMPSWEB_` para obter o nome da variável de ambiente
- Use sublinhados duplos para configurações de dicionário aninhadas, por exemplo, `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` definirá o valor da opção de configuração `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Observe que as opções de configuração definidas via ambiente têm precedência sobre as que estão no arquivo de configuração. Se ambas estiverem presentes, a variável de ambiente "vence".

## Configurações de configuração existentes
As seguintes opções de configuração existem.

### Configurações obrigatórias

Chave | Descrição
----|-------------
`TREE` | O nome do banco de dados da árvore genealógica a ser usado. Mostre as árvores disponíveis com `gramps -l`. Se uma árvore com esse nome não existir, uma nova vazia será criada.
`SECRET_KEY` | A chave secreta para o Flask. A chave secreta não deve ser compartilhada publicamente. Alterá-la invalidará todos os tokens de acesso.
`USER_DB_URI` | A URL do banco de dados do usuário. Qualquer URL compatível com SQLAlchemy é permitida.

!!! info
    Você pode gerar uma chave secreta segura, por exemplo, com o comando

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Configurações opcionais

Chave | Descrição
----|-------------
`MEDIA_BASE_DIR` | Caminho a ser usado como diretório base para arquivos de mídia, substituindo o diretório base de mídia definido no Gramps. Ao usar [S3](s3.md), deve ter a forma `s3://<bucket_name>`
`SEARCH_INDEX_DB_URI` | URL do banco de dados para o índice de pesquisa. Apenas `sqlite` ou `postgresql` são permitidos como backends. O padrão é `sqlite:///indexdir/search_index.db`, criando um arquivo SQLite na pasta `indexdir` em relação ao caminho onde o script é executado
`STATIC_PATH` | Caminho para servir arquivos estáticos (por exemplo, um frontend web estático)
`BASE_URL` | URL base onde a API pode ser acessada (por exemplo, `https://mygramps.mydomain.com/`). Isso é necessário, por exemplo, para construir links corretos de redefinição de senha
`CORS_ORIGINS` | Origens de onde as solicitações CORS são permitidas. Por padrão, todas são desautorizadas. Use `"*"` para permitir solicitações de qualquer domínio.
`EMAIL_HOST` | Host do servidor SMTP (por exemplo, para enviar e-mails de redefinição de senha)
`EMAIL_PORT` | Porta do servidor SMTP. O padrão é 465
`EMAIL_HOST_USER` | Nome de usuário do servidor SMTP
`EMAIL_HOST_PASSWORD` | Senha do servidor SMTP
`EMAIL_USE_TLS` | Booleano, se deve usar TLS para enviar e-mails. O padrão é `True`. Ao usar STARTTLS, defina isso como `False` e use uma porta diferente de 25.
`DEFAULT_FROM_EMAIL` | Endereço "De" para e-mails automatizados
`THUMBNAIL_CACHE_CONFIG` | Dicionário com configurações para o cache de miniaturas. Veja [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para possíveis configurações.
`REQUEST_CACHE_CONFIG` | Dicionário com configurações para o cache de solicitações. Veja [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para possíveis configurações.
`PERSISTENT_CACHE_CONFIG` | Dicionário com configurações para o cache persistente, usado, por exemplo, para telemetria. Veja [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para possíveis configurações.
`CELERY_CONFIG` | Configurações para a fila de tarefas em segundo plano Celery. Veja [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) para possíveis configurações.
`REPORT_DIR` | Diretório temporário onde a saída da execução de relatórios do Gramps será armazenada
`EXPORT_DIR` | Diretório temporário onde a saída da exportação do banco de dados do Gramps será armazenada
`REGISTRATION_DISABLED` | Se `True`, desabilita o registro de novos usuários (padrão `False`)
`DISABLE_TELEMETRY` | Se `True`, desabilita a telemetria de estatísticas (padrão `False`). Veja [telemetria](telemetry.md) para detalhes.

!!! info
    Ao usar variáveis de ambiente para configuração, opções booleanas como `EMAIL_USE_TLS` devem ser a string `true` ou `false` (case sensitive!).

### Configurações apenas para banco de dados backend PostgreSQL

Isso é necessário se você configurou seu banco de dados Gramps para trabalhar com o [complemento PostgreSQL](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL).

Chave | Descrição
----|-------------
`POSTGRES_USER` | O nome de usuário para a conexão com o banco de dados
`POSTGRES_PASSWORD` | A senha para o usuário do banco de dados

### Configurações relevantes para hospedagem de múltiplas árvores

As seguintes configurações são relevantes ao [hospedar múltiplas árvores](multi-tree.md).

Chave | Descrição
----|-------------
`MEDIA_PREFIX_TREE` | Booleano, se deve ou não usar uma subpasta separada para os arquivos de mídia de cada árvore. O padrão é `False`, mas é fortemente recomendado usar `True` em uma configuração de múltiplas árvores
`NEW_DB_BACKEND` | O backend do banco de dados a ser usado para novas árvores genealógicas criadas. Deve ser um dos `sqlite`, `postgresql` ou `sharedpostgresql`. O padrão é `sqlite`.
`POSTGRES_HOST` | O nome do host do servidor PostgreSQL usado para criar novas árvores ao usar uma configuração de múltiplas árvores com o backend SharedPostgreSQL
`POSTGRES_PORT` | A porta do servidor PostgreSQL usada para criar novas árvores ao usar uma configuração de múltiplas árvores com o backend SharedPostgreSQL

### Configurações para autenticação OIDC

Essas configurações são necessárias se você deseja usar autenticação OpenID Connect (OIDC) com provedores externos. Para instruções detalhadas de configuração e exemplos, veja [Autenticação OIDC](oidc.md).

Chave | Descrição
----|-------------
`OIDC_ENABLED` | Booleano, se deve habilitar a autenticação OIDC. O padrão é `False`.
`OIDC_ISSUER` | URL do emissor do provedor OIDC (para provedores OIDC personalizados)
`OIDC_CLIENT_ID` | ID do cliente OAuth (para provedores OIDC personalizados)
`OIDC_CLIENT_SECRET` | Segredo do cliente OAuth (para provedores OIDC personalizados)
`OIDC_NAME` | Nome de exibição personalizado para o provedor. O padrão é "OIDC"
`OIDC_SCOPES` | Escopos OAuth. O padrão é "openid email profile"
`OIDC_USERNAME_CLAIM` | A reivindicação a ser usada para o nome de usuário. O padrão é "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Opcional: URL para o endpoint de configuração OpenID Connect (se não estiver usando o padrão `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Booleano, se deve desabilitar a autenticação local por nome de usuário/senha. O padrão é `False`
`OIDC_AUTO_REDIRECT` | Booleano, se deve redirecionar automaticamente para OIDC quando apenas um provedor estiver configurado. O padrão é `False`

#### Provedores OIDC integrados

Para provedores integrados (Google, Microsoft, GitHub), use estas configurações:

Chave | Descrição
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID do cliente para Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Segredo do cliente para Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID do cliente para Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Segredo do cliente para Microsoft OAuth
`OIDC_GITHUB_CLIENT_ID` | ID do cliente para GitHub OAuth
`OIDC_GITHUB_CLIENT_SECRET` | Segredo do cliente para GitHub OAuth

#### Mapeamento de Funções OIDC

Essas configurações permitem mapear grupos/funções OIDC do seu provedor de identidade para funções de usuário do Gramps Web:

Chave | Descrição
----|-------------
`OIDC_ROLE_CLAIM` | O nome da reivindicação no token OIDC que contém os grupos/funções do usuário. O padrão é "groups"
`OIDC_GROUP_ADMIN` | O nome do grupo/função do seu provedor OIDC que mapeia para a função "Admin" do Gramps
`OIDC_GROUP_OWNER` | O nome do grupo/função do seu provedor OIDC que mapeia para a função "Owner" do Gramps
`OIDC_GROUP_EDITOR` | O nome do grupo/função do seu provedor OIDC que mapeia para a função "Editor" do Gramps
`OIDC_GROUP_CONTRIBUTOR` | O nome do grupo/função do seu provedor OIDC que mapeia para a função "Contributor" do Gramps
`OIDC_GROUP_MEMBER` | O nome do grupo/função do seu provedor OIDC que mapeia para a função "Member" do Gramps
`OIDC_GROUP_GUEST` | O nome do grupo/função do seu provedor OIDC que mapeia para a função "Guest" do Gramps

### Configurações apenas para recursos de IA

Essas configurações são necessárias se você deseja usar recursos impulsionados por IA, como chat ou busca semântica.

Chave | Descrição
----|-------------
`LLM_BASE_URL` | URL base para a API de chat compatível com OpenAI. O padrão é `None`, que usa a API da OpenAI.
`LLM_MODEL` | O modelo a ser usado para a API de chat compatível com OpenAI. Se não definido (o padrão), o chat é desativado.
`VECTOR_EMBEDDING_MODEL` | O modelo [Sentence Transformers](https://sbert.net/) a ser usado para embeddings vetoriais de busca semântica. Se não definido (o padrão), a busca semântica e o chat são desativados.
`LLM_MAX_CONTEXT_LENGTH` | Limite de caracteres para o contexto da árvore genealógica fornecido ao LLM. O padrão é 50000.

## Exemplo de arquivo de configuração

Um arquivo de configuração mínimo para produção pode parecer assim:
```python
TREE="Minha Árvore Genealógica"
BASE_URL="https://minhatree.exemplo.com"
SECRET_KEY="..."  # sua chave secreta
USER_DB_URI="sqlite:////caminho/para/users.sqlite"
EMAIL_HOST="mail.exemplo.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@exemplo.com"
EMAIL_HOST_PASSWORD="..." # sua senha SMTP
DEFAULT_FROM_EMAIL="gramps@exemplo.com"
