# Pesquisa

A página de pesquisa é acessível clicando no ícone de lupa na barra superior do aplicativo ou pressionando a tecla `s` [atalho de teclado](shortcuts.md).

## Pesquisa de texto completo

Digite qualquer consulta no campo de pesquisa e pressione Enter (ou clique no botão de pesquisa). O Gramps Web pesquisa em todos os tipos de objetos – pessoas, famílias, eventos, lugares, fontes, citações, repositórios, notas e mídias – e retorna resultados correspondentes classificados por relevância.

Os resultados mostram o tipo de objeto, nome e um breve resumo. Clique em qualquer resultado para abrir a página de detalhes correspondente.

## Sintaxe de pesquisa

- **Todas as palavras devem corresponder.** `Müller Berlin` encontra objetos que contêm ambas as palavras.
- **`ou`** encontra objetos que contêm qualquer uma das palavras, por exemplo, `Meyer ou Maier`. `e` também pode ser digitado entre as palavras, mas não faz diferença.
- `ou` se aplica às palavras diretamente ao lado: `Meyer ou Maier Berlin` significa "(Meyer ou Maier) e Berlin". Parênteses não são suportados.
- **Aspas** correspondem a uma frase, ou seja, palavras nesta ordem: `"Johann Georg"`.
- **Coringa:** um `*` no final corresponde a qualquer finalização, por exemplo, `Mey*` corresponde a "Meyer", "Meyers", "Meyerhofer", etc. Isso também funciona para frases: `"Johann Georg"*`.
- `ou` e `e` são reconhecidos em qualquer caso. Para pesquisar uma dessas palavras, coloque-a entre aspas.
- Palavras não podem ser excluídas; não há "não".

## O que a pesquisa encontra

- Acentos não precisam corresponder: "Müller" também encontra "Muller", e "muller" encontra "Müller".
- Famílias e eventos também são encontrados pelos nomes de suas pessoas, por exemplo, "Müller" encontra as famílias e eventos de todos os nomeados Müller. Esses resultados são classificados abaixo das correspondências diretas.
- Tipos padrão são encontrados pelos seus nomes na sua língua de interface, por exemplo, "Taufe" encontra batismos na interface em alemão.
- Underscores separam palavras, então "microfilm" encontra um arquivo de mídia chamado `scanned_microfilm.png`.
- Usuários que não podem visualizar registros privados não encontram objetos através de informações privadas, como uma família pelo nome de um membro privado.

## Filtrando por tipo de objeto

Abaixo do campo de pesquisa, botões de alternância para cada tipo de objeto (Pessoas, Famílias, Eventos, Lugares, …) permitem que você restrinja os resultados a um ou mais tipos específicos. Por padrão, todos os tipos são pesquisados. Ativar um ou mais botões de alternância restringe os resultados apenas a esses tipos.
