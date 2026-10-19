# Utilizzo dell'Assistente AI

!!! info
    L'Assistente AI richiede la versione 2.5.0 o superiore dell'API Gramps Web e la versione 24.10.0 o superiore di Gramps Web. La versione 3.6.0 dell'API Gramps Web ha introdotto capacità di chiamata degli strumenti per interazioni più intelligenti.

La vista **Assistente** in Gramps Web (se disponibile nella tua installazione, etichettata "Chat" nelle versioni precedenti) offre accesso a un assistente AI che può rispondere a domande sul tuo albero genealogico.

!!! warning
    Poiché questa è ancora una funzionalità nuova ed in evoluzione, alcuni tipi di domande funzionano bene mentre altri no. Inoltre, come con qualsiasi assistente AI, può fornire risposte fattualmente errate, quindi assicurati sempre di controllare.

## Come funziona

Per capire quali tipi di domande l'assistente può rispondere, è utile comprendere come funziona sotto il cofano:

1. L'utente pone una domanda.
2. L'assistente interroga direttamente il tuo database utilizzando strumenti specializzati: cerca nell'albero con la [ricerca full-text](search.md), filtra persone/eventi/famiglie/luoghi in base a criteri specifici, calcola relazioni tra individui e cerca record completi, comprese le loro note.
3. Un grande modello linguistico formula una risposta basata sui record trovati.
4. La risposta viene visualizzata, con collegamenti ai record su cui si basa.

Su server che eseguono una versione dell'API Gramps Web precedente alla 3.24, l'assistente si basava anche sulla ricerca semantica, che è in fase di dismissione.

Mentre l'assistente sta lavorando, indicatori mostrano quali strumenti sta attualmente utilizzando (ad es. ricerca di persone, ricerca di relazioni) in modo da poter seguire mentre costruisce la sua risposta. Le domande che richiedono più tempo vengono elaborate come attività in background – puoi navigare altrove e tornare, e i progressi sono anche riflessi nelle [Notifiche](notifications.md). Le risposte sono formattate con Markdown (liste, enfasi, collegamenti, ecc.) per una lettura più facile.

## Cosa puoi chiedere

Con le capacità di chiamata degli strumenti introdotte nella versione 3.6.0 dell'API Gramps Web, l'assistente AI può ora gestire domande più complesse:

- **Relazioni familiari**: "Chi sono i nonni di Jane Smith?" o "Come è imparentato John Doe con Mary Johnson?"
- **Ricerche filtrate**: "Mostrami tutte le persone nate a Londra dopo il 1850" o "Quali eventi sono accaduti a Parigi?"
- **Domande basate su date**: "Chi è morto prima del 1900?" o "Elenca i matrimoni avvenuti tra il 1920 e il 1950"
- **Informazioni sui luoghi**: "Quali luoghi ci sono in Francia?" o "Parlami della Chiesa di St. Mary"
- **Domande generali**: "Qual è il nome dei figli di John Doe?" o "Quando è nata Mary Smith?"

## Suggerimenti per porre domande

Per ottenere i migliori risultati dall'assistente AI:

- **Sii specifico**: Formula la tua domanda con il maggior numero di dettagli possibile per evitare ambiguità. Ad esempio, "Quando si è sposato John Smith nato nel 1850 a Boston?" è meglio di "Quando si è sposato John Smith?"
- **Usa nomi propri**: Menziona nomi, luoghi e date specifici quando rilevante.
- **Chiedi una cosa alla volta**: Suddividi domande complesse in parti più semplici per risultati migliori.
- **Usa la tua lingua**: I grandi modelli linguistici sono multilingue, quindi puoi porre domande nella tua lingua e ricevere risposte nella stessa lingua.

!!! tip
    Ti preghiamo di condividere la tua esperienza riguardo a ciò che funziona e non funziona con la comunità.
