---
hide:
  - toc
---

# Guia do Usuário

Esta seção documenta os recursos disponíveis para os usuários do Gramps Web.

!!! note "Não está vendo todos os recursos?"
    O Gramps Web utiliza um sistema de permissões baseado em funções. Alguns recursos – como editar dados, gerenciar tags ou visualizar registros privados – estão disponíveis apenas para usuários com permissões suficientes. Você pode verificar sua função atual em [Configurações do Usuário](settings.md). Se precisar de mais acesso, entre em contato com o proprietário da sua árvore ou administrador. Consulte [Sistema de Usuários](../install_setup/users.md) para uma descrição de todas as funções.

## Navegando pela interface

### Navegação principal

A barra lateral (ou menu hambúrguer no celular) é a principal forma de se mover entre seções:

- **Início** – o painel de controle (veja abaixo)
- **Blog** – histórias de história da família escritas como postagens de blog
- **Árvore Genealógica** – gráficos de árvore interativos
- **Linha do Tempo** – visualização cronológica de eventos na árvore (requer uma versão da API do Gramps Web suficientemente recente)
- **Mapa** – visualização geográfica de lugares na árvore
- **DNA** – ferramentas de análise de correspondência de DNA
- **Listas** – navegue por todos os objetos de cada tipo: Pessoas, Famílias, Eventos, Lugares, Fontes, Citações, Repositórios, Notas
- **Mídia** – navegue por todos os arquivos de mídia (fotos, documentos, etc.)
- **Assistente** – assistente de chat de IA (se habilitado pelo administrador)
- **Histórico** – objetos alterados recentemente
- **Favoritos** – seus favoritos salvos
- **Tarefas** – tarefas de pesquisa
- **Relatórios** – gerar relatórios
- **Exportar** – exportar a árvore genealógica
- **Revisões** – histórico completo de transações (visível para membros e acima)
- **Notificações** – notificações passadas

!!! note
    As tags não são mais gerenciadas a partir da barra lateral – o gerenciamento de tags foi movido para [Configurações de Administração](../administration/settings.md#tags) (apenas Proprietário/Administrador). Consulte [Tags](tags.md) para saber como as tags são usadas.

### Barra superior do aplicativo

A barra no topo de cada página contém:

- **Adicionar** (ícone de mais, visível para colaboradores e acima) – abre um menu para criar um novo objeto: Pessoa, Família, Evento, Lugar, Fonte, Citação, Repositório, Nota, Objeto de Mídia ou Tarefa
- **Pesquisar** (lupa) – abre a página de pesquisa
- **Ícone do usuário** – abre o menu de configurações: Configurações do Usuário, Administração (apenas proprietários), Gerenciar Usuários (apenas proprietários), Informações do Sistema

## A página inicial (painel de controle)

O painel de controle é exibido quando você faz login pela primeira vez. Ele possui duas colunas:

**Coluna esquerda:**

- **Cartão da pessoa em casa** – mostra o nome, foto (se disponível) e fatos principais da sua pessoa em casa escolhida, com um link para seu perfil completo e navegação rápida para a árvore genealógica. Clique no botão **Definir Pessoa em Casa** no cartão para pesquisar e selecionar uma pessoa diferente.
- **Aniversários** – próximos aniversários e datas comemorativas da árvore, com base na data de hoje.
- **Alterações recentes** – uma lista curta dos objetos mais recentemente modificados, útil para rastrear edições colaborativas.

**Coluna direita:**

- **Postagens recentes do blog** – as últimas entradas do [blog](blog.md), se existirem.
- **Estatísticas** – um resumo das contagens de objetos na árvore (número de pessoas, famílias, eventos, etc.).

Enquanto a árvore ainda estiver vazia, o painel de controle oculta os painéis que não teriam nada a mostrar e, em vez disso, exibe um cartão **Comece** para usuários com permissões de edição: ele primeiro oferece criar uma pessoa ou importar um arquivo de árvore genealógica e, uma vez que as pessoas existam, conectá-las criando uma família. O cartão desaparece assim que a árvore contém uma família.

Se o administrador da árvore configurou uma **nota da página inicial** e/ou uma **imagem da página inicial**, estas são exibidas de forma proeminente acima das colunas principais. A imagem aparece ao lado do texto da nota quando ambos estão configurados. Consulte [Configurações de Administração](../administration/customization.md) para saber como configurar isso.

!!! tip
    Se a árvore estiver vazia e você tiver permissões de edição, o painel de controle mostrará um prompt "Comece" com botões para adicionar sua primeira pessoa ou importar um arquivo de árvore genealógica.

## Instalando o Gramps Web como um aplicativo

O Gramps Web é um aplicativo web progressivo (PWA), o que significa que seu navegador pode instalá-lo ao lado de seus outros aplicativos, em vez de mantê-lo em uma aba do navegador. Ele então recebe seu próprio ícone e abre em sua própria janela, sem a barra de endereços e barras de ferramentas do navegador.

Como você o instala depende do seu navegador:

- **Android (Chrome)** – abra o menu e escolha "Instalar aplicativo" ou "Adicionar à tela inicial".
- **iOS/iPadOS (Safari)** – toque no botão de compartilhar e escolha "Adicionar à Tela de Início".
- **Desktop (Chrome, Edge)** – clique no ícone de instalação no final direito da barra de endereços, ou use a entrada "Instalar" no menu do navegador.
- **Desktop (Firefox, Safari)** – a instalação não é suportada; use uma aba ou janela normal do navegador.

Nada muda em como o Gramps Web funciona, e nenhum dado é armazenado de forma diferente – é o mesmo aplicativo, apenas apresentado como um aplicativo independente.

!!! note
    O Gramps Web ainda precisa acessar seu servidor para mostrar seus dados, então um aplicativo instalado não permite que você navegue em sua árvore genealógica offline.
