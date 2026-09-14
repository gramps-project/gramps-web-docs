# Gerenciar Usuários

A interface de gerenciamento de usuários é acessível via **Configurações > Gerenciar Usuários** (o ícone de usuário na barra superior do aplicativo). Está disponível apenas para usuários com o papel de Proprietário ou Administrador.

## Papéis de usuário

Veja [Sistema de usuários](../install_setup/users.md) para uma descrição completa dos papéis de usuário disponíveis e suas permissões.

## Visualizar e filtrar usuários

A página de gerenciar usuários mostra uma tabela de todas as contas de usuário registradas com as seguintes colunas:

- **Nome de usuário** – o nome de login
- **Nome completo** – o nome exibido
- **E-mail** – o endereço de e-mail do usuário
- **Papel** – o papel atribuído (Convidado, Membro, Contribuidor, Editor, Proprietário ou Administrador)
- **Fonte da conta** – "Senha" (conta local) ou o nome de um provedor de identidade externo (por exemplo, ao usar OIDC)

Use o campo de pesquisa e o menu suspenso de papéis no topo da tabela para filtrar a lista. Clique no botão de limpar filtro para redefinir todos os filtros.

## Editar um usuário

Clique no ícone de editar (lápis) em qualquer linha para abrir a caixa de diálogo de edição. Você pode alterar:

- Nome completo
- Endereço de e-mail
- Papel

Esta é a principal maneira de **habilitar um novo usuário auto-registrado**: mude seu papel de *desativado* para qualquer papel ativo (por exemplo, Membro ou Editor).

Os endereços de e-mail não precisam ser exclusivos (desde a API Web do Gramps 3.22), portanto, várias contas podem compartilhar o mesmo endereço.

## Adicionar um usuário manualmente

Clique no ícone de **adicionar usuário** (pessoa-adicionar) acima da tabela para criar uma nova conta de usuário diretamente, sem exigir auto-registro. Preencha o nome de usuário, nome completo, endereço de e-mail, senha e papel na caixa de diálogo e clique em **Salvar**.

## Excluir um usuário

Clique no ícone de excluir (lixeira) em qualquer linha e confirme na caixa de diálogo. Esta ação não pode ser desfeita.

!!! nota
    Para evitar que uma árvore fique sem ninguém que possa administrá-la, você não pode reduzir seu próprio papel abaixo de Proprietário ou excluir sua própria conta se você for o único Proprietário ou Administrador da árvore. Promova outro usuário a Proprietário primeiro. Um administrador ainda pode alterar ou remover o último proprietário da árvore de outro usuário, já que pode nomear um novo.

## Exportar e importar contas de usuário

Esses botões são úteis ao [migrar para uma instância diferente do Gramps Web](export.md).

- **Exportar detalhes do usuário** (ícone de download) – baixa um arquivo JSON contendo todas as contas de usuário (sem senhas, já que as senhas são armazenadas em forma criptografada).
- **Importar contas de usuário** (ícone de grupo-adicionar) – faz o upload de um arquivo JSON exportado anteriormente para criar contas de usuário em massa. Todos os usuários importados precisarão definir uma nova senha através do link "Esqueci a senha", já que as senhas não podem ser transferidas.

## Link de registro (somente configuração de múltiplas árvores)

Em uma configuração de múltiplas árvores, o link de registro para novos usuários é exibido no topo da página de gerenciar usuários. Você pode copiar este link e compartilhá-lo com pessoas que deseja convidar para registrar uma conta em sua árvore.

!!! nota
    Em uma configuração de árvore única, há um link genérico "Registrar" na página de login; o link de registro por árvore é necessário apenas em instalações de múltiplas árvores.

## Permissões de chat de IA

Se o chat de IA foi habilitado no servidor, um menu suspenso no topo da página permite que você controle quais papéis de usuário têm permissão para usar o recurso de chat:

- Todos (incluindo convidados)
- Membro e acima
- Contribuidor e acima
- Editor e acima
- Somente Proprietários e administradores
- Ninguém (desabilitar chat para todos os usuários)
