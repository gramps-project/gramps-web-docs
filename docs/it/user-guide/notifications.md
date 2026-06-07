# Notifiche

**Notifiche** è un elemento della barra laterale con un'icona a forma di campana. Quando si verificano errori o sono in esecuzione attività in background, un badge mostra il numero di notifiche non lette. Cliccaci sopra per aprire il registro delle notifiche.

Il registro delle notifiche ha due scopi:

- È un registro degli errori che si sono verificati durante la tua sessione – richieste API non riuscite, errori delle attività in background, errori di salvataggio o errori a livello di browser.
- Tiene traccia del progresso delle attività in background a lungo termine – come importazioni ed esportazioni, generazione di report, riconoscimento del testo OCR, aggiornamenti del database e ricostruzioni dell'indice di ricerca/semantico – mostrando il loro stato (ad es. in attesa, avviato, in corso) e notificandoti quando vengono completate o falliscono.

Ogni voce mostra un breve messaggio, la fonte (Rete, Attività, Salvataggio o Browser) e un timestamp.

Alcune notifiche includono dettagli strutturati. Cliccando su tale voce si apre un dialogo con una suddivisione dei dati di errore e un pulsante **Copia JSON**. Questo è utile quando si segnala un bug, poiché il JSON contiene le informazioni di errore esatte dal server.

Usa **Cancella tutto** per rimuovere tutte le notifiche.

!!! nota
    Le notifiche sono memorizzate solo in memoria e vengono cancellate quando ricarichi la pagina.
