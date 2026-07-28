# Configurações de Administração

A página **Configurações > Administração** é acessível através do ícone do usuário na barra superior do aplicativo. Ela está disponível apenas para usuários com o papel de Proprietário ou Administrador e fornece ferramentas para gerenciar o banco de dados da árvore genealógica.

A página é organizada em seções colapsáveis. Clique no cabeçalho de uma seção para expandi-la.

## Dados

Cobre cotas de uso, importação de dados e gerenciamento de arquivos de mídia.

### Cotas de uso

O topo da seção mostra o uso atual em relação a quaisquer limites configurados:

- **Pessoas** – o número de objetos de pessoa na árvore em comparação com o máximo configurado (∞ se ilimitado)
- **Armazenamento de mídia** – tamanho total dos arquivos de mídia carregados em comparação com a cota de armazenamento configurada (∞ se ilimitado)

As cotas são definidas pelo administrador do servidor; consulte [Configuração do servidor](../install_setup/configuration.md) para mais detalhes.

### Importar dados

A seção de importação permite que você carregue um arquivo de árvore genealógica ou um arquivo de mídia. Consulte [Importar dados](import.md) para instruções completas.

### Status do arquivo de mídia

Esta seção mostra:

- O número total de objetos de mídia na árvore e se algum está sem um checksum
- O número de objetos de mídia cujo arquivo associado está faltando no servidor

Um sinal verde indica que está tudo em ordem. Se problemas forem detectados, links para os objetos afetados são mostrados. Checksums ausentes geralmente ocorrem quando os dados foram importados de um formato como GEDCOM que inclui referências de mídia, mas não os arquivos reais. Os arquivos ausentes podem ser carregados através do recurso de importação de arquivo de mídia.

### Importar arquivo de mídia

Permite o upload de um arquivo ZIP de arquivos de mídia para preencher arquivos ausentes. Consulte [Importar dados](import.md) para instruções completas.

## Índice de Pesquisa

### Gerenciar índice de pesquisa

Gramps Web mantém um índice de pesquisa de texto completo que normalmente é atualizado automaticamente sempre que os dados mudam. O indicador de status mostra quantos objetos estão atualmente indexados em comparação com o total de objetos.

Clique em **Atualizar índice de pesquisa** para acionar uma reconstrução completa. Um indicador de progresso é exibido enquanto a tarefa é executada em segundo plano. Isso geralmente é necessário apenas após uma atualização do servidor.

### Índice de pesquisa semântica

Se o servidor tiver [pesquisa semântica (potencializada por IA) habilitada](../install_setup/configuration.md), uma seção adicional aparece com duas ações:

- **Regenerar índice de pesquisa semântica** – reconstrói todo o índice semântico do zero. Isso é computacionalmente caro e pode levar muito tempo.
- **Atualizar índice de pesquisa semântica** – realiza uma atualização incremental, adicionando apenas objetos que ainda não foram indexados. Mais rápido do que uma reconstrução completa.

## Configurações da Árvore

### Nome da Árvore Genealógica

!!! note
    Renomear a árvore só funciona em uma [configuração de múltiplas árvores](../install_setup/multi-tree.md) ou quando `TREE_ID` é explicitamente definido na [configuração do servidor](../install_setup/configuration.md). Em uma instalação padrão de árvore única sem `TREE_ID` definido, isso gerará um erro.

Isso permite alterar o nome do banco de dados subjacente da árvore genealógica do Gramps. Insira um novo nome e clique em **Renomear** para aplicar.

