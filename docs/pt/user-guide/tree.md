# Árvore Genealógica

A página da Árvore Genealógica é acessível a partir da barra lateral e exibe gráficos interativos centrados em uma pessoa selecionada. Cinco tipos de gráficos estão disponíveis através de abas na parte superior da página.

## Selecionando a pessoa inicial

Todos os gráficos começam a partir da pessoa atualmente selecionada na árvore (mostrada na barra de ferramentas). A pessoa atualmente centrada é destacada com uma sombra. Use o botão **Pessoa Inicial** para voltar à sua pessoa inicial, ou o botão **Voltar** para retornar à pessoa visualizada anteriormente. Clicar no cartão de uma pessoa em qualquer gráfico recentra o gráfico nessa pessoa.

Se nenhuma pessoa inicial tiver sido definida, a página oferece um botão **Definir Pessoa Inicial** para pesquisar e selecionar uma diretamente. Se a árvore ainda não contiver nenhuma pessoa, usuários com a função de Editor ou superior verão em vez disso um botão **Nova Pessoa** – a primeira pessoa criada em uma árvore vazia automaticamente se torna sua pessoa inicial, então o gráfico é exibido imediatamente.

## Tipos de gráficos

### Árvore de Antepassados

Um gráfico de pedigree mostrando os antepassados da pessoa selecionada. Os pais aparecem à esquerda (ou à direita, dependendo do layout), os avós mais afastados, e assim por diante.

### Árvore de Descendentes

Mostra os descendentes da pessoa selecionada – filhos, netos, e assim por diante.

### Gráfico de Ampulheta

Combina antepassados acima e descendentes abaixo da pessoa selecionada em uma única visão.

### Gráfico de Relação

Mostra o caminho de relação entre duas pessoas. A pessoa selecionada é uma extremidade; clique em qualquer outra pessoa no gráfico para definir a segunda extremidade e exibir o caminho de relação mais curto entre elas.

!!! note
    A mesma pessoa pode aparecer mais de uma vez no gráfico – por exemplo, quando alguém foi casado várias vezes e aparece em várias unidades familiares ao longo do caminho. Isso é intencional, não um erro.

### Gráfico em Leque

Um gráfico de pedigree circular. Os antepassados irradiam para fora a partir da pessoa selecionada no centro.

## Movendo-se para parentes e expandindo ramos

Na Árvore de Antepassados e no Gráfico em Leque, a pessoa selecionada tem um botão de chevron que abre um menu de seus filhos. Na Árvore de Descendentes, ele abre um menu de seus pais em vez disso. Escolher uma pessoa no menu centra o gráfico nela.

Na Árvore de Antepassados, Árvore de Descendentes e Gráfico de Ampulheta, as pessoas na borda do gráfico cujos pais ou filhos não estão mostrados têm um chevron no lado onde seu ramo continua. Clicar nele adiciona mais uma geração a esse ramo, enquanto a pessoa selecionada permanece a mesma. Dessa forma, você pode, por exemplo, olhar para todos os avós e depois seguir apenas uma linha mais para trás. Os ramos expandidos são redefinidos quando você seleciona outra pessoa ou muda para um gráfico diferente.

## Controles de navegação

Todos os tipos de gráficos compartilham uma barra de ferramentas com os seguintes botões:

- **Pessoa Inicial** – volte para sua pessoa inicial
- **Voltar** – retorne à pessoa centrada anteriormente
- **Detalhes da Pessoa** – abra a página de perfil completa da pessoa atualmente centrada
- **Preferências** – abra um diálogo para ajustar opções de exibição específicas do gráfico (veja abaixo)

Todos os gráficos suportam **pan** (clique e arraste) e **zoom** (rolagem ou pinça).

## Preferências do gráfico

O diálogo de **Preferências** (ícone de engrenagem na barra de ferramentas) permite que você ajuste as seguintes opções, dependendo do tipo de gráfico:

- **Gerações Máximas de Antepassados** – quantas gerações de antepassados exibir
- **Gerações Máximas de Descendentes** – quantas gerações de descendentes exibir
- **Grau Máximo de Separação** – para o Gráfico de Relação, o comprimento máximo do caminho a ser pesquisado
- **Número Máximo de Imagens exibidas** – limita as fotos de perfil mostradas no gráfico para desempenho
- **Formato de Exibição do Nome** – controla como os nomes são exibidos nos cartões de pessoas

Clique em **Redefinir** para restaurar os padrões, ou **Fechar** para aplicar suas alterações.

As configurações de preferências do gráfico são armazenadas no armazenamento local do navegador, portanto, persistem entre as sessões no mesmo dispositivo.

## Tipo de gráfico padrão

O tipo de gráfico exibido quando você abre pela primeira vez a página da Árvore Genealógica pode ser configurado em [Configurações do Usuário](settings.md). O seu padrão escolhido se aplica em todos os seus dispositivos.

## Editando a árvore

Usuários com a função de Editor ou superior podem adicionar e vincular pessoas diretamente da Árvore de Antepassados. Veja [Editando a árvore genealógica](tree-edit.md) para mais detalhes.
