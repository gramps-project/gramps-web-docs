# Pesquisa

A página de pesquisa é acessível clicando no ícone da lupa na barra superior do aplicativo, ou pressionando `s` [atalho de teclado](shortcuts.md).

## Pesquisa de texto completo

Digite qualquer consulta no campo de pesquisa e pressione Enter (ou clique no botão de pesquisa). O Gramps Web pesquisa em todos os tipos de objeto – pessoas, famílias, eventos, lugares, fontes, citações, repositórios, notas e mídias – e retorna resultados correspondentes classificados por relevância.

Os resultados mostram o tipo de objeto, nome e um breve resumo. Clique em qualquer resultado para abrir a página de detalhes correspondente.

Um `*` final pode ser usado como um caractere curinga, por exemplo, `Mey*` corresponde a "Meyer", "Meyers", "Meyerhofer", etc.

## Filtrando por tipo de objeto

Abaixo do campo de pesquisa, botões de alternância para cada tipo de objeto (Pessoas, Famílias, Eventos, Lugares, …) permitem que você restrinja os resultados a um ou mais tipos específicos. Por padrão, todos os tipos são pesquisados. Ativar um ou mais botões de alternância restringe os resultados apenas a esses tipos.

## Pesquisa semântica

!!! warning "Depreciado"
    A pesquisa semântica está depreciada e será removida na API do Gramps Web 3.25. A pesquisa de texto completo descrita acima não é afetada.

Se o administrador do servidor ativou a [pesquisa semântica (impulsionada por IA)](../install_setup/chat.md#semantic-search-deprecated), um botão de alternância de modo aparece no canto superior direito da página de pesquisa com duas opções:

- **Pesquisar** – pesquisa padrão de texto completo (o padrão)
- **Semântico** – pesquisa impulsionada por IA que entende o significado da sua consulta em vez de corresponder a palavras exatas

A pesquisa semântica é útil para consultas em linguagem natural, como "fazendeiro na Baviera no século 19". Ela requer que o índice de pesquisa semântica esteja populado; consulte [Configurações de administração](../administration/settings.md) para saber como construir ou atualizar o índice.
