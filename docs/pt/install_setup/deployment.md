# Implantando o Gramps Web com Docker

A opção mais conveniente para hospedar o Gramps Web em seu próprio servidor (ou servidor virtual) é com o Docker Compose.

Assumiremos que o Docker e o Docker Compose já estão instalados em seu sistema. Você pode usar Windows, Mac OS ou Linux como sistema host. As arquiteturas suportadas incluem não apenas x86-64 (sistemas desktop), mas também sistemas ARM, como um Raspberry Pi, que pode servir como um servidor web de baixo custo, mas poderoso (o suficiente).

!!! note
    Você não precisa instalar o Gramps no servidor, pois ele está contido na imagem do docker.


## Passo 1: Configuração do Docker

Crie um novo arquivo no servidor chamado `docker-compose.yml` e insira o seguinte conteúdo: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).



Isso gerará seis volumes nomeados para garantir que todos os dados relevantes persistam ao reiniciar o contêiner.

!!! warning
    O acima tornará a API disponível na porta 80 da máquina host **sem proteção SSL/TLS**. Você pode usar isso para testes locais, mas não exponha isso diretamente à internet, é completamente inseguro!

## Passo 2: Acesso seguro com SSL/TLS

A API web **deve** ser servida ao público na internet via HTTPS. Existem várias opções, por exemplo:

- Usar um serviço de hospedagem Docker que inclua SSL/TLS automaticamente
- Usar um Nginx Reverse Proxy com um certificado Let's Encrypt

Veja [Docker com Let's Encrypt](lets_encrypt.md) para saber como configurar a primeira opção.

Se você planeja usar o Gramps Web apenas em sua rede local, pode pular esta etapa.

## Passo 3: Iniciar o servidor

Execute

```
docker compose up -d
```

Na primeira execução, o aplicativo exibirá um assistente de primeira execução que permitirá que você

- Crie uma conta para o usuário proprietário (admin)
- Defina algumas opções de configuração necessárias
- Importe uma árvore genealógica no formato XML do Gramps (`.gramps`)

## Passo 4: Fazer upload de arquivos de mídia

Existem várias opções para fazer upload de arquivos de mídia.

- Ao usar arquivos armazenados no mesmo servidor que o Gramps Web, você pode montar um diretório no contêiner Docker em vez de usar um volume nomeado, ou seja, `/home/server_user/gramps_media/:/app/media` em vez de `gramps_media:/app/media`, e fazer o upload de seus arquivos de mídia lá.
- Ao usar arquivos de mídia [hospedados no S3](s3.md), você pode usar o Addon S3 Media Uploader
- A opção indiscutivelmente mais conveniente é usar [Gramps Web Sync](../administration/sync.md).
