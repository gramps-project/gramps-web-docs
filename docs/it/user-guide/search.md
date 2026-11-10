# Ricerca

La pagina di ricerca è accessibile cliccando sull'icona della lente di ingrandimento nella barra superiore dell'app, o premendo il tasto `s` [scorciatoia da tastiera](shortcuts.md).

## Ricerca full-text

Digita una query nel campo di ricerca. I risultati appaiono mentre digiti, dal secondo carattere in poi; premi Invio per cercare un singolo carattere. Gramps Web cerca tra tutti i tipi di oggetti – persone, famiglie, eventi, luoghi, fonti, citazioni, archivi, note e media – e restituisce risultati corrispondenti ordinati per rilevanza. Per cancellare la ricerca, clicca sul pulsante di cancellazione nel campo o premi Esc.

Ogni risultato mostra il tipo di oggetto, il suo nome e alcuni dettagli, ad esempio la nascita e la morte di una persona, il matrimonio di una famiglia, l'autore di una fonte, o la prima riga di una nota. Clicca su qualsiasi risultato per aprire la corrispondente pagina di dettaglio.

## Sintassi di ricerca

- **Tutte le parole devono corrispondere.** `Müller Berlin` trova oggetti che contengono entrambe le parole.
- **`or`** trova oggetti che contengono una delle due parole, ad esempio `Meyer or Maier`. Anche `and` può essere digitato tra le parole, ma non fa differenza.
- `or` si applica alle parole immediatamente adiacenti: `Meyer or Maier Berlin` significa "(Meyer or Maier) e Berlin". Le parentesi non sono supportate.
- **Virgolette** corrispondono a una frase, cioè parole in quest'ordine: `"Johann Georg"`.
- **Carattere jolly:** un `*` finale corrisponde a qualsiasi termine finale, ad esempio `Mey*` corrisponde a "Meyer", "Meyers", "Meyerhofer", ecc. Questo funziona anche per le frasi: `"Johann Georg"*`.
- **L'ultima parola è completata.** Se la query termina con una lettera o un numero, viene cercata come se terminasse in `*`, quindi `Anna Smi` trova già "Anna Smith". Per cercare l'ultima parola esattamente, termina la query con uno spazio, o metti la parola tra virgolette. Lo stesso vale per le caselle di ricerca dei selettori di oggetti e per la [mappa](map.md#search).
- `or` e `and` sono riconosciuti in qualsiasi maiuscolo/minuscolo. Per cercare una di queste parole stesse, mettila tra virgolette.
- Le parole non possono essere escluse; non esiste "not".

## Cosa trova la ricerca

- Gli accenti non devono corrispondere: "Müller" trova anche "Muller", e "muller" trova "Müller".
- Le famiglie e gli eventi sono trovati anche dai nomi delle loro persone, ad esempio "Müller" trova le famiglie e gli eventi di tutti coloro che si chiamano Müller. Questi risultati sono classificati sotto i corrispondenti abbinamenti diretti.
- I tipi standard sono trovati dai loro nomi nella lingua dell'interfaccia, ad esempio "Taufe" trova battesimi nell'interfaccia tedesca.
- Gli underscore separano le parole, quindi "microfilm" trova un file multimediale chiamato `scanned_microfilm.png`.
- Gli utenti che non possono visualizzare registri privati non trovano oggetti attraverso informazioni private, come una famiglia attraverso il nome di un membro privato.

## Filtraggio per tipo di oggetto

Sotto il campo di ricerca, i pulsanti di attivazione per ogni tipo di oggetto (Persone, Famiglie, Eventi, Luoghi, …) ti consentono di restringere i risultati a uno o più tipi specifici. Per impostazione predefinita, vengono cercati tutti i tipi. Attivare uno o più pulsanti di attivazione limita i risultati solo a quei tipi.
