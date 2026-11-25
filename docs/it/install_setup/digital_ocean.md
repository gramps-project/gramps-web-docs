# App Gramps Web 1-Click di DigitalOcean

Invece di [configurare Gramps Web autonomamente](deployment.md), puoi anche utilizzare l'[App Gramps Web 1-Click di DigitalOcean](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). DigitalOcean ospita la versione demo di Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="Badge di referral di DigitalOcean" /></a>

Come parte della procedura di configurazione, dovrai creare un account con DigitalOcean e selezionare un piano a pagamento per il "droplet" (macchina virtuale) da utilizzare.

A tutti gli effetti, questo è attualmente il modo più semplice per distribuire la tua istanza Gramps Web, ospitata autonomamente e protetta con SSL, senza utilizzare il tuo hardware.

!!! info
    Tieni presente che pagherai DigitalOcean per i servizi di hosting. Il progetto open source Gramps non fornisce supporto a pagamento.

## Passaggio 1: crea un account DigitalOcean

Crea un account su [DigitalOcean](https://www.digitalocean.com/) se non ne hai ancora uno.

## Passaggio 2: crea il droplet

- Vai all'[App Gramps Web 1-Click](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) e fai clic su "Create Gramps Web Droplet".
- Scegli un piano con almeno 2 GB di RAM.
- Configura l'autenticazione per il tuo droplet
- Fai clic su "Create Droplet"

## Passaggio 3: configura un nome di dominio

Avrai bisogno di un nome di dominio (o sottodominio). Se possiedi un dominio, indirizzalo all'indirizzo IP del tuo droplet. In caso contrario, puoi utilizzare un servizio gratuito come [DuckDNS](https://www.duckdns.org/).

## Passaggio 4: accedi al tuo droplet

Accedi al tuo droplet tramite SSH. Dovresti visualizzare il messaggio "Welcome to the Gramps Web DigitalOcean 1-click app setup!". In caso contrario, attendi alcuni minuti e riprova (l'installazione non è ancora terminata).

Lo script di configurazione ti chiederà il nome di dominio (ad esempio `mygrampswebinstance.duckdns.org`) e un indirizzo e-mail (necessario per il certificato Let's Encrypt). Facoltativamente, ti chiederà anche le impostazioni SMTP utilizzate da Gramps Web per inviare e-mail, ad esempio per la reimpostazione delle password; lascia vuoto l'host SMTP per saltare questo passaggio.

Al termine, attendi che la configurazione venga completata in background

## Passaggio 5: avvia Gramps Web

La tua istanza Gramps Web dovrebbe ora essere accessibile alla radice del tuo dominio, con un certificato SSL valido, e dovrebbe mostrare l'assistente di primo avvio.

## Modificare la configurazione in un secondo momento

Lo script di configurazione memorizza l'URL di base e le impostazioni e-mail nel file `/root/letsencrypt.env` come [opzioni di configurazione](configuration.md) precedute da `GRAMPSWEB_`, ad esempio

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Per aggiungere o modificare le impostazioni, modifica questo file sul droplet e applica la modifica con

```bash
cd /opt/grampsweb && docker compose up -d
```
