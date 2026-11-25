# Aplicativo Gramps Web 1-Click da DigitalOcean

Em vez de [configurar o Gramps Web por conta própria](deployment.md), você também pode usar o [aplicativo Gramps Web 1-Click da DigitalOcean](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). A DigitalOcean hospeda a versão Demo do Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Como parte do procedimento de configuração, você precisará criar uma conta na DigitalOcean e selecionar um plano pago para o "droplet" (máquina virtual) a ser usado.

Pode-se dizer que esta é atualmente a maneira mais simples de implantar sua própria instância auto-hospedada do Gramps Web, protegida com SSL, sem usar seu próprio hardware.

!!! info
    Observe que você pagará à DigitalOcean pelos serviços de hospedagem. O projeto de código aberto Gramps não oferece suporte pago.

## Etapa 1: Crie uma conta na DigitalOcean

Crie uma conta na [DigitalOcean](https://www.digitalocean.com/) se ainda não tiver uma.

## Etapa 2: Crie o droplet

- Acesse o [aplicativo Gramps Web 1-Click](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) e clique em "Create Gramps Web Droplet".
- Escolha um plano com pelo menos 2 GB de RAM.
- Configure a autenticação do seu droplet
- Clique em "Create Droplet"

## Etapa 3: Configure um nome de domínio

Você precisará de um nome de domínio (ou subdomínio). Se você possui um domínio, aponte-o para o endereço IP do seu droplet. Caso contrário, você pode usar um serviço gratuito, como o [DuckDNS](https://www.duckdns.org/).

## Etapa 4: Faça login no seu droplet

Conecte-se ao seu droplet via SSH. Você deverá ver a mensagem "Welcome to the Gramps Web DigitalOcean 1-click app setup!". Se esse não for o caso, aguarde alguns minutos e tente novamente (a instalação ainda não foi concluída).

O script de configuração solicitará o nome de domínio (por exemplo, `mygrampswebinstance.duckdns.org`) e um endereço de e-mail (necessário para o certificado do Let's Encrypt). Opcionalmente, ele também solicitará as configurações de SMTP usadas pelo Gramps Web para enviar e-mails, por exemplo, para redefinições de senha; deixe o host SMTP vazio para ignorar esta etapa.

Quando isso estiver concluído, aguarde a conclusão da configuração em segundo plano

## Etapa 5: Inicie o Gramps Web

Sua instância do Gramps Web agora deverá estar acessível na raiz do seu domínio, com um certificado SSL válido, e deverá exibir o assistente de primeira execução.

## Alterar a configuração posteriormente

O script de configuração armazena a URL base e as configurações de e-mail no arquivo `/root/letsencrypt.env` como [opções de configuração](configuration.md) prefixadas com `GRAMPSWEB_`, por exemplo:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Para adicionar ou alterar configurações, edite este arquivo no droplet e aplique a alteração com

```bash
cd /opt/grampsweb && docker compose up -d
```
