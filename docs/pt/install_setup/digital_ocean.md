# Gramps Web DigitalOcean 1-Click App

Em vez de [configurar o Gramps Web você mesmo](deployment.md), você também pode usar o [Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). A Digital Ocean hospeda a versão Demo do Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Como parte do procedimento de configuração, você terá que se inscrever para uma conta na DigitalOcean e selecionar um plano pago para o "droplet" (máquina virtual) a ser utilizado.

Pode-se argumentar que esta é atualmente a maneira mais simples de implantar sua própria instância do Gramps Web auto-hospedada, segura com SSL, sem usar seu próprio hardware.

!!! info
    Observe que você estará pagando à DigitalOcean pelos serviços de hospedagem. O projeto de código aberto Gramps não oferece suporte pago.

## Passo 1: Criar uma conta na DigitalOcean

Crie uma conta em [DigitalOcean](https://www.digitalocean.com/) se você ainda não tiver uma.

## Passo 2: Criar o droplet

- Vá para [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) e clique em "Criar Droplet do Gramps Web".
- Escolha um plano com pelo menos 2 GB de RAM.
- Configure a autenticação para o seu droplet.
- Clique em "Criar Droplet".

!!! info
    Você pode precisar esperar até dez minutos para que o 1-Click App instale a versão mais recente do `docker-compose`.
    Usar a versão mais recente do `docker-compose` pode mitigar erros que fazem referência ao `firstlogin.sh`. 
    
## Passo 3: Configurar um nome de domínio

Você precisará de um nome de domínio (ou subdomínio). Se você possui um domínio, aponte-o para o endereço IP do seu droplet. Caso contrário, você pode usar um serviço gratuito como o [DuckDNS](https://www.duckdns.org/).

## Passo 4: Fazer login no seu droplet

Acesse seu droplet via SSH. Você deve ver a mensagem "Bem-vindo à configuração do Gramps Web DigitalOcean 1-click app!". Se não for o caso, aguarde alguns minutos e tente novamente (a instalação ainda não foi concluída).

O script de configuração solicitará o nome de domínio (por exemplo, `mygrampswebinstance.duckdns.org`) e um endereço de e-mail (necessário para o certificado Let's Encrypt).

Quando isso estiver feito, aguarde a conclusão da configuração em segundo plano.

## Passo 5: Iniciar o Gramps Web

Sua instância do Gramps Web agora deve estar acessível na raiz do seu domínio, com um certificado SSL válido, e deve estar exibindo o assistente de primeiro uso.
