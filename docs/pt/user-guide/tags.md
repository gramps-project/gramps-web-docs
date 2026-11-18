# Tags

Tags são rótulos que podem ser aplicados a qualquer objeto no banco de dados do Gramps – pessoas, famílias, eventos, lugares, fontes, citações, repositórios, notas e mídias. Elas são úteis para agrupar e filtrar objetos. As tags são armazenadas no banco de dados da árvore genealógica do Gramps e são compartilhadas entre todos os usuários; elas também são totalmente compatíveis com tags criadas no Gramps Desktop.

## Gerenciando tags

As tags são gerenciadas na seção **Tags** das [Configurações de Administração](../administration/settings.md#tags), que está disponível apenas para usuários com o papel de Proprietário ou Administrador. Ela mostra todas as tags existentes e permite que você:

- **Crie** uma nova tag usando o botão **Nova Tag**
- **Renomeie** uma tag usando o ícone de editar (lápis)
- **Mude a cor** de uma tag usando o seletor de cores
- **Delete** uma tag usando o ícone de deletar

!!! note
    Deletar uma tag a remove de todos os objetos aos quais foi aplicada.

## Aplicando tags a objetos

As tags podem ser aplicadas ou removidas de um objeto na sua página de detalhes quando em modo de edição. Para marcar muitos objetos de uma vez, selecione-os em uma lista e use a ação **Adicionar Tag** ou **Remover Tag**, veja [Listas](lists.md#tags-and-privacy).

As tags são exibidas na coluna **Tags** das listas, e nos resultados de busca, favoritos e histórico. Se uma lista não mostrar a coluna, ative-a no seletor de colunas.

## Filtrando por tag

Todas as [páginas de lista de objetos](lists.md) (Pessoas, Famílias, Eventos, Lugares, Fontes, Citações, Repositórios, Notas, Mídia) incluem um filtro de tags. Use-o para mostrar apenas objetos que têm uma tag específica aplicada.

## Tags especiais

Duas tags têm um significado especial no Gramps Web:

- **`Blog`** – qualquer fonte marcada como `Blog` é tratada como uma postagem de blog e aparece na visualização de [Blog](blog.md)
- **`ToDo`** – qualquer nota marcada como `ToDo` é tratada como uma tarefa de pesquisa e aparece na visualização de [Tarefas](tasks.md)

Essas tags são criadas automaticamente quando você usa pela primeira vez os recursos de Blog ou Tarefas. Renomeá-las ou deletá-las quebrará o recurso correspondente.
