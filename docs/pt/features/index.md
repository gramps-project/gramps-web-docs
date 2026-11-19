---
hide:
  - toc
  - navigation
---

# Recursos

Gramps Web é um aplicativo web para genealogia colaborativa. Ele é construído sobre o [Gramps](https://gramps-project.org/), o programa de genealogia de código aberto, e funciona com os mesmos dados. Você pode executá-lo em seu próprio servidor ou usar um provedor de hospedagem.

[Experimente a demonstração](#demo){ .md-button .md-button--primary } [Comece agora](../install_setup/setup.md){ .md-button }

## Explore sua árvore genealógica { .feature-group }

![Gráfico em leque mostrando sete gerações de ancestrais](screenshots/fan.png){ align=right width="400"}

### Gráficos interativos da árvore genealógica

Navegue pela sua árvore genealógica como uma árvore de ancestrais, árvore de descendentes, gráfico de ampulheta, gráfico de relacionamentos ou gráfico em leque, com gráficos interativos de alta qualidade e um número configurável de gerações.

Passe o mouse sobre qualquer pessoa para ver um cartão de pré-visualização com seus fatos principais e pule diretamente do gráfico para a página de detalhes completa.

<div style="clear:both;"></div>

---

![Linha do tempo de eventos familiares entre as décadas de 1940 e 1970](screenshots/timeline.png){ align=left width="400"}

### Linha do tempo cronológica

Veja cada evento em sua árvore genealógica disposto em uma linha do tempo horizontal e ampliável. Role e amplie através dos séculos, depois filtre para uma única pessoa – ou para todos os seus ancestrais ou descendentes – ou para tudo que aconteceu em um único lugar.

Veja [Linha do Tempo](../user-guide/timeline.md).

<div style="clear:both;"></div>

---

![Mapa de Londres com um local selecionado, mostrando sua foto e eventos](screenshots/map.png){ align=right width="400"}

### Mapa interativo

Exiba todos os locais em sua árvore em um mapa interativo e pesquisável. Pesquise novos locais diretamente no OpenStreetMap ao criar um local, trace as pessoas em seu banco de dados geograficamente e siga a vida de uma única pessoa conectando seus eventos com linhas no mapa.

<div style="clear:both;"></div>

---

![Londres no layer OpenHistoricalMap, com o controle deslizante de tempo definido para 1707](screenshots/ohm.png){ align=left width="400"}

### Mapas históricos

Transforme um mapa histórico armazenado como um objeto de mídia no Gramps em uma sobreposição de mapa personalizada.

Você também pode alternar para os mapas vetoriais históricos do projeto [OpenHistoricalMap](https://www.openhistoricalmap.org/). Use o controle deslizante de tempo para percorrer a evolução dos locais na sua história familiar e exibir os lugares onde os ancestrais viveram ou onde os eventos aconteceram.

<div style="clear:both;"></div>

---

![Resultados da pesquisa para "Albert" em pessoas, eventos e mídias](screenshots/search.png){ align=right width="400"}

### Encontre qualquer coisa

O mecanismo de busca de texto completo cobre todos os tipos de objetos do Gramps, incluindo o conteúdo de notas de texto, e suporta curingas e operadores lógicos.

Para consultas precisas, as visualizações de lista de objetos oferecem um modo de filtro avançado baseado na [Gramps Object Query Language](../user-guide/goql.md), juntamente com filtros rápidos por texto, tag e privacidade.

Na página de qualquer pessoa, [Pesquisa Externa](../user-guide/external-search.md) abre uma pesquisa pré-preenchida no FamilySearch, Ancestry, CompGen e outros sites – e você pode adicionar os seus próprios.

<div style="clear:both;"></div>

## Construir e pesquisar { .feature-group }

![Árvore de ancestrais em modo de edição com o diálogo para adicionar um membro da família](screenshots/tree-edit.png){ align=left width="400"}

### Construa sua árvore diretamente no gráfico

Mude a visualização da árvore para o modo de edição e faça crescer sua árvore genealógica sem sair do gráfico. Cada cartão de pessoa recebe um botão **+** para adicionar um pai, mãe, filho ou cônjuge – vinculando alguém já em seu banco de dados ou criando uma nova pessoa na hora. Cada mudança é salva imediatamente.

Veja [Editando a Árvore Genealógica](../user-guide/tree-edit.md).

<div style="clear:both;"></div>

---

![O assistente de IA lendo uma certidão de nascimento e propondo novos registros](screenshots/chat.png){ align=right width="400"}

### Assistente de IA integrado

Faça perguntas sobre sua árvore genealógica em seu próprio idioma e obtenha respostas baseadas em seus dados.

O assistente não apenas pesquisa: ele consulta seu banco de dados diretamente com um conjunto de ferramentas, filtrando pessoas, eventos, famílias e locais, e calculando relacionamentos entre indivíduos. Você pode ver quais ferramentas ele está usando enquanto constrói uma resposta, e perguntas mais longas são executadas como tarefas em segundo plano, para que você possa navegar para longe e voltar.

O assistente é opcional e precisa ser [configurado pelo administrador do servidor](../install_setup/chat.md) com um provedor de modelo de IA.

<div style="clear:both;"></div>

---

![Navegador de cromossomos mostrando os segmentos de DNA compartilhados de onze correspondências](screenshots/dna.png){ align=left width="400"}

### Correspondências de DNA, navegador de cromossomos e Y-DNA

Carregue dados de correspondência de DNA do seu provedor de testes de DNA, armazene-os ao lado de sua árvore genealógica e visualize suas correspondências em um navegador de cromossomos interativo.

Dados brutos de SNP do cromossomo Y podem ser usados para determinar o [haplogrupo Y-DNA](../user-guide/y-dna.md) mais provável de uma pessoa e exibir seus ancestrais patrilineares na árvore do cromossomo Y humano, com estimativas de tempo. A análise é executada inteiramente em seu próprio servidor – nenhum dado é enviado a terceiros.

<div style="clear:both;"></div>

---

![Pintura com duas pessoas marcadas e os outros rostos detectados contornados](screenshots/tag.png){ align=right width="400"}

### Marque pessoas em fotos com detecção automática de rostos

Identifique ancestrais em fotos antigas da família junto com seus parentes. Os rostos são detectados automaticamente, então marcar uma pessoa leva dois cliques.

<div style="clear:both;"></div>

---

![Lista de tarefas de pesquisa com status, prioridade e tags](screenshots/tasks.png){ align=left width="400"}

### Aplicativo de gerenciamento de tarefas integrado

Gramps Web vem com um aplicativo de gerenciamento de tarefas integrado para organizar e planejar sua pesquisa genealógica. Dê a cada tarefa um status, uma prioridade e tags, documente seu progresso em uma descrição em rich-text e anexe a mídia que você coletou ao longo do caminho.

As tarefas são armazenadas como fontes no banco de dados do Gramps, portanto, fazem parte dos seus dados genealógicos e podem ser acessadas e editadas no Gramps Desktop também.

<div style="clear:both;"></div>

---

![Postagem de blog sobre a identificação das pessoas em uma fotografia de família](screenshots/blog.png){ align=right width="400"}

### Blog de genealogia incluído

Resuma sua pesquisa na forma de histórias de blog com imagens e compartilhe-as com seus parentes. Um editor dedicado torna a escrita de uma nova postagem simples. Todos os dados são armazenados no banco de dados do Gramps.

<div style="clear:both;"></div>

## Trabalhe em conjunto { .feature-group }

![Lista de pessoas na árvore genealógica](screenshots/list.png){ align=left width="400"}

### Níveis de privacidade e acesso do usuário

Você pode [marcar registros como privados](../user-guide/privacy.md) – até um único nome, link de evento ou correspondência de DNA – e controlar quais usuários têm permissão para visualizar registros privados. Registros privados são filtrados na camada do banco de dados para máxima segurança. Além disso, você pode controlar o que os usuários podem adicionar e editar.

Os usuários podem fazer login com uma senha ou através de um provedor de identidade externo usando [OpenID Connect](../install_setup/oidc.md) – Google e Microsoft por padrão, além de provedores personalizados como Keycloak, Authentik e Authelia.

<div style="clear:both;"></div>

---

![Uma revisão mostrando os campos alterados em um registro de pessoa](screenshots/revisions.png){ align=right width="400"}

### Histórico completo de revisões – com desfazer

Cada edição em sua árvore genealógica é registrada. Navegue pelo histórico completo agrupado por transação, aprofunde-se em qualquer mudança individual para ver exatamente quais campos foram adicionados, removidos ou modificados, e desfaça uma transação se descobrir que foi um erro. A página de cada objeto também possui sua própria aba de revisões mostrando quem a alterou e quando.

Veja [Histórico de Revisões](../user-guide/revisions.md).

<div style="clear:both;"></div>

---

![Menu Ferramentas do Gramps Desktop com a entrada Gramps Web Sync](screenshots/sync.png){ align=left width="300"}

### Integração completa com o Gramps Desktop

Gramps Web usa o mesmo modelo de dados e banco de dados que o [Gramps Desktop](https://gramps-project.org/). Você pode navegar e editar todos os mesmos [tipos de registros](https://gramps-project.org/wiki/index.php/Gramps_Data_Model): pessoas, famílias, eventos, lugares, repositórios, fontes, citações, objetos de mídia e notas.

Com o [complemento Gramps Web Sync](../administration/sync.md) para o Gramps Desktop, você pode sincronizar seus dados em ambas as direções, para que possa continuar trabalhando no Gramps Desktop e no Gramps Web lado a lado.

<div style="clear:both;"></div>

## Relatórios e exportação de dados { .feature-group }

![Relatório de ancestrais gerado como um PDF](screenshots/report.png){ align=right width="400"}

### Gere relatórios imprimíveis

Gramps Web é construído sobre o mesmo núcleo que o Gramps Desktop, então você pode gerar quase todos os [relatórios](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports) que o aplicativo desktop suporta diretamente do navegador, incluindo gráficos de relacionamento ou relatórios em livro como PDF.

<div style="clear:both;"></div>

---

![Página de exportação com a lista de formatos de arquivo disponíveis](screenshots/export.png){ align=left width="300"}

### Sem bloqueio – importação e exportação de dados

Importe dados em vários formatos, incluindo Gramps XML e GEDCOM, e baixe todos os seus dados a qualquer momento – dados da árvore genealógica, arquivos de mídia e contas de usuário – para backups ou para mover para um servidor diferente.

As importações podem ser visualizadas como um teste antes que qualquer coisa seja escrita, e um backup completo pode ser restaurado de volta na árvore.

<div style="clear:both;"></div>

## Use em qualquer lugar { .feature-group }

![A mesma página de pessoa em um desktop e em um telefone](screenshots/mobile.png){ align=right width="400"}

### Funciona em todos os dispositivos

Use Gramps Web em qualquer dispositivo com um navegador web: carregue fotos, crie ou edite registros, ou mostre sua árvore genealógica para parentes na próxima reunião de família.

Gramps Web é um aplicativo web progressivo: instale-o na tela inicial ou desktop e ele se comporta como um aplicativo nativo. No desktop, [atalhos de teclado](../user-guide/shortcuts.md) levam você a qualquer lugar em algumas teclas – pressione `?` para vê-los todos.

<div style="clear:both;"></div>

---

![Menu de seleção de idioma](screenshots/lang.png){ align=left width="300"}

### Totalmente internacionalizado

Use a interface em qualquer um de mais de 50 idiomas traduzidos pela comunidade Gramps.

<div style="clear:both;"></div>

## E mais

- **Notificações e tarefas em segundo plano** – importações, exportações, relatórios e reconstruções de índice são executados em segundo plano, com progresso e erros coletados em um só lugar
- **Tags, marcadores e histórico** – organize objetos com tags codificadas por cores e volte ao que estava trabalhando
- **Edição em massa** – selecione vários objetos nas visualizações de lista para excluí-los de uma vez ou mesclar objetos duplicados
- **Visualizações de lista personalizáveis** – escolha quais colunas mostrar e filtre por texto, tag ou privacidade
- **Reconhecimento de texto (OCR)** – extraia texto de documentos digitalizados em sua galeria de mídia
- **Verificação de dados** – verifique sua árvore para datas implausíveis e outros problemas de dados
- **Calendários** – insira datas no calendário gregoriano, juliano, hebraico, republicano francês, persa, islâmico ou sueco
- **Personalize** – dê ao seu site seu próprio nome, cores de tema e texto e imagem da página inicial

## Demonstração

Para fazer login na demonstração, use uma das seguintes combinações de nome de usuário/senha. Cada uma representa um dos papéis de usuário no Gramps Web.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

A demonstração é redefinida a cada duas horas, então quaisquer alterações que você fizer são temporárias.

[Vá para o Login da Demonstração](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### Agradecimentos

A demonstração é gentilmente apoiada pela DigitalOcean.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
