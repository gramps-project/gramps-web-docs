# Pesquisa

A página de pesquisa é acessível clicando no ícone da lupa na barra superior do aplicativo ou pressionando o atalho de teclado `s` [atalho de teclado](shortcuts.md).

## Pesquisa de texto completo

Digite uma consulta no campo de pesquisa. Os resultados aparecem à medida que você digita, a partir do segundo caractere; pressione Enter para pesquisar um único caractere. O Gramps Web pesquisa em todos os tipos de objeto – pessoas, famílias, eventos, lugares, fontes, citações, repositórios, notas e mídias – e retorna resultados correspondentes classificados por relevância. Para limpar a pesquisa, clique no botão de limpar no campo ou pressione Escape.

Cada resultado mostra o tipo de objeto, seu nome e alguns detalhes, por exemplo, o nascimento e a morte de uma pessoa, o casamento de uma família, o autor de uma fonte ou a primeira linha de uma nota. Clique em qualquer resultado para abrir a página de detalhes correspondente.

## Sintaxe de pesquisa

- **Todas as palavras devem corresponder.** `Müller Berlin` encontra objetos que contêm ambas as palavras.
- **`or`** encontra objetos que contêm qualquer uma das palavras, por exemplo, `Meyer or Maier`. `and` também pode ser digitado entre palavras, mas não faz diferença.
- `or` se aplica às palavras diretamente ao seu lado: `Meyer or Maier Berlin` significa "(Meyer or Maier) and Berlin". Parênteses não são suportados.
- **Aspas** correspondem a uma frase, ou seja, palavras nesta ordem: `"Johann Georg"`.
- **Coringa:** um `*` final corresponde a qualquer final, por exemplo, `Mey*` corresponde a "Meyer", "Meyers", "Meyerhofer", etc. Isso também funciona para frases: `"Johann Georg"*`.
- **A última palavra é completada.** Se a consulta termina em uma letra ou dígito, ela é pesquisada como se terminasse em `*`, então `Anna Smi` já encontra "Anna Smith". Para pesquisar a última palavra exatamente, termine a consulta com um espaço ou coloque a palavra entre aspas. O mesmo se aplica às caixas de pesquisa dos seletores de objeto e ao [mapa](map.md#search).
- `or` e `and` são reconhecidos em qualquer caso. Para pesquisar uma dessas palavras, coloque-a entre aspas.
- Palavras não podem ser excluídas; não há "não".

## O que a pesquisa encontra

- Acentos não precisam corresponder: "Müller" também encontra "Muller", e "muller" encontra "Müller".
- Famílias e eventos também são encontrados pelos nomes de suas pessoas, por exemplo, "Müller" encontra as famílias e eventos de todos os nomeados Müller. Esses resultados são classificados abaixo das correspondências diretas.
- Tipos padrão são encontrados pelos seus nomes na língua da sua interface, por exemplo, "Taufe" encontra batismos na interface em alemão.
- Underscores separam palavras, então "microfilm" encontra um arquivo de mídia chamado `scanned_microfilm.png`.
- Usuários que não podem visualizar registros privados não encontram objetos através de informações privadas, como uma família pelo nome de um membro privado.

## Filtrando por tipo de objeto

Abaixo do campo de pesquisa, botões de alternância para cada tipo de objeto (Pessoas, Famílias, Eventos, Lugares, …) permitem que você restrinja os resultados a um ou mais tipos específicos. Por padrão, todos os tipos são pesquisados. Ativar um ou mais botões de alternância restringe os resultados apenas a esses tipos.
