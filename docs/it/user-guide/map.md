# Mappa

La pagina Mappa visualizza tutti i luoghi nel tuo albero genealogico come marcatori interattivi su una mappa geografica. È accessibile dalla barra laterale.

## Marcatori di luogo

Solo i luoghi che hanno coordinate GPS memorizzate nel database di Gramps vengono mostrati sulla mappa. I luoghi senza coordinate vengono omessi silenziosamente. Le coordinate GPS possono essere impostate nella pagina di dettaglio del luogo (modifica il luogo e compila i campi di latitudine e longitudine).

!!! tip
    Se molti dei tuoi luoghi mancano dalla mappa, apri una pagina di dettaglio del luogo e controlla se la latitudine e la longitudine sono impostate. Puoi aggiungere o correggere le coordinate direttamente dalla vista di modifica del luogo.

Ogni luogo con coordinate è mostrato come un marcatore. Cliccando su un marcatore si apre una scheda di riepilogo che mostra il nome del luogo e i suoi eventi e persone collegati. Clicca sul nome del luogo nella scheda per aprire la pagina di dettaglio completa del luogo.

## Ricerca

La casella di ricerca nell'angolo in alto a sinistra della mappa ti consente di saltare a qualsiasi posizione nel mondo per nome. Questo non filtra i luoghi dell'albero – semplicemente sposta e ingrandisce la mappa nella posizione cercata.

## Slider temporale

Lo slider temporale nella parte inferiore della pagina filtra quali marcatori di luogo vengono mostrati in base all'anno dei loro eventi associati:

- Trascina il cursore per selezionare un anno.
- Vengono mostrati solo i luoghi collegati a eventi che rientrano nella finestra temporale selezionata.
- Usa questo per tracciare dove vivevano i tuoi antenati in un particolare momento della storia.

## Livelli della mappa

Un pulsante di commutazione dei livelli (icona dei livelli impilati, in basso a sinistra) ti consente di scegliere tra due mappe di base:

### Mappa di Base

Il livello predefinito, alimentato da [OpenFreeMap](https://openfreemap.org) (stile Liberty per la modalità chiara, stile scuro per la modalità scura). Questa è una mappa moderna di uso generale adatta per localizzare luoghi.

### Mappa Storica

Cambia la mappa di base in [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), un progetto guidato dalla comunità che mappa il mondo così com'era in diversi momenti nel tempo – pensala come un corrispondente storico di OpenStreetMap.

Quando il livello della Mappa Storica è attivo, lo slider temporale filtra anche i riquadri della mappa: OHM rende la mappa così come appariva nell'anno selezionato, quindi vengono mostrati confini storici, nomi di luoghi e caratteristiche invece di quelli moderni. Questo rende possibile vedere sia la posizione dei tuoi antenati che il contesto geografico e politico contemporaneo in un'unica vista.

!!! note
    La copertura di OpenHistoricalMap varia per regione e periodo. Aree o epoche con contributi scarsi possono mostrare dettagli storici limitati. Se noti dati storici mancanti o inaccurati, considera di [contribuire a OpenHistoricalMap](https://www.openhistoricalmap.org) – è un progetto comunitario aperto che chiunque può modificare.

## Sovrapposizioni di mappa personalizzate

In aggiunta ai livelli di base integrati, puoi trasformare qualsiasi immagine di mappa storica scansionata – memorizzata in Gramps come oggetto **Media** – in una sovrapposizione personalizzata posizionata sulla mappa dal vivo. Questo è utile per le scansioni di vecchi piani urbani, mappe parrocchiali o mappe di proprietà che desideri confrontare direttamente con la geografia moderna o storica.

### Georeferenziare un'immagine

1. Apri l'oggetto media per l'immagine della mappa scansionata e passa alla modalità di modifica.
2. Apri la scheda "Mappa" e clicca su **Modifica coordinate**. Questo apre una finestra di dialogo di georeferenziazione con l'immagine accanto a una mappa.
3. Clicca su **Seleziona un punto sulla mappa**, quindi clicca sulla posizione sulla mappa a cui un punto sull'immagine dovrebbe corrispondere. L'immagine viene posizionata sulla mappa per la prima volta non appena viene selezionato un punto.
4. Usa il cursore **Scala** per ridimensionare l'immagine e il cursore **Opacità** per vedere la mappa di base attraverso di essa mentre la posizioni.
5. Clicca su **Allinea l'immagine** e clicca di nuovo sulla mappa per spostare l'immagine in modo che il punto fissato si allinei precisamente.
6. Ripeti i passaggi di scala, opacità e allineamento fino a quando l'immagine non corrisponde alla geografia sottostante, quindi salva.

Dietro le quinte, questo memorizza le coordinate degli angoli dell'immagine in un attributo `map:bounds` sull'oggetto media.

### Visualizzazione delle sovrapposizioni nella pagina Mappa

Una volta che un oggetto media è stato georeferenziato in questo modo, diventa automaticamente disponibile come un livello attivabile sulla pagina Mappa. Apri il commutatore dei livelli (icona dei livelli impilati, in basso a sinistra) per mostrare o nascondere ciascuna sovrapposizione indipendentemente dalla mappa di base. Le sovrapposizioni sono elencate in base al titolo dell'oggetto media.
