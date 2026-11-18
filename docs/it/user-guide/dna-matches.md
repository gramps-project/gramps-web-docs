# Lavorare con i match del DNA

I match del DNA sono segmenti di DNA che concordano tra due individui, identificati dalla presenza di marcatori, i cosiddetti SNP (l'acronimo per polimorfismi a singolo nucleotide, pronunciato “snips”).

Per ottenere questi dati, è necessario avere accesso a un test del DNA caricato su un database di corrispondenza che consente di visualizzare i dati di corrispondenza dei segmenti di DNA (ad es. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web non esegue la corrispondenza stessa, poiché ha solo accesso ai dati che carichi.

## Inserimento dei dati di corrispondenza del DNA

Per inserire i dati di corrispondenza del DNA, hai bisogno di [permessi di modifica](../install_setup/users.md) poiché i dati sono memorizzati come una nota nel database di Gramps. La vista DNA, accessibile dal menu principale, fornisce un modo conveniente per inserire questi dati nel formato corretto.

Per inserire un nuovo match, fai clic sul pulsante + nell'angolo in basso a destra. Nella finestra di dialogo che si apre, seleziona i due individui. Nota che la “Prima persona” e la “Seconda persona” vengono trattate in modo diverso: il match è memorizzato come un'associazione dalla prima alla seconda persona. Solo la prima persona sarà selezionabile per la vista di corrispondenza del DNA e il browser dei cromosomi. Tipicamente, la prima persona è quella di cui hai accesso al test del DNA e la seconda persona è un parente più lontano.

Se la seconda persona non è nel database, devi crearla prima utilizzando il pulsante “Crea persona” nell'angolo in alto a destra dell'interfaccia utente. Una volta creata la persona, puoi tornare alla vista di corrispondenza del DNA e selezionare la persona appena creata.

Successivamente, incolla i dati grezzi nel campo di testo. I dati dovrebbero essere una tabella di corrispondenze separata da virgole o tabulazioni, contenente tipicamente il numero del cromosoma, la posizione di inizio e fine del match, il numero di SNP nel match e la lunghezza del match in centimorgani (cM). Puoi anche trascinare e rilasciare un file con i dati di corrispondenza nel campo di testo.

Un esempio minimo di tale tabella è:

```csv
Cromosoma,Posizione di Inizio,Posizione di Fine,Centimorgani,SNP
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Se il formato è valido, un'anteprima viene mostrata sotto il campo di testo come una tabella.

Infine, fai clic sul pulsante “Salva” per memorizzare il match nel database.

## Visualizzazione dei dati di corrispondenza del DNA

La vista di corrispondenza del DNA ha un menu a discesa che consente di selezionare ciascuna persona nel database che ha un match del DNA associato. Una volta selezionata una persona, i suoi match vengono elencati in una tabella: il nome del match, la loro relazione con la persona selezionata, la lunghezza totale del DNA condiviso in centimorgani (cM), il numero di segmenti condivisi e la lunghezza del segmento più grande di questi.

Per i match già collocati nell'albero, la colonna della relazione mostra la relazione registrata nell'albero (determinata automaticamente dal database di Gramps). Per i match che non sono correlati alla persona selezionata nell'albero, mostra la relazione stimata dal DNA condiviso, contrassegnata con "≈".

Cliccando su un match si apre la sua pagina, con un riepilogo del DNA condiviso, la [stima della relazione](#relationship-estimate), un grafico della relazione nell'albero e l'elenco dei segmenti. Ogni segmento mostra se è sul lato paterno o materno. Il lato può essere inserito manualmente (fornendo un `P` per paterno o `M` per materno in una colonna chiamata `Lato` nei dati grezzi) o determinato automaticamente dall'antenato comune più recente. Il pulsante di download accanto ai segmenti li salva come file CSV nel formato accettato dalla finestra di dialogo di corrispondenza.

## Stima della relazione

Il DNA condiviso non è prova di una relazione specifica: la quantità di DNA che due parenti condividono varia molto e le diverse relazioni si sovrappongono. Gramps Web mostra quindi un intervallo di relazioni possibili con le loro probabilità, calcolate dal numero e dalla lunghezza dei segmenti condivisi (richiede Gramps Web API 3.26 o versioni successive).

Le relazioni sono raggruppate per *grado*:

- **Genitore o figlio** e **Fratello/sorella pieno** sono mostrati da soli.
- **Parente di grado 2** include fratelli, nonni e nipoti, e zie, zii, nipoti e nipoti.
- **Parente di grado 3** include cugini di primo grado, bisnonni, prozie e prozii, e mezzi zii e zie.
- Ogni grado ulteriore è circa una generazione più lontana, ad esempio, i cugini di primo grado una volta rimossi sono di grado 4 e i cugini di secondo grado sono di grado 5. Il grado 9 e oltre sono raggruppati come "9+".

Le relazioni con lo stesso grado condividono in media circa la stessa quantità di DNA, quindi il DNA da solo non può distinguerle. Usa le età delle persone per decidere tra di loro: un parente di grado 2 di 30 anni di un 60enne è più probabile che sia un nipote piuttosto che un nonno.

L stima è più affidabile per i parenti stretti. Per relazioni lontane, i match condividono solo pochi segmenti e le probabilità si distribuiscono su diversi gradi.

### Controllare l'albero rispetto al DNA

Se il match è collocato nell'albero, Gramps Web verifica se il DNA condiviso si adatta alla relazione registrata lì. Se il DNA è molto improbabile per quella relazione, un'icona di avviso viene mostrata nella tabella dei match e un avviso sulla pagina del match. Il numero tra parentesi, ad esempio "1 : 500", confronta quanto è probabile che il DNA sia per la relazione registrata con quanto è probabile per la relazione più probabile.

Un avviso è un motivo per esaminare più attentamente, non prova di un errore. Le cause comuni sono:

- un errore nell'albero, come un genitore sbagliato,
- una paternità attribuita erroneamente, ad es. un'adozione sconosciuta o un padre biologico diverso,
- dati di corrispondenza incompleti, ad esempio se solo i segmenti sopra una soglia alta sono stati copiati dal servizio di test,
- relazioni attraverso più di una linea, ad es. persone correlate sia attraverso la madre che attraverso il padre ("collasso del pedigree"), che condividono più DNA del previsto.

Le relazioni che non sono per nascita, come attraverso un'adozione, non vengono controllate.

## Modifica di un match

Per modificare un match, apri la sua pagina e fai clic sul pulsante di modifica, oppure premi `e`. Nota che puoi cambiare i dati grezzi, ma non gli individui associati al match: devi eliminare il match e crearne uno nuovo se desideri cambiare gli individui.

## Match privati

Le finestre di dialogo per aggiungere e modificare un match hanno un interruttore **Privato**. Un match privato, inclusi i suoi segmenti, è nascosto agli utenti che non possono visualizzare i record privati. I match privati sono contrassegnati con un lucchetto per tutti gli altri. Vedi [Record privati](privacy.md) per ulteriori informazioni sulla privacy.

## Lavorare con i dati di corrispondenza in Gramps Desktop

I dati di corrispondenza del DNA sono memorizzati come una nota nel database di Gramps. Il formato è compatibile con il 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
disponibile per Gramps Desktop. La sua pagina wiki contiene ulteriori dettagli su come ottenere i dati, come interpretarli e come inserire i dati in Gramps.

!!! info
    Gramps Web API v2.8.0 ha introdotto alcune modifiche per accettare un'ampia gamma di dati di corrispondenza del DNA grezzi, che non sono ancora disponibili nell'Addon di Gramps Desktop. L'Addon di Gramps Desktop sarà aggiornato in futuro per supportare gli stessi formati.
