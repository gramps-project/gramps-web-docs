# Usando o Assistente de IA

!!! info
    O Assistente de IA requer a versão 2.5.0 ou superior da API Web do Gramps e a versão 24.10.0 ou superior do Gramps Web. A versão 3.6.0 da API Web do Gramps introduziu capacidades de chamada de ferramentas para interações mais inteligentes.

A visão **Assistente** no Gramps Web (se disponível na sua instalação, rotulada como "Chat" em versões mais antigas) dá acesso a um assistente de IA que pode responder perguntas sobre sua árvore genealógica.

!!! warning
    Como esta ainda é uma funcionalidade nova e em evolução, alguns tipos de perguntas funcionam bem enquanto outros não. Além disso, como acontece com qualquer assistente de IA, ele pode fornecer respostas factualmente incorretas, então sempre verifique duas vezes.

## Como funciona

Para entender quais tipos de perguntas o assistente pode responder, é útil entender como ele funciona por trás das cenas:

1. O usuário faz uma pergunta.
2. O assistente consulta diretamente seu banco de dados usando ferramentas especializadas: ele pesquisa a árvore com a [pesquisa de texto completo](search.md), filtra pessoas/eventos/famílias/lugares por critérios específicos, calcula relacionamentos entre indivíduos e busca registros completos, incluindo suas notas.
3. Um grande modelo de linguagem formula uma resposta com base nos registros que encontrou.
4. A resposta é exibida para você, com links para os registros nos quais se baseia.

Em servidores que executam uma versão da API Web do Gramps anterior à 3.24, o assistente também dependia da pesquisa semântica, que está sendo descontinuada.

Enquanto o assistente está trabalhando, indicadores mostram quais ferramentas ele está usando atualmente (por exemplo, buscando pessoas, procurando relacionamentos), para que você possa acompanhar enquanto ele constrói sua resposta. Perguntas que levam mais tempo para serem processadas são tratadas como tarefas em segundo plano – você pode navegar para longe e voltar, e o progresso também é refletido em [Notificações](notifications.md). As respostas são formatadas com Markdown (listas, ênfase, links, etc.) para facilitar a leitura.

## O que você pode perguntar

Com as capacidades de chamada de ferramentas introduzidas na versão 3.6.0 da API Web do Gramps, o assistente de IA agora pode lidar com perguntas mais complexas:

- **Relacionamentos familiares**: "Quem são os avós de Jane Smith?" ou "Como John Doe está relacionado a Mary Johnson?"
- **Pesquisas filtradas**: "Mostre-me todas as pessoas nascidas em Londres após 1850" ou "Quais eventos aconteceram em Paris?"
- **Consultas baseadas em datas**: "Quem morreu antes de 1900?" ou "Liste os casamentos que ocorreram entre 1920 e 1950"
- **Informações sobre lugares**: "Quais lugares estão na França?" ou "Conte-me sobre a Igreja de St. Mary"
- **Perguntas gerais**: "Qual é o nome dos filhos de John Doe?" ou "Quando Mary Smith nasceu?"

## Dicas para fazer perguntas

Para obter os melhores resultados do assistente de IA:

- **Seja específico**: Formule sua pergunta com o máximo de detalhes possível para evitar ambiguidades. Por exemplo, "Quando John Smith, nascido em 1850 em Boston, se casou?" é melhor do que "Quando John Smith se casou?"
- **Use nomes próprios**: Mencione nomes, lugares e datas específicos quando relevante.
- **Pergunte uma coisa de cada vez**: Divida perguntas complexas em partes mais simples para melhores resultados.
- **Use sua língua**: Grandes modelos de linguagem são multilíngues, então você pode fazer perguntas em sua própria língua e receber respostas na mesma língua.

!!! tip
    Por favor, compartilhe sua experiência sobre o que funciona e o que não funciona com a comunidade.
