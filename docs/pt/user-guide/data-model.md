# Como o Gramps organiza dados

O Gramps Web armazena uma árvore genealógica não como um gráfico, mas como objetos separados – pessoas, famílias, eventos, lugares, fontes, e assim por diante – que estão interligados. Uma vez que você saiba como esses objetos se encaixam, inserir dados se torna previsível: qualquer coisa que você queira vincular deve existir primeiro.

O Gramps Web usa o mesmo modelo de dados que o Gramps Desktop, então tudo nesta página se aplica a ambos.

## Os blocos de construção

| Objeto | O que representa | Exemplos |
|---|---|---|
| Pessoa | Um indivíduo | Você, sua avó |
| Família | Um casal, seus filhos, ou ambos | Seus pais e seus filhos |
| Evento | Algo que aconteceu, com uma data e um lugar | Nascimento, casamento, censo, emigração |
| Lugar | Uma localização geográfica | Uma vila, uma paróquia, um país |
| Fonte | Um documento ou coleção de informações | Um registro de paróquia, um censo, um livro |
| Citação | Uma referência específica dentro de uma fonte | Página 12, entrada 3 do registro da paróquia |
| Repositório | Onde uma fonte é mantida | Um arquivo, uma biblioteca, um site |
| Nota | Texto livre | Uma transcrição, observações de pesquisa |
| Objeto de mídia | Um arquivo | Uma foto, um certificado escaneado |

Cada tipo de objeto tem sua própria lista no Gramps Web, veja [Listas](lists.md).

## Pessoas e famílias

Pais e filhos não estão vinculados diretamente entre si, mas através de uma **família**. Uma família tem até dois parceiros e qualquer número de filhos:

- Seus pais e você estão vinculados através da família na qual você é uma criança.
- Seus irmãos são os outros filhos da mesma família.
- Você e seu cônjuge formam outra família, na qual você é um parceiro, junto com seus filhos.

Uma pessoa pode ser uma criança em uma família e um parceiro em várias. Cada filho tem um relacionamento com cada um dos pais, como nascimento, adoção ou enteado, e cada família tem um tipo de relacionamento, como casado ou união civil.

É por isso que "adicionar pais" a uma pessoa significa adicionar a pessoa como uma criança a uma família – o que o [gráfico da árvore](tree-edit.md) faz por você em um passo.

## Eventos

Um nascimento, morte ou casamento não é um campo de uma pessoa, mas um **evento** próprio, com um tipo, uma data, um lugar e uma descrição. As pessoas estão vinculadas a um evento com um **papel**: a pessoa cujo nascimento é tem o papel de "Primário", enquanto alguém mais pode estar vinculado ao mesmo evento como uma testemunha.

Eventos que dizem respeito a um casal, como um casamento, pertencem à família em vez de a qualquer um dos parceiros. Um evento também pode ser compartilhado por várias pessoas – por exemplo, um registro de censo listando um lar inteiro – em vez de ser inserido uma vez por pessoa.

## Objetos compartilhados: lugares e fontes

Lugares, fontes, citações, repositórios, notas e objetos de mídia existem por si mesmos, e qualquer número de outros objetos pode se referir ao mesmo. Isso tem algumas consequências:

- **Criar uma vez, selecionar muitas vezes.** A vila onde dez de seus ancestrais nasceram é um lugar, selecionado em dez eventos de nascimento. Se você corrigir seu nome ou coordenadas, a correção se aplica em todos os lugares.
- **Crie antes de selecionar.** Formulários no Gramps Web selecionam lugares e fontes que já existem. Crie um novo lugar ou fonte primeiro usando o botão **+** (Adicionar) na barra de aplicativos superior.
- **Lugares são aninhados.** Um lugar pode ser contido por um maior – uma vila por um condado, o condado por um país – então você não precisa repetir toda a hierarquia para cada vila.
- **Fontes e citações são separadas.** Uma fonte é o registro da paróquia como um todo; uma citação é a entrada específica que apoia um fato, com sua página, data e sua confiança nela. Muitas citações podem apontar para a mesma fonte.

