# Utilizzo di un database PostgreSQL

Per impostazione predefinita, Gramps utilizza un database SQLite basato su file per memorizzare l'albero genealogico. Questo funziona perfettamente per Gramps Web ed è raccomandato per la maggior parte degli utenti. Tuttavia, a partire dalla versione 0.3.0 dell'API Gramps Web, è supportato anche un server PostgreSQL con un singolo albero genealogico per database, alimentato dall'[Addon PostgreSQL di Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). Dalla [versione 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0), è supportato anche l'Addon SharedPostgreSQL, che consente di ospitare più alberi genealogici in un singolo database, particolarmente utile se utilizzato insieme al [supporto multi-albero](multi-tree.md) dell'API Gramps Web.

!!! warning "Backend PostgreSQL deprecato"
    Il supporto per il backend PostgreSQL (un albero genealogico per database) sarà rimosso in una futura versione dell'API Gramps Web, poiché non è compatibile con l'hosting di più alberi. I backend SharedPostgreSQL e SQLite rimangono completamente supportati. Per nuove installazioni, utilizzare SharedPostgreSQL.

## Configurazione del server PostgreSQL

Se desideri configurare un nuovo database da utilizzare con l'Addon PostgreSQL, puoi seguire le [istruzioni nel Wiki di Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) per configurare il server.

In alternativa, puoi anche utilizzare Docker Compose per eseguire il server PostgreSQL in un contenitore sullo stesso host Docker di Gramps Web.

Utilizzare un PostgreSQL dockerizzato con Gramps è complicato solo dal fatto che le immagini PostgreSQL predefinite non hanno alcuna localizzazione installata, necessaria a Gramps per la collazione localizzata degli oggetti. L'opzione più semplice è utilizzare l'immagine `gramps-postgres` rilasciata in [questo repository](https://github.com/DavidMStraub/gramps-postgres-docker/). Per utilizzarla, aggiungi la seguente sezione al tuo `docker-compose.yml`:
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
e aggiungi anche `postgres_data:` come chiave sotto la sezione `volumes:` di questo file YAML. Questa immagine contiene un database separato per i dati genealogici di Gramps e per il database utente di Gramps; ciascuno può avere password separate.

## Importazione di un albero genealogico di Gramps

Ancora una volta, se hai configurato il server PostgreSQL da solo, puoi seguire le [istruzioni nel Wiki di Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) per importare un albero genealogico nel database.

In alternativa, se hai seguito le istruzioni di Docker Compose sopra, puoi utilizzare il seguente comando per importare un file XML di Gramps situato sul tuo host Docker:

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## Configurazione dell'API Web per l'uso con il database

Per configurare l'API Web per l'uso con il database PostgreSQL, aggiungi quanto segue sotto la chiave `environment:` del servizio `grampsweb` in `docker-compose.yml`:

```yaml
      # l'addon PostgreSQL presume che il nome dell'albero sia
      # uguale al nome del database e qui viene utilizzato il nome
      # del database predefinito dell'immagine PostgreSQL
      GRAMPSWEB_TREE: postgres
      # Le credenziali devono corrispondere a quelle utilizzate per
      # il contenitore PostgreSQL
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

## Utilizzo di un database PostgreSQL condiviso in un'installazione multi-albero

Quando si utilizza una [configurazione multi-albero](multi-tree.md), l'addon SharedPostgreSQL è un'opzione comoda per ospitare tutti gli alberi, anche quelli appena creati tramite l'API, in un singolo database PostgreSQL senza compromettere la privacy o la sicurezza.

Per ottenere ciò, configura un contenitore basato sull'immagine `gramps-postgres` come descritto sopra e imposta semplicemente l'opzione di configurazione `NEW_DB_BACKEND` su `sharedpostgresql`, ad esempio tramite la variabile d'ambiente `GRAMPSWEB_NEW_DB_BACKEND`.

## Utilizzo di un database PostgreSQL per il database utente

Indipendentemente dal backend del database utilizzato per i dati genealogici, il database utente può essere ospitato in un database PostgreSQL fornendo un'appropriata URL del database. L'immagine Docker `gramps-postgres` menzionata sopra contiene un database separato `grampswebuser` che può essere utilizzato a questo scopo. In tal caso, il valore appropriato per l'opzione di configurazione `USER_DB_URI` sarebbe
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Utilizzo di un database PostgreSQL per l'indice di ricerca

Dalla versione 2.4.0 dell'API Gramps Web, l'indice di ricerca è ospitato in un database SQLite (il predefinito) o in un database PostgreSQL. Anche per questo scopo, può essere utilizzata l'immagine `gramps-postgres`. Per l'indice di ricerca, possiamo utilizzare il database `gramps` fornito dall'immagine, indipendentemente dal fatto che stiamo ospitando i nostri dati genealogici in PostgreSQL o meno (l'indice di ricerca e i dati genealogici possono coesistere nello stesso database). Questo può essere ottenuto, nell'esempio sopra, impostando l'opzione di configurazione `SEARCH_INDEX_DB_URI` su
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Problemi

In caso di problemi, si prega di monitorare l'output del log di Gramps Web e del server PostgreSQL. Nel caso di Docker, ciò si ottiene con

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Se sospetti che ci sia un problema con Gramps Web (o la documentazione), ti preghiamo di segnalare un problema [su Github](https://github.com/gramps-project/gramps-web-api/issues).
