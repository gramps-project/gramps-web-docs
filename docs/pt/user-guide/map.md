# Mapa

A página do Mapa exibe todos os lugares em sua árvore genealógica como marcadores interativos em um mapa geográfico. Ela é acessível pela barra lateral.

## Marcadores de lugar

Apenas os lugares que têm coordenadas GPS armazenadas no banco de dados do Gramps são mostrados no mapa. Lugares sem coordenadas são omitidos silenciosamente. As coordenadas GPS podem ser definidas na página de detalhes do lugar (edite o lugar e preencha os campos de latitude e longitude).

!!! dica
    Se muitos dos seus lugares estiverem faltando no mapa, abra a página de detalhes de um lugar e verifique se a latitude e a longitude estão definidas. Você pode adicionar ou corrigir coordenadas diretamente na visualização de edição do lugar.

Cada lugar com coordenadas é mostrado como um marcador. Clicar em um marcador abre um cartão de resumo mostrando o nome do lugar e seus eventos e pessoas vinculados. Clique no nome do lugar no cartão para abrir a página completa de detalhes do lugar.

## Pesquisa

A caixa de pesquisa no canto superior esquerdo do mapa pesquisa enquanto você digita e agrupa os resultados sob três cabeçalhos:

- **Lugares** – lugares em sua árvore genealógica. Selecionar um faz com que o mapa se mova para ele e destaque seu marcador.
- **Pessoas** – pessoas em sua árvore genealógica. Selecionar uma muda o mapa para a visualização da pessoa descrita [abaixo](#seguindo-uma-pessoa-pelo-mapa).
- **Externo** – locais do [OpenStreetMap](https://www.openstreetmap.org/), para qualquer lugar do mundo. Selecionar um simplesmente move e aproxima o mapa para aquele local; não filtra nem altera os lugares da sua árvore.

Os resultados externos também são úteis ao adicionar coordenadas a um lugar: você pode procurar a localização aqui para ver onde ela está antes de inserir sua latitude e longitude.

## Seguindo uma pessoa pelo mapa

Selecionar uma pessoa – a partir da caixa de pesquisa do mapa ou com o botão **Abrir no mapa** na página de detalhes de uma pessoa – mostra os lugares conectados aos eventos daquela pessoa, unidos por linhas em ordem cronológica. Pequenas setas ao longo de cada linha indicam a direção da viagem, para que você possa seguir a vida de uma pessoa desde o nascimento até a morte pelo mapa.

Lugares em uma página de detalhes de lugar também têm um botão **Abrir no mapa**, que abre o mapa centrado naquele lugar.

## Controle deslizante de tempo

O controle deslizante de tempo na parte inferior da página filtra quais marcadores de lugar são mostrados com base no ano de seus eventos associados:

- Arraste a alça para selecionar um ano.
- Apenas lugares vinculados a eventos que caem dentro da janela de tempo selecionada são mostrados.
- Use isso para traçar onde seus ancestrais viveram em um determinado ponto da história.

## Camadas do mapa

Um botão de alternância de camadas (ícone de camadas empilhadas, canto inferior esquerdo) permite que você escolha entre dois mapas base:

### Mapa Base

A camada padrão, alimentada pelo [OpenFreeMap](https://openfreemap.org) (estilo Liberty para modo claro, estilo escuro para modo escuro). Este é um mapa moderno de uso geral adequado para localizar lugares.

### Mapa Histórico

Muda o mapa base para o [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), um projeto comunitário que mapeia o mundo como ele existia em diferentes pontos no tempo – pense nisso como um contraparte histórica do OpenStreetMap.

Quando a camada do Mapa Histórico está ativa, o controle deslizante de tempo também filtra os próprios blocos do mapa: o OHM renderiza o mapa como ele apareceu no ano selecionado, então fronteiras históricas, nomes de lugares e características são mostrados em vez das modernas. Isso torna possível ver tanto a localização do seu ancestral quanto o contexto geográfico e político contemporâneo em uma única visualização.

!!! nota
    A cobertura do OpenHistoricalMap varia por região e período. Áreas ou épocas com contribuições escassas podem mostrar detalhes históricos limitados. Se você notar dados históricos ausentes ou imprecisos, considere [contribuir para o OpenHistoricalMap](https://www.openhistoricalmap.org) – é um projeto comunitário aberto que qualquer um pode editar.

## Sobreposições de mapa personalizadas

Além das camadas base integradas, você pode transformar qualquer imagem de mapa histórico escaneada – armazenada no Gramps como um objeto **Mídia** – em uma sobreposição personalizada posicionada no mapa ao vivo. Isso é útil para escaneamentos de antigos planos de cidades, mapas de paróquias ou mapas de propriedades que você deseja comparar diretamente com a geografia moderna ou histórica.

### Georreferenciando uma imagem

1. Abra o objeto de mídia para a imagem do mapa escaneado e mude para o modo de edição.
2. Abra a aba "Mapa" e clique em **Editar coordenadas**. Isso abre uma caixa de diálogo de georreferenciamento com a imagem ao lado de um mapa.
3. Clique em **Selecionar um ponto no mapa**, depois clique na localização no mapa que um ponto na imagem deve corresponder. A imagem é colocada no mapa pela primeira vez assim que um ponto é selecionado.
4. Use o controle deslizante **Escala** para redimensionar a imagem e o controle deslizante **Opacidade** para ver o mapa base através dela enquanto posiciona.
5. Clique em **Alinhar a imagem** e clique no mapa novamente para mover a imagem de modo que o ponto fixado se alinhe precisamente.
6. Repita os passos de escala, opacidade e alinhamento até que a imagem corresponda à geografia subjacente, depois salve.

Nos bastidores, isso armazena as coordenadas dos cantos da imagem em um atributo `map:bounds` no objeto de mídia.

### Visualizando sobreposições na página do Mapa

Uma vez que um objeto de mídia foi georreferenciado dessa forma, ele automaticamente se torna disponível como uma camada alternável na página do Mapa. Abra o alternador de camadas (ícone de camadas empilhadas, canto inferior esquerdo) para mostrar ou ocultar cada sobreposição independentemente do mapa base. As sobreposições são listadas pelo título do objeto de mídia.