Se você acidentalmente criou o mesmo lugar ou fonte duas vezes, você pode [mesclar os duplicados](lists.md#merge).

## A Pessoa Principal

A Pessoa Principal é a pessoa a partir da qual os gráficos da árvore genealógica começam e o ponto de partida padrão para relatórios. Veja [Primeiro login](first-login.md) para saber como configurá-la.

!!! note "Diferente do Gramps Desktop"
    No Gramps Desktop, a Pessoa Principal é armazenada no banco de dados da árvore genealógica, então é a mesma para todos que abrem esse banco de dados. O Gramps Web não a utiliza. Em vez disso, a Pessoa Principal é armazenada em seu navegador, separadamente para cada árvore: não é compartilhada com outros usuários, e não a acompanha para um navegador ou dispositivo diferente. Após importar uma árvore do Gramps Desktop, ou quando você usa o Gramps Web em outro dispositivo, você precisa configurá-la novamente.

## Uma ordem recomendada

Ao inserir uma nova família manualmente, esta ordem evita saltos entre formulários:

1. **Lugares e fontes.** Crie os lugares que você precisa e, se você registrar fontes, a fonte da qual você está trabalhando.
2. **Pessoas.** Adicione as pessoas com suas datas e lugares de nascimento e morte. Isso é mais rápido no modo de edição do gráfico da Árvore Genealógica, que cria as famílias para você – veja [Começar uma nova árvore](start-tree.md) e [Editando a árvore genealógica](tree-edit.md).
3. **Eventos adicionais.** Abra uma família (por exemplo, a partir da aba de Relacionamentos de uma pessoa) para adicionar o casamento, e a página de uma pessoa para adicionar outros eventos.
4. **Citações.** Na aba de Citações de Fonte da pessoa, evento ou outro objeto que uma fonte apoia, adicione uma nova citação, selecione a fonte e insira a página.
5. **Notas e mídia.** Anexe transcrições, fotos e escaneamentos – veja [Adicionar arquivos de mídia](media.md).

## Inserindo datas

Uma data é inserida como campos separados de ano, mês e dia, que também podem ser preenchidos usando um seletor de data. Deixe de fora as partes que você não sabe: um ano sozinho é uma data válida.

Em vez de adivinhar um dia exato, descreva o que você realmente sabe com o **Tipo** da data:

| O que você sabe | Tipo | Exemplo |
|---|---|---|
| A data exata, ou parte dela | Regular | 12 de março de 1850, ou apenas 1850 |
| Uma data aproximada | cerca de | cerca de 1850 |
| Um limite | antes, depois | antes de 1900 |
| A data está em algum lugar dentro de um período | Intervalo | entre 1850 e 1855 |
| Algo durou por um período | Duração | de 1850 a 1855 |
| Apenas o início ou o fim de um período | de, até | de 1850 |

O campo **Qualidade** registra como você chegou a uma data: "Estimado" para uma suposição educada, "Calculado" para uma data derivada de outras informações, como um ano de nascimento calculado a partir de uma idade na morte.

!!! warning "Datas sobre e estimadas cobrem 50 anos para cada lado"
    Quando o Gramps compara datas, ele trata uma data do tipo "cerca de" – e qualquer data com a qualidade "Estimado" – como um intervalo que vai de 50 anos antes a 50 anos depois da data dada. Por exemplo, filtrar a lista de Pessoas para pessoas nascidas entre 1840 e 1860 também encontra uma pessoa nascida "cerca de 1880", porque essa data é considerada como cobrindo 1830 a 1930. Da mesma forma, "antes" e "depois" são considerados como abrangendo até 50 anos antes ou depois da data.

    Isso pode levar a resultados surpreendentes, então use "cerca de" e "Estimado" apenas quando você não puder restringir a data. Se você souber um período mais curto, um Intervalo como "entre 1878 e 1882" é mais preciso.

O campo **Calendário** permite que você insira uma data no calendário usado no registro original, como o calendário juliano, em vez de convertê-la você mesmo.