!!! tip
    Se você apenas quiser mudar o nome exibido na barra do aplicativo sem renomear o banco de dados, use a configuração [Título do aplicativo](#app-title) em vez disso.

### Informações do Pesquisador

Defina o nome, endereço e detalhes de contato do pesquisador principal. Essas informações são incorporadas nas exportações (por exemplo, arquivos GEDCOM).

## Personalização

### Cores do Tema

Defina uma **cor primária** e uma **cor de destaque** personalizadas para a interface do Gramps Web. Essas cores são aplicadas a todos os usuários desta árvore e entram em vigor imediatamente após a salvamento.

Use os seletores de cores para escolher cores, em seguida, clique em **Salvar**. Clique em **Redefinir** para reverter aos padrões.

### Título do Aplicativo

Defina um título personalizado para a aplicação. Se definido, isso substitui o nome da árvore genealógica na barra de título do navegador e na barra superior do aplicativo.

Insira um título e clique em **Salvar**. Deixe em branco para usar o padrão (o nome da árvore genealógica).

### Nota da Página Inicial

Selecione um objeto **Nota** do Gramps para exibir na página inicial do painel. O conteúdo da nota é renderizado abaixo das colunas principais do painel e é visível para todos os usuários com acesso à árvore.

Use o seletor de objetos para pesquisar e escolher uma nota, em seguida, salve. Clique em **Remover** para limpar a nota atual da página inicial.

### Imagem da Página Inicial

Selecione um objeto **Mídia** do Gramps para exibir como uma imagem na página inicial do painel. Quando combinado com uma nota da página inicial, a imagem aparece ao lado do texto da nota. Sem uma nota, apenas a imagem é exibida.

Use o seletor de objetos para pesquisar e escolher um objeto de mídia, em seguida, salve. Clique em **Remover** para limpar a imagem atual da página inicial.

### Configurações de Exportação/Importação

As configurações em nível de árvore (título do aplicativo, cores do tema, nota/imagem da página inicial, etc.) podem ser exportadas como um arquivo JSON para backup ou para copiar para outra instância do Gramps Web.

- Clique em **Exportar configurações** para baixar as configurações atuais como um arquivo JSON.
- Clique em **Importar configurações da árvore** para carregar um arquivo JSON exportado anteriormente e aplicar as configurações.

## Processamento da Árvore Genealógica

### Verificar e Reparar Banco de Dados

Esta ferramenta verifica o banco de dados do Gramps em busca de inconsistências internas e corrige as que pode – análogo à ferramenta [Verificar e Reparar Banco de Dados](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) no Gramps Desktop.

Clique em **Verificar e Reparar** e aguarde o indicador de progresso completar. O resultado é mostrado abaixo do botão:

- Se nenhum erro for encontrado, uma mensagem de confirmação é exibida.
- Se erros forem encontrados, um resumo das correções aplicadas é mostrado.

Execute esta ferramenta se você encontrar erros ou comportamentos inesperados que podem ser causados por inconsistências no banco de dados, como relacionamentos ausentes entre objetos.

## Etiquetas

### Gerenciar etiquetas

Crie, renomeie, mude a cor e exclua [etiquetas](../user-guide/tags.md) para a árvore genealógica. As etiquetas são armazenadas no banco de dados do Gramps, compartilhadas entre todos os usuários e totalmente compatíveis com o Gramps Desktop.

Clique em **Nova Etiqueta** para criar uma etiqueta. Use os controles ao lado de uma etiqueta existente para renomeá-la (ícone de lápis), mudar sua cor (seletor de cor) ou excluí-la (ícone de exclusão).

!!! note
    Excluir uma etiqueta a remove de todos os objetos aos quais foi aplicada.

Consulte [Etiquetas](../user-guide/tags.md) para saber como as etiquetas são usadas em todo o Gramps Web, incluindo as etiquetas especiais `Blog` e `ToDo`.

## Zona de Perigo

!!! danger
    As ações na Zona de Perigo são **irreversíveis**. Faça um backup antes de prosseguir.

### Excluir todos os objetos

Remove objetos da árvore genealógica. Clicar em **Excluir** abre um diálogo onde você pode escolher excluir:

- **Todos os objetos** – limpa completamente a árvore
- **Tipos de objetos específicos** – por exemplo, apenas eventos ou apenas objetos de mídia

Você será solicitado a reautenticar (fazer login novamente) para confirmar a ação. A exclusão é executada como uma tarefa em segundo plano e um indicador de progresso é exibido.

!!! warning
    Excluir apenas um subconjunto de tipos de objetos (em vez de todos os objetos de uma vez) pode levar muito tempo para árvores grandes, pois o servidor deve verificar e atualizar todos os relacionamentos entre objetos.

!!! tip
    Use isso para começar do zero antes de importar uma nova árvore ou para remover tipos de objetos específicos que foram importados incorretamente.

### Restaurar de Backup

Restaura a árvore para corresponder a um arquivo de backup XML do Gramps (`.gramps`) carregado, adicionando, atualizando e excluindo objetos conforme necessário para que a árvore termine idêntica ao backup.

!!! danger
    Esta é uma substituição destrutiva, não uma mesclagem. Qualquer objeto existente que não esteja presente no backup carregado será excluído.

Carregue um arquivo `.gramps`, em seguida, clique em **Visualizar Restauração**. Você será solicitado a reautenticar se sua sessão não estiver fresca o suficiente. Uma pré-visualização é executada como uma tarefa em segundo plano e, uma vez completa, abre um diálogo resumindo as mudanças por tipo de objeto (pessoas, famílias, eventos, lugares, citações, fontes, repositórios, objetos de mídia, notas, etiquetas):

- **Adicionar** – objetos presentes no backup, mas ausentes na árvore atual
- **Atualizar** – objetos presentes em ambos que diferem
- **Excluir** – objetos na árvore atual que estão ausentes do backup
- **Inalterado** – objetos idênticos em ambos

Se algum objeto for excluído, o diálogo avisa quantos. Revise o resumo e clique em **Restaurar** para aplicar as mudanças ou **Cancelar** para abortar.

!!! note
    Somente dados de objetos e referências de mídia são restaurados. Arquivos de mídia binários em si e metadados da árvore (pessoa padrão, marcadores, grupos de nomes) não são afetados. Restaure arquivos de mídia ausentes separadamente via [Importar arquivo de mídia](#import-media-archive) se necessário.

!!! tip
    Use isso para reverter uma árvore para um backup XML do Gramps conhecido como bom, por exemplo, após uma importação ruim ou uma edição em massa indesejada.
