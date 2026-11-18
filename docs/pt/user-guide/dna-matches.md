# Trabalhando com correspondências de DNA

As correspondências de DNA são segmentos de DNA que concordam entre dois indivíduos, identificados pela presença de marcadores, os chamados SNPs (o acrônimo para polimorfismos de nucleotídeo único, pronunciado “snips”).

Para obter esses dados, você precisa de acesso a um teste de DNA que esteja carregado em um banco de dados de correspondência que permita visualizar os dados de correspondência de segmentos de DNA (por exemplo, MyHeritage, Gedmatch, FamilytreeDNA). O Gramps Web não realiza a correspondência em si, pois apenas tem acesso aos dados que você carrega.

## Inserindo dados de correspondência de DNA

Para inserir dados de correspondência de DNA, você precisa de [permissões de edição](../install_setup/users.md), pois os dados são armazenados como uma nota no banco de dados do Gramps. A visualização de DNA, acessível a partir do menu principal, fornece uma maneira conveniente de inserir esses dados no formato correto.

Para inserir uma nova correspondência, clique no botão + no canto inferior direito. Na caixa de diálogo que se abre, selecione os dois indivíduos. Observe que a “Primeira pessoa” e a “Segunda pessoa” são tratadas de maneira diferente: a correspondência é armazenada como uma associação da primeira para a segunda pessoa. Apenas a primeira pessoa será selecionável para a visualização de correspondência de DNA e o navegador de cromossomos. Normalmente, a primeira pessoa é aquela cujo teste de DNA você tem acesso e a segunda pessoa é um parente mais distante.

Se a segunda pessoa não estiver no banco de dados, você precisa criá-la primeiro usando o botão “Criar pessoa” no canto superior direito da interface do usuário. Depois de criar a pessoa, você pode retornar à visualização de correspondência de DNA e selecionar a pessoa recém-criada.

Em seguida, cole os dados brutos no campo de texto. Os dados devem ser uma tabela de correspondências separada por vírgulas ou tabulações, contendo tipicamente o número do cromossomo, a posição inicial e final da correspondência, o número de SNPs na correspondência e o comprimento da correspondência em unidades de centimorgans (cM). Você também pode arrastar e soltar um arquivo com os dados de correspondência no campo de texto.

Um exemplo mínimo de tal tabela é:

