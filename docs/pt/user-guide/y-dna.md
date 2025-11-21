# Usando o Gramps Web para Análise de Y-DNA

!!! note "Nota"
    Este recurso requer a versão 3.3.0 ou posterior da API do Gramps Web e a versão 25.9.0 ou posterior do frontend do Gramps Web.

A visualização de Y-DNA no Gramps Web pode usar dados brutos de polimorfismo de nucleotídeo único (SNP) do cromossomo Y para determinar o haplogrupo Y-DNA mais provável de uma pessoa e exibir os ancestrais derivados na árvore do cromossomo Y humano, juntamente com estimativas de tempo.

## Como obter e armazenar os dados SNP de Y-DNA

Para obter os dados SNP de Y-DNA, você precisa realizar um teste de Y-DNA através de um serviço de testes genéticos. O resultado é representado como um conjunto de mutações (SNPs), cada uma identificada por uma string (por exemplo, `R-BY44535`) e um sinal `+` ou `-` indicando se a mutação está presente ou ausente. O Gramps Web espera a string de todos os SNPs testados no formato `SNP1+, SNP2-, SNP3+,...` para ser armazenada em um atributo de pessoa de tipo personalizado `Y-DNA` (sensível a maiúsculas e minúsculas). Você pode criar manualmente esse atributo no Gramps Web ou no Gramps Desktop, ou navegar até a visualização de Y-DNA no Gramps Web e clicar no botão azul "Adicionar", selecionar a pessoa para a qual adicionar os dados e colar a string SNP. Em qualquer caso, os dados serão armazenados como um atributo de pessoa em seu banco de dados Gramps.

[Veja abaixo](#instruções-para-obter-dados-snp-de-serviços-de-teste) para instruções sobre como obter os dados SNP de vários serviços de teste.

## Como funciona

Uma vez que uma pessoa tenha um atributo `Y-DNA` contendo os dados SNP, o Gramps Web usará a biblioteca Python de código aberto [yclade](https://github.com/DavidMStraub/yclade) para determinar a posição mais provável da pessoa na árvore do cromossomo Y humano. A árvore foi criada pelo projeto [YFull](https://www.yfull.com/) com base em dezenas de milhares de testes de Y-DNA. Observe que o Gramps Web usa uma cópia local da árvore YFull, portanto, nenhum dado é enviado a terceiros.

A árvore é percorrida da raiz até as folhas, e em cada nó, os SNPs associados a esse nó são comparados aos SNPs testados positivamente e negativamente da pessoa, e o ramo apropriado é seguido.

O resultado final é uma sucessão de clados da raiz da árvore (o [“Adão” cromossômico Y](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) até o clado mais derivado que é consistente com os dados SNP da pessoa. Cada clado tem uma idade estimada com base nas idades das amostras no banco de dados YFull que pertencem a esse clado.

Como os cromossomos Y são herdados de pai para filho, essa sucessão corresponde a um trecho da ancestralidade patrilinear da pessoa.

## Como interpretar os resultados

A informação mais importante é o haplogrupo mais provável da pessoa, mostrado na parte superior da página. O nome está vinculado à página correspondente no site [YFull](https://www.yfull.com/), que contém mais informações, como o país de origem das amostras testadas pertencentes a esse haplogrupo.

Na árvore de ancestrais patrilineares mostrada no Gramps Web, a caixa diretamente acima da pessoa testada é o ancestral comum mais recente (MRCA) de todas as amostras testadas pertencentes ao haplogrupo da pessoa. A data mostrada para esse ancestral é sua data de nascimento aproximada estimada. O ancestral acima dele é o ancestral onde a mutação que define esse haplogrupo apareceu pela primeira vez.

Devido à lenta taxa de mutação dos cromossomos Y, o MRCA pode estar muitos centenas de anos no passado. Para haplogrupos raros (ou seja, haplogrupos onde poucas pessoas foram testadas até agora), pode até ser milhares de anos.

## Instruções para obter dados SNP de serviços de teste

### [YSEQ](https://www.yseq.net/)

Uma vez logado em "Minha Conta", vá para "Meus Resultados / Ver meus Alelos" e navegue até o final da página. O campo de texto "Lista de alelos compacta" foi adicionado especificamente para o Gramps Web e está exatamente no formato certo para colar no atributo `Y-DNA`.
