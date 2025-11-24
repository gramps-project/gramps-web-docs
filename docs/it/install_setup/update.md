# Aggiornare Gramps Web

Se stai utilizzando uno dei metodi di installazione basati su Docker Compose, aggiornare Gramps Web all'ultima versione è semplice. Nella cartella in cui si trova il tuo `docker-compose.yml`, esegui i seguenti comandi

```bash
docker compose pull
docker compose up -d
```

Per salti di versione minori dell'[API di Gramps Web](https://github.com/gramps-project/gramps-web-api), questo è tutto ciò che è necessario. Segui comunque le [note di rilascio dell'API di Gramps Web](https://github.com/gramps-project/gramps-web-api/releases), poiché potrebbero esserci modifiche significative che richiedono ulteriore attenzione o modifiche di configurazione.

Nota che l'immagine docker predefinita `grampsweb:latest` combina sempre l'ultima versione dell'API con l'ultima versione del frontend. Se desideri aggiornare i due componenti separatamente - il che è possibile - è necessaria una configurazione più complessa di quella descritta qui.
