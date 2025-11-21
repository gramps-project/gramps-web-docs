# Trabalhando com correspondências de DNA

Correspondências de DNA são segmentos de DNA que concordam entre dois indivíduos, identificados pela presença de marcadores, os chamados SNPs (a sigla para polimorfismos de nucleotídeo único, pronunciado “snips”).

Para obter esses dados, você precisa de acesso a um teste de DNA que foi carregado em um banco de dados de correspondência que permite visualizar dados de correspondência de segmentos de DNA (por exemplo, MyHeritage, Gedmatch, FamilytreeDNA). O Gramps Web não realiza a correspondência em si, pois apenas tem acesso aos dados que você carrega.

## Inserindo dados de correspondência de DNA

Para inserir dados de correspondência de DNA, você precisa de [permissões de edição](../install_setup/users.md), pois os dados são armazenados como uma nota no banco de dados do Gramps. A visualização de DNA, acessível a partir do menu principal, fornece uma maneira conveniente de inserir esses dados no formato correto.

Para inserir uma nova correspondência, clique no botão + no canto inferior direito. Na caixa de diálogo que se abre, selecione os dois indivíduos. Observe que a “Primeira pessoa” e a “Segunda pessoa” são tratadas de maneira diferente: a correspondência é armazenada como uma associação da primeira para a segunda pessoa. Apenas a primeira pessoa será selecionável para a visualização de correspondência de DNA e o navegador de cromossomos. Normalmente, a primeira pessoa é aquela cujo teste de DNA você tem acesso e a segunda pessoa é um parente mais distante.

Se a segunda pessoa não estiver no banco de dados, você precisará criá-la primeiro usando o botão “Criar pessoa” no canto superior direito da interface do usuário. Depois de criar a pessoa, você pode retornar à visualização de correspondência de DNA e selecionar a pessoa recém-criada.

Em seguida, cole os dados brutos no campo de texto. Os dados devem ser uma tabela separada por vírgulas ou tabulações de correspondências, contendo tipicamente o número do cromossomo, a posição inicial e final da correspondência, o número de SNPs na correspondência e o comprimento da correspondência em unidades de centimorgans (cM). Você também pode arrastar e soltar um arquivo com os dados de correspondência no campo de texto.

Um exemplo mínimo de tal tabela é:

```csv
Cromossomo,Localização Inicial,Localização Final,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Se o formato for válido, uma pré-visualização é exibida abaixo do campo de texto como uma tabela.

Finalmente, clique no botão “Salvar” para armazenar a correspondência no banco de dados.

## Visualizando dados de correspondência de DNA

A visualização de correspondência de DNA possui um menu suspenso que permite selecionar cada pessoa no banco de dados que tem uma correspondência de DNA associada. Uma vez que uma pessoa é selecionada, os dados de correspondência de DNA são exibidos em uma tabela abaixo do menu suspenso. Ela mostra o nome da pessoa com a qual a correspondência está associada, a relação com a pessoa selecionada no menu suspenso (determinada automaticamente a partir do banco de dados do Gramps), o comprimento total de DNA compartilhado em centimorgans (cM), o número de segmentos compartilhados e o comprimento do maior desses segmentos.

Quando você clica em uma correspondência individual, abre uma página de detalhes mostrando todos os segmentos e se a correspondência está do lado materno ou paterno. Essas informações podem ser inseridas manualmente (fornecendo um `P` para paterno ou `M` para materno em uma coluna chamada `Lado` nos dados brutos) ou determinadas automaticamente pelo Gramps com base no ancestral comum mais recente.

## Editando uma correspondência

Você pode editar uma correspondência clicando no botão de lápis no canto inferior direito na visualização de detalhes da correspondência. Isso abre uma caixa de diálogo semelhante à de quando você cria uma nova correspondência, mas com os dados preenchidos. Observe que você pode alterar os dados brutos, mas não os indivíduos associados à correspondência – você precisa excluir a correspondência e criar uma nova se quiser alterar os indivíduos.

## Trabalhando com dados de correspondência no Gramps Desktop

Os dados de correspondência de DNA são armazenados como uma nota no banco de dados do Gramps. O formato é compatível com o 
[Addon Mapa de Segmentos de DNA](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
disponível para o Gramps Desktop. Sua página na wiki contém mais detalhes sobre como obter os dados, como interpretá-los e como inserir os dados no Gramps.

!!! info
    A API do Gramps Web v2.8.0 introduziu algumas mudanças para aceitar uma gama mais ampla de dados brutos de correspondência de DNA, que ainda não estão disponíveis no Addon do Gramps Desktop. O Addon do Gramps Desktop será atualizado no futuro para suportar os mesmos formatos também.
