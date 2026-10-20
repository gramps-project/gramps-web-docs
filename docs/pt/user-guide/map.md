# Mapa

A página do Mapa exibe todos os lugares na sua árvore genealógica como marcadores interativos em um mapa geográfico. Ela é acessível a partir da barra lateral.

## Marcadores de lugar

Apenas os lugares que têm coordenadas GPS armazenadas no banco de dados do Gramps são mostrados no mapa. Lugares sem coordenadas são omitidos silenciosamente. As coordenadas GPS podem ser definidas na página de detalhes do lugar (edite o lugar e preencha os campos de latitude e longitude).

!!! dica
    Se muitos dos seus lugares estiverem faltando no mapa, abra a página de detalhes de um lugar e verifique se a latitude e a longitude estão definidas. Você pode adicionar ou corrigir coordenadas diretamente na visualização de edição do lugar.

Cada lugar com coordenadas é mostrado como um marcador. Clicar em um marcador abre um cartão de resumo mostrando o nome do lugar e seus eventos e pessoas vinculados. Clique no nome do lugar no cartão para abrir a página completa de detalhes do lugar.

## Pesquisa

A caixa de pesquisa no canto superior esquerdo do mapa pesquisa enquanto você digita e agrupa os resultados sob três cabeçalhos:

- **Lugares** – lugares na sua árvore genealógica. Selecionar um faz o mapa se mover para ele e destaca seu marcador.
- **Pessoas** – pessoas na sua árvore genealógica. Selecionar uma muda o mapa para a visualização da pessoa descrita [abaixo](#seguindo-uma-pessoa-pelo-mapa).
- **Externo** – locais do [OpenStreetMap](https://www.openstreetmap.org/), para qualquer lugar do mundo. Selecionar um simplesmente move e amplia o mapa para aquele local; não filtra nem altera os lugares da sua árvore.

Os resultados externos também são úteis ao adicionar coordenadas a um lugar: você pode procurar a localização aqui para ver onde ela está antes de inserir sua latitude e longitude.

## Seguindo uma pessoa pelo mapa

Selecionar uma pessoa – a partir da caixa de pesquisa do mapa, ou com o botão **Abrir no mapa** na página de detalhes de uma pessoa – mostra os lugares conectados aos eventos daquela pessoa, unidos por linhas em ordem cronológica. Pequenas setas ao longo de cada linha indicam a direção da viagem, para que você possa seguir a vida de uma pessoa desde o nascimento até a morte pelo mapa.

Lugares em uma página de detalhes de lugar também têm um botão **Abrir no mapa**, que abre o mapa centrado naquele lugar.

## Controle deslizante de tempo

O controle deslizante de tempo na parte inferior da página filtra quais marcadores de lugar são mostrados com base no ano de seus eventos associados:

- Arraste a alça para selecionar um ano.
- Apenas lugares vinculados a eventos que caem dentro da janela de tempo selecionada são mostrados.
- Use isso para rastrear onde seus ancestrais viveram em um determinado ponto da história.

## Camadas do mapa

Um botão de alternância de camadas (ícone de camadas empilhadas, canto inferior esquerdo) permite que você escolha entre dois mapas base. Abaixo deles, lista suas próprias camadas de mapa sob "Seus mapas" (veja [Sobreposições de mapa personalizadas](#sobreposições-de-mapa-personalizadas) e [Arquivos de mapa de lugares](#arquivos-de-mapa-de-lugares)) e a camada de [edifícios do Wikidata](#edificios-do-wikidata) sob "Externo", cada uma das quais pode ser ativada ou desativada.

Os rótulos de ambos os mapas base são mostrados no idioma que você selecionou no Gramps Web, onde os dados do mapa têm um nome nesse idioma, e no nome local, caso contrário.

### Mapa Base

A camada padrão, alimentada por [OpenFreeMap](https://openfreemap.org) (estilo Liberty para modo claro, estilo escuro para modo escuro). Este é um mapa moderno de uso geral adequado para localizar lugares.

### Mapa Histórico

Muda o mapa base para [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), um projeto comunitário que mapeia o mundo como ele existiu em diferentes momentos no tempo – pense nisso como um contraparte histórica do OpenStreetMap.

Quando a camada do Mapa Histórico está ativa, o controle deslizante de tempo também filtra os próprios blocos do mapa: OHM renderiza o mapa como ele apareceu no ano selecionado, então fronteiras históricas, nomes de lugares e características são mostrados em vez dos modernos. Isso torna possível ver tanto a localização do seu ancestral quanto o contexto geográfico e político contemporâneo em uma única visualização.

!!! nota
    A cobertura do OpenHistoricalMap varia por região e período. Áreas ou épocas com contribuições escassas podem mostrar detalhes históricos limitados. Se você notar dados históricos ausentes ou imprecisos, considere [contribuir para o OpenHistoricalMap](https://www.openhistoricalmap.org) – é um projeto comunitário aberto que qualquer um pode editar.

## Sobreposições de mapa personalizadas

Além das camadas base integradas, você pode transformar qualquer imagem de mapa histórico escaneada – armazenada no Gramps como um objeto **Mídia** – em uma sobreposição personalizada posicionada no mapa ao vivo. Isso é útil para escaneamentos de antigos planos de cidades, mapas de paróquias ou mapas de propriedades que você deseja comparar diretamente com a geografia moderna ou histórica.

### Georreferenciando uma imagem

1. Abra o objeto de mídia para a imagem do mapa escaneado e mude para o modo de edição.
2. Abra a aba "Mapa" e clique em **Editar coordenadas**. Isso abre uma caixa de diálogo de georreferenciamento com a imagem ao lado de um mapa.
3. Clique em **Selecionar um ponto no mapa**, em seguida clique na localização no mapa que um ponto na imagem deve corresponder. A imagem é colocada no mapa pela primeira vez assim que um ponto é selecionado.
4. Use o controle deslizante **Escala** para redimensionar a imagem e o controle deslizante **Opacidade** para ver o mapa base através dela enquanto posiciona.
5. Clique em **Alinhar a imagem** e clique no mapa novamente para mover a imagem de modo que o ponto fixado se alinhe precisamente.
6. Repita os passos de escala, opacidade e alinhamento até que a imagem corresponda à geografia subjacente, e então salve.

Nos bastidores, isso armazena as coordenadas dos cantos da imagem em um atributo `map:bounds` no objeto de mídia.

### Visualizando sobreposições na página do Mapa

Uma vez que um objeto de mídia foi georreferenciado dessa maneira, ele se torna automaticamente disponível como uma camada alternável na página do Mapa. Abra o alternador de camadas (ícone de camadas empilhadas, canto inferior esquerdo) para mostrar ou ocultar cada sobreposição independentemente do mapa base. As sobreposições são listadas pelo título do objeto de mídia.

## Arquivos de mapa de lugares

Lugares podem ter arquivos de mapa anexados como objetos de mídia – por exemplo, os limites de uma paróquia, um distrito ou uma propriedade, ou uma rota. São suportados arquivos KML (`.kml`), GeoJSON (`.geojson`) e GPX (`.gpx`).

Quando você seleciona um lugar no mapa, seus arquivos de mapa são desenhados sobre o mapa, usando as cores armazenadas no arquivo onde as tem. Isso também funciona para lugares sem coordenadas: o mapa então se aproxima da área coberta pelos arquivos. Enquanto o lugar estiver selecionado, seus arquivos são listados no alternador de camadas sob "Seus mapas", onde você pode desligar cada um deles.

Para adicionar um arquivo de mapa a um lugar, adicione-o à galeria do lugar como qualquer outro [arquivo de mídia](media.md).

## Edifícios do Wikidata

A camada "edifícios do Wikidata" mostra edifícios registrados no [Wikidata](https://www.wikidata.org/), como igrejas, fazendas ou casas de cidade. Ela está desativada por padrão e pode ser ativada no alternador de camadas sob "Externo". Edifícios só são mostrados quando o mapa está ampliado o suficiente. Quando o controle deslizante de tempo está ativo, apenas edifícios que existiam no momento selecionado são mostrados.

Clique em um edifício para ver seus detalhes do Wikidata, como quando foi construído ou demolido, seus endereços, ocupantes e proprietários.

### Salvando um edifício como um lugar

Usuários que podem adicionar objetos veem um botão **Salvar como lugar** nos detalhes do edifício. Isso abre o formulário para um novo lugar, pré-preenchido com o nome do edifício no seu idioma, um tipo de lugar (`Fazenda` para fazendas, caso contrário `Edifício`), suas coordenadas e um link para o item do Wikidata. Complete o formulário, por exemplo, selecionando o lugar que o envolve, e salve.

Se um lugar na sua árvore estiver na mesma localização que o edifício, o botão lê **Abrir lugar salvo** em vez disso e mostra esse lugar.

!!! info
    O administrador do servidor pode remover a camada de edifícios do Wikidata com a opção `mapWikidata` da [configuração do frontend](../install_setup/frontend-config.md).
