# Mappa

La pagina Mappa visualizza tutti i luoghi nel tuo albero genealogico come marcatori interattivi su una mappa geografica. È accessibile dalla barra laterale.

## Marcatori di luogo

Solo i luoghi che hanno coordinate GPS memorizzate nel database di Gramps vengono mostrati sulla mappa. I luoghi senza coordinate vengono omessi silenziosamente. Le coordinate GPS possono essere impostate nella pagina di dettaglio del luogo (modifica il luogo e compila i campi di latitudine e longitudine).

!!! consiglio
    Se molti dei tuoi luoghi mancano dalla mappa, apri una pagina di dettaglio del luogo e verifica se la latitudine e la longitudine sono impostate. Puoi aggiungere o correggere le coordinate direttamente dalla vista di modifica del luogo.

Ogni luogo con coordinate è mostrato come un marcatore. Cliccando su un marcatore si apre una scheda di riepilogo che mostra il nome del luogo e i suoi eventi e persone collegati. Clicca sul nome del luogo nella scheda per aprire la pagina di dettaglio completa del luogo.

## Ricerca

La casella di ricerca nell'angolo in alto a sinistra della mappa cerca mentre digiti e raggruppa i risultati sotto tre intestazioni:

- **Luoghi** – luoghi nel tuo albero genealogico. Selezionandone uno, la mappa si sposta su di esso e ne evidenzia il marcatore.
- **Persone** – persone nel tuo albero genealogico. Selezionandone una, la mappa passa alla vista della persona descritta [di seguito](#seguire-una-persona-sulla-mappa).
- **Esterni** – località da [OpenStreetMap](https://www.openstreetmap.org/), per qualsiasi luogo nel mondo. Selezionandone una, la mappa si sposta e zooma semplicemente su quella posizione; non filtra né cambia i luoghi del tuo albero.

I risultati esterni sono anche utili quando si aggiungono coordinate a un luogo: puoi cercare la posizione qui per vedere dove si trova prima di inserire la sua latitudine e longitudine.

## Seguire una persona sulla mappa

Selezionare una persona – dalla casella di ricerca della mappa o con il pulsante **Apri nella mappa** nella pagina di dettaglio di una persona – mostra i luoghi collegati agli eventi di quella persona, uniti da linee in ordine cronologico. Piccole frecce lungo ciascuna linea indicano la direzione del viaggio, così puoi seguire la vita di una persona dalla nascita fino alla morte sulla mappa.

I luoghi in una pagina di dettaglio del luogo hanno anche un pulsante **Apri nella mappa**, che apre la mappa centrata su quel luogo.

## Slider temporale

Lo slider temporale in fondo alla pagina filtra quali marcatori di luogo vengono mostrati in base all'anno dei loro eventi associati:

- Trascina il cursore per selezionare un anno.
- Vengono mostrati solo i luoghi collegati a eventi che rientrano nella finestra temporale selezionata.
- Usa questo per tracciare dove vivevano i tuoi antenati in un determinato momento della storia.

## Livelli della mappa

Un pulsante di commutazione dei livelli (icona dei livelli sovrapposti, in basso a sinistra) ti consente di scegliere tra due mappe di base:

### Mappa di Base

Il livello predefinito, alimentato da [OpenFreeMap](https://openfreemap.org) (stile Liberty per la modalità chiara, stile scuro per la modalità scura). Questa è una mappa moderna di uso generale adatta per localizzare luoghi.

### Mappa Storica

Cambia la mappa di base in [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), un progetto guidato dalla comunità che mappa il mondo com'era in diversi momenti nel tempo – pensala come un corrispettivo storico di OpenStreetMap.

Quando il livello della Mappa Storica è attivo, lo slider temporale filtra anche le tessere della mappa: OHM rende la mappa com'era nell'anno selezionato, quindi vengono mostrati confini storici, nomi di luoghi e caratteristiche invece di quelli moderni. Questo rende possibile vedere sia la posizione del tuo antenato sia il contesto geografico e politico contemporaneo in un'unica vista.

!!! nota
    La copertura di OpenHistoricalMap varia a seconda della regione e del periodo. Aree o epoche con contributi scarsi possono mostrare dettagli storici limitati. Se noti dati storici mancanti o inaccurati, considera di [contribuire a OpenHistoricalMap](https://www.openhistoricalmap.org) – è un progetto comunitario aperto che chiunque può modificare.

## Sovrapposizioni personalizzate della mappa

Oltre ai livelli di base integrati, puoi trasformare qualsiasi immagine di mappa storica scansionata – memorizzata in Gramps come oggetto **Media** – in una sovrapposizione personalizzata posizionata sulla mappa live. Questo è utile per le scansioni di vecchi piani urbani, mappe parrocchiali o mappe di proprietà che desideri confrontare direttamente con la geografia moderna o storica.

### Georeferenziare un'immagine

1. Apri l'oggetto media per l'immagine della mappa scansionata e passa alla modalità di modifica.
2. Apri la scheda "Mappa" e clicca su **Modifica coordinate**. Questo apre una finestra di dialogo di georeferenziazione con l'immagine accanto a una mappa.
3. Clicca su **Seleziona un punto sulla mappa**, quindi clicca sulla posizione sulla mappa a cui un punto sull'immagine dovrebbe corrispondere. L'immagine viene posizionata sulla mappa per la prima volta non appena viene selezionato un punto.
4. Usa il cursore **Scala** per ridimensionare l'immagine e il cursore **Opacità** per vedere la mappa di base attraverso di essa mentre posizioni.
5. Clicca su **Allinea l'immagine** e clicca di nuovo sulla mappa per spostare l'immagine in modo che il punto fissato si allinei precisamente.
6. Ripeti i passaggi di scala, opacità e allineamento fino a quando l'immagine non corrisponde alla geografia sottostante, quindi salva.

Dietro le quinte, questo memorizza le coordinate degli angoli dell'immagine in un attributo `map:bounds` sull'oggetto media.

### Visualizzare le sovrapposizioni sulla pagina Mappa

Una volta che un oggetto media è stato georeferenziato in questo modo, diventa automaticamente disponibile come un livello attivabile sulla pagina Mappa. Apri il commutatore dei livelli (icona dei livelli sovrapposti, in basso a sinistra) per mostrare o nascondere ciascuna sovrapposizione indipendentemente dalla mappa di base. Le sovrapposizioni sono elencate in base al titolo dell'oggetto media.
