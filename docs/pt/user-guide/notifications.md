# Notificações

**Notificações** é um item da barra lateral com um ícone de sino. Quando erros ocorrem ou tarefas em segundo plano estão em execução, um badge mostra o número de notificações não lidas. Clique nele para abrir o registro de notificações.

O registro de notificações serve a dois propósitos:

- É um registro de erros que ocorreram durante sua sessão – solicitações de API falhadas, erros de tarefas em segundo plano, falhas de salvamento ou erros a nível de navegador.
- Ele rastreia o progresso de tarefas em segundo plano de longa duração – como importações e exportações, geração de relatórios, reconhecimento de texto OCR, atualizações de banco de dados e reconstruções de índice de pesquisa/semântico – mostrando seu estado (por exemplo, pendente, iniciado, em progresso) e notificando você quando elas são concluídas ou falham.

Cada entrada mostra uma mensagem curta, a fonte (Rede, Tarefa, Salvamento ou Navegador) e um carimbo de data/hora.

Algumas notificações incluem detalhes estruturados. Clicar em tal entrada abre um diálogo com uma análise dos dados de erro e um botão **Copiar JSON**. Isso é útil ao relatar um bug, pois o JSON contém as informações exatas do erro do servidor.

Use **Limpar Tudo** para descartar todas as notificações.

!!! nota
    As notificações são armazenadas apenas na memória e são limpas quando você recarrega a página.
