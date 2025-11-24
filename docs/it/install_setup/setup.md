# Installazione / Configurazione di Gramps Web

Questa sezione tratta dell'installazione e configurazione di Gramps Web, così come altre opzioni per iniziare.

## Iniziare con Gramps Web

Gramps Web è un'app web che gira su un server ed è accessibile tramite il browser web. È progettata per essere resa accessibile a utenti autenticati tramite internet.

Se desideri utilizzare Gramps Web per i tuoi dati di ricerca genealogica, devi scegliere una delle seguenti opzioni:

1. Autoinstallazione sul proprio hardware
2. Autoinstallazione nel cloud
3. Iscrizione a un'istanza ospitata

Mentre la prima opzione ti offre la massima flessibilità e controllo, può anche essere tecnicamente impegnativa.

!!! tip
    Uno dei principi fondamentali di Gramps Web è mettere gli utenti al controllo dei propri dati in qualsiasi momento, quindi migrare i dati da un'istanza all'altra è semplice. Non preoccuparti di essere bloccato dopo aver scelto una delle opzioni!

## Autoinstallazione sul proprio hardware

Il modo più conveniente per autoinstallare Gramps Web è tramite Docker Compose. Forniamo anche immagini Docker per l'architettura ARM, così puoi eseguire Gramps Web su un Raspberry Pi nel tuo seminterrato.

Consulta [Distribuzione con Docker](deployment.md) per le istruzioni di configurazione.

## Autoinstallazione nel cloud

Installare Gramps Web può essere più impegnativo rispetto ad altre semplici applicazioni web e non è compatibile con i normali fornitori di "hosting condiviso". Puoi iscriverti a un server virtuale e installare Gramps Web [manualmente](deployment.md).

Un'opzione più semplice è utilizzare un'immagine cloud preinstallata. Un esempio è la nostra [app DigitalOcean 1-click](digital_ocean.md).

## Iscrizione a un'istanza ospitata

Un Gramps Web ospitato è il modo più semplice per iniziare con Gramps Web, poiché non è richiesta alcuna installazione o configurazione.

Ecco un elenco di fornitori di hosting dedicati per Gramps Web (la comunità open source di Gramps non si assume responsabilità per i loro servizi):

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), offerto da uno dei principali contributori di Gramps Web

Se utilizzi un'opzione ospitata per Gramps Web, puoi saltare il resto di questa sezione e passare direttamente alla sezione [Amministrazione](../administration/admin.md).
