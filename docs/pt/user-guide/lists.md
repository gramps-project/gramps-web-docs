# Listas

Todo tipo de objeto no Gramps Web possui uma visualização em lista: Pessoas, Famílias, Eventos, Lugares, Fontes, Citações, Repositórios, Notas e Mídia. Todos funcionam da mesma forma e compartilham as mesmas ferramentas para ordenação, filtragem e edição em massa.

## Ordenação e paginação

Clique no cabeçalho de uma coluna para ordenar por essa coluna; clique novamente para reverter a ordem. A ordenação é realizada pelo servidor, portanto, aplica-se a toda a lista, não apenas à página que você está visualizando.

Listas longas são divididas em páginas. Use os controles de paginação na parte inferior para navegar entre elas.

Em telas estreitas, a tabela muda automaticamente para um layout compacto, para que as visualizações de lista permaneçam utilizáveis em um telefone.

## Escolhendo colunas

Clique no ícone de engrenagem na extremidade direita da barra de ferramentas acima da lista para abrir o diálogo **Colunas**. Marque ou desmarque uma coluna para exibi-la ou ocultá-la. **Redefinir** restaura a seleção padrão para essa lista.

Pelo menos uma coluna deve permanecer visível, portanto, a última coluna restante não pode ser desmarcada.

Além das colunas padrão, cada lista oferece uma coluna **Tags** e, para usuários que podem visualizar registros privados, uma coluna **Privacidade** que mostra um cadeado para cada objeto privado. Se você alterou a seleção de colunas de uma lista anteriormente, novas colunas como **Tags** não são adicionadas automaticamente; marque-as no diálogo.

Sua seleção de colunas é lembrada por tipo de objeto e por árvore genealógica. Ela é armazenada no seu navegador, portanto, não é visível para outros usuários – mas também não segue você para um navegador ou dispositivo diferente.

## Filtragem

Clique no botão **filtrar** para abrir o painel de filtro. Ele oferece três maneiras de filtrar, que podem ser combinadas:

