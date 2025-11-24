## Esegui il backup del tuo albero genealogico

Per creare un backup del tuo albero genealogico, apri la pagina di esportazione in Gramps Web e seleziona il formato Gramps XML.

Cliccando su "esporta" verrà generato il file e inizierà il download una volta pronto.

Nota che se il tuo utente Gramps Web non ha il permesso di visualizzare i record privati, l'esportazione non sarà un backup completo, poiché non conterrà alcun record privato.

## Condividi il tuo albero genealogico con utenti di altri programmi genealogici

Quando la condivisione dei dati genealogici come Gramps XML non è un'opzione, puoi anche esportare un file GEDCOM. Nota che questo non è adatto come backup del tuo albero Gramps Web.

## Esegui il backup dei tuoi file multimediali

Per eseguire il backup dei tuoi file multimediali, puoi creare e scaricare un archivio ZIP di tutti i file multimediali nella pagina di esportazione.

Nota che, specialmente per alberi di grandi dimensioni, questa può essere un'operazione costosa per il server e dovrebbe essere eseguita solo se assolutamente necessario.

Un'opzione migliore per eseguire il backup dei tuoi file multimediali su base regolare è utilizzare il [complemento Gramps Web Sync](sync.md) (che di per sé non è una soluzione di backup) e creare backup incrementali sul tuo computer locale.

In entrambi i casi, se il tuo utente Gramps Web non ha il permesso di visualizzare i record privati, l'esportazione non conterrà file di oggetti multimediali privati.

## Spostati su un'altra istanza di Gramps Web

Gramps Web non ti vincola a un fornitore specifico e puoi sempre spostarti su un'altra istanza di Gramps Web senza perdere dati e senza avere accesso diretto a nessuno dei server.

Per ottenere una migrazione completa, segui questi passaggi (supponendo che tu abbia i permessi di proprietario dell'albero):

1. Vai alla pagina di esportazione ed esporta il tuo albero come file Gramps XML (`.gramps`). Se utilizzi il [complemento Sync](sync.md), puoi anche generare l'esportazione in Gramps desktop.
2. Nella pagina di esportazione, genera e scarica un archivio multimediale. Se utilizzi il [complemento Sync](sync.md), puoi anche semplicemente ZIP della tua cartella multimediale locale di Gramps.
3. Vai su Impostazioni > Amministrazione > Gestisci utenti e clicca sul pulsante "Esporta dettagli utente". Verrà scaricato un file JSON.
4. Nella nuova istanza di Gramps Web, apri la pagina di importazione. Importa il file `.gramps` esportato nel passaggio 1.
5. Nella pagina di importazione della nuova istanza di Gramps Web, carica l'archivio multimediale (ZIP).
6. Vai su Impostazioni > Amministrazione > Gestisci utenti della nuova istanza di Gramps Web. Clicca sul pulsante "Importa account utente" e carica il file JSON scaricato nel passaggio 3.

Nota che, mentre i tuoi account utente verranno migrati, tutti i tuoi utenti dovranno impostare nuove password utilizzando il link "password dimenticata", poiché le password sono memorizzate in forma crittografata e non possono essere esportate.
