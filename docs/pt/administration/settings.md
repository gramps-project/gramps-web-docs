# Configurações de Administração

A página **Configurações > Administração** é acessível através do ícone do usuário na barra superior do aplicativo. Ela está disponível apenas para usuários com o papel de Proprietário ou Administrador e fornece ferramentas para gerenciar o banco de dados da árvore genealógica.

A página está organizada em seções colapsáveis. Clique no cabeçalho de uma seção para expandi-la.

## Dados

Abrange cotas de uso, importação de dados e gerenciamento de arquivos de mídia.

### Cotas de uso

O topo da seção mostra o uso atual em relação a quaisquer limites configurados:

- **Pessoas** – o número de objetos de pessoa na árvore em comparação com o máximo configurado (∞ se ilimitado)
- **Armazenamento de mídia** – tamanho total dos arquivos de mídia carregados em comparação com a cota de armazenamento configurada (∞ se ilimitado)

As cotas são definidas pelo administrador do servidor; veja [Configuração do servidor](../install_setup/configuration.md) para detalhes.

### Importar dados

A seção de importação permite que você carregue um arquivo de árvore genealógica ou um arquivo de mídia. Veja [Importar dados](import.md) para instruções completas.

### Status dos arquivos de mídia

Esta seção mostra:

- O número total de objetos de mídia na árvore e se algum está sem uma soma de verificação
- O número de objetos de mídia cujo arquivo associado está ausente do servidor

Um sinal verde indica que tudo está em ordem. Se problemas forem detectados, links para os objetos afetados são exibidos. Somatórias de verificação ausentes normalmente ocorrem quando os dados foram importados de um formato como GEDCOM que inclui referências de mídia, mas não os arquivos reais. Os arquivos ausentes podem ser carregados através do recurso de importação de arquivo de mídia.

### Importar arquivo de mídia

Permite carregar um arquivo ZIP de arquivos de mídia para preencher arquivos ausentes. Veja [Importar dados](import.md) para instruções completas.

## Índice de pesquisa

### Gerenciar índice de pesquisa

Gramps Web mantém um índice de pesquisa de texto completo que normalmente é atualizado automaticamente sempre que os dados mudam. O indicador de status mostra quantos objetos estão atualmente indexados em comparação com o total de objetos.

Clique em **Atualizar índice de pesquisa** para acionar uma reconstrução completa. Um indicador de progresso é exibido enquanto a tarefa é executada em segundo plano. Isso geralmente é necessário apenas após uma atualização do servidor.

### Índice de pesquisa semântica

!!! warning "Depreciado"
    A pesquisa semântica está depreciada e será removida na API Gramps Web 3.25, juntamente com esta seção. O chat de IA não precisa dela, pois a API Gramps Web 3.24 já está disponível.

