# Pesquisa

A página de pesquisa é acessível clicando no ícone da lupa na barra superior do aplicativo, ou pressionando `s` [atalho de teclado](shortcuts.md).

## Pesquisa de texto completo

Digite qualquer consulta no campo de pesquisa e pressione Enter (ou clique no botão de pesquisa). O Gramps Web pesquisa em todos os tipos de objetos – pessoas, famílias, eventos, lugares, fontes, citações, repositórios, notas e mídias – e retorna resultados correspondentes classificados por relevância.

Os resultados mostram o tipo de objeto, nome e um breve resumo. Clique em qualquer resultado para abrir a página de detalhes correspondente.

Um `*` no final pode ser usado como um caractere curinga, por exemplo, `Mey*` corresponde a "Meyer", "Meyers", "Meyerhofer", etc.

## Filtrando por tipo de objeto

Abaixo do campo de pesquisa, botões de alternância para cada tipo de objeto (Pessoas, Famílias, Eventos, Lugares, …) permitem que você restrinja os resultados a um ou mais tipos específicos. Por padrão, todos os tipos são pesquisados. Ativar um ou mais botões de alternância restringe os resultados apenas a esses tipos.

## Pesquisa semântica

Se o administrador do servidor ativou a [pesquisa semântica (com inteligência artificial)](../install_setup/configuration.md), um botão de alternância de modo aparece no canto superior direito da página de pesquisa com duas opções:

- **Pesquisa** – pesquisa de texto completo padrão (o padrão)
- **Semântica** – pesquisa com inteligência artificial que entende o significado da sua consulta em vez de corresponder a palavras exatas

A pesquisa semântica é útil para consultas em linguagem natural, como "fazendeiro na Baviera no século XIX". Ela requer que o índice de pesquisa semântica esteja populado; consulte as [configurações de administração](../administration/settings.md) para saber como construir ou atualizar o índice.
