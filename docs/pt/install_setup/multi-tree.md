# Configuração para hospedar várias árvores

Por padrão, o Gramps Web permite acessar apenas um único banco de dados de árvore genealógica (“árvore”), especificado no arquivo de configuração.

No entanto, a partir da versão 0.7.0 do backend da API Gramps Web, também é possível servir várias árvores a partir de uma única instalação. No entanto, cada usuário está (atualmente) vinculado a uma única árvore, portanto, essa configuração não é adequada para compartilhar árvores entre usuários, mas para hospedar várias instâncias isoladas do Gramps Web.

## Habilitar suporte a múltiplas árvores

Para habilitar o suporte a múltiplas árvores, a opção de configuração `TREE` deve ser definida como um único asterisco `*`, por exemplo, em um arquivo de configuração:

```python
TREE = "*"
```

Isso tornará todas as árvores no diretório do banco de dados Gramps do servidor acessíveis (dadas permissões de usuário suficientes). O ID da árvore é o nome do subdiretório. Você pode listar as árvores existentes (nomes e IDs) com o comando

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Além disso, você deve definir a opção de configuração `MEDIA_PREFIX_TREE` como `True` para garantir que os arquivos de mídia sejam armazenados em subpastas separadas. Caso contrário, os usuários poderão acessar arquivos de mídia que pertencem a uma árvore para a qual não têm permissão!

## Adicionar uma conta de usuário a uma árvore específica

Para adicionar um usuário a uma árvore específica, basta adicionar a opção de linha de comando `--tree TREEID` ao comando de adicionar usuário. Você também pode fazer um POST para o endpoint `/users/` com a propriedade `tree` definida na carga útil JSON.

Os nomes de usuário e endereços de e-mail devem ser exclusivos em *todas* as árvores.

## Criar uma nova árvore

Para criar uma nova árvore, é recomendável fazer um POST para o endpoint `/trees/` em vez de usar o CLI do Gramps. Isso usará um UUIDv4 como ID da árvore, o que leva a uma segurança adicional, pois o nome não pode ser adivinhado. Atualmente, apenas SQLite é suportado para árvores recém-criadas.

## Autorizar

Para autorizar (buscar um token), apenas o nome de usuário e a senha são necessários, como no modo de árvore única, uma vez que o ID da árvore é conhecido para cada usuário, portanto, não há necessidade de fornecê-lo.

## Migrar arquivos de mídia existentes

Se você deseja migrar uma instância existente do Gramps Web para suporte a múltiplas árvores e está usando arquivos de mídia locais, pode simplesmente movê-los para uma subpasta da localização original com o ID da árvore como nome.

Se você estiver usando arquivos de mídia hospedados no S3, pode usar o script fornecido no diretório `scripts` do repositório `gramps-web-api`:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Isso assume que as chaves de acesso relevantes já estão definidas como variáveis de ambiente.

## Migrar banco de dados de usuários existentes

Se você deseja habilitar o suporte a múltiplas árvores e reutilizar usuários existentes, precisa atribuí-los a uma árvore específica. Você pode usar o seguinte comando fornecido para esse fim,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Personalizar o frontend

A página de registro acessível a partir da página de login não funciona em uma configuração de múltiplas árvores, uma vez que uma árvore precisa ser especificada para o registro. Portanto, é aconselhável definir `hideRegisterLink` como `true` na [configuração do frontend](frontend-config.md).
