# Gramps Web DigitalOcean 1-Click App

Invece di [configurare Gramps Web da solo](deployment.md), puoi anche utilizzare il [Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean ospita la versione Demo di Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Come parte della procedura di configurazione, dovrai registrarti per un account con DigitalOcean e selezionare un piano a pagamento per il "droplet" (macchina virtuale) da utilizzare.

Si può dire che questo sia attualmente il modo più semplice per distribuire la propria istanza di Gramps Web auto-ospitata, protetta con SSL, senza utilizzare il proprio hardware.

!!! info
    Tieni presente che pagherai DigitalOcean per i servizi di hosting. Il progetto open source Gramps non fornisce supporto a pagamento.

## Passo 1: Crea un account DigitalOcean

Crea un account su [DigitalOcean](https://www.digitalocean.com/) se non ne hai già uno.

## Passo 2: Crea il droplet

- Vai su [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) e clicca su "Crea Droplet Gramps Web".
- Scegli un piano con almeno 2 GB di RAM.
- Configura l'autenticazione per il tuo droplet.
- Clicca su "Crea Droplet".

## Passo 3: Configura un nome di dominio

Avrai bisogno di un nome di dominio (o sottodominio). Se possiedi un dominio, puntalo all'indirizzo IP del tuo droplet. In caso contrario, puoi utilizzare un servizio gratuito come [DuckDNS](https://www.duckdns.org/).

## Passo 4: Accedi al tuo droplet

Accedi al tuo droplet tramite SSH. Dovresti vedere il messaggio "Benvenuto nella configurazione dell'app Gramps Web DigitalOcean 1-click!". Se così non fosse, aspetta qualche minuto e riprova (l'installazione non è ancora terminata).

Lo script di configurazione ti chiederà il nome di dominio (ad es. `mygrampswebinstance.duckdns.org`) e un indirizzo e-mail (necessario per il certificato Let's Encrypt). Facoltativamente, ti chiederà anche le impostazioni SMTP che Gramps Web utilizza per inviare e-mail, ad esempio per il ripristino della password; lascia vuoto l'host SMTP per saltare questo passaggio.

Quando questo è fatto, aspetta che la configurazione venga completata in background.

## Passo 5: Avvia Gramps Web

La tua istanza di Gramps Web dovrebbe ora essere accessibile alla radice del tuo dominio, con un certificato SSL valido, e dovrebbe mostrare l'assistente per il primo avvio.

## Modificare la configurazione in seguito

Lo script di configurazione memorizza l'URL di base e le impostazioni e-mail nel file `/root/letsencrypt.env` come [opzioni di configurazione](configuration.md) con prefisso `GRAMPSWEB_`, ad esempio:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Per aggiungere o modificare le impostazioni, modifica questo file sul droplet e applica la modifica con

```bash
cd /opt/grampsweb && docker compose up -d