Se o servidor tiver [pesquisa semântica (com IA) habilitada](../install_setup/chat.md#semantic-search-deprecated), uma seção adicional aparece com duas ações:

- **Regenerar índice de pesquisa semântica** – reconstrói todo o índice semântico do zero. Isso é computacionalmente caro e pode levar muito tempo.
- **Atualizar índice de pesquisa semântica** – realiza uma atualização incremental, adicionando apenas objetos que ainda não foram indexados. Mais rápido do que uma reconstrução completa.

## Configurações da árvore

### Nome da Árvore Genealógica

!!! note
    Renomear a árvore só funciona em uma [configuração de múltiplas árvores](../install_setup/multi-tree.md) ou quando `TREE_ID` está explicitamente definido na [configuração do servidor](../install_setup/configuration.md). Em uma instalação padrão de árvore única sem `TREE_ID` definido, isso gerará um erro.

Isso permite alterar o nome do banco de dados da árvore genealógica do Gramps subjacente. Insira um novo nome e clique em **Renomear** para aplicar.

!!! tip
    Se você só quiser mudar o nome exibido na barra do aplicativo sem renomear o banco de dados, use a configuração [Título do aplicativo](#app-title) em vez disso.

### Informações do Pesquisador

Defina o nome, endereço e detalhes de contato do pesquisador principal. Essas informações estão incorporadas nas exportações (por exemplo, arquivos GEDCOM).

## Personalização

### Cores do tema

Defina uma **cor primária** e uma **cor de destaque** personalizadas para a interface do Gramps Web. Essas cores são aplicadas a todos os usuários desta árvore e entram em vigor imediatamente após a salvamento.

Use os seletores de cores para escolher as cores e, em seguida, clique em **Salvar**. Clique em **Redefinir** para reverter aos padrões.

### Título do aplicativo

Defina um título personalizado para o aplicativo. Se definido, isso substitui o nome da árvore genealógica na barra de título do navegador e na barra superior do aplicativo.

Insira um título e clique em **Salvar**. Deixe em branco para usar o padrão (o nome da árvore genealógica).

### Nota da página inicial

Selecione um objeto **Nota** do Gramps para exibir na página inicial do painel. O conteúdo da nota é renderizado abaixo das colunas principais do painel e é visível para todos os usuários com acesso à árvore.

Use o seletor de objetos para pesquisar e escolher uma nota, e então salve. Clique em **Remover** para limpar a nota atual da página inicial.

### Imagem da página inicial

Selecione um objeto **Mídia** do Gramps para exibir como uma imagem na página inicial do painel. Quando combinado com uma nota da página inicial, a imagem aparece ao lado do texto da nota. Sem uma nota, apenas a imagem é exibida.

Use o seletor de objetos para pesquisar e escolher um objeto de mídia, e então salve. Clique em **Remover** para limpar a imagem atual da página inicial.

### Configurações de Exportação/Importação

As configurações de nível de árvore (título do aplicativo, cores do tema, nota/imagem da página inicial, etc.) podem ser exportadas como um arquivo JSON para backup ou para copiar para outra instância do Gramps Web.

- Clique em **Exportar configurações** para baixar as configurações atuais como um arquivo JSON.
- Clique em **Importar configurações da árvore** para carregar um arquivo JSON exportado anteriormente e aplicar as configurações.

## Processamento da Árvore Genealógica

### Verificar e Reparar Banco de Dados

Esta ferramenta verifica o banco de dados do Gramps em busca de inconsistências internas e corrige aquelas que pode – análogo à ferramenta [Verificar e Reparar Banco de Dados](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) no Gramps Desktop.

Clique em **Verificar e Reparar** e aguarde o indicador de progresso ser concluído. O resultado é exibido abaixo do botão:

- Se nenhum erro for encontrado, uma mensagem de confirmação é exibida.
- Se erros forem encontrados, um resumo das correções aplicadas é exibido.

Execute esta ferramenta se você encontrar erros ou comportamentos inesperados que podem ser causados por inconsistências no banco de dados, como relacionamentos ausentes entre objetos.

### Verificar os Dados

Enquanto [Verificar e Reparar Banco de Dados](#check-and-repair-database) procura por inconsistências *técnicas*, esta ferramenta procura por dados *implausíveis* – análogo à ferramenta [Verificar os Dados](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) no Gramps Desktop. Ela relata coisas que não são impossíveis, mas são improváveis o suficiente para merecer uma segunda olhada, como uma mãe com 12 anos ou uma pessoa que viveu até 130 anos.

Sob **Opções**, você pode ajustar os limites que os testes usam – idade máxima, idade mínima e máxima para casar ou ter filhos, número máximo de filhos, e assim por diante – bem como se deve estimar datas ausentes ou imprecisas e se deve relatar datas inválidas, como 31 de fevereiro.

Clique em **Verificar os Dados** para começar. A verificação é executada como uma tarefa em segundo plano, e os resultados são listados sob **Resultados da Verificação de Dados**. Nada é alterado por esta ferramenta: ela apenas relata o que encontra.

!!! note
    Um achado não é prova de um erro. Vidas longas e grandes diferenças de idade ocorrem, então trate os resultados como uma lista de coisas a verificar, em vez de uma lista de coisas a corrigir.

## Etiquetas

### Gerenciar etiquetas

Crie, renomeie, mude a cor e exclua [etiquetas](../user-guide/tags.md) para a árvore genealógica. As etiquetas são armazenadas no banco de dados do Gramps, compartilhadas entre todos os usuários e totalmente compatíveis com o Gramps Desktop.

Clique em **Nova Etiqueta** para criar uma etiqueta. Use os controles ao lado de uma etiqueta existente para renomeá-la (ícone de lápis), mudar sua cor (seletor de cor) ou excluí-la (ícone de excluir).

!!! note
    Excluir uma etiqueta a remove de todos os objetos aos quais foi aplicada.

Veja [Etiquetas](../user-guide/tags.md) para como as etiquetas são usadas em todo o Gramps Web, incluindo as etiquetas especiais `Blog` e `ToDo`.

## Backups

Um backup contém os dados da árvore genealógica, incluindo registros privados, as configurações da árvore e os usuários da árvore. Arquivos de mídia não estão incluídos; veja [Faça backup dos seus arquivos de mídia](export.md#back-up-your-media-files).

### Backups armazenados

Se o administrador do servidor configurou um diretório de backup (`BACKUP_DIR`, veja [Configuração do servidor](../install_setup/configuration.md)), os backups podem ser armazenados no servidor. Caso contrário, a seção mostra um aviso de que o armazenamento de backups não está configurado, e apenas a restauração a partir de um arquivo carregado está disponível.

Clique em **Fazer Backup...** para criar um backup. Ele é criado como uma tarefa em segundo plano e, em seguida, aparece na lista de backups armazenados, com sua data, o número de pessoas e seu tamanho. O servidor mantém apenas os backups mais recentes (cinco por padrão) e exclui os mais antigos automaticamente. O número de backups que podem ser criados por dia também é limitado.

Para cada backup armazenado, você pode:

- **Baixar** como um arquivo `.tar`, por exemplo, para manter uma cópia em outro lugar.
- **Restaurar**, conforme descrito abaixo.
- **Excluir**, após confirmação.

Um backup feito com uma versão mais nova do Gramps Web do que a que está sendo executada no servidor é marcado com um ícone de aviso e não pode ser restaurado.

### Restaurar a partir de Backup

Restaura a árvore a partir de um backup armazenado ou de um arquivo carregado. Para restaurar um backup armazenado, clique no botão de restauração ao lado dele. Para restaurar a partir de um arquivo, selecione um backup do Gramps Web (`.tar`) ou um arquivo XML do Gramps (`.gramps`) e clique em **Restaurar**.

!!! danger
    Restaurar os dados é uma substituição destrutiva, não uma mesclagem. Qualquer objeto existente que não esteja presente no backup será excluído.

Para um backup do Gramps Web, uma caixa de diálogo mostra quando o backup foi feito, para qual árvore, e com qual versão, e permite que você escolha quais partes restaurar:

- **Dados** – os objetos da árvore genealógica
- **Configurações da árvore** – as configurações desta página, como cores do tema, título do aplicativo e nota da página inicial
- **Usuários** – os usuários da árvore

Clique em **Visualizar** para ver o que a restauração mudaria. Um arquivo XML do Gramps contém apenas dados, então para tal arquivo a visualização começa imediatamente. Você será solicitado a reautenticar se sua sessão não estiver fresca o suficiente. A visualização é executada como uma tarefa em segundo plano e, uma vez concluída, abre uma caixa de diálogo resumindo as mudanças por tipo de objeto (pessoas, famílias, eventos, lugares, citações, fontes, repositórios, objetos de mídia, notas, etiquetas), e para as configurações da árvore e usuários, se selecionados:

- **Adicionar** – objetos presentes no backup, mas ausentes na árvore atual
- **Atualizar** – objetos presentes em ambos que diferem
- **Excluir** – objetos na árvore atual que estão ausentes do backup
- **Inalterado** – objetos idênticos em ambos

Se algum objeto for excluído, a caixa de diálogo avisa quantos. Revise o resumo e clique em **Restaurar** para aplicar as mudanças, ou **Cancelar** para abortar.

Após a restauração, os usuários que foram adicionados a partir do backup são listados. Eles recebem uma senha aleatória, então precisam redefinir sua senha antes de poderem fazer login. Usuários que já existem no servidor nunca são alterados. Objetos de mídia cujos arquivos estão ausentes no servidor também são listados; faça o upload deles através da [Importar arquivo de mídia](#import-media-archive).

!!! note
    Restaurar dados apenas restaura dados de objetos e referências de mídia. Arquivos de mídia binários em si e metadados da árvore (pessoa padrão, marcadores, grupos de nomes) não são afetados.

!!! tip
    Use isso para reverter uma árvore para um backup conhecido como bom, por exemplo, após uma importação ruim ou uma edição em massa indesejada.

## Zona de Perigo

!!! danger
    Ações na Zona de Perigo são **irreversíveis**. Faça um [backup](#backups) antes de prosseguir.

### Excluir todos os objetos

Remove objetos da árvore genealógica. Clicar em **Excluir** abre uma caixa de diálogo onde você pode escolher excluir:

- **Todos os objetos** – limpa completamente a árvore
- **Tipos de objetos específicos** – por exemplo, apenas eventos ou apenas objetos de mídia

Você será solicitado a reautenticar (fazer login novamente) para confirmar a ação. A exclusão é executada como uma tarefa em segundo plano e um indicador de progresso é exibido.

!!! warning
    Excluir apenas um subconjunto de tipos de objetos (em vez de todos os objetos de uma vez) pode levar muito tempo para árvores grandes, pois o servidor deve verificar e atualizar todos os relacionamentos entre objetos.

!!! tip
    Use isso para começar do zero antes de importar uma nova árvore, ou para remover tipos de objetos específicos que foram importados incorretamente.
