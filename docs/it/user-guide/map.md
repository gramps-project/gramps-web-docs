# Mappa

La pagina Mappa visualizza tutti i luoghi nel tuo albero genealogico come marcatori interattivi su una mappa geografica. È accessibile dalla barra laterale.

## Marcatori di luogo

Solo i luoghi che hanno coordinate GPS memorizzate nel database di Gramps vengono mostrati sulla mappa. I luoghi senza coordinate vengono omessi silenziosamente. Le coordinate GPS possono essere impostate nella pagina di dettaglio del luogo (modifica il luogo e compila i campi di latitudine e longitudine).

!!! tip
    Se molti dei tuoi luoghi mancano dalla mappa, apri una pagina di dettaglio del luogo e controlla se la latitudine e la longitudine sono impostate. Puoi aggiungere o correggere le coordinate direttamente dalla vista di modifica del luogo.

Ogni luogo con coordinate è mostrato come un marcatore. Cliccando su un marcatore si apre una scheda di riepilogo che mostra il nome del luogo e i suoi eventi e persone collegati. Clicca sul nome del luogo nella scheda per aprire la pagina di dettaglio completa del luogo.

## Ricerca

La casella di ricerca nell'angolo in alto a sinistra della mappa cerca mentre digiti e raggruppa i risultati sotto tre intestazioni:

