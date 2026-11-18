# Notificações

O sino na barra superior do aplicativo abre as notificações. Um ícone no sino mostra o número de notificações não lidas. O menu lista tarefas em execução e as últimas notificações; **Mostrar tudo** abre o log completo de notificações. Em telas pequenas, o sino abre o log diretamente.

As notificações dizem respeito a:

- **Mudanças por outros usuários.** Quando outros usuários alteram a árvore enquanto você está usando o Gramps Web, uma notificação informa quem mudou o que, por exemplo, "Editar Pessoa" ou "12 alterações". Clique para abrir a alteração no [histórico de revisões](revisions.md). Mudanças que não têm um usuário do Gramps Web, como alterações feitas diretamente em um banco de dados compartilhado com o Gramps Desktop, são mostradas sem um nome. Isso está disponível apenas para usuários que podem ver o histórico de revisões (membros e acima).
- **Tarefas em segundo plano** – como importações e exportações, geração de relatórios, reconhecimento de texto OCR, atualizações de banco de dados, exclusão ou edição de muitos objetos e reconstruções de índice de pesquisa – mostrando seu estado (por exemplo, pendente, iniciado, em progresso) e notificando você quando são concluídas ou falham.
- **Erros** que ocorreram durante sua sessão – falhas em solicitações de API, erros em tarefas em segundo plano, falhas de salvamento ou erros a nível de navegador.

Exportações concluídas e arquivos de mídia podem ser baixados a partir de suas notificações, mesmo após você ter saído da [página de Exportação](../administration/export.md).

Algumas notificações incluem detalhes estruturados, como a mensagem de erro de uma tarefa falhada. Clicar em tal entrada no log de notificações abre um diálogo com uma análise dos dados de erro e um botão **Copiar JSON**. Isso é útil ao relatar um bug, pois o JSON contém as informações exatas do erro do servidor.

Use **Limpar Tudo** no log de notificações para descartar todas as notificações.

Tarefas que alteram toda a árvore, como uma importação, uma restauração, exclusão de todos os objetos ou reconstrução do índice de pesquisa, não podem ser executadas ao mesmo tempo. Se você iniciar uma enquanto outra está em execução, uma mensagem informa que outra tarefa já está em execução nesta árvore, e a tarefa em execução é mostrada com seu progresso.

!!! nota
    As notificações são armazenadas apenas na memória e são limpas quando você recarrega a página. O Gramps Web verifica alterações por outros usuários apenas enquanto está aberto, portanto, alterações feitas enquanto você estava ausente não são relatadas; veja [Histórico de Revisões](revisions.md) para essas.
