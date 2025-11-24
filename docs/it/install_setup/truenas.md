# Configurazione di TrueNAS

Questa guida spiega come configurare Gramps Web su TrueNAS Community Edition 25.04.

!!! warning
    Questa guida è destinata a TrueNAS Community Edition 25.04 o versioni successive, che ha introdotto un nuovo sistema di app basato su Docker Compose. Non si applica alle versioni precedenti di TrueNAS.

## Requisiti

- TrueNAS Community Edition 25.04 o versioni successive
- Familiarità di base con l'interfaccia web di TrueNAS
- Un dataset per memorizzare i dati di Gramps Web

## Panoramica

TrueNAS Community Edition 25.04 ha introdotto un nuovo sistema di app basato su Docker Compose che sostituisce l'approccio precedente basato su Helm chart. Questa guida ti guiderà nella creazione di un'app personalizzata per Gramps Web utilizzando Docker Compose.

## Passo 1: Preparare lo Storage

1. Naviga su **Datasets** nell'interfaccia web di TrueNAS
2. Crea un nuovo dataset per Gramps Web (ad esempio, `grampsweb`). Prendi nota del percorso completo di questo dataset, ad esempio, `/mnt/storage/grampsweb`, poiché ne avrai bisogno in seguito.

Crea sottodirectory per i vari componenti:
- `users` - Database utenti
- `database` - File del database di Gramps
- `media` - File multimediali

## Passo 2: Creare l'App Docker Compose

1. Naviga su **Apps** nell'interfaccia web di TrueNAS
2. Clicca su **Discover Apps**
3. Cerca "Gramps Web" e clicca su di esso
4. Clicca su "Install"

Questo ti porterà alla pagina di configurazione dell'app.

## Passo 3: Configurare l'App

### Configurazione di Gramps Web

- **Fuso orario:** Imposta sul tuo fuso orario locale (ad esempio, `Europe/Berlin`)
- **Password Redis:** Imposta una password per Redis. Questa sarà utilizzata solo internamente dall'app.
- **Disabilita telemetria:** ti preghiamo di lasciare questa casella deselezionata – vedi [qui per dettagli](telemetry.md).
- **Chiave segreta:** è fondamentale che tu imposti questo su un valore forte e unico. Vedi [configurazione del server](configuration.md#existing-configuration-settings) per istruzioni su come generare una chiave casuale.
- **Variabili ambientali aggiuntive:** Dovrai impostare tutte le opzioni di [configurazione](configuration.md) aggiuntive come variabili ambientali prefissate da `GRAMPSWEB_`. Ti preghiamo di controllare la [documentazione di configurazione](configuration.md) in dettaglio – ad esempio, il fatto che i valori booleani devono essere impostati come `true` o `false` (tutto in minuscolo) nel caso delle variabili ambientali, un errore comune.

Ti preghiamo di **impostare almeno** `GRAMPSWEB_BASE_URL` sull'URL a cui sarà accessibile la tua istanza di Gramps Web – questo è necessario per un funzionamento corretto.

Potresti anche voler configurare l'email a questo punto. Se lo fai, puoi saltare il passaggio di configurazione dell'email nella procedura guidata di onboarding. Le variabili ambientali pertinenti sono:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Tutte le impostazioni di configurazione possono essere modificate in seguito cliccando su "Edit" nell'interfaccia delle App di TrueNAS.

### Configurazione dello Storage

- **Storage Utenti**: Seleziona il percorso della directory `users` che hai creato in precedenza.
- **Storage Indice**: Puoi lasciare l'impostazione predefinita "ixVolume (Dataset creato automaticamente dal sistema)"
- **Storage Cache Miniature**: Puoi lasciare l'impostazione predefinita "ixVolume (Dataset creato automaticamente dal sistema)"
- **Storage Cache**: Puoi lasciare l'impostazione predefinita "ixVolume (Dataset creato automaticamente dal sistema)"
- **Storage Media**: Seleziona il percorso della directory `media` che hai creato in precedenza.
- **Storage Database di Gramps**: Seleziona il percorso della directory `database` che hai creato in precedenza.

### Configurazione delle Risorse

Ti consigliamo di allocare almeno 2 CPU e 4096 MB di RAM per garantire un funzionamento fluido.

## Passo 4: Accedere a Gramps Web

Una volta che l'app è stata distribuita, puoi accedere a Gramps Web cliccando sul pulsante "Web UI" nell'interfaccia delle App di TrueNAS. Dovresti vedere la procedura guidata di onboarding "Benvenuto in Gramps Web".

Se desideri consentire agli utenti di accedere alla tua interfaccia Gramps Web, **non** esporre l'app direttamente a Internet, ma procedi al passaggio successivo.

## Passo 5: Configurare un Reverse Proxy

Per esporre in modo sicuro la tua istanza di Gramps Web agli utenti, è consigliato configurare un reverse proxy. Questo ti consente di gestire i certificati SSL/TLS e controllare l'accesso.

L'opzione più semplice è utilizzare l'app ufficiale TrueNAS Nginx Proxy Manager. Cerca l'app nell'interfaccia delle App di TrueNAS e installala. Puoi lasciare tutte le impostazioni ai loro valori predefiniti, ma ti consigliamo di impostare una variabile ambientale aggiuntiva: `DISABLE_IPV6` con valore `true` per evitare potenziali problemi legati a IPv6.

Una volta distribuito, apri l'interfaccia web di Nginx Proxy Manager e crea un nuovo host proxy con le seguenti impostazioni:

- Schema: `http`
- Hostname / IP di Forward: il nome host del tuo server TrueNAS (ad esempio, `truenas`)
- Porta di Forward: la porta assegnata alla tua app Gramps Web (controlla l'interfaccia delle App di TrueNAS per la porta esatta)
- Nella scheda "SSL", seleziona "Force SSL"
- Sotto "Certificati SSL", seleziona "Aggiungi certificato SSL" > "Let's Encrypt" per creare un nuovo certificato Let's Encrypt per il tuo dominio.

Ti preghiamo di consultare la [documentazione di Nginx Proxy Manager](https://nginxproxymanager.com/guide/) per ulteriori dettagli sulla configurazione del tuo router e sull'ottenimento di certificati SSL.
