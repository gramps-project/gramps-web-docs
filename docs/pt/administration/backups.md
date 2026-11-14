# Backup e restauração

Os proprietários da árvore podem criar, baixar e restaurar backups da árvore na seção **Backups** das [configurações de administração](settings.md).

Um backup contém os dados da árvore genealógica, incluindo registros privados, as configurações da árvore e os usuários da árvore. Arquivos de mídia não estão incluídos; veja [Faça backup dos seus arquivos de mídia](export.md#back-up-your-media-files).

## Backups armazenados

Se o administrador do servidor configurou um diretório de backup (`BACKUP_DIR`, veja [Configuração do servidor](../install_setup/configuration.md)), os backups podem ser armazenados no servidor. Caso contrário, a seção exibe um aviso de que o armazenamento de backups não está configurado, e apenas a restauração a partir de um arquivo enviado está disponível.

Clique em **Fazer Backup...** para criar um backup. Ele é criado como uma tarefa em segundo plano e, em seguida, aparece na lista de backups armazenados, com sua data, o número de pessoas e seu tamanho. O servidor mantém apenas os backups mais recentes (cinco por padrão) e exclui os mais antigos automaticamente. O número de backups que podem ser criados por dia também é limitado.

Para cada backup armazenado, você pode:

- **Baixar** como um arquivo `.tar`, por exemplo, para manter uma cópia em outro lugar.
- **Restaurar**, conforme descrito abaixo.
- **Excluir**, após confirmação.

Um backup feito com uma versão mais nova do Gramps Web do que a que está rodando no servidor é marcado com um ícone de aviso e não pode ser restaurado.

## Restaurar a partir do Backup

Restaura a árvore de um backup armazenado ou de um arquivo enviado. Para restaurar um backup armazenado, clique no botão de restauração ao lado dele. Para restaurar de um arquivo, selecione um backup do Gramps Web (`.tar`) ou um arquivo XML do Gramps (`.gramps`) e clique em **Restaurar**.

!!! danger
    Restaurar os dados é uma substituição destrutiva, não uma mesclagem. Qualquer objeto existente que não esteja presente no backup é excluído.

Para um backup do Gramps Web, uma caixa de diálogo mostra quando o backup foi feito, para qual árvore e com qual versão, e permite que você escolha quais partes restaurar:

- **Dados** – os objetos da árvore genealógica
- **Configurações da árvore** – as configurações da página de Administração, como cores do tema, título do aplicativo e nota da página inicial
- **Usuários** – os usuários da árvore

Clique em **Visualizar** para ver o que a restauração mudaria. Um arquivo XML do Gramps contém apenas dados, então para tal arquivo a visualização começa imediatamente. Você será solicitado a re-autenticar se sua sessão não estiver atualizada o suficiente. A visualização é executada como uma tarefa em segundo plano e, uma vez concluída, abre uma caixa de diálogo resumindo as mudanças por tipo de objeto (pessoas, famílias, eventos, lugares, citações, fontes, repositórios, objetos de mídia, notas, tags), e para as configurações da árvore e usuários, se selecionados:

- **Adicionar** – objetos presentes no backup, mas ausentes na árvore atual
- **Atualizar** – objetos presentes em ambos que diferem
- **Excluir** – objetos na árvore atual que estão ausentes do backup
- **Inalterado** – objetos idênticos em ambos

Se algum objeto for excluído, a caixa de diálogo avisa quantos. Revise o resumo, em seguida, clique em **Restaurar** para aplicar as mudanças ou **Cancelar** para abortar.

Após a restauração, os usuários que foram adicionados a partir do backup são listados. Eles recebem uma senha aleatória, então precisam redefinir sua senha antes de poderem fazer login. Usuários que já existem no servidor nunca são alterados. Objetos de mídia cujos arquivos estão ausentes no servidor também são listados; faça o upload deles via [Importar arquivos de mídia](import-media.md).

!!! note
    Restaurar dados apenas restaura dados de objetos e referências de mídia. Arquivos de mídia binários em si e metadados da árvore (pessoa padrão, marcadores, grupos de nomes) não são afetados.

!!! tip
    Use isso para reverter uma árvore para um backup conhecido como bom, por exemplo, após uma importação ruim ou uma edição em massa indesejada.

## Gramps XML como backup

Se o armazenamento de backups não estiver disponível, ou se você apenas quiser manter uma cópia dos dados da árvore genealógica, [exporte](export.md) a árvore como Gramps XML. Tal arquivo pode ser restaurado via [Restaurar a partir do Backup](#restore-from-backup) também.

Observe que, se seu usuário do Gramps Web não tiver permissão para visualizar registros privados, a exportação não será um backup completo, pois não conterá nenhum registro privado.
