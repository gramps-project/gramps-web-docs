# Cronologia delle revisioni

La vista della cronologia delle revisioni mostra tutte le modifiche che sono state apportate all'albero genealogico.

La vista elenco mostra le modifiche raggruppate per "transazioni". Una transazione è un gruppo di una o più aggiunte, cancellazioni o modifiche agli oggetti Gramps. Ad esempio, aggiungere una nuova famiglia con due persone esistenti come padre e madre genera una transazione con un oggetto famiglia aggiunto e due oggetti persona modificati (perché contengono il link al nuovo oggetto famiglia).

Cliccando su una transazione si apre la vista dei dettagli della transazione. Contiene l'elenco delle singole aggiunte, cancellazioni e aggiornamenti per oggetto Gramps.

Selezionando una modifica individuale si apre una vista della rappresentazione JSON grezza dell'oggetto Gramps con aggiunte e cancellazioni evidenziate in verde e rosso, rispettivamente.

## Annullare una revisione

Nella pagina dei dettagli della transazione, un pulsante **Annulla** consente di invertire quella transazione. Cliccando su di esso si verifica se l'annullamento può essere eseguito senza problemi.

**Annullamento pulito** – se nessuno degli oggetti interessati dalla transazione è stato modificato nel frattempo, l'annullamento può procedere senza rischi. Viene mostrata una finestra di conferma e cliccando su **Annulla** si inverte la transazione.

**Forza richiesta** – se uno o più oggetti interessati sono stati modificati da una transazione successiva, un annullamento pulito non è possibile. La finestra avverte che forzare l'annullamento potrebbe comportare incoerenze nei dati, poiché le modifiche successive che dipendono dagli oggetti in questione verranno mantenute così come sono, anche se gli oggetti sottostanti vengono ripristinati. Puoi quindi annullare oppure cliccare su **Forza annullamento** per procedere comunque.

In entrambi i casi, l'annullamento viene eseguito come un'attività in background e viene mostrato un indicatore di progresso.
