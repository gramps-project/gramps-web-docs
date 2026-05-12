# Configurações de Administração

A página **Configurações > Administração** é acessível através do ícone do usuário na barra superior do aplicativo. Está disponível apenas para usuários com o papel de Proprietário ou Administrador e fornece ferramentas para gerenciar o banco de dados da árvore genealógica.

## Cotas de uso

O topo da página mostra o uso atual em relação a quaisquer limites configurados:

- **Pessoas** — o número de objetos de pessoa na árvore em comparação com o máximo configurado (∞ se ilimitado)
- **Armazenamento de mídia** — tamanho total dos arquivos de mídia carregados em comparação com a cota de armazenamento configurada (∞ se ilimitado)

As cotas são definidas pelo administrador do servidor; veja [Configuração do servidor](../install_setup/configuration.md) para detalhes.

## Importar dados

A seção de importação permite que você carregue um arquivo de árvore genealógica ou um arquivo de mídia. Veja [Importar dados](import.md) para instruções completas.

## Status do arquivo de mídia

Esta seção mostra:

- O número total de objetos de mídia na árvore e se algum está sem uma soma de verificação
- O número de objetos de mídia cujo arquivo associado está faltando no servidor

Uma marca de verificação verde indica que tudo está em ordem. Se problemas forem detectados, links para os objetos afetados são exibidos. Sombras de verificação ausentes geralmente ocorrem quando os dados foram importados de um formato como GEDCOM que inclui referências de mídia, mas não os arquivos reais. Os arquivos ausentes podem ser carregados através do recurso de importação de arquivo de mídia.

## Importar arquivo de mídia

Permite o upload de um arquivo ZIP de arquivos de mídia para preencher arquivos ausentes. Veja [Importar dados](import.md) para instruções completas.

## Gerenciar índice de pesquisa

O Gramps Web mantém um índice de pesquisa de texto completo que normalmente é atualizado automaticamente sempre que os dados mudam. O indicador de status mostra quantos objetos estão atualmente indexados em comparação com o total de objetos.

Clique em **Atualizar índice de pesquisa** para acionar uma reconstrução completa. Um indicador de progresso é exibido enquanto a tarefa é executada em segundo plano. Isso geralmente é necessário apenas após uma atualização do servidor.

### Índice de pesquisa semântica

Se o servidor tiver [pesquisa semântica (potencializada por IA) habilitada](../install_setup/configuration.md), uma seção adicional aparece com duas ações:

- **Regenerar índice de pesquisa semântica** — reconstrói todo o índice semântico do zero. Isso é computacionalmente caro e pode levar muito tempo.
- **Atualizar índice de pesquisa semântica** — realiza uma atualização incremental, adicionando apenas objetos que ainda não foram indexados. Mais rápido do que uma reconstrução completa.

## Nome da Árvore Genealógica

!!! note
    Renomear a árvore só funciona em uma [configuração de múltiplas árvores](../install_setup/multi-tree.md) ou quando `TREE_ID` é explicitamente definido na [configuração do servidor](../install_setup/configuration.md). Em uma instalação padrão de árvore única sem `TREE_ID` definido, isso gerará um erro.

Isso permite alterar o nome do banco de dados da árvore genealógica do Gramps subjacente. Insira um novo nome e clique em **Renomear** para aplicar.

## Verificar e Reparar Banco de Dados

Esta ferramenta verifica o banco de dados do Gramps em busca de inconsistências internas e corrige aquelas que pode — análogo à ferramenta [Verificar e Reparar Banco de Dados](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) no Gramps Desktop.

Clique em **Verificar e Reparar** e aguarde a conclusão do indicador de progresso. O resultado é exibido abaixo do botão:

- Se nenhum erro for encontrado, uma mensagem de confirmação é exibida.
- Se erros forem encontrados, um resumo das correções aplicadas é mostrado.

Execute esta ferramenta se você encontrar erros ou comportamentos inesperados que possam ser causados por inconsistências no banco de dados, como relacionamentos ausentes entre objetos.

## Zona de Perigo

!!! danger
    Ações na Zona de Perigo são **irreversíveis**. Faça um backup antes de prosseguir.

### Excluir todos os objetos

Remove objetos da árvore genealógica. Clicar em **Excluir** abre uma caixa de diálogo onde você pode escolher excluir:

- **Todos os objetos** — limpa completamente a árvore
- **Tipos de objetos específicos** — por exemplo, apenas eventos ou apenas objetos de mídia

Você será solicitado a reautenticar (fazer login novamente) para confirmar a ação. A exclusão é executada como uma tarefa em segundo plano e um indicador de progresso é exibido.

!!! warning
    Excluir apenas um subconjunto de tipos de objetos (em vez de todos os objetos de uma vez) pode levar muito tempo para árvores grandes, pois o servidor deve verificar e atualizar todos os relacionamentos entre objetos.

!!! tip
    Use isso para começar do zero antes de importar uma nova árvore ou para remover tipos de objetos específicos que foram importados incorretamente.
