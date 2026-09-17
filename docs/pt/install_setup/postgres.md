# Usando um banco de dados PostgreSQL

Por padrão, o Gramps Web armazena cada árvore genealógica em seu próprio arquivo de banco de dados SQLite. Isso não requer nenhum serviço adicional, os backups são tão simples quanto copiar arquivos, e funciona bem para a maioria das instalações, incluindo aquelas que [hospedam várias árvores](multi-tree.md).

Alternativamente, as árvores genealógicas podem ser hospedadas em um servidor PostgreSQL usando o complemento SharedPostgreSQL, que mantém todas as árvores em um único banco de dados. Isso pode fazer sentido se você já estiver executando um servidor PostgreSQL e quiser gerenciar backups e monitoramento lá, ou se você espera que muitos usuários editem ao mesmo tempo. O PostgreSQL também pode hospedar o [banco de dados de usuários](#using-a-postgresql-database-for-the-user-database) e o [índice de pesquisa](#using-a-postgresql-database-for-the-search-index), independentemente de onde as árvores genealógicas estão armazenadas.

!!! warning "Complemento PostgreSQL obsoleto"
    O complemento PostgreSQL mais antigo, que armazena uma única árvore genealógica por banco de dados, está obsoleto e não será mais suportado em uma versão futura da API do Gramps Web. Se você estiver usando-o, consulte [Movendo uma árvore do complemento PostgreSQL para SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Configurando o servidor PostgreSQL

A opção mais fácil é executar o servidor PostgreSQL em um contêiner no mesmo host Docker que o Gramps Web, usando o Docker Compose.

O Gramps precisa de locais instalados no servidor PostgreSQL para classificar objetos corretamente em diferentes idiomas, e as imagens padrão do PostgreSQL não incluem nenhum. A imagem [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) as adiciona. Para usá-la, adicione a seguinte seção ao seu `docker-compose.yml`:
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
e também adicione `postgres_data:` como chave na seção `volumes:` deste arquivo YAML. A imagem contém dois bancos de dados, cada um com seu próprio usuário e senha: `gramps` para os dados genealógicos e `grampswebuser` para o banco de dados de usuários do Gramps Web.

Se você usar seu próprio servidor PostgreSQL, crie um banco de dados chamado `gramps` no qual o usuário configurado possa criar tabelas, e certifique-se de que os locais que seus usuários precisam estejam instalados.

## Configurando o Gramps Web

Novas árvores genealógicas são criadas no banco de dados SharedPostgreSQL quando o Gramps Web é executado em [modo multi-tree](multi-tree.md) e a opção de configuração `NEW_DB_BACKEND` está definida como `sharedpostgresql`. Com a configuração do Docker Compose acima, adicione o seguinte sob a chave `environment:` do serviço `grampsweb` em `docker-compose.yml`:

```yaml
      # habilitar modo multi-tree
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # criar novas árvores no banco de dados SharedPostgreSQL
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # O host e a porta do servidor PostgreSQL. O
      # host é o nome do serviço PostgreSQL acima
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # As credenciais devem concordar com as usadas para
      # o contêiner PostgreSQL
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Consulte [Configuração](configuration.md) para uma descrição de todas essas opções. Observe que o host e a porta são salvos com cada árvore quando ela é criada, portanto, alterá-los mais tarde afeta apenas novas árvores.

## Criando uma árvore e importando dados

Para criar uma nova árvore, envie um POST para o endpoint `/trees/` conforme descrito em [Configuração para hospedagem de várias árvores](multi-tree.md#create-a-new-tree). A resposta contém o ID da nova árvore, que você precisa para [criar a conta do proprietário da árvore](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Uma vez que o proprietário da árvore tenha feito login, ele pode [importar](../administration/import.md) uma árvore genealógica existente, por exemplo, um arquivo XML do Gramps exportado do Gramps Desktop, através da interface web.

## Usando um banco de dados PostgreSQL para o banco de dados de usuários

O banco de dados de usuários é geralmente um arquivo SQLite, independentemente de onde as árvores genealógicas estão hospedadas. Para usar o PostgreSQL em vez disso, defina a opção de configuração `USER_DB_URI` para uma URL de banco de dados PostgreSQL. Com a imagem `gramps-postgres` acima, use seu banco de dados `grampswebuser`:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Usando um banco de dados PostgreSQL para o índice de pesquisa

O índice de pesquisa também é armazenado em SQLite por padrão. Para usar o PostgreSQL em vez disso, defina a opção de configuração `SEARCH_INDEX_DB_URI` para uma URL de banco de dados PostgreSQL. Com a imagem `gramps-postgres` acima, você pode usar seu banco de dados `gramps`, independentemente de suas árvores genealógicas estarem hospedadas lá também:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Movendo uma árvore do complemento PostgreSQL para SharedPostgreSQL

Instalações mais antigas podem hospedar sua árvore genealógica com o complemento PostgreSQL, que armazena uma única árvore por banco de dados e está obsoleto. Para descobrir qual complemento uma árvore usa, olhe o arquivo `database.txt` no subdiretório da árvore no diretório do banco de dados do Gramps: ele contém `postgresql` para o complemento PostgreSQL obsoleto e `sharedpostgresql` para SharedPostgreSQL.

Para mover uma árvore do complemento PostgreSQL para SharedPostgreSQL dentro da mesma instalação, mantendo suas contas de usuário e arquivos de mídia:

1. [Faça backup da sua árvore genealógica](../administration/export.md#back-up-your-family-tree) como um arquivo XML do Gramps (`.gramps`), usando uma conta que pode visualizar registros privados.
2. Altere sua configuração conforme descrito em [Configurando o Gramps Web](#configuring-gramps-web). Você pode continuar usando seu contêiner `gramps-postgres` existente.
3. [Crie uma nova árvore](multi-tree.md#create-a-new-tree) e anote seu ID da árvore.
4. Atribua suas contas de usuário existentes à nova árvore, conforme descrito em [Migrar banco de dados de usuários existentes](multi-tree.md#migrate-existing-user-database).
5. Mova seus arquivos de mídia para o local esperado para a nova árvore, conforme descrito em [Migrar arquivos de mídia existentes](multi-tree.md#migrate-existing-media-files).
6. Faça login e [importe](../administration/import.md) o arquivo XML do Gramps para a nova árvore.

Mantenha o arquivo XML do Gramps até que você tenha verificado que a nova árvore está completa.

Se você estiver se mudando para uma instalação separada do Gramps Web, siga os passos em [Mover para uma instância diferente do Gramps Web](../administration/export.md#move-to-a-different-gramps-web-instance).

## Problemas

Em caso de problemas, monitore a saída de log do Gramps Web e do servidor PostgreSQL. No caso do docker, isso é feito com

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Se você suspeitar que há um problema com o Gramps Web (ou a documentação), por favor, registre um problema [no Github](https://github.com/gramps-project/gramps-web-api/issues).
