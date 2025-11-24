# Sistema de usuários

O Gramps Web não deve ser exposto à internet para acesso público, mas apenas por usuários autenticados. Contas de usuário podem ser criadas pelo proprietário do site via linha de comando ou interface web, ou por auto-registro e subsequente aprovação pelo proprietário do site.

## Papéis de usuário

Os seguintes papéis de usuário estão atualmente definidos.

Papel | ID do Papel | Permissões
------|-------------|------------
Convidado | 0 | Visualizar objetos não privados
Membro | 1 | Convidado + visualizar objetos privados
Contribuidor* | 2 | Membro + adicionar objetos
Editor | 3 | Contribuidor + editar e excluir objetos
Proprietário | 4 | Editor + gerenciar usuários
Admin | 5 | Proprietário + editar outras árvores em configuração de múltiplas árvores

\* Observe que o papel "Contribuidor" atualmente é suportado apenas parcialmente; por exemplo, objetos de família não podem ser adicionados, pois implicam uma modificação dos objetos de pessoa subjacentes do Gramps dos membros da família. Recomenda-se usar os outros papéis sempre que possível.

## Configurando quem pode usar o chat de IA

Se você [configurou o chat de IA](chat.md), você verá uma opção aqui para escolher quais grupos de usuários têm permissão para usar o recurso de chat.

## Gerenciando usuários

Existem duas maneiras de gerenciar usuários:

- Com permissões de proprietário usando a interface web
- Na linha de comando no servidor

A conta de proprietário necessária para acessar o aplicativo web pela primeira vez pode ser adicionada no assistente de integração que é automaticamente iniciado ao acessar o Gramps Web com um banco de dados de usuários vazio.

### Gerenciando usuários na linha de comando

Ao usar [Docker Compose](deployment.md), o comando básico é

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

O `COMMAND` pode ser `add` ou `delete`. Use `--help` para `[ARGS]` para mostrar a sintaxe e as possíveis opções de configuração.

### Aprovando usuários auto-registrados

Quando um usuário se auto-registra, ele não recebe acesso imediato. Um e-mail é enviado ao proprietário da árvore sobre o novo registro de usuário e o usuário recebe um e-mail solicitando a confirmação de seu endereço de e-mail. Confirmar com sucesso seu endereço de e-mail altera seu papel de `unconfirmed` para `disabled`. Enquanto a conta do usuário estiver em um desses dois papéis, o usuário não poderá fazer login. O proprietário da árvore deve revisar o pedido do usuário e atribuir ao usuário um papel apropriado antes que ele possa fazer login.