- **Filtros prontos** em seções colapsáveis que dependem do tipo de objeto. Para pessoas, por exemplo, você pode filtrar por nome, ano de nascimento, ano de falecimento, várias propriedades da pessoa, o número de associações, tags e se um objeto é privado ou público. Famílias podem ser filtradas pelo nome do pai, mãe ou de uma criança, fontes pelo autor, e lugares e repositórios pelo seu tipo.
- **Filtro avançado** – um construtor de condições para filtros que os prontos não conseguem expressar, descrito [abaixo](#filtro-avançado).
- **GOQL** – um campo de texto para uma expressão na [Gramps Object Query Language](goql.md), com destaque de sintaxe. Digite a expressão e pressione Enter ou clique em **Aplicar**. Se a expressão for inválida, o campo é marcado como um erro. Uma expressão se aplica sobre os outros filtros.

Filtros ativos são mostrados como chips em uma linha abaixo da barra de ferramentas. Remova um único filtro clicando no botão de limpar do chip, ou use **Limpar todos os filtros** para removê-los todos de uma vez.

### Filtro avançado

Clique em **Filtro avançado** na parte inferior do painel de filtro para abrir o construtor de condições. Suas condições são as regras de filtro conhecidas do Gramps Desktop, como "Pessoas com o &lt;nome&gt;" ou "Antepassados de &lt;pessoa&gt;".

- Clique em **Adicionar condição** para escolher uma regra. As regras estão agrupadas em categorias e podem ser pesquisadas por nome ou descrição.
- Preencha os parâmetros da regra. Cada parâmetro tem uma entrada correspondente, por exemplo, um campo de data, um seletor de tag ou um seletor de objeto para uma pessoa ou lugar.
- Escolha como as condições de um grupo são combinadas: **Todas as condições**, **Qualquer condição**, ou – através do menu ao lado delas – **Exatamente uma condição**.
- Clique em **Adicionar grupo** para adicionar um grupo de condições dentro de outro grupo, com sua própria forma de combiná-las.
- Selecione **Não** em uma condição ou grupo para inverter.

Clique em **Aplicar** para filtrar a lista.

Os filtros prontos e a expressão GOQL que estão ativos quando você abre o construtor aparecem lá como condições. Uma expressão GOQL também pode ser adicionada como uma condição própria, por exemplo, para combinar várias expressões com **Qualquer condição**. Se o filtro que você constrói pode ser expresso com os filtros prontos, ele é mostrado com eles após a aplicação. Caso contrário, ele é mostrado como um único chip de **Filtro avançado**, e o painel de filtro oferece um botão **Editar** para reabrir o construtor.

!!! nota
    Regras que se referem a filtros personalizados salvos no Gramps Desktop não estão disponíveis no construtor. As regras são mostradas em seu idioma com a Gramps Web API 3.24 ou mais recente.

#### Filtros salvos

Para reutilizar um filtro que você construiu, clique em **Salvar** no construtor de condições e dê um nome a ele. Salvar sob um nome existente substitui esse filtro. **Filtros salvos** no construtor lista os filtros salvos para o tipo de objeto atual; escolher um carrega-o no construtor, onde você pode alterá-lo antes de clicar em **Aplicar**.

Filtros salvos são armazenados no seu navegador, por árvore genealógica e tipo de objeto, portanto, não estão disponíveis para outros usuários ou em seus outros dispositivos.

Um filtro salvo pode parar de funcionar quando a árvore muda, por exemplo, se ele se referir a uma pessoa que foi excluída desde então (o seletor de objeto então mostra "Não encontrado"). Tal filtro não pode ser aplicado ou salvo até que a condição seja corrigida.

## Selecionando objetos e agindo sobre eles em massa

Usuários com permissões de edição veem um botão **Selecionar** ao lado do botão de filtro. Clique nele para entrar no modo de seleção, que adiciona uma caixa de seleção a cada linha.

Marque os objetos que você deseja, e uma barra de ferramentas aparece mostrando quantos estão selecionados, junto com um menu suspenso **Ação** e um botão **Aplicar**.

A caixa de seleção no cabeçalho da tabela seleciona todos os objetos na página atual. Se mais objetos corresponderem aos filtros atuais, a barra de ferramentas então oferece **Selecionar Todos (N)**, que seleciona todos os N objetos correspondentes em todas as páginas. Desmarcar uma linha, mudar de página ou de filtros, ou sair do modo de seleção encerra essa seleção.

### Excluir

Selecione um ou mais objetos, escolha **Excluir** e clique em **Aplicar**. Uma caixa de diálogo de confirmação pede que você confirme, alertando que a ação não pode ser desfeita.

Excluir mais de dez objetos é executado como uma tarefa em segundo plano. Seu progresso é mostrado ao lado do botão **Aplicar** e em [Notificações](notifications.md), e a lista é recarregada quando estiver concluída.

!!! dica
    Exclusões são registradas no [histórico de revisões](revisions.md) como qualquer outra alteração, portanto, uma exclusão em massa equivocada pode ser revertida desfazendo a transação correspondente.

### Tags e privacidade

As ações **Adicionar Tag**, **Remover Tag** e **Privacidade** alteram todos os objetos selecionados de uma vez (requer Gramps Web API 3.26 ou mais recente):

- **Adicionar Tag** adiciona uma tag existente ou uma nova que você cria no diálogo.
- **Remover Tag** remove uma tag dos objetos selecionados que a possuem.
- **Privacidade** marca os objetos selecionados como privados ou públicos. Isso altera apenas os próprios objetos, não suas partes ou os registros aos quais eles estão vinculados – veja [Registros privados](privacy.md).

Assim como na exclusão, editar mais de dez objetos é executado como uma tarefa em segundo plano. As alterações são registradas no [histórico de revisões](revisions.md) como uma única transação, para que possam ser desfeitas juntas.

### Mesclar

Selecione **exatamente dois** objetos, escolha **Mesclar** e clique em **Aplicar**. Uma caixa de diálogo pergunta qual dos dois deve fornecer os dados primários para o objeto mesclado; clique naquele que você deseja manter como primário. Os dados do outro objeto são mesclados nele e as referências são atualizadas.

A mesclagem está disponível para pessoas, famílias, eventos, lugares, fontes e citações. Não está disponível para repositórios, notas e objetos de mídia.

Na visualização de mídia, a seleção funciona tanto no layout de galeria quanto no de lista: no modo de seleção, clicar em um tile ou linha alterna sua seleção. Objetos de mídia não podem ser mesclados.

Se você escolher uma ação sem uma seleção válida – por exemplo, uma mesclagem com apenas um objeto selecionado – uma caixa de diálogo explica o que é necessário.
