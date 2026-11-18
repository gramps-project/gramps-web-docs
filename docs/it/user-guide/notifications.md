# Notifiche

La campanella nella barra superiore dell'app apre le notifiche. Un badge sulla campanella mostra il numero di notifiche non lette. Il menu elenca i compiti in esecuzione e le ultime notifiche; **Mostra tutto** apre il registro completo delle notifiche. Su schermi piccoli, la campanella apre direttamente il registro.

Le notifiche riguardano:

- **Modifiche da parte di altri utenti.** Quando altri utenti modificano l'albero mentre stai utilizzando Gramps Web, una notifica indica chi ha cambiato cosa, ad esempio "Modifica Persona" o "12 modifiche". Cliccaci sopra per aprire la modifica nella [cronologia delle revisioni](revisions.md). Le modifiche che non hanno un utente Gramps Web, come quelle apportate direttamente a un database condiviso con Gramps Desktop, vengono mostrate senza un nome. Questo è disponibile solo per gli utenti che possono vedere la cronologia delle revisioni (membri e superiori).
- **Compiti in background** – come importazioni ed esportazioni, generazione di report, riconoscimento del testo OCR, aggiornamenti del database, eliminazione o modifica di molti oggetti e ricostruzione degli indici di ricerca – mostrando il loro stato (ad esempio, in attesa, avviato, in corso) e notificandoti quando vengono completati o falliscono.
- **Errori** che si sono verificati durante la tua sessione – richieste API fallite, errori nei compiti in background, fallimenti nel salvataggio o errori a livello di browser.

Le esportazioni completate e gli archivi multimediali possono essere scaricati dalla loro notifica, anche dopo che hai lasciato la [pagina di esportazione](../administration/export.md).

Alcune notifiche includono dettagli strutturati, come il messaggio di errore di un compito fallito. Cliccando su un tale elemento nel registro delle notifiche si apre una finestra di dialogo con una suddivisione dei dati di errore e un pulsante **Copia JSON**. Questo è utile quando si segnala un bug, poiché il JSON contiene le informazioni di errore esatte dal server.

Usa **Cancella tutto** nel registro delle notifiche per ignorare tutte le notifiche.

I compiti che cambiano l'intero albero, come un'importazione, un ripristino, l'eliminazione di tutti gli oggetti o la ricostruzione dell'indice di ricerca, non possono essere eseguiti contemporaneamente. Se ne avvii uno mentre un altro è in esecuzione, un messaggio indica che un altro compito è già in esecuzione su questo albero, e il compito in esecuzione viene mostrato con il suo progresso.

!!! nota
    Le notifiche sono memorizzate solo in memoria e vengono cancellate quando ricarichi la pagina. Gramps Web controlla le modifiche da parte di altri utenti solo mentre è aperto, quindi le modifiche apportate mentre eri assente non vengono segnalate; consulta la [Cronologia delle revisioni](revisions.md) per quelle.
