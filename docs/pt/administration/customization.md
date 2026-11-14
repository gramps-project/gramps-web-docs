# Personalizar a árvore

Os proprietários e administradores da árvore podem adaptar o nome e a aparência da árvore, bem como sua página inicial, para todos os usuários. Essas configurações estão localizadas nas seções **Configurações da árvore** e **Personalização** das [Configurações de administração](settings.md).

## Nome da Árvore Genealógica

!!! note
    Renomear a árvore só funciona em uma [configuração de múltiplas árvores](../install_setup/multi-tree.md) ou quando `TREE_ID` está explicitamente definido na [configuração do servidor](../install_setup/configuration.md). Em uma instalação padrão de árvore única sem `TREE_ID` definido, isso gerará um erro.

Isso permite mudar o nome do banco de dados subjacente da árvore genealógica Gramps. Digite um novo nome e clique em **Renomear** para aplicar.

!!! tip
    Se você só quiser mudar o nome exibido na barra do aplicativo sem renomear o banco de dados, use a configuração de [Título do aplicativo](#app-title) em vez disso.

## Informações do Pesquisador

Defina o nome, endereço e detalhes de contato do pesquisador principal. Essas informações estão embutidas nas exportações (por exemplo, arquivos GEDCOM).

## Cores do Tema

Defina uma **cor primária** e uma **cor de destaque** personalizadas para a interface da Web do Gramps. Essas cores são aplicadas a todos os usuários desta árvore e entram em vigor imediatamente após a salvamento.

Use os seletores de cores para escolher as cores e, em seguida, clique em **Salvar**. Clique em **Redefinir** para reverter aos padrões.

## Título do aplicativo

Defina um título personalizado para o aplicativo. Se definido, isso substitui o nome da árvore genealógica na barra de título do navegador e na barra superior do aplicativo.

Digite um título e clique em **Salvar**. Deixe em branco para usar o padrão (o nome da árvore genealógica).

## Nota da página inicial

Selecione um objeto **Nota** do Gramps para exibir na página inicial do painel. O conteúdo da nota é renderizado abaixo das colunas principais do painel e é visível para todos os usuários com acesso à árvore.

Use o seletor de objetos para pesquisar e escolher uma nota, em seguida, salve. Clique em **Remover** para limpar a nota atual da página inicial.

## Imagem da página inicial

Selecione um objeto **Mídia** do Gramps para exibir como uma imagem na página inicial do painel. Quando combinado com uma nota da página inicial, a imagem aparece ao lado do texto da nota. Sem uma nota, apenas a imagem é exibida.

Use o seletor de objetos para pesquisar e escolher um objeto de mídia, em seguida, salve. Clique em **Remover** para limpar a imagem atual da página inicial.

## Configurações de Exportação/Importação

As configurações em nível de árvore (título do aplicativo, cores do tema, nota/imagem da página inicial, etc.) podem ser exportadas como um arquivo JSON para backup ou para copiar para outra instância do Gramps Web.

- Clique em **Exportar configurações** para baixar as configurações atuais como um arquivo JSON.
- Clique em **Importar configurações da árvore** para enviar um arquivo JSON exportado anteriormente e aplicar as configurações.
