# Use o gerenciamento de tarefas embutido

O Gramps Web contém uma ferramenta de gerenciamento de tarefas genealógicas embutida. Ela é destinada a permitir que os pesquisadores planejem e priorizem, mas também documentem suas tarefas. É por isso que as tarefas são representadas como fontes no banco de dados do Gramps. Após a conclusão de uma tarefa, o conteúdo associado pode servir como uma fonte documentando o processo de pesquisa.

## Noções básicas sobre tarefas

As tarefas têm as seguintes propriedades:

- Status. Isso pode ser "Aberto", "Em Andamento", "Bloqueado" ou "Concluído"
- Prioridade. Isso pode ser "Baixa", "Média" ou "Alta"
- Tags. Os rótulos são tags normais do Gramps da fonte subjacente. (Observe que todas as tarefas têm adicionalmente o rótulo `ToDo` para identificá-las como tarefas, mas esse rótulo é ocultado na lista de tarefas para evitar desordem.)
- Título. Exibido na lista de tarefas
- Descrição. Um campo de texto rico que pode ser usado para descrever a declaração do problema, mas também documentar qualquer progresso feito
- Mídia. Quaisquer arquivos de mídia anexados à tarefa

## Criar uma tarefa

Como as tarefas são objetos normais do Gramps, elas podem ser editadas ou criadas pelo mesmo grupo de usuários que pode editar ou criar outros objetos (como pessoas ou eventos).

Para criar uma tarefa, clique no botão + na página da lista de tarefas. Insira pelo menos um título e, opcionalmente, uma prioridade, uma descrição, anexos e tags. O status será sempre "Aberto" na criação.

## A lista de tarefas

A lista de tarefas é ordenada por status – tarefas concluídas por último – e dentro de cada status por prioridade, da mais alta para a mais baixa.

Clique em uma tarefa para abri-la. Usuários com permissões de edição também podem clicar no ícone de status de uma tarefa para mudar seu status diretamente na lista, por exemplo, para marcá-la como concluída.

O botão **filtro** acima da lista filtra as tarefas por tag, com uma expressão [GOQL](goql.md) ou com o [filtro avançado](lists.md#advanced-filter).

## Editar uma tarefa

A página da tarefa não possui um "modo de edição" separado como outros objetos do Gramps:

- Clique no título para editá-lo. Pressione Enter, clique em ✓ ou clique em outro lugar para salvar; pressione Escape ou clique em ✕ para cancelar.
- As alterações no status e na prioridade são aplicadas imediatamente.
- Para editar a descrição ou os anexos, clique no botão de edição ao lado do cabeçalho da seção. A descrição é salva com o botão "salvar" abaixo dela; a edição de anexos termina com **Concluído**.
- O botão de bloqueio define se a tarefa é privada. A descrição da tarefa recebe a mesma privacidade.

Usuários sem permissões de edição veem o status e a prioridade como texto, e seções sem conteúdo são ocultadas.

Abaixo do título, os editores veem mais dois botões: **Editar Fonte** abre a fonte que representa a tarefa, onde suas outras notas, citações e atributos podem ser editados. **Excluir** exclui a tarefa após uma confirmação e retorna à lista de tarefas; a mensagem que aparece tem um botão de desfazer para restaurar a tarefa.

## Alteração em massa das propriedades da tarefa

Usuários com permissões de edição veem uma caixa de seleção em cada linha da lista de tarefas. Selecione tarefas e use **Definir Prioridade** ou **Definir Status** acima da lista para alterar todas as tarefas selecionadas de uma vez.

## Tarefas no Gramps Desktop

Ao adicionar tarefas via Gramps Web, tanto as fontes quanto as notas terão a tag `ToDo` anexada a elas, de modo que as tarefas aparecerão no [Gramplet de Notas a Fazer do Gramps Desktop](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) assim como no [Relatório de Tarefas a Fazer](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Para adicionar ou editar uma tarefa no Gramps Desktop, use as seguintes diretrizes:

- Adicione uma fonte com a tag `ToDo` e o título da tarefa como título
- Opcionalmente, adicione uma nota à fonte com a tag `ToDo`, tipo "A Fazer", e a descrição como texto
- Adicione um atributo "Status" e defina como "Aberto", "Em Andamento", "Bloqueado" ou "Concluído"
- Adicione um atributo "Prioridade" e defina como 9 para baixa, 5 para média ou 1 para alta (esses valores contra-intuitivos são retirados da especificação iCalendar)