```csv
Cromossomo,Localização Inicial,Localização Final,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Se o formato for válido, uma prévia é exibida abaixo do campo de texto como uma tabela.

Por fim, clique no botão “Salvar” para armazenar a correspondência no banco de dados.

## Visualizando dados de correspondência de DNA

A visualização de correspondência de DNA possui um menu suspenso que permite selecionar cada pessoa no banco de dados que tem uma correspondência de DNA associada. Uma vez que uma pessoa é selecionada, suas correspondências são listadas em uma tabela: o nome da correspondência, seu relacionamento com a pessoa selecionada, o comprimento total de DNA compartilhado em centimorgans (cM), o número de segmentos compartilhados e o comprimento do maior desses segmentos.

Para correspondências que já estão colocadas na árvore, a coluna de relacionamento mostra o relacionamento registrado na árvore (determinado automaticamente a partir do banco de dados do Gramps). Para correspondências que não estão relacionadas à pessoa selecionada na árvore, ela mostra o relacionamento estimado a partir do DNA compartilhado, marcado com "≈".

Clicar em uma correspondência abre sua página, com um resumo do DNA compartilhado, a [estimativa de relacionamento](#relationship-estimate), um gráfico do relacionamento na árvore e a lista de segmentos. Cada segmento mostra se está do lado paterno ou materno. O lado pode ser inserido manualmente (fornecendo um `P` para paterno ou `M` para materno em uma coluna chamada `Lado` nos dados brutos) ou determinado automaticamente a partir do ancestral comum mais recente. O botão de download ao lado dos segmentos os salva como um arquivo CSV no formato que a caixa de diálogo de correspondência aceita.

## Estimativa de relacionamento

O DNA compartilhado não é prova de um relacionamento específico: a quantidade de DNA que dois parentes compartilham varia bastante, e diferentes relacionamentos se sobrepõem. Portanto, o Gramps Web mostra uma gama de relacionamentos possíveis com suas probabilidades, calculadas a partir do número e dos comprimentos dos segmentos compartilhados (requer Gramps Web API 3.26 ou mais recente).

Os relacionamentos são agrupados por seu *grau*:

- **Pai ou filho** e **Irmão completo** são mostrados por conta própria.
- **Parente de grau 2** inclui meio-irmãos, avós e netos, e tias, tios, sobrinhas e sobrinhos.
- **Parente de grau 3** inclui primos de primeiro grau, bisavós, tias-avós e tios-avós, e meio-tias e meio-tios.
- Cada grau adicional é cerca de uma geração mais distante, por exemplo, primos de primeiro grau uma vez removidos são grau 4 e primos de segundo grau são grau 5. O grau 9 e além são agrupados como "9+".

Relacionamentos com o mesmo grau compartilham aproximadamente a mesma quantidade de DNA em média, portanto, o DNA sozinho não pode diferenciá-los. Use as idades das pessoas para decidir entre eles – um parente de grau 2 de 30 anos de idade de uma pessoa de 60 anos é mais provável que seja um sobrinho do que um avô.

A estimativa é mais confiável para parentes próximos. Para relacionamentos distantes, as correspondências compartilham apenas alguns segmentos, e as probabilidades se espalham por vários graus.

### Verificando a árvore em relação ao DNA

Se a correspondência estiver colocada na árvore, o Gramps Web verifica se o DNA compartilhado se encaixa no relacionamento registrado lá. Se o DNA for muito improvável para aquele relacionamento, um ícone de aviso é exibido na tabela de correspondências e um aviso na página da correspondência. O número entre parênteses, por exemplo, "1 : 500", compara quão provável é o DNA para o relacionamento registrado com quão provável é para o relacionamento mais provável.

Um aviso é um motivo para olhar mais de perto, não prova de um erro. Causas comuns são:

- um erro na árvore, como um pai errado,
- uma paternidade atribuída incorretamente, por exemplo, uma adoção desconhecida ou um pai biológico diferente,
- dados de correspondência incompletos, por exemplo, se apenas segmentos acima de um alto limiar foram copiados do serviço de teste,
- relacionamentos por mais de uma linha, por exemplo, pessoas relacionadas por meio de sua mãe e pai ("colapso de pedigree"), que compartilham mais DNA do que o esperado.

Relacionamentos que não são por nascimento, como por meio de uma adoção, não são verificados.

## Editando uma correspondência

Para editar uma correspondência, abra sua página e clique no botão de edição, ou pressione `e`. Observe que você pode alterar os dados brutos, mas não os indivíduos associados à correspondência – você precisa excluir a correspondência e criar uma nova se quiser alterar os indivíduos.

## Correspondências privadas

As caixas de diálogo para adicionar e editar uma correspondência têm um interruptor **Privado**. Uma correspondência privada, incluindo seus segmentos, é ocultada de usuários que não podem visualizar registros privados. Correspondências privadas são marcadas com um cadeado para todos os outros. Veja [Registros privados](privacy.md) para mais informações sobre privacidade.

## Trabalhando com dados de correspondência no Gramps Desktop

Os dados de correspondência de DNA são armazenados como uma nota no banco de dados do Gramps. O formato é compatível com o 
[Addon do Mapa de Segmentos de DNA](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
disponível para o Gramps Desktop. Sua página na wiki contém mais detalhes sobre como obter os dados, como interpretá-los e como inserir os dados no Gramps.

!!! info
    A Gramps Web API v2.8.0 introduziu algumas mudanças para aceitar uma gama mais ampla de dados brutos de correspondência de DNA, que ainda não estão disponíveis no Addon do Gramps Desktop. O Addon do Gramps Desktop será atualizado no futuro para suportar os mesmos formatos também.
