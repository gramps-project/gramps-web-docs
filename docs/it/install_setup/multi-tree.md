# Configurazione per l'hosting di più alberi

Per impostazione predefinita, Gramps Web consente di accedere solo a un singolo database di alberi genealogici (“albero”), specificato nel file di configurazione.

Tuttavia, a partire dalla versione 0.7.0 del backend dell'API Gramps Web, è anche possibile servire più alberi da un'unica installazione. Tuttavia, ogni utente è (attualmente) legato a un singolo albero, quindi questa configurazione non è adatta per condividere alberi tra utenti, ma per ospitare più istanze isolate di Gramps Web.

## Abilitare il supporto multi-albero

Per abilitare il supporto multi-albero, l'opzione di configurazione `TREE` deve essere impostata su un singolo asterisco `*`, ad esempio in un file di configurazione:

```python
TREE = "*"
```

Questo renderà accessibili tutti gli alberi nella directory del database Gramps del server (data la sufficiente autorizzazione dell'utente). L'ID dell'albero è il nome della sottodirectory. Puoi elencare gli alberi esistenti (nomi e ID) con il comando

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Inoltre, dovresti impostare l'opzione di configurazione `MEDIA_PREFIX_TREE` su `True` per garantire che i file multimediali siano memorizzati in sottocartelle separate. Altrimenti, gli utenti possono accedere a file multimediali che appartengono a un albero per il quale non hanno autorizzazione!

## Aggiungere un'account utente a un albero specifico

Per aggiungere un utente a un albero specifico, basta aggiungere l'opzione della riga di comando `--tree TREEID` al comando di aggiunta utente. Puoi anche POSTare all'endpoint `/users/` con la proprietà `tree` impostata nel payload JSON.

I nomi utente e gli indirizzi e-mail devono essere unici in *tutti* gli alberi.

## Creare un nuovo albero

Per creare un nuovo albero, è consigliabile POSTare all'endpoint `/trees/` piuttosto che utilizzare il CLI di Gramps. Questo utilizzerà un UUIDv4 come ID dell'albero, il che porta a una maggiore sicurezza poiché il nome non può essere indovinato. Attualmente, solo SQLite è supportato per gli alberi appena creati.

## Autorizzare

Per autorizzare (recuperare un token), sono necessari solo nome utente e password, come nella modalità a singolo albero, poiché l'ID dell'albero è noto per ogni utente, quindi non è necessario fornirlo.

## Migrare file multimediali esistenti

Se desideri migrare un'istanza Gramps Web esistente al supporto multi-albero e stai utilizzando file multimediali locali, puoi semplicemente spostarli in una sottocartella della posizione originale con l'ID dell'albero come nome.

Se stai utilizzando file multimediali ospitati su S3, puoi utilizzare lo script fornito nella directory `scripts` del repository `gramps-web-api`:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Questo presuppone che le chiavi di accesso pertinenti siano già impostate come variabili di ambiente.

## Migrare il database utenti esistente

Se desideri abilitare il supporto multi-albero e riutilizzare utenti esistenti, devi assegnarli a un albero specifico. Puoi utilizzare il seguente comando fornito per questo scopo,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Personalizzare il frontend

La pagina di registrazione accessibile dalla pagina di accesso non funziona in una configurazione multi-albero, poiché è necessario specificare un albero per la registrazione. È quindi consigliabile impostare `hideRegisterLink` su `true` nella [configurazione del frontend](frontend-config.md).
