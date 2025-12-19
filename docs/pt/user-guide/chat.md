# Usando o chat de IA

!!! info
    O chat de IA requer a versão 2.5.0 ou superior da Gramps Web API e a versão 24.10.0 ou superior da Gramps Web.

A visualização do chat no Gramps Web (se disponível na sua instalação) dá acesso a um assistente de IA que pode responder perguntas sobre sua árvore genealógica.

!!! warning
    Como esta ainda é uma funcionalidade nova e em evolução, alguns tipos de perguntas funcionam bem enquanto outros não. Além disso, como em qualquer assistente de IA, ele pode fornecer respostas factualmente incorretas, então sempre verifique duas vezes.

## Como funciona

Para entender quais tipos de perguntas o assistente pode responder, é útil compreender como ele funciona por trás das cenas:

1. O usuário faz uma pergunta.
2. O Gramps Web identifica um número de (por exemplo, dez) objetos Gramps que provavelmente contêm as informações que respondem à pergunta. Para isso, utiliza uma técnica chamada "busca semântica". Por exemplo, se você perguntar "Qual é o nome dos filhos de John Doe?", se existir uma família com John Doe como pai, é provável que esteja entre os principais resultados.
3. O Gramps Web envia a pergunta do usuário junto com as informações de contexto recuperadas para um grande modelo de linguagem ("chatbot") e pede que ele extraia a resposta correta.
4. A resposta é exibida para o usuário.

## Como fazer uma pergunta

Devido à forma como o chat funciona, atualmente não é possível para o assistente de IA responder perguntas sobre relacionamentos específicos além de pais ou filhos, a menos que essa informação esteja contida como texto em uma nota.

Como cada resposta é baseada em um número limitado de principais resultados de busca semântica, ele também não pode responder perguntas sobre estatísticas ("quantas pessoas estão no meu banco de dados ...").

Para evitar ambiguidades e mal-entendidos, é útil formular a pergunta da forma mais detalhada possível.

Observe que grandes modelos de linguagem são multilíngues, então você pode se comunicar com ele em seu próprio idioma e ele responderá no mesmo idioma.

!!! tip
    Por favor, compartilhe sua experiência sobre o que funciona e o que não funciona com a comunidade.
