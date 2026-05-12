# Ricerca

La pagina di ricerca è accessibile cliccando sull'icona della lente di ingrandimento nella barra superiore dell'app, oppure premendo il tasto `s` [scorciatoia da tastiera](shortcuts.md).

## Ricerca full-text

Digita qualsiasi query nel campo di ricerca e premi Invio (o clicca sul pulsante di ricerca). Gramps Web cerca tra tutti i tipi di oggetti – persone, famiglie, eventi, luoghi, fonti, citazioni, archivi, note e media – e restituisce risultati corrispondenti ordinati per rilevanza.

I risultati mostrano il tipo di oggetto, il nome e un breve riassunto. Clicca su qualsiasi risultato per aprire la corrispondente pagina di dettaglio.

Un `*` finale può essere usato come carattere jolly, ad esempio `Mey*` corrisponde a "Meyer", "Meyers", "Meyerhofer", ecc.

## Filtraggio per tipo di oggetto

Sotto il campo di ricerca, i pulsanti di attivazione per ciascun tipo di oggetto (Persone, Famiglie, Eventi, Luoghi, …) ti permettono di restringere i risultati a uno o più tipi specifici. Per impostazione predefinita, vengono cercati tutti i tipi. Attivando uno o più pulsanti di attivazione, i risultati vengono limitati solo a quei tipi.

## Ricerca semantica

Se l'amministratore del server ha abilitato la [ricerca semantica (basata su AI)](../install_setup/configuration.md), appare un interruttore di modalità nell'angolo in alto a destra della pagina di ricerca con due opzioni:

- **Ricerca** – ricerca full-text standard (predefinita)
- **Semantica** – ricerca basata su AI che comprende il significato della tua query piuttosto che corrispondere a parole esatte

La ricerca semantica è utile per query in linguaggio naturale come "contadino in Baviera nel XIX secolo". Richiede che l'indice di ricerca semantica sia popolato; consulta le [impostazioni di amministrazione](../administration/settings.md) per sapere come costruire o aggiornare l'indice.
