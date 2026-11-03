# Ricerca

La pagina di ricerca è accessibile cliccando sull'icona della lente di ingrandimento nella barra superiore dell'app, o premendo il tasto `s` [scorciatoia da tastiera](shortcuts.md).

## Ricerca full-text

Digita qualsiasi query nel campo di ricerca e premi Invio (o clicca sul pulsante di ricerca). Gramps Web cerca tra tutti i tipi di oggetti – persone, famiglie, eventi, luoghi, fonti, citazioni, archivi, note e media – e restituisce risultati corrispondenti classificati per rilevanza.

I risultati mostrano il tipo di oggetto, il nome e un breve riassunto. Clicca su qualsiasi risultato per aprire la corrispondente pagina di dettaglio.

## Sintassi di ricerca

- **Tutte le parole devono corrispondere.** `Müller Berlin` trova oggetti che contengono entrambe le parole.
- **`or`** trova oggetti che contengono una delle due parole, ad esempio `Meyer or Maier`. Anche `and` può essere digitato tra le parole, ma non fa differenza.
- `or` si applica alle parole direttamente adiacenti: `Meyer or Maier Berlin` significa "(Meyer or Maier) e Berlin". Le parentesi non sono supportate.
- **Virgolette** corrispondono a una frase, cioè parole in quest'ordine: `"Johann Georg"`.
- **Carattere jolly:** un `*` finale corrisponde a qualsiasi termine finale, ad esempio `Mey*` corrisponde a "Meyer", "Meyers", "Meyerhofer", ecc. Questo funziona anche per le frasi: `"Johann Georg"*`.
- `or` e `and` sono riconosciuti in qualsiasi maiuscolo/minuscolo. Per cercare una di queste parole stesse, mettila tra virgolette.
- Le parole non possono essere escluse; non esiste "not".

## Cosa trova la ricerca

- Gli accenti non devono corrispondere: "Müller" trova anche "Muller", e "muller" trova "Müller".
- Le famiglie e gli eventi sono trovati anche dai nomi delle loro persone, ad esempio "Müller" trova le famiglie e gli eventi di tutti coloro che si chiamano Müller. Questi risultati sono classificati sotto le corrispondenze dirette.
- I tipi standard sono trovati dai loro nomi nella lingua dell'interfaccia, ad esempio "Taufe" trova battesimi nell'interfaccia tedesca.
- Gli underscore separano le parole, quindi "microfilm" trova un file multimediale chiamato `scanned_microfilm.png`.
- Gli utenti che non possono visualizzare i record privati non trovano oggetti attraverso informazioni private, come una famiglia tramite il nome di un membro privato.

## Filtraggio per tipo di oggetto

Sotto il campo di ricerca, i pulsanti di attivazione per ogni tipo di oggetto (Persone, Famiglie, Eventi, Luoghi, …) ti consentono di restringere i risultati a uno o più tipi specifici. Per impostazione predefinita, vengono cercati tutti i tipi. Attivando uno o più pulsanti di attivazione, i risultati vengono limitati solo a quei tipi.
