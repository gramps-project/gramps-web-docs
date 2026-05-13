# Mapa

A página do Mapa exibe todos os lugares na sua árvore genealógica como marcadores interativos em um mapa geográfico. Ela é acessível a partir da barra lateral.

## Marcadores de lugar

Apenas os lugares que têm coordenadas GPS armazenadas no banco de dados do Gramps são exibidos no mapa. Lugares sem coordenadas são omitidos silenciosamente. As coordenadas GPS podem ser definidas na página de detalhes do lugar (edite o lugar e preencha os campos de latitude e longitude).

!!! dica
    Se muitos dos seus lugares estiverem faltando no mapa, abra a página de detalhes de um lugar e verifique se a latitude e a longitude estão definidas. Você pode adicionar ou corrigir coordenadas diretamente na visualização de edição do lugar.

Cada lugar com coordenadas é mostrado como um marcador. Clicar em um marcador abre um cartão de resumo mostrando o nome do lugar e seus eventos e pessoas vinculados. Clique no nome do lugar no cartão para abrir a página completa de detalhes do lugar.

## Pesquisa

A caixa de pesquisa no canto superior esquerdo do mapa permite que você pule para qualquer localização no mundo pelo nome. Isso não filtra os lugares da árvore – simplesmente move e amplia o mapa para a localização pesquisada.

## Controle deslizante de tempo

O controle deslizante de tempo na parte inferior da página filtra quais marcadores de lugar são exibidos com base no ano de seus eventos associados:

- Arraste a alça para selecionar um ano.
- Apenas os lugares vinculados a eventos que caem dentro da janela de tempo selecionada são mostrados.
- Use isso para rastrear onde seus ancestrais viveram em um determinado momento da história.

## Camadas do mapa

Um botão de alternância de camadas (ícone de camadas empilhadas, canto inferior esquerdo) permite que você escolha entre dois mapas base:

### Mapa Base

A camada padrão, alimentada por [OpenFreeMap](https://openfreemap.org) (estilo Liberty para modo claro, estilo escuro para modo escuro). Este é um mapa moderno de uso geral adequado para localizar lugares.

### Mapa Histórico

Troca o mapa base para [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), um projeto comunitário que mapeia o mundo como ele existiu em diferentes pontos no tempo – pense nisso como um contraparte histórica do OpenStreetMap.

Quando a camada do Mapa Histórico está ativa, o controle deslizante de tempo também filtra os próprios blocos do mapa: o OHM renderiza o mapa como ele aparecia no ano selecionado, então fronteiras históricas, nomes de lugares e características são mostrados em vez das modernas. Isso torna possível ver tanto a localização do seu ancestral quanto o contexto geográfico e político contemporâneo em uma única visualização.

!!! nota
    A cobertura do OpenHistoricalMap varia por região e período. Áreas ou épocas com contribuições escassas podem mostrar detalhes históricos limitados. Se você notar dados históricos ausentes ou imprecisos, considere [contribuir para o OpenHistoricalMap](https://www.openhistoricalmap.org) – é um projeto comunitário aberto que qualquer um pode editar.
