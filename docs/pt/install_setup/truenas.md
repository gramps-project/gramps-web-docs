# Configuração do TrueNAS

Este guia explica como configurar o Gramps Web no TrueNAS Community Edition 25.04.

!!! warning
    Este guia é destinado ao TrueNAS Community Edition 25.04 ou posterior, que introduziu um novo sistema de aplicativos baseado em Docker Compose. Não se aplica a versões anteriores do TrueNAS.

## Pré-requisitos

- TrueNAS Community Edition 25.04 ou posterior
- Familiaridade básica com a interface web do TrueNAS
- Um conjunto de dados para armazenar os dados do Gramps Web

## Visão Geral

O TrueNAS Community Edition 25.04 introduziu um novo sistema de aplicativos baseado em Docker Compose que substitui a abordagem anterior baseada em Helm chart. Este guia irá orientá-lo na criação de um aplicativo personalizado para o Gramps Web usando Docker Compose.

## Passo 1: Preparar Armazenamento

1. Navegue até **Conjuntos de Dados** na interface web do TrueNAS
2. Crie um novo conjunto de dados para o Gramps Web (por exemplo, `grampsweb`). Anote o caminho completo para este conjunto de dados, por exemplo, `/mnt/storage/grampsweb`, pois você precisará dele mais tarde.

Crie subdiretórios para os vários componentes:
- `users` - Banco de dados de usuários
- `database` - Arquivo(s) do banco de dados do Gramps
- `media` - Arquivos de mídia

## Passo 2: Criar o Aplicativo Docker Compose

1. Navegue até **Aplicativos** na interface web do TrueNAS
2. Clique em **Descobrir Aplicativos**
3. Pesquise por "Gramps Web" e clique nele
4. Clique em "Instalar"

Isso o levará à página de configuração do aplicativo.

## Passo 3: Configurar o Aplicativo

### Configuração do Gramps Web

- **Fuso horário:** Defina para o seu fuso horário local (por exemplo, `Europe/Berlin`)
- **Senha do Redis:** Defina uma senha para o Redis. Isso será usado apenas internamente pelo aplicativo.
- **Desativar telemetria:** por favor, deixe esta caixa desmarcada – veja [aqui para mais detalhes](telemetry.md).
- **Chave secreta:** é crucial que você defina isso como um valor forte e único. Veja [configuração do servidor](configuration.md#existing-configuration-settings) para instruções sobre como gerar uma chave aleatória.
- **Variáveis de Ambiente Adicionais:** Você precisará definir todas as [opções de configuração](configuration.md) adicionais como variáveis de ambiente prefixadas por `GRAMPSWEB_`. Por favor, verifique a [documentação de configuração](configuration.md) em detalhes – por exemplo, o fato de que valores booleanos precisam ser definidos como `true` ou `false` (tudo em letras minúsculas) no caso de variáveis de ambiente, um erro comum.

Por favor, **pelo menos** defina o `GRAMPSWEB_BASE_URL` para a URL onde sua instância do Gramps Web estará acessível – isso é necessário para o funcionamento adequado.

Você também pode querer configurar a configuração de e-mail nesta fase. Se o fizer, pode pular a etapa de configuração de e-mail no assistente de integração. As variáveis de ambiente relevantes são:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Todas as configurações podem ser alteradas posteriormente clicando em "Editar" na interface de Aplicativos do TrueNAS.

### Configuração de Armazenamento

- **Armazenamento de Usuários:** Selecione o caminho para o diretório `users` que você criou anteriormente.
- **Armazenamento de Índice:** Você pode deixar a configuração padrão "ixVolume (Conjunto de dados criado automaticamente pelo sistema)"
- **Armazenamento de Cache de Miniaturas:** Você pode deixar a configuração padrão "ixVolume (Conjunto de dados criado automaticamente pelo sistema)"
- **Armazenamento de Cache:** Você pode deixar a configuração padrão "ixVolume (Conjunto de dados criado automaticamente pelo sistema)"
- **Armazenamento de Mídia:** Selecione o caminho para o diretório `media` que você criou anteriormente.
- **Armazenamento do Banco de Dados do Gramps:** Selecione o caminho para o diretório `database` que você criou anteriormente.

### Configuração de Recursos

Recomendamos que você aloque pelo menos 2 CPUs e 4096 MB de RAM para garantir um funcionamento suave.

## Passo 4: Acessar o Gramps Web

Uma vez que o aplicativo esteja implantado, você pode acessar o Gramps Web clicando no botão "Interface Web" na interface de Aplicativos do TrueNAS. Você deve ver o assistente de integração "Bem-vindo ao Gramps Web".

Se você quiser permitir que os usuários acessem sua interface do Gramps Web, **não** exponha o aplicativo diretamente à internet, mas prossiga para o próximo passo.

## Passo 5: Configurar um Proxy Reverso

Para expor sua instância do Gramps Web de forma segura para os usuários, é recomendado configurar um proxy reverso. Isso permite que você gerencie certificados SSL/TLS e controle o acesso.

A opção mais fácil é usar o aplicativo oficial TrueNAS Nginx Proxy Manager. Pesquise o aplicativo na interface de Aplicativos do TrueNAS e instale-o. Você pode deixar todas as configurações em seus padrões, mas recomendamos que você defina uma variável de ambiente adicional: `DISABLE_IPV6` com valor `true` para evitar possíveis problemas relacionados ao IPv6.

Uma vez implantado, abra a interface web do Nginx Proxy Manager e crie um novo host proxy com as seguintes configurações:

- Esquema: `http`
- Nome do Host / IP de Encaminhamento: o nome do host do seu servidor TrueNAS (por exemplo, `truenas`)
- Porta de Encaminhamento: a porta atribuída ao seu aplicativo Gramps Web (verifique a interface de Aplicativos do TrueNAS para a porta exata)
- Na aba "SSL", marque "Forçar SSL"
- Em "Certificados SSL", selecione "Adicionar Certificado SSL" > "Let's Encrypt" para criar um novo certificado Let's Encrypt para seu domínio.

Por favor, consulte a [documentação do Nginx Proxy Manager](https://nginxproxymanager.com/guide/) para mais detalhes sobre como configurar seu roteador e obter certificados SSL.
