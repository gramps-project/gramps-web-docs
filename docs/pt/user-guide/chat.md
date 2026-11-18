# Usando o Assistente de IA

A visualização **Assistente** no Gramps Web (se habilitada na sua instalação) dá acesso a um assistente de IA que responde perguntas sobre sua árvore genealógica.

!!! warning
    Assim como qualquer assistente de IA, as respostas podem estar erradas. Use os links na resposta para verificar os registros nos quais se baseia.

## Como funciona

O assistente não conhece sua árvore de antemão. Para responder a uma pergunta, um modelo de linguagem grande procura os registros necessários, assim como você faria:

- ele pesquisa a árvore com a [pesquisa de texto completo](search.md),
- ele filtra pessoas, eventos e famílias por critérios como nomes, datas, lugares ou o número de filhos,
- ele encontra ancestrais, descendentes e outros parentes de uma pessoa, com seu relacionamento,
- ele lê registros completos de pessoas, famílias, eventos, lugares e notas.

Ele então responde com base nos registros que encontrou, com links para eles. Enquanto está trabalhando, as ferramentas que está usando são mostradas, para que você possa acompanhar. Perguntas que levam mais tempo são executadas em segundo plano – você pode navegar para longe e voltar.

O assistente responde apenas com base na sua árvore, não no conhecimento geral do modelo de linguagem – mesmo sobre pessoas bem conhecidas. Se a árvore não registrar algo, ele diz isso, mencionando informações relacionadas que encontrou, por exemplo, em uma nota. Ele só vê o que você tem permissão para ver: links para registros privados são mostrados como texto simples para usuários que não podem visualizá-los.

Perguntas de acompanhamento mantêm o contexto de perguntas anteriores na mesma conversa, para que você possa perguntar "E quando ele morreu?" após perguntar sobre uma pessoa.

## O que você pode perguntar

- **Fatos sobre pessoas**: "Quando nasceu Mary Smith?" ou "Quais são os nomes dos filhos de John Doe?"
- **Parentes**: "Quem são os avós de Jane Smith?" ou "Quais descendentes de Johann Meyer emigraram para a América?"
- **Pesquisas com critérios**: "Quem nasceu em Londres após 1850?", "Liste casamentos entre 1920 e 1950", ou "Quais casais tiveram cinco ou mais filhos?"
- **Lugares**: "Quais eventos aconteceram em Paris?" ou "Quem nasceu na Dinamarca?" – lugares dentro de um lugar maior estão incluídos.
- **Notas**: "O que as notas dizem sobre a fazenda da família Meyer?"

Perguntas que precisam da árvore inteira de uma vez, como "Qual é o nome próprio mais comum?", funcionam menos bem, já que o assistente vê apenas um número limitado de registros por pesquisa.

## Perguntando sobre imagens

Se o administrador do servidor habilitou, o prompt tem um botão para anexar imagens. Você também pode colar uma imagem ou arrastar arquivos de imagem para o prompt. Até quatro imagens podem ser anexadas a uma pergunta, por exemplo, um escaneamento de um registro de igreja para perguntar "Quem é mencionado nesta entrada, e eles estão na minha árvore?"

As imagens são enviadas apenas com a pergunta à qual estão anexadas. Perguntas de acompanhamento podem se referir ao que o assistente disse sobre elas, mas não às próprias imagens, então anexe-as novamente se necessário. Se sua árvore tem um limite de uso de IA, cada imagem conta como uma pergunta adicional.

## Permitindo que o assistente mude sua árvore

Se o administrador do servidor habilitou, editores, proprietários e administradores podem pedir ao assistente para mudar a árvore, por exemplo, "Adicione um batismo em 3 de maio de 1802 em St. Mary's para Johann Meyer" ou "Corrija o ano de nascimento de Anna Smith, deve ser 1871".

O assistente nunca muda nada por conta própria. Ele responde com um cartão de **Mudanças propostas** que lista cada registro que ele adicionaria, editária ou excluiria, com os valores antigos riscado e os novos valores destacados. Nada acontece até que você clique em **Aplicar**. As mudanças são então feitas em um único passo, que você pode desfazer como qualquer outra edição, a partir da mensagem que aparece ou na [história de revisões](revisions.md).

Verifique uma proposta cuidadosamente antes de aplicá-la – em particular, se o assistente escolheu a pessoa certa, e se ele não adicionou um novo registro (como um lugar ou fonte) que já existe na sua árvore sob um nome ligeiramente diferente. Se uma proposta não estiver exatamente certa, diga o que mudar, e o assistente proporá novamente.

Uma vez que uma proposta foi aplicada, propostas mais antigas na mesma conversa não podem mais ser aplicadas, já que foram feitas para a árvore como estava antes. O mesmo acontece se um dos registros afetados foi alterado nesse meio tempo.

## Dicas para fazer perguntas

- **Nomeie as pessoas.** O assistente não sabe quem você é ou quem é sua pessoa de referência, então em vez de "minha avó", pergunte sobre "a avó de Anna Smith (nascida em 1950)". Você também pode usar IDs do Gramps, por exemplo, "os filhos de I0042".
- **Seja específico** quando os nomes são comuns: "Quando o John Smith nascido em 1850 em Boston se casou?" é melhor do que "Quando John Smith se casou?"
- **Use seu idioma.** Você pode perguntar em seu próprio idioma e receber respostas no mesmo idioma.
- **Pergunte novamente de forma diferente** se uma resposta parecer incompleta – por exemplo, nomeando o lugar ou período de tempo que você está interessado.

!!! tip
    Por favor, compartilhe sua experiência sobre o que funciona e o que não funciona com a comunidade.
