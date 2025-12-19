# Usando chat de IA

!!! info
    O chat de IA requer a versão 2.5.0 ou superior da API Gramps Web e a versão 24.10.0 ou superior do Gramps Web. A versão 3.6.0 da API Gramps Web introduziu capacidades de chamada de ferramentas para interações mais inteligentes.

A visualização do chat no Gramps Web (se disponível em sua instalação) dá acesso a um assistente de IA que pode responder perguntas sobre sua árvore genealógica.

!!! warning
    Como este ainda é um recurso novo e em evolução, alguns tipos de perguntas funcionam bem enquanto outros não. Além disso, como em qualquer assistente de IA, ele pode fornecer respostas factualmente incorretas, então tenha certeza de sempre verificar.

## Como funciona

Para entender quais tipos de perguntas o assistente pode responder, é útil entender como funciona por trás das cenas:

1. O usuário faz uma pergunta.
2. O assistente de IA pode usar várias abordagens para encontrar respostas:
   - **Busca Semântica**: O Gramps Web identifica objetos em sua árvore genealógica que provavelmente contêm informações relevantes. Por exemplo, se você perguntar "Qual é o nome dos filhos de John Doe?", famílias com John Doe como pai estarão entre os principais resultados.
   - **Chamada de Ferramentas (API Gramps Web v3.6.0+)**: O assistente pode consultar diretamente seu banco de dados usando ferramentas especializadas para pesquisar, filtrar pessoas/eventos/famílias/lugares por critérios específicos, calcular relacionamentos entre indivíduos e recuperar informações detalhadas.
3. O Gramps Web alimenta a pergunta junto com as informações recuperadas para um grande modelo de linguagem para formular uma resposta.
4. A resposta é exibida para você.

## O que você pode perguntar

Com as capacidades de chamada de ferramentas introduzidas na versão 3.6.0 da API Gramps Web, o assistente de IA agora pode lidar com perguntas mais complexas:

- **Relacionamentos familiares**: "Quem são os avós de Jane Smith?" ou "Como John Doe está relacionado a Mary Johnson?"
- **Pesquisas filtradas**: "Mostre-me todas as pessoas nascidas em Londres após 1850" ou "Quais eventos aconteceram em Paris?"
- **Consultas baseadas em datas**: "Quem morreu antes de 1900?" ou "Liste os casamentos que ocorreram entre 1920 e 1950"
- **Informações sobre lugares**: "Quais lugares estão na França?" ou "Fale-me sobre a Igreja de St. Mary"
- **Perguntas gerais**: "Qual é o nome dos filhos de John Doe?" ou "Quando nasceu Mary Smith?"

## Dicas para fazer perguntas

Para obter os melhores resultados do assistente de IA:

- **Seja específico**: Formule sua pergunta com o máximo de detalhes possível para evitar ambiguidades. Por exemplo, "Quando John Smith, nascido em 1850 em Boston, se casou?" é melhor do que "Quando John Smith se casou?"
- **Use nomes próprios**: Mencione nomes, lugares e datas específicos quando relevante.
- **Pergunte uma coisa de cada vez**: Divida perguntas complexas em partes mais simples para melhores resultados.
- **Use seu idioma**: Grandes modelos de linguagem são multilíngues, então você pode fazer perguntas em seu próprio idioma e receber respostas no mesmo idioma.

!!! tip
    Por favor, compartilhe sua experiência sobre o que funciona e o que não funciona com a comunidade.
