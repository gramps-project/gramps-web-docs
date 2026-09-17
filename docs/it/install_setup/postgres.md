# Utilizzo di un database PostgreSQL

Per impostazione predefinita, Gramps Web memorizza ogni albero genealogico nel proprio file di database SQLite. Questo non richiede alcun servizio aggiuntivo, i backup sono semplici come copiare file e funziona bene per la maggior parte delle installazioni, comprese quelle [che ospitano più alberi](multi-tree.md).

In alternativa, gli alberi genealogici possono essere ospitati su un server PostgreSQL utilizzando l'addon SharedPostgreSQL, che mantiene tutti gli alberi in un unico database. Questo può avere senso se gestisci già un server PostgreSQL e desideri gestire i backup e il monitoraggio lì, o se ti aspetti che molti utenti modifichino contemporaneamente. PostgreSQL può anche ospitare il [database utenti](#using-a-postgresql-database-for-the-user-database) e l'[indice di ricerca](#using-a-postgresql-database-for-the-search-index), indipendentemente da dove siano memorizzati gli alberi genealogici.

!!! warning "Addon PostgreSQL deprecato"
    L'addon PostgreSQL più vecchio, che memorizza un singolo albero genealogico per database, è deprecato e non sarà più supportato in una futura versione dell'API Gramps Web. Se lo stai utilizzando, consulta [Spostare un albero dall'addon PostgreSQL a SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Configurazione del server PostgreSQL

L'opzione più semplice è eseguire il server PostgreSQL in un container sullo stesso host Docker di Gramps Web, utilizzando Docker Compose.

Gramps ha bisogno di localizzazioni installate sul server PostgreSQL per ordinare correttamente gli oggetti in diverse lingue, e le immagini PostgreSQL predefinite non includono alcuna. L'immagine [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) le aggiunge. Per usarla, aggiungi la seguente sezione al tuo `docker-compose.yml`:
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
e aggiungi anche `postgres_data:` come chiave sotto la sezione `volumes:` di questo file YAML. L'immagine contiene due database, ciascuno con il proprio utente e password: `gramps` per i dati genealogici e `grampswebuser` per il database utenti di Gramps Web.

Se utilizzi il tuo server PostgreSQL, crea un database chiamato `gramps` in cui l'utente configurato può creare tabelle e assicurati che le localizzazioni necessarie ai tuoi utenti siano installate.

## Configurazione di Gramps Web

Nuovi alberi genealogici vengono creati nel database SharedPostgreSQL quando Gramps Web è in esecuzione in [modalità multi-albero](multi-tree.md) e l'opzione di configurazione `NEW_DB_BACKEND` è impostata su `sharedpostgresql`. Con la configurazione Docker Compose sopra, aggiungi quanto segue sotto la chiave `environment:` del servizio `grampsweb` in `docker-compose.yml`:

```yaml
      # abilita la modalità multi-albero
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # crea nuovi alberi nel database SharedPostgreSQL
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # L'host e la porta del server PostgreSQL. L'
      # host è il nome del servizio PostgreSQL sopra
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Le credenziali devono corrispondere a quelle utilizzate per
      # il container PostgreSQL
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Consulta [Configurazione](configuration.md) per una descrizione di tutte queste opzioni. Nota che l'host e la porta vengono salvati con ogni albero quando viene creato, quindi modificarli in seguito influisce solo sui nuovi alberi.

## Creazione di un albero e importazione dei dati

Per creare un nuovo albero, invia una richiesta POST all'endpoint `/trees/` come descritto in [Configurazione per l'hosting di più alberi](multi-tree.md#create-a-new-tree). La risposta contiene l'ID del nuovo albero, necessario per [creare l'account del proprietario dell'albero](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Una volta che il proprietario dell'albero ha effettuato l'accesso, può [importare](../administration/import.md) un albero genealogico esistente, ad esempio un file XML di Gramps esportato da Gramps Desktop, tramite l'interfaccia web.

## Utilizzo di un database PostgreSQL per il database utenti

Il database utenti è solitamente un file SQLite, indipendentemente da dove siano ospitati gli alberi genealogici. Per utilizzare PostgreSQL invece, imposta l'opzione di configurazione `USER_DB_URI` su un URL di database PostgreSQL. Con l'immagine `gramps-postgres` sopra, utilizza il suo database `grampswebuser`:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Utilizzo di un database PostgreSQL per l'indice di ricerca

L'indice di ricerca è anch'esso memorizzato in SQLite per impostazione predefinita. Per utilizzare PostgreSQL invece, imposta l'opzione di configurazione `SEARCH_INDEX_DB_URI` su un URL di database PostgreSQL. Con l'immagine `gramps-postgres` sopra, puoi utilizzare il suo database `gramps`, sia che i tuoi alberi genealogici siano ospitati lì o meno:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Spostare un albero dall'addon PostgreSQL a SharedPostgreSQL

Le installazioni più vecchie possono ospitare il loro albero genealogico con l'addon PostgreSQL, che memorizza un singolo albero per database ed è deprecato. Per scoprire quale addon utilizza un albero, controlla il file `database.txt` nella sottodirectory dell'albero nella directory del database di Gramps: contiene `postgresql` per l'addon PostgreSQL deprecato e `sharedpostgresql` per SharedPostgreSQL.

Per spostare un albero dall'addon PostgreSQL a SharedPostgreSQL all'interno della stessa installazione, mantenendo i tuoi account utente e file multimediali:

1. [Esegui il backup del tuo albero genealogico](../administration/export.md#back-up-your-family-tree) come file XML di Gramps (`.gramps`), utilizzando un account che può visualizzare record privati.
2. Modifica la tua configurazione come descritto in [Configurazione di Gramps Web](#configuring-gramps-web). Puoi continuare a utilizzare il tuo container `gramps-postgres` esistente.
3. [Crea un nuovo albero](multi-tree.md#create-a-new-tree) e annota il suo ID albero.
4. Assegna i tuoi account utente esistenti al nuovo albero, come descritto in [Migrare il database utenti esistente](multi-tree.md#migrate-existing-user-database).
5. Sposta i tuoi file multimediali nella posizione prevista per il nuovo albero, come descritto in [Migrare i file multimediali esistenti](multi-tree.md#migrate-existing-media-files).
6. Accedi e [importa](../administration/import.md) il file XML di Gramps nel nuovo albero.

Conserva il file XML di Gramps fino a quando non hai verificato che il nuovo albero sia completo.

Se stai migrando a un'installazione separata di Gramps Web, segui i passaggi in [Spostare a un'altra istanza di Gramps Web](../administration/export.md#move-to-a-different-gramps-web-instance).

## Problemi

In caso di problemi, monitora l'output del log di Gramps Web e del server PostgreSQL. Nel caso di Docker, questo si ottiene con

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Se sospetti che ci sia un problema con Gramps Web (o la documentazione), ti preghiamo di segnalare un problema [su Github](https://github.com/gramps-project/gramps-web-api/issues).
