## Esegui il backup del tuo albero genealogico

I proprietari dell'albero possono creare, scaricare e ripristinare backup completi dell'albero – inclusi le sue impostazioni e gli utenti – nella sezione [Backup](settings.md#backups) delle impostazioni di amministrazione.

In alternativa, per creare un backup solo dei dati dell'albero genealogico, apri la pagina di Esportazione in Gramps Web e seleziona il formato Gramps XML.

Cliccando su "esporta" verrà generato il file e inizierà il download non appena sarà pronto.

Nota che se il tuo utente di Gramps Web non ha il permesso di visualizzare i record privati, l'esportazione non sarà un backup completo, poiché non conterrà alcun record privato.

Questo file Gramps XML può essere utilizzato in seguito per ripristinare l'albero a questo stato esatto tramite [Ripristina da Backup](settings.md#restore-from-backup).

## Condividi il tuo albero genealogico con utenti di altri programmi genealogici

Quando la condivisione dei dati genealogici come Gramps XML non è un'opzione, puoi anche esportare un file GEDCOM. Nota che questo non è adatto come backup del tuo albero di Gramps Web.

## Esegui il backup dei tuoi file multimediali

Per eseguire il backup dei tuoi file multimediali, puoi creare e scaricare un archivio ZIP di tutti i file multimediali nella pagina di Esportazione.

Nota che, specialmente per alberi di grandi dimensioni, questa può essere un'operazione costosa per il server e dovrebbe essere eseguita solo se assolutamente necessario. Per questo motivo, il numero di archivi multimediali che possono essere creati è limitato (di default a uno all'ora). Se raggiungi il limite, il messaggio di errore lo mostra.

Un'opzione migliore per eseguire il backup dei tuoi file multimediali su base regolare è utilizzare il [complemento Gramps Web Sync](sync.md) (che di per sé non è una soluzione di backup) e creare backup incrementali sul tuo computer locale.

In entrambi i casi, se il tuo utente di Gramps Web non ha il permesso di visualizzare i record privati, l'esportazione non conterrà file di oggetti multimediali privati.

## Trasferisci a un'altra istanza di Gramps Web

Gramps Web non ti blocca con un fornitore specifico e puoi sempre trasferirti a un'altra istanza di Gramps Web senza perdere dati e senza avere accesso diretto a nessuno dei server.

Per ottenere una migrazione completa, segui questi passaggi (supponendo che tu abbia i permessi di proprietario dell'albero):

1. Vai alla pagina di Esportazione ed esporta il tuo albero come file Gramps XML (`.gramps`). Se utilizzi il [complemento Sync](sync.md), puoi anche generare l'esportazione in Gramps desktop.
2. Nella pagina di Esportazione, genera e scarica un archivio multimediale. Se utilizzi il [complemento Sync](sync.md), puoi anche semplicemente comprimere la tua cartella multimediale di Gramps locale in un file ZIP.
3. Vai su Impostazioni > Amministrazione > Gestisci utenti e clicca sul pulsante "Esporta dettagli utente". Verrà scaricato un file JSON.
4. Nella nuova istanza di Gramps Web, apri la pagina di Importazione. Importa il file `.gramps` esportato nel passaggio 1.
5. Nella pagina di Importazione della nuova istanza di Gramps Web, carica l'archivio multimediale (ZIP).
6. Vai su Impostazioni > Amministrazione > Gestisci utenti della nuova istanza di Gramps Web. Clicca sul pulsante "Importa account utente" e carica il file JSON scaricato nel passaggio 3.

Nota che, mentre i tuoi account utente verranno migrati, tutti i tuoi utenti dovranno impostare nuove password utilizzando il link "password dimenticata", poiché le password sono memorizzate in forma crittografata e non possono essere esportate.
