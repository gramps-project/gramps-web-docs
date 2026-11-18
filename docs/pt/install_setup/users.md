# Sistema de usuários

Gramps Web não deve ser exposto à internet para acesso público, mas apenas por usuários autenticados. Contas de usuário podem ser criadas pelo proprietário do site via linha de comando ou interface web, ou por auto-registro e subsequente aprovação pelo proprietário do site.

## Papéis de usuário

Os seguintes papéis de usuário estão atualmente definidos.

Papel | ID do Papel | Permissões
------|-------------|------------
Convidado | 0 | Ver objetos não privados
Membro | 1 | Convidado + ver objetos privados
Contribuidor* | 2 | Membro + adicionar objetos
Editor | 3 | Contribuidor + editar e excluir objetos
Proprietário | 4 | Editor + gerenciar usuários
Admin | 5 | Proprietário + editar outras árvores em configuração de múltiplas árvores

Se um registro é privado é definido por registro, veja [Registros privados](../user-guide/privacy.md). Nada é privado por padrão, nem mesmo pessoas vivas.

\* Observe que o papel de "Contribuidor" atualmente é suportado apenas parcialmente; por exemplo, objetos familiares não podem ser adicionados, pois implicam uma modificação dos objetos de pessoa subjacentes do Gramps dos membros da família. Recomenda-se usar os outros papéis sempre que possível.

## Configurando quem pode usar o chat de IA

Se você [configurou o chat de IA](chat.md), verá uma opção aqui para escolher quais grupos de usuários têm permissão para usar o recurso de chat.

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

O `COMMAND` pode ser `add`, `set-password` ou `delete`. Use `--help` para `[ARGS]` para mostrar a sintaxe e as possíveis opções de configuração.

`set-password NAME` define uma nova senha para um usuário existente sem precisar da antiga, por exemplo, quando ninguém consegue mais fazer login e o e-mail não está configurado para redefinições de senha (Gramps Web API 3.26+). Ele solicita a senha duas vezes sem mostrá-la, para que a senha não acabe no histórico do shell. Todas as sessões do usuário são encerradas.

### Aprovando usuários auto-registrados

Quando um usuário se auto-registra, ele não recebe acesso imediato. Um e-mail é enviado ao proprietário da árvore sobre o novo registro de usuário e o usuário recebe um e-mail solicitando a confirmação de seu endereço de e-mail. Confirmar com sucesso seu endereço de e-mail altera seu papel de `unconfirmed` para `disabled`. Enquanto a conta do usuário estiver em qualquer um desses dois papéis, o usuário não pode fazer login. O proprietário da árvore deve revisar o pedido do usuário e atribuir ao usuário um papel apropriado antes que ele possa fazer login.
