# Utilizzo della chat AI

!!! info
    La chat AI richiede la versione 2.5.0 o superiore dell'API Web di Gramps e la versione 24.10.0 o superiore di Gramps Web.

La visualizzazione della chat in Gramps Web (se disponibile nella tua installazione) offre accesso a un assistente AI che può rispondere a domande sul tuo albero genealogico.

!!! warning
    Poiché questa è ancora una funzionalità nuova e in evoluzione, alcuni tipi di domande funzionano bene mentre altri no. Inoltre, come con qualsiasi assistente AI, può fornire risposte fattualmente errate, quindi assicurati sempre di controllare.

## Come funziona

Per capire quali tipi di domande l'assistente può rispondere, è utile comprendere come funziona sotto il cofano:

1. L'utente pone una domanda.
2. Gramps Web identifica un numero di oggetti Gramps (ad esempio, dieci) che sono più probabilmente in grado di contenere le informazioni che rispondono alla domanda. A tal fine, utilizza una tecnica chiamata "ricerca semantica". Ad esempio, se chiedi "Qual è il nome dei figli di John Doe?", se esiste una famiglia con John Doe come padre, è probabile che sia tra i risultati principali.
3. Gramps Web fornisce la domanda dell'utente insieme alle informazioni di contesto recuperate a un grande modello linguistico ("chatbot") e gli chiede di estrarre la risposta corretta.
4. La risposta viene visualizzata all'utente.

## Come porre una domanda

A causa del modo in cui funziona la chat, attualmente non è possibile per l'assistente AI rispondere a domande su relazioni specifiche diverse da genitori o figli, a meno che queste informazioni non siano contenute come testo in una nota.

Poiché ogni risposta si basa su un numero limitato di risultati principali della ricerca semantica, non può nemmeno rispondere a domande sulle statistiche ("quante persone nel mio database ...").

Per evitare ambiguità e malintesi, è utile formulare la domanda nel modo più dettagliato possibile.

Nota che i grandi modelli linguistici sono multilingue, quindi puoi parlare con esso nella tua lingua e risponderà nella stessa lingua.

!!! tip
    Ti preghiamo di condividere la tua esperienza riguardo a ciò che funziona e non funziona con la comunità.
