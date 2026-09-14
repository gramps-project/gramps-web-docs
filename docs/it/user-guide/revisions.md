# Cronologia delle revisioni

La visualizzazione della cronologia delle revisioni mostra tutte le modifiche apportate all'albero genealogico.

La visualizzazione dell'elenco mostra le modifiche raggruppate per "transazioni". Una transazione è un gruppo di una o più aggiunte, eliminazioni o modifiche agli oggetti Gramps. Ad esempio, aggiungere una nuova famiglia con due persone esistenti come padre e madre genera una transazione con un oggetto famiglia aggiunto e due oggetti persona modificati (perché contengono il collegamento al nuovo oggetto famiglia).

Cliccando su una transazione si apre la visualizzazione dei dettagli della transazione. Contiene l'elenco delle singole aggiunte, eliminazioni e aggiornamenti per oggetto Gramps.

Selezionando una modifica individuale si apre una visualizzazione della rappresentazione JSON grezza dell'oggetto Gramps con aggiunte ed eliminazioni evidenziate in verde e rosso, rispettivamente. Un pulsante sopra il diff ti porta direttamente alla pagina dell'oggetto stesso.

## Revisioni di un singolo oggetto

Per vedere la cronologia di una persona, famiglia, evento o altro oggetto particolare, apri la sua pagina e passa alla scheda **Revisioni**. Elenca ogni modifica apportata a quell'oggetto, dalla più recente alla più vecchia, con il tipo di modifica (aggiunto, aggiornato o eliminato), l'utente che l'ha effettuata e quando. Cliccando su un'entrata si apre la transazione a cui appartiene, dove puoi ispezionare il diff o annullarla.

Clicca su **Mostra di più** per caricare voci più vecchie; per oggetti con una cronologia molto lunga, vengono mostrate solo le revisioni più recenti. Per gli oggetti modificati l'ultima volta prima che la cronologia delle revisioni fosse registrata, la scheda mostra solo il momento dell'ultima modifica.

!!! nota
    La scheda Revisioni è visibile ai membri e superiori e richiede la versione 3.22 o successiva dell'API Web di Gramps.

## Annullare una revisione

Nella pagina dei dettagli della transazione, un pulsante **Annulla** ti consente di invertire quella transazione. Cliccando su di esso si verifica se l'annullamento può essere eseguito senza problemi.

**Annullamento pulito** – se nessuno degli oggetti interessati dalla transazione è stato modificato da allora, l'annullamento può procedere senza rischi. Viene mostrata una finestra di conferma e cliccando su **Annulla** si inverte la transazione.

**Forza richiesta** – se uno o più oggetti interessati sono stati modificati da una transazione successiva, un annullamento pulito non è possibile. La finestra di dialogo avverte che forzare l'annullamento potrebbe comportare incoerenze nei dati, poiché le modifiche successive che dipendono dagli oggetti in questione verranno mantenute così come sono, anche se gli oggetti sottostanti vengono ripristinati. Puoi quindi annullare oppure cliccare su **Forza annullamento** per procedere comunque.

In entrambi i casi, l'annullamento viene eseguito come un'attività in background e viene mostrato un indicatore di progresso.
