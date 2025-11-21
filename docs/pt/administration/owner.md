# Criar uma conta para o proprietário da árvore

Antes de começar a usar o Gramps Web, você precisa criar uma conta para o proprietário da árvore. Se nenhuma conta de usuário existir para uma determinada árvore, um formulário será exibido para criar uma conta. O formulário depende da configuração do servidor, que pode ser para uma única árvore ou para várias árvores.

## Configuração de árvore única: criar conta de administrador

Em um servidor com configuração de árvore única, quando nenhuma conta de usuário existir ainda, abrir o Gramps Web mostrará um formulário para criar uma conta de administrador. O usuário administrador será tanto o proprietário da árvore (única) quanto o administrador da instalação. O formulário também permite configurar a configuração de e-mail necessária para notificações por e-mail (por exemplo, redefinição de senha de usuário). Se a configuração de e-mail já tiver sido adicionada por meio de um arquivo de configuração ou variáveis de ambiente no servidor, esta parte do formulário pode ser deixada em branco.

## Configuração de várias árvores: criar conta de administrador

Em uma configuração de várias árvores, o mesmo formulário para criar uma conta de administrador será exibido se nenhum usuário existir *em qualquer árvore*, ou seja, quando o servidor foi criado recentemente.

## Configuração de várias árvores: criar conta de proprietário da árvore

Em uma configuração de várias árvores, cada usuário está vinculado a uma única árvore. Mesmo que usuários já existam em outras árvores, um proprietário da árvore pode ser criado na interface da web se nenhum proprietário existir *para esta árvore* ainda.

No entanto, o formulário de criação do proprietário não será exibido automaticamente na página inicial do Gramps Web, que é a mesma para todas as árvores. Em vez disso, ele pode ser acessado em `https://my-gramps-instance/firstrun/my-tree-id`, onde `https://my-gramps-instance` é o endereço base da sua instalação do Gramps Web, e `my-tree-id` é o ID da sua árvore.

Um possível fluxo de trabalho para um administrador do site criar uma nova árvore é:

- Criar uma árvore via API REST, obtendo o ID da nova árvore
- Compartilhar o link para o formulário de criação do proprietário com o ID da árvore apropriado com o potencial proprietário da árvore

O formulário de criação do proprietário da árvore é análogo ao formulário de criação do administrador descrito acima, exceto que não permite alterar a configuração de e-mail (o que é permitido apenas para administradores).
