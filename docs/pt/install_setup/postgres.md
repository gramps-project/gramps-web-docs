# Usando um banco de dados PostgreSQL

Por padrão, o Gramps usa um banco de dados SQLite baseado em arquivo para armazenar a árvore genealógica. Isso funciona perfeitamente bem para o Gramps Web e é recomendado para a maioria dos usuários. No entanto, a partir da versão 0.3.0 da API do Gramps Web, também é suportado um servidor PostgreSQL com uma única árvore genealógica por banco de dados, alimentado pelo [Gramps PostgreSQL Addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). Desde a [versão 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0), também é suportado o Addon SharedPostgreSQL, que permite hospedar várias árvores genealógicas em um único banco de dados, o que é particularmente útil quando usado em conjunto com o suporte a [múltiplas árvores da API do Gramps Web](multi-tree.md).

## Configurando o servidor PostgreSQL

Se você deseja configurar um novo banco de dados para uso com o PostgreSQLAddon, pode seguir as [instruções na Wiki do Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) para configurar o servidor.

Alternativamente, você também pode usar o Docker Compose para executar o servidor PostgreSQL em um contêiner no mesmo host Docker que o Gramps Web.

Usar um PostgreSQL dockerizado com o Gramps é complicado apenas pelo fato de que as imagens padrão do PostgreSQL não têm locais instalados, que são, no entanto, necessários pelo Gramps para a ordenação localizada de objetos. A opção mais fácil é usar a imagem `gramps-postgres` lançada [neste repositório](https://github.com/DavidMStraub/gramps-postgres-docker/). Para usá-la, adicione a seguinte seção ao seu `docker-compose.yml`:
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
e também adicione `postgres_data:` como chave na seção `volumes:` deste arquivo YAML. Esta imagem contém um banco de dados separado para os dados genealógicos do Gramps e para o banco de dados do usuário do Gramps; cada um pode ter senhas separadas.

## Importando uma árvore genealógica do Gramps

Novamente, se você configurou o servidor PostgreSQL por conta própria, pode seguir as [instruções na Wiki do Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) para importar uma árvore genealógica para o banco de dados.

Alternativamente, se você seguiu as instruções do Docker Compose acima, pode usar o seguinte comando para importar um arquivo XML do Gramps localizado no seu host Docker:

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

## Configurando a API Web para uso com o banco de dados

Para configurar a API Web para uso com o banco de dados PostgreSQL, adicione o seguinte sob a chave `environment:` do serviço `grampsweb` em `docker-compose.yml`:

```yaml
      # o addon PostgreSQL assume que o nome da árvore é
      # igual ao nome do banco de dados e aqui o padrão
      # nome do banco de dados da imagem PostgreSQL é usado
      TREE: postgres
      # As credenciais devem concordar com as usadas para
      # o contêiner PostgreSQL
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Usando um banco de dados PostgreSQL compartilhado em uma instalação de múltiplas árvores

Ao usar uma [configuração de múltiplas árvores](multi-tree.md), o addon SharedPostgreSQL é uma opção conveniente para hospedar todas as árvores, também as recém-criadas via API, em um único banco de dados PostgreSQL sem comprometer a privacidade ou segurança.

Para conseguir isso, configure um contêiner baseado na imagem `gramps-postgres`, conforme descrito acima, e simplesmente defina a opção de configuração `NEW_DB_BACKEND` como `sharedpostgresql`, por exemplo, através da variável de ambiente `GRAMPSWEB_NEW_DB_BACKEND`.

## Usando um banco de dados PostgreSQL para o banco de dados do usuário

Independentemente de qual backend de banco de dados é usado para os dados genealógicos, o banco de dados do usuário pode ser hospedado em um banco de dados PostgreSQL fornecendo uma URL de banco de dados apropriada. A imagem Docker `gramps-postgres` mencionada acima contém um banco de dados separado `grampswebuser` que pode ser usado para esse propósito. Nesse caso, o valor apropriado para a opção de configuração `USER_DB_URI` seria
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Usando um banco de dados PostgreSQL para o índice de pesquisa

Desde a versão 2.4.0 da API do Gramps Web, o índice de pesquisa é hospedado em um banco de dados SQLite (o padrão) ou em um banco de dados PostgreSQL. Também para esse propósito, a imagem `gramps-postgres` pode ser usada. Para o índice de pesquisa, podemos usar o banco de dados `gramps` fornecido pela imagem, independentemente de estarmos hospedando nossos dados genealógicos em PostgreSQL ou não (o índice de pesquisa e os dados genealógicos podem coexistir no mesmo banco de dados). Isso pode ser alcançado, no exemplo acima, definindo a opção de configuração `SEARCH_INDEX_DB_URI` como
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Problemas

Em caso de problemas, monitore a saída de log do Gramps Web e do servidor PostgreSQL. No caso do Docker, isso é feito com

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Se você suspeitar que há um problema com o Gramps Web (ou a documentação), por favor, registre um problema [no Github](https://github.com/gramps-project/gramps-web-api/issues).
