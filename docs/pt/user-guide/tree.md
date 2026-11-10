# Árvore Genealógica

A página da Árvore Genealógica é acessível a partir da barra lateral e exibe gráficos interativos centrados em uma pessoa selecionada. Cinco tipos de gráficos estão disponíveis através de abas na parte superior da página.

## Selecionando a pessoa inicial

Todos os gráficos começam a partir da pessoa atualmente selecionada na árvore (mostrada na barra de ferramentas). A pessoa atualmente centrada é destacada com uma sombra. Use o botão **Pessoa Inicial** para voltar à sua pessoa inicial ou o botão **Voltar** para retornar à pessoa visualizada anteriormente. Clicar no cartão de uma pessoa em qualquer gráfico recentra o gráfico nessa pessoa.

Se nenhuma pessoa inicial tiver sido definida, a página oferece um botão **Definir Pessoa Inicial** para pesquisar e selecionar uma diretamente. Se a árvore ainda não contiver nenhuma pessoa, os usuários com a função de Editor ou superior verão um botão **Nova Pessoa** – a primeira pessoa criada em uma árvore vazia automaticamente se torna sua pessoa inicial, então o gráfico é exibido imediatamente.

## Tipos de gráficos

### Árvore de Antepassados

Um gráfico de pedigree mostrando os antepassados da pessoa selecionada. Os pais aparecem à esquerda (ou à direita, dependendo do layout), os avós mais distantes, e assim por diante.

### Árvore de Descendentes

Mostra os descendentes da pessoa selecionada – filhos, netos, e assim por diante.

### Gráfico de Ampulheta

Combina antepassados acima e descendentes abaixo da pessoa selecionada em uma única visão.

### Gráfico de Relações

Mostra o caminho de relacionamento entre duas pessoas. A pessoa selecionada é uma extremidade; clique em qualquer outra pessoa no gráfico para definir a segunda extremidade e exibir o caminho de relacionamento mais curto entre elas.

!!! note
    A mesma pessoa pode aparecer mais de uma vez no gráfico – por exemplo, quando alguém foi casado várias vezes e aparece em várias unidades familiares ao longo do caminho. Isso é intencional, não um erro.

### Gráfico em Leque

Um gráfico de pedigree circular. Os antepassados irradiam para fora da pessoa selecionada no centro.

O botão **Cor** na barra de ferramentas colore os segmentos por uma propriedade de cada pessoa: o número de eventos ou notas, ano de nascimento, ano de falecimento, idade, sobrenome, religião ou frequência de antepassados (com que frequência uma pessoa aparece no gráfico). A coloração por sobrenome utiliza o sobrenome do nome de nascimento da pessoa ou do nome principal se não houver nome de nascimento. Para remover a coloração, limpe o chip que mostra a cor escolhida.

## Navegando para parentes e expandindo ramos

Na Árvore de Antepassados e no Gráfico em Leque, a pessoa selecionada tem um botão de chevron que abre um menu de seus filhos. Na Árvore de Descendentes, ele abre um menu de seus pais. Escolher uma pessoa no menu centra o gráfico nela.

Na Árvore de Antepassados, na Árvore de Descendentes e no Gráfico de Ampulheta, as pessoas na borda do gráfico cujos pais ou filhos não estão mostrados têm um chevron no lado onde seu ramo continua. Clicar nele adiciona mais uma geração a esse ramo, enquanto a pessoa selecionada permanece a mesma. Dessa forma, você pode, por exemplo, olhar para todos os avós e depois seguir apenas uma linha mais para trás. Os ramos expandidos são redefinidos quando você seleciona outra pessoa ou muda para um gráfico diferente.

## Controles de navegação

Todos os tipos de gráficos compartilham uma barra de ferramentas com os seguintes botões:

- **Pessoa Inicial** – volte para sua pessoa inicial
- **Voltar** – volte para a pessoa que estava centrada anteriormente
- **Detalhes da Pessoa** – abra a página de perfil completa da pessoa atualmente centrada
- **Preferências** – abra um diálogo para ajustar opções de exibição específicas do gráfico (veja abaixo)

Todos os gráficos suportam **pan** (clique e arraste) e **zoom** (rolagem do mouse ou pinça).

## Preferências do gráfico

O diálogo **Preferências** (ícone de engrenagem na barra de ferramentas) permite que você ajuste as seguintes opções, dependendo do tipo de gráfico:

- **Máx. Gerações de Antepassados** – quantas gerações de antepassados exibir
- **Máx. Gerações de Descendentes** – quantas gerações de descendentes exibir
- **Máx. Grau de Separação** – para o Gráfico de Relações, o comprimento máximo do caminho a ser pesquisado, até 6
- **Máx. Número de Imagens exibidas** – limita as fotos de perfil mostradas no gráfico para desempenho
- **Formato de Exibição do Nome** – controla como os nomes são exibidos nos cartões das pessoas

Clique em **Redefinir** para restaurar os padrões ou **Fechar** para aplicar suas alterações.

As configurações de preferências do gráfico são armazenadas no armazenamento local do navegador, para que persistam entre sessões no mesmo dispositivo.

## Tipo de gráfico padrão

O tipo de gráfico exibido quando você abre pela primeira vez a página da Árvore Genealógica pode ser configurado em [Configurações do Usuário](settings.md). O padrão escolhido se aplica em todos os seus dispositivos.

## Editando a árvore

Usuários com a função de Editor ou superior podem adicionar e vincular pessoas diretamente da Árvore de Antepassados. Veja [Editando a árvore genealógica](tree-edit.md) para mais detalhes.
