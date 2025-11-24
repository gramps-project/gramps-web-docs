# Distribuire Gramps Web con Docker

L'opzione più conveniente per ospitare Gramps Web sul proprio server (o server virtuale) è con Docker Compose.

Assumeremo che Docker e Docker Compose siano già installati nel tuo sistema. Puoi utilizzare Windows, Mac OS o Linux come sistema host. Le architetture supportate includono non solo x86-64 (sistemi desktop), ma anche sistemi ARM come un Raspberry Pi, che può fungere da server web a basso costo, ma potente (abbastanza).

!!! nota
    Non è necessario installare Gramps sul server poiché è contenuto nell'immagine docker.


## Passo 1: Configurazione di Docker

Crea un nuovo file sul server chiamato `docker-compose.yml` e inserisci il seguente contenuto: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).



Questo genererà sei volumi nominati per assicurarsi che tutti i dati rilevanti persistano al riavvio del container.

!!! avviso
    Quanto sopra renderà l'API disponibile sulla porta 80 della macchina host **senza protezione SSL/TLS**. Puoi utilizzare questo per test locali, ma non esporlo direttamente a Internet, è completamente insicuro!

## Passo 2: Accesso sicuro con SSL/TLS

L'API web **deve** essere servita al pubblico su Internet tramite HTTPS. Ci sono diverse opzioni, ad esempio:

- Utilizzare un hosting Docker che include automaticamente SSL/TLS
- Utilizzare un Nginx Reverse Proxy con un certificato Let's Encrypt

Consulta [Docker con Let's Encrypt](lets_encrypt.md) per come configurare la prima opzione.

Se prevedi di utilizzare Gramps Web solo sulla tua rete locale, puoi saltare questo passaggio.

## Passo 3: Avviare il server

Esegui

```
docker compose up -d
```

Al primo avvio, l'app mostrerà una procedura guidata di primo avvio che ti permetterà di

- Creare un account per l'utente proprietario (admin)
- Impostare alcune opzioni di configurazione necessarie
- Importare un albero genealogico in formato Gramps XML (`.gramps`)

## Passo 4: Caricare file multimediali

Ci sono diverse opzioni per caricare file multimediali.

- Quando si utilizzano file memorizzati sullo stesso server di Gramps Web, puoi montare una directory nel container Docker invece di utilizzare un volume nominato, ad esempio `/home/server_user/gramps_media/:/app/media` invece di `gramps_media:/app/media`, e caricare i tuoi file multimediali lì.
- Quando si utilizzano file multimediali [ospitati su S3](s3.md), puoi utilizzare l'Addon S3 Media Uploader
- L'opzione probabilmente più conveniente è utilizzare [Gramps Web Sync](../administration/sync.md).
