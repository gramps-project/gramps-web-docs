# Tags

Tags são rótulos que podem ser aplicados a qualquer objeto no banco de dados do Gramps – pessoas, famílias, eventos, lugares, fontes, citações, repositórios, notas e mídias. Elas são úteis para agrupar e filtrar objetos. As tags são armazenadas no banco de dados da árvore genealógica do Gramps e são compartilhadas entre todos os usuários; elas também são totalmente compatíveis com tags criadas no Gramps Desktop.

## Gerenciando tags

As tags são gerenciadas a partir da seção **Tags** das [Configurações de Administração](../administration/settings.md#tags), que está disponível apenas para usuários com o papel de Proprietário ou Administrador. Ela mostra todas as tags existentes e permite que você:

- **Crie** uma nova tag usando o botão **Nova Tag**
- **Renomeie** uma tag usando o ícone de editar (lápis)
- **Mude a cor** de uma tag usando o seletor de cores
- **Exclua** uma tag usando o ícone de excluir

!!! note
    Excluir uma tag a remove de todos os objetos a que foi aplicada.

## Aplicando tags a objetos

As tags podem ser aplicadas ou removidas de um objeto na sua página de detalhes quando estiver no modo de edição.

## Filtrando por tag

Todas as páginas de lista de objetos (Pessoas, Famílias, Eventos, Lugares, Fontes, Citações, Repositórios, Notas, Mídia) incluem um filtro de tags. Use-o para mostrar apenas objetos que têm uma tag específica aplicada.

## Tags especiais

Duas tags têm um significado especial no Gramps Web:

- **`Blog`** – qualquer fonte marcada como `Blog` é tratada como uma postagem de blog e aparece na visualização de [Blog](blog.md)
- **`ToDo`** – qualquer nota marcada como `ToDo` é tratada como uma tarefa de pesquisa e aparece na visualização de [Tarefas](tasks.md)

Essas tags são criadas automaticamente quando você usa pela primeira vez os recursos de Blog ou Tarefas. Renomeá-las ou excluí-las quebrará o recurso correspondente.
