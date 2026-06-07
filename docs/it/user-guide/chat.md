# Utilizzo dell'Assistente AI

!!! info
    L'Assistente AI richiede Gramps Web API versione 2.5.0 o superiore e Gramps Web versione 24.10.0 o superiore. La versione 3.6.0 della Gramps Web API ha introdotto capacità di chiamata degli strumenti per interazioni più intelligenti.

La vista **Assistente** in Gramps Web (se disponibile nella tua installazione, etichettata come "Chat" nelle versioni precedenti) offre accesso a un assistente AI che può rispondere a domande sul tuo albero genealogico.

!!! warning
    Poiché questa è ancora una funzione nuova e in evoluzione, alcuni tipi di domande funzionano bene mentre altri no. Inoltre, come con qualsiasi assistente AI, può fornire risposte fattualmente errate, quindi assicurati sempre di controllare.

## Come funziona

Per capire quali tipi di domande l'assistente può rispondere, è utile comprendere come funziona sotto il cofano:

1. L'utente pone una domanda.
2. L'assistente AI può utilizzare più approcci per trovare risposte:
   - **Ricerca Semantica**: Gramps Web identifica gli oggetti nel tuo albero genealogico che sono più probabili contenere informazioni rilevanti. Ad esempio, se chiedi "Qual è il nome dei figli di John Doe?", le famiglie con John Doe come padre saranno tra i risultati principali.
   - **Chiamata agli Strumenti (Gramps Web API v3.6.0+)**: L'assistente può interrogare direttamente il tuo database utilizzando strumenti specializzati per cercare, filtrare persone/eventi/famiglie/luoghi in base a criteri specifici, calcolare relazioni tra individui e recuperare informazioni dettagliate.
3. Gramps Web invia la domanda insieme alle informazioni recuperate a un grande modello linguistico per formulare una risposta.
4. La risposta viene visualizzata per te.

Mentre l'assistente sta lavorando, indicatori mostrano quali strumenti sta attualmente utilizzando (ad es. cercando persone, cercando relazioni) in modo da poter seguire mentre costruisce la sua risposta. Le domande che richiedono più tempo vengono elaborate come attività in background – puoi navigare via e tornare indietro, e i progressi sono anche riflessi nelle [Notifiche](notifications.md). Le risposte sono formattate con Markdown (liste, enfasi, link, ecc.) per una lettura più facile.

## Cosa puoi chiedere

Con le capacità di chiamata agli strumenti introdotte nella versione 3.6.0 della Gramps Web API, l'assistente AI può ora gestire domande più complesse:

- **Relazioni familiari**: "Chi sono i nonni di Jane Smith?" o "In che modo John Doe è imparentato con Mary Johnson?"
- **Ricerche filtrate**: "Mostrami tutte le persone nate a Londra dopo il 1850" o "Quali eventi sono accaduti a Parigi?"
- **Domande basate su date**: "Chi è morto prima del 1900?" o "Elenca i matrimoni che si sono svolti tra il 1920 e il 1950"
- **Informazioni sui luoghi**: "Quali luoghi ci sono in Francia?" o "Parlami della Chiesa di St. Mary"
- **Domande generali**: "Qual è il nome dei figli di John Doe?" o "Quando è nata Mary Smith?"

## Suggerimenti per porre domande

Per ottenere i migliori risultati dall'assistente AI:

- **Sii specifico**: Formula la tua domanda con il maggior numero di dettagli possibile per evitare ambiguità. Ad esempio, "Quando si è sposato John Smith nato nel 1850 a Boston?" è meglio di "Quando si è sposato John Smith?"
- **Usa nomi propri**: Meniona nomi specifici, luoghi e date quando rilevante.
- **Chiedi una cosa alla volta**: Suddividi domande complesse in parti più semplici per ottenere risultati migliori.
- **Usa la tua lingua**: I grandi modelli linguistici sono multilingue, quindi puoi porre domande nella tua lingua e ricevere risposte nella stessa lingua.

!!! tip
    Ti preghiamo di condividere la tua esperienza riguardo a ciò che funziona e non funziona con la comunità.
