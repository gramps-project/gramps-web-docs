# Listas

Cada tipo de objeto no Gramps Web possui uma visualização em lista: Pessoas, Famílias, Eventos, Lugares, Fontes, Citações, Repositórios, Notas e Mídia. Todos funcionam da mesma forma e compartilham as mesmas ferramentas para ordenação, filtragem e edição em massa.

## Ordenação e paginação

Clique no cabeçalho de uma coluna para ordenar por essa coluna; clique novamente para inverter a ordem. A ordenação é realizada pelo servidor, portanto, aplica-se a toda a lista, não apenas à página que você está visualizando.

Listas longas são divididas em páginas. Use os controles de paginação na parte inferior para navegar entre elas.

Em telas estreitas, a tabela muda automaticamente para um layout compacto, para que as visualizações de lista permaneçam utilizáveis em um celular.

## Escolhendo colunas

Clique no ícone de engrenagem acima da lista para abrir o diálogo **Colunas**. Marque ou desmarque uma coluna para exibi-la ou ocultá-la. **Redefinir** restaura a seleção padrão para essa lista.

Pelo menos uma coluna deve permanecer visível, portanto, a última coluna restante não pode ser desmarcada.

Sua seleção de colunas é lembrada por tipo de objeto e por árvore genealógica. Ela é armazenada em seu navegador, portanto, não é visível para outros usuários – mas também não é transferida para um navegador ou dispositivo diferente.

## Filtragem

Clique no botão **filtrar** para abrir o painel de filtro. Um botão de alternância na parte superior do painel muda entre dois modos:

- **simples** – um conjunto de filtros prontos que dependem do tipo de objeto. Para pessoas, por exemplo, você pode filtrar por ano de nascimento, ano de falecimento, várias propriedades da pessoa, o número de associações, tags e se um objeto é privado ou público.
- **GQL** – um único campo de texto para uma consulta avançada na [Linguagem de Consulta Gramps](gql.md). Digite a consulta e pressione Enter ou clique em **Aplicar**. Se a consulta for inválida, a moldura do campo fica vermelha.

Filtros ativos são exibidos como chips acima da lista. Remova um único filtro clicando no botão de limpar do chip, ou use **Limpar todos os filtros** para removê-los todos de uma vez.

!!! nota
    Os dois modos são alternativos, não aditivos: uma consulta GQL substitui os filtros simples, e voltar ao modo simples descarta a consulta.

## Selecionando objetos e agindo sobre eles em massa

Usuários com permissões de edição veem um botão **Selecionar** ao lado do botão de filtro. Clique nele para entrar no modo de seleção, que adiciona uma caixa de seleção a cada linha.

Marque os objetos que deseja, e uma barra de ferramentas aparece mostrando quantos estão selecionados, juntamente com um menu suspenso de **Ação** e um botão **Aplicar**.

### Excluir

Selecione um ou mais objetos, escolha **Excluir** e clique em **Aplicar**. Uma caixa de diálogo de confirmação solicita que você confirme, alertando que a ação não pode ser desfeita.

!!! dica
    Exclusões são registradas no [histórico de revisões](revisions.md) como qualquer outra alteração, portanto, uma exclusão em massa equivocada pode ser revertida desfazendo a transação correspondente.

### Mesclar

Selecione **exatamente dois** objetos, escolha **Mesclar** e clique em **Aplicar**. Uma caixa de diálogo pergunta qual dos dois deve fornecer os dados primários para o objeto mesclado; clique naquele que você deseja manter como primário. Os dados do outro objeto são mesclados nele e as referências são atualizadas.

A mesclagem está disponível para pessoas, famílias, eventos, lugares, fontes e citações. Não está disponível para repositórios, notas e objetos de mídia.

Se você escolher uma ação sem uma seleção válida – por exemplo, uma mesclagem com apenas um objeto selecionado – uma caixa de diálogo explica o que é necessário.