- **Luoghi** – luoghi nel tuo albero genealogico. Selezionando uno, la mappa si sposta su di esso e ne evidenzia il marcatore.
- **Persone** – persone nel tuo albero genealogico. Selezionando una si passa alla vista della persona descritta [di seguito](#seguire-una-persona-sulla-mappa).
- **Esterni** – località da [OpenStreetMap](https://www.openstreetmap.org/), per qualsiasi luogo nel mondo. Selezionando una si sposta e zooma semplicemente la mappa su quella posizione; non filtra né cambia i luoghi del tuo albero.

I risultati esterni sono anche utili quando si aggiungono coordinate a un luogo: puoi cercare qui la posizione per vedere dove si trova prima di inserire la sua latitudine e longitudine.

## Seguire una persona sulla mappa

Selezionando una persona – dalla casella di ricerca della mappa, o con il pulsante **Apri nella mappa** nella pagina di dettaglio di una persona – vengono mostrati i luoghi collegati agli eventi di quella persona, uniti da linee in ordine cronologico. Piccole frecce lungo ogni linea indicano la direzione del viaggio, così puoi seguire la vita di una persona dalla nascita fino alla morte sulla mappa.

I luoghi in una pagina di dettaglio del luogo hanno anche un pulsante **Apri nella mappa**, che apre la mappa centrata su quel luogo.

## Slider temporale

Lo slider temporale nella parte inferiore della pagina filtra quali marcatori di luogo vengono mostrati in base all'anno dei loro eventi associati:

- Trascina il cursore per selezionare un anno.
- Vengono mostrati solo i luoghi collegati a eventi che rientrano nella finestra temporale selezionata.
- Usa questo per tracciare dove vivevano i tuoi antenati in un particolare momento della storia.

## Livelli della mappa

Un pulsante di commutazione dei livelli (icona a strati sovrapposti, in basso a sinistra) ti consente di scegliere tra due mappe di base. Sotto di esse, elenca i tuoi livelli di mappa sotto "Le tue mappe" (vedi [Sovrapposizioni di mappa personalizzate](#sovrapposizioni-di-mappa-personalizzate) e [File mappa dei luoghi](#file-mappa-dei-luoghi)) e il livello [Wikidata buildings](#wikidata-buildings) sotto "Esterni", ciascuno dei quali può essere attivato o disattivato.

Le etichette di entrambe le mappe di base sono mostrate nella lingua che hai selezionato in Gramps Web, dove i dati della mappa hanno un nome in quella lingua, e nel nome locale altrimenti.

### Mappa di Base

Il livello predefinito, alimentato da [OpenFreeMap](https://openfreemap.org) (stile Liberty per la modalità chiara, stile scuro per la modalità scura). Questa è una mappa moderna di uso generale adatta per localizzare luoghi.

### Mappa Storica

Cambia la mappa di base in [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), un progetto guidato dalla comunità che mappa il mondo così com'era in diversi momenti nel tempo – pensala come un corrispondente storico di OpenStreetMap.

Quando il livello della Mappa Storica è attivo, lo slider temporale filtra anche i riquadri della mappa: OHM rende la mappa come appariva nell'anno selezionato, quindi vengono mostrati confini storici, nomi di luoghi e caratteristiche invece di quelli moderni. Questo rende possibile vedere sia la posizione del tuo antenato che il contesto geografico e politico contemporaneo in un'unica vista.

!!! note
    La copertura di OpenHistoricalMap varia per regione e periodo. Aree o epoche con contributi scarsi possono mostrare dettagli storici limitati. Se noti dati storici mancanti o inaccurati, considera di [contribuire a OpenHistoricalMap](https://www.openhistoricalmap.org) – è un progetto comunitario aperto che chiunque può modificare.

## Sovrapposizioni di mappa personalizzate

Oltre ai livelli di base integrati, puoi trasformare qualsiasi immagine di mappa storica scansionata – memorizzata in Gramps come oggetto **Media** – in una sovrapposizione personalizzata posizionata sulla mappa dal vivo. Questo è utile per scansioni di vecchi piani di città, mappe parrocchiali o mappe di proprietà che desideri confrontare direttamente con la geografia moderna o storica.

### Georeferenziare un'immagine

1. Apri l'oggetto media per l'immagine della mappa scansionata e passa alla modalità di modifica.
2. Apri la scheda "Mappa" e clicca su **Modifica coordinate**. Questo apre una finestra di dialogo di georeferenziazione con l'immagine accanto a una mappa.
3. Clicca su **Seleziona un punto sulla mappa**, quindi clicca sulla posizione sulla mappa a cui un punto sull'immagine dovrebbe corrispondere. L'immagine viene posizionata sulla mappa per la prima volta non appena viene selezionato un punto.
4. Usa il cursore **Scala** per ridimensionare l'immagine e il cursore **Opacità** per vedere la mappa di base attraverso di essa mentre posizioni.
5. Clicca su **Allinea l'immagine** e clicca di nuovo sulla mappa per spostare l'immagine in modo che il punto fissato si allinei precisamente.
6. Ripeti i passaggi di scala, opacità e allineamento fino a quando l'immagine non corrisponde alla geografia sottostante, quindi salva.

Dietro le quinte, questo memorizza le coordinate degli angoli dell'immagine in un attributo `map:bounds` sull'oggetto media.

### Visualizzare le sovrapposizioni nella pagina Mappa

Una volta che un oggetto media è stato georeferenziato in questo modo, diventa automaticamente disponibile come livello attivabile nella pagina Mappa. Apri il commutatore di livelli (icona a strati sovrapposti, in basso a sinistra) per mostrare o nascondere ciascuna sovrapposizione indipendentemente dalla mappa di base. Le sovrapposizioni sono elencate in base al titolo dell'oggetto media.

Ogni sovrapposizione ha un cursore di opacità sotto il suo nome, così puoi vedere la mappa di base attraverso di essa.

## File mappa dei luoghi

I luoghi possono avere file mappa allegati come oggetti media – ad esempio i confini di una parrocchia, un distretto, o un'azienda, o un percorso. Sono supportati file KML (`.kml`), GeoJSON (`.geojson`), e GPX (`.gpx`).

Quando selezioni un luogo sulla mappa, i suoi file mappa vengono disegnati sopra la mappa, utilizzando i colori memorizzati nel file dove li ha. Questo funziona anche per luoghi senza coordinate: la mappa si zooma quindi sull'area coperta dai file. Mentre il luogo è selezionato, i suoi file sono elencati nel commutatore di livelli sotto "Le tue mappe", dove puoi disattivarli ciascuno.

Per aggiungere un file mappa a un luogo, aggiungilo alla galleria del luogo come qualsiasi altro [file media](media.md).

## Wikidata buildings

Il livello "Wikidata buildings" mostra edifici registrati in [Wikidata](https://www.wikidata.org/), come chiese, fattorie o case di città. È disattivato per impostazione predefinita e può essere attivato nel commutatore di livelli sotto "Esterni". Gli edifici vengono mostrati solo quando la mappa è ingrandita abbastanza. Quando lo slider temporale è attivo, vengono mostrati solo gli edifici che esistevano nel momento selezionato.

Clicca su un edificio per vedere i suoi dettagli da Wikidata, come quando è stato costruito o demolito, i suoi indirizzi, occupanti e proprietari.

### Salvare un edificio come luogo

Gli utenti che possono aggiungere oggetti vedono un pulsante **Salva come luogo** nei dettagli dell'edificio. Questo apre il modulo per un nuovo luogo, precompilato con il nome dell'edificio nella tua lingua, un tipo di luogo (`Fattoria` per le fattorie, altrimenti `Edificio`), le sue coordinate e un link all'elemento di Wikidata. Completa il modulo, ad esempio selezionando il luogo circostante, e salvalo.

Se un luogo nel tuo albero si trova nella stessa posizione dell'edificio, il pulsante legge **Apri luogo salvato** invece e mostra quel luogo.

!!! info
    L'amministratore del server può rimuovere il livello degli edifici di Wikidata con l'opzione `mapWikidata` della [configurazione del frontend](../install_setup/frontend-config.md).
