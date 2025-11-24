# Lavorare con i match del DNA

I match del DNA sono segmenti di DNA che concordano tra due individui, identificati dalla presenza di marcatori, noti come SNP (l'acronimo di single nucleotide polymorphisms, pronunciato “snips”).

Per ottenere questi dati, è necessario avere accesso a un test del DNA che è caricato in un database di corrispondenza che consente di visualizzare i dati di corrispondenza dei segmenti di DNA (ad es. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web non esegue la corrispondenza stessa, poiché ha solo accesso ai dati che carichi.

## Inserimento dei dati di corrispondenza del DNA

Per inserire i dati di corrispondenza del DNA, hai bisogno di [permessi di modifica](../install_setup/users.md) poiché i dati sono memorizzati come una nota nel database di Gramps. La vista DNA, accessibile dal menu principale, fornisce un modo conveniente per inserire questi dati nel formato corretto.

Per inserire un nuovo match, fai clic sul pulsante + nell'angolo in basso a destra. Nella finestra di dialogo che si apre, seleziona i due individui. Nota che la “Prima persona” e la “Seconda persona” vengono trattate in modo diverso: il match è memorizzato come un'associazione dalla prima alla seconda persona. Solo la prima persona sarà selezionabile per la vista di corrispondenza del DNA e il browser dei cromosomi. Tipicamente, la prima persona è quella di cui hai accesso al test del DNA e la seconda persona è un parente più lontano.

Se la seconda persona non è nel database, devi prima crearla utilizzando il pulsante “Crea persona” nell'angolo in alto a destra dell'interfaccia utente. Una volta creata la persona, puoi tornare alla vista di corrispondenza del DNA e selezionare la persona appena creata.

Successivamente, incolla i dati grezzi nel campo di testo. I dati dovrebbero essere una tabella di corrispondenze separata da virgole o tabulazioni, contenente tipicamente il numero del cromosoma, la posizione di inizio e fine del match, il numero di SNP nel match e la lunghezza del match in unità di centimorgani (cM). Puoi anche trascinare e rilasciare un file con i dati di corrispondenza nel campo di testo.

Un esempio minimo di tale tabella è:

```csv
Cromosoma,Posizione di Inizio,Posizione di Fine,Centimorgani,SNP
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Se il formato è valido, un'anteprima viene mostrata sotto il campo di testo come una tabella.

Infine, fai clic sul pulsante “Salva” per memorizzare il match nel database.

## Visualizzazione dei dati di corrispondenza del DNA

La vista di corrispondenza del DNA ha un menu a discesa che consente di selezionare ciascuna persona nel database che ha un match del DNA associato. Una volta selezionata una persona, i dati di corrispondenza del DNA vengono mostrati in una tabella sotto il menu a discesa. Mostra il nome della persona con cui è associato il match, la relazione con la persona selezionata nel menu a discesa (determinata automaticamente dal database di Gramps), la lunghezza totale del DNA condiviso in centimorgani (cM), il numero di segmenti condivisi e la lunghezza del più grande di questi segmenti.

Quando fai clic su un match individuale, si apre una pagina di dettaglio che mostra tutti i segmenti e se il match è sul lato materno o paterno. Queste informazioni possono essere inserite manualmente (fornendo una `P` per paterno o `M` per materno in una colonna chiamata `Side` nei dati grezzi) o determinate automaticamente da Gramps in base all'antenato comune più recente.

## Modifica di un match

Puoi modificare un match facendo clic sul pulsante a forma di matita nell'angolo in basso a destra nella vista di dettaglio del match. Questo apre una finestra di dialogo simile a quella per la creazione di un nuovo match, ma con i dati già compilati. Nota che puoi cambiare i dati grezzi, ma non gli individui associati al match – devi eliminare il match e crearne uno nuovo se desideri cambiare gli individui.

## Lavorare con i dati di corrispondenza in Gramps Desktop

I dati di corrispondenza del DNA sono memorizzati come una nota nel database di Gramps. Il formato è compatibile con il 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
disponibile per Gramps Desktop. La sua pagina wiki contiene ulteriori dettagli su come ottenere i dati, come interpretarli e come inserire i dati in Gramps.

!!! info
    L'API Gramps Web v2.8.0 ha introdotto alcune modifiche per accettare una gamma più ampia di dati grezzi di corrispondenza del DNA, che non sono ancora disponibili nell'Addon di Gramps Desktop. L'Addon di Gramps Desktop sarà aggiornato in futuro per supportare gli stessi formati.
