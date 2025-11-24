# Instalação / Configuração do Gramps Web

Esta seção trata da instalação e configuração do Gramps Web, bem como de outras opções para começar.

## Começando com o Gramps Web

Gramps Web é um aplicativo web que roda em um servidor e é acessado via navegador. Ele deve ser acessível a usuários autenticados pela internet.

Se você deseja usar o Gramps Web para seus dados de pesquisa genealógica, deve escolher uma das seguintes opções:

1. Auto-hospedagem em seu próprio hardware
2. Auto-hospedagem na nuvem
3. Inscrever-se para uma instância hospedada

Enquanto a primeira opção oferece máxima flexibilidade e controle, ela também pode ser tecnicamente desafiadora.

!!! tip
    Um dos principais princípios do Gramps Web é colocar os usuários no controle de seus próprios dados a qualquer momento, portanto, migrar dados de uma instância para outra é simples. Não se preocupe em ficar preso após escolher uma das opções!

## Auto-hospedagem em seu próprio hardware

A maneira mais conveniente de auto-hospedar o Gramps Web é via Docker Compose. Também fornecemos imagens Docker para a arquitetura ARM, para que você possa rodar o Gramps Web em um Raspberry Pi no seu porão.

Veja [Implantar com Docker](deployment.md) para instruções de configuração.

## Auto-hospedagem na nuvem

Instalar o Gramps Web pode ser mais desafiador do que outras aplicações web simples e não é compatível com provedores de "hospedagem compartilhada" comuns. Você pode se inscrever para um servidor virtual e instalar o Gramps Web [manualmente](deployment.md).

Uma opção mais simples é usar uma imagem de nuvem pré-instalada. Um exemplo é nosso [aplicativo de 1 clique do DigitalOcean](digital_ocean.md).

## Inscrever-se para uma instância hospedada

Um Gramps Web hospedado é a maneira mais fácil de começar com o Gramps Web, já que nenhuma instalação ou configuração é necessária.

Aqui está uma lista de provedores de hospedagem dedicados para o Gramps Web (a comunidade de código aberto do Gramps não se responsabiliza por seus serviços):

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), oferecido por um dos principais colaboradores do Gramps Web

Se você usar uma opção hospedada para o Gramps Web, pode pular o restante desta seção e ir direto para a seção de [Administração](../administration/admin.md).
