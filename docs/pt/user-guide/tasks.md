# Use a gestão de tarefas embutida

O Gramps Web contém uma ferramenta de gestão de tarefas genealógicas embutida. Ela é destinada a permitir que os pesquisadores planejem e priorizem, mas também documentem suas tarefas. É por isso que as tarefas são representadas como fontes no banco de dados do Gramps. Após a conclusão de uma tarefa, o conteúdo associado pode servir como uma fonte documentando o processo de pesquisa.

## Noções básicas sobre tarefas

As tarefas têm as seguintes propriedades:

- Status. Isso pode ser "Aberto", "Em Progresso", "Bloqueado" ou "Concluído"
- Prioridade. Isso pode ser "Baixa", "Média" ou "Alta"
- Tags. Os rótulos são tags normais do Gramps da fonte subjacente. (Observe que todas as tarefas têm adicionalmente o rótulo `ToDo` para identificá-las como tarefas, mas esse rótulo está oculto na lista de tarefas para evitar desordem.)
- Título. Exibido na lista de tarefas
- Descrição. Um campo de texto rico que pode ser usado para descrever a declaração do problema, mas também documentar qualquer progresso feito
- Mídia. Quaisquer arquivos de mídia anexados à tarefa

## Criar uma tarefa

Como as tarefas são objetos normais do Gramps, elas podem ser editadas ou criadas pelo mesmo grupo de usuários que pode editar ou criar outros objetos (como pessoas ou eventos).

Para criar uma tarefa, clique no botão + na página da lista de tarefas. Insira pelo menos um título. O status será sempre "Aberto" na criação.

## Editar uma tarefa

Para editar qualquer um dos detalhes da tarefa, clique nela na lista de tarefas.

A página de detalhes da tarefa não possui um "modo de edição" separado como outros objetos do Gramps. As alterações no título, status e prioridade são aplicadas imediatamente. As alterações na descrição em texto rico requerem que você clique no botão "salvar" abaixo dela.

## Alteração em massa das propriedades da tarefa

A prioridade e o status das tarefas podem ser alterados em massa usando as caixas de seleção na lista de tarefas para seleção e os botões apropriados acima da lista de tarefas.

## Tarefas no Gramps Desktop

Ao adicionar tarefas via Gramps Web, tanto as fontes quanto as notas terão a tag `ToDo` anexada a elas, então as tarefas aparecerão no [Gramplet de Notas a Fazer](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) do desktop, bem como no [Relatório de Tarefas a Fazer](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Para adicionar ou editar uma tarefa no Gramps Desktop, use as seguintes diretrizes

- Adicione uma fonte com a tag `ToDo` e o título da tarefa como título
- Opcionalmente, adicione uma nota à fonte com a tag `ToDo`, tipo "A Fazer", e a descrição como texto
- Adicione um atributo "Status" e defina como "Aberto", "Em Progresso", "Bloqueado" ou "Concluído"
- Adicione um atributo "Prioridade" e defina como 9 para baixa, 5 para média ou 1 para alta (esses valores contra-intuitivos são retirados da especificação do iCalendar)
