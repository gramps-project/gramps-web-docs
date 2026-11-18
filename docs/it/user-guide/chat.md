# Utilizzo dell'Assistente AI

La vista **Assistente** in Gramps Web (se abilitata nella tua installazione) offre accesso a un assistente AI che risponde a domande riguardanti il tuo albero genealogico.

!!! warning
    Come con qualsiasi assistente AI, le risposte possono essere errate. Usa i link nella risposta per controllare i registri su cui si basa.

## Come funziona

L'assistente non conosce il tuo albero in anticipo. Per rispondere a una domanda, un modello linguistico di grandi dimensioni cerca i registri di cui ha bisogno, proprio come faresti tu:

- cerca nell'albero con la [ricerca full-text](search.md),
- filtra persone, eventi e famiglie in base a criteri come nomi, date, luoghi o numero di figli,
- trova antenati, discendenti e altri parenti di una persona, con il loro rapporto,
- legge registri completi di persone, famiglie, eventi, luoghi e note.

Risponde quindi in base ai registri che ha trovato, con link ad essi. Mentre lavora, vengono mostrati gli strumenti che sta utilizzando, così puoi seguire il processo. Le domande che richiedono più tempo vengono eseguite in background – puoi navigare altrove e tornare.

L'assistente risponde solo in base al tuo albero, non alla conoscenza generale del modello linguistico – anche riguardo a persone famose. Se l'albero non registra qualcosa, lo dice, menzionando informazioni correlate che ha trovato, ad esempio in una nota. Vede solo ciò che sei autorizzato a vedere: i link ai registri privati sono mostrati come testo normale per gli utenti che non possono visualizzarli.

Le domande di follow-up mantengono il contesto delle domande precedenti nella stessa conversazione, quindi puoi chiedere "E quando è morto?" dopo aver chiesto di una persona.

## Cosa puoi chiedere

- **Fatti sulle persone**: "Quando è nata Mary Smith?" o "Quali sono i nomi dei figli di John Doe?"
- **Parenti**: "Chi sono i nonni di Jane Smith?" o "Quali discendenti di Johann Meyer sono emigrati in America?"
- **Ricerche con criteri**: "Chi è nato a Londra dopo il 1850?", "Elenca i matrimoni tra il 1920 e il 1950", o "Quali coppie hanno avuto cinque o più figli?"
- **Luoghi**: "Quali eventi sono accaduti a Parigi?" o "Chi è nato in Danimarca?" – i luoghi all'interno di un luogo più grande sono inclusi.
- **Note**: "Cosa dicono le note sulla fattoria della famiglia Meyer?"

Le domande che richiedono l'intero albero contemporaneamente, come "Qual è il nome di battesimo più comune?", funzionano meno bene, poiché l'assistente vede solo un numero limitato di registri per ricerca.

## Chiedere riguardo alle immagini

Se l'amministratore del server lo ha abilitato, il prompt ha un pulsante per allegare immagini. Puoi anche incollare un'immagine o trascinare file immagine sul prompt. Fino a quattro immagini possono essere allegate a una domanda, ad esempio una scansione di un registro parrocchiale per chiedere "Chi è menzionato in questa voce, e sono nel mio albero?"

Le immagini vengono inviate solo con la domanda a cui sono allegate. Le domande di follow-up possono riferirsi a ciò che l'assistente ha detto su di esse, ma non alle immagini stesse, quindi allegale di nuovo se necessario. Se il tuo albero ha un limite sull'uso dell'AI, ogni immagine conta come una domanda aggiuntiva.

## Consentire all'assistente di modificare il tuo albero

Se l'amministratore del server lo ha abilitato, editor, proprietari e amministratori possono chiedere all'assistente di modificare l'albero, ad esempio "Aggiungi un battesimo il 3 maggio 1802 a St. Mary's per Johann Meyer" o "Correggi l'anno di nascita di Anna Smith, dovrebbe essere 1871".

L'assistente non modifica mai nulla autonomamente. Risponde con una scheda **Modifiche proposte** che elenca ogni registro che aggiungerebbe, modificherebbe o eliminerebbe, con i vecchi valori barrati e i nuovi valori evidenziati. Nulla accade finché non fai clic su **Applica**. Le modifiche vengono quindi apportate in un'unica operazione, che puoi annullare come qualsiasi altra modifica, dal messaggio che appare o nella [cronologia delle revisioni](revisions.md).

Controlla attentamente una proposta prima di applicarla – in particolare che l'assistente abbia scelto la persona giusta e che non abbia aggiunto un nuovo registro (come un luogo o una fonte) che esiste già nel tuo albero con un nome leggermente diverso. Se una proposta non è del tutto corretta, indica cosa cambiare e l'assistente proporrà di nuovo.

Una volta che una proposta è stata applicata, le proposte più vecchie nella stessa conversazione non possono più essere applicate, poiché sono state fatte per l'albero com'era prima. Lo stesso accade se uno dei registri interessati è stato modificato nel frattempo.

## Suggerimenti per porre domande

- **Nomina le persone.** L'assistente non sa chi sei o chi è la tua persona principale, quindi invece di "mia nonna", chiedi della "nonna di Anna Smith (nata nel 1950)". Puoi anche usare gli ID di Gramps, ad esempio "i figli di I0042".
- **Sii specifico** quando i nomi sono comuni: "Quando si è sposato John Smith nato nel 1850 a Boston?" è meglio di "Quando si è sposato John Smith?"
- **Usa la tua lingua.** Puoi chiedere nella tua lingua e ricevere risposte nella stessa lingua.
- **Chiedi di nuovo in modo diverso** se una risposta sembra incompleta – ad esempio, nominando il luogo o il periodo di tempo che ti interessa.

!!! tip
    Ti preghiamo di condividere la tua esperienza riguardo a ciò che funziona e non funziona con la comunità.
