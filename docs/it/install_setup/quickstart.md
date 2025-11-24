Per provare Gramps Web sul tuo computer locale (Linux, Mac o Windows) senza interferire con la tua installazione di Gramps Desktop, puoi utilizzare Docker con il seguente comando:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Questo renderà accessibile una nuova istanza vuota di Gramps Web all'indirizzo [http://localhost:5055](http://localhost:5055), dove puoi creare un utente admin e importare un file XML di Gramps.

!!! info
    Poiché questa semplice configurazione non consente di eseguire attività lunghe in un processo separato, l'importazione di un grande file XML di Gramps potrebbe non riuscire a causa di un timeout nell'assistente di primo avvio.


Per utilizzare file multimediali dal tuo computer, puoi montare la cartella multimediale di Gramps nel contenitore con

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Nota che questo non persisterà le modifiche che apporti al database quando riavvii il contenitore. Per configurare correttamente Gramps Web, continua a leggere riguardo al [Deployment](deployment.md).
