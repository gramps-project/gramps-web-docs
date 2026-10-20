Ci sono due modi per aggiungere un nuovo file multimediale (un'immagine, un file audio, un file video o qualsiasi altro file), e i file multimediali esistenti possono essere collegati a nuovi oggetti mentre vengono creati:

## Aggiungi un nuovo file multimediale autonomo

Per aggiungere un file multimediale autonomo, fai clic sull'icona + nella barra superiore dell'app e seleziona "Oggetto multimediale".

Fai clic su "seleziona un file" per selezionare un file dal tuo computer. Su un dispositivo mobile, facendo clic su questo pulsante avrai l'opzione di scattare direttamente una foto con la fotocamera del tuo dispositivo.

Facoltativamente,

- inserisci una descrizione del file multimediale sotto "titolo"
- inserisci una data
- imposta il file multimediale come privato (il che lo renderà visibile solo agli utenti con autorizzazione sufficiente)

Fai clic su "aggiungi" per caricare il file e creare l'oggetto multimediale.

## Aggiungi un nuovo file multimediale e collegalo a un altro oggetto

I seguenti tipi di oggetti in Gramps possono avere oggetti multimediali allegati: persone, famiglie, eventi, luoghi, fonti e citazioni.

Nella vista dettagliata di qualsiasi oggetto, fai clic sul pulsante blu di modifica in basso a destra (se non lo vedi, il tuo utente non ha permessi di modifica). Fai clic sulla scheda "galleria" e fai clic sul pulsante blu +.

Si aprirà una finestra di dialogo che offre gli stessi campi descritti nella sezione precedente. Fai clic su "salva" per caricare il file, aggiungere un nuovo oggetto multimediale e collegarlo all'oggetto visualizzato.

## Foto profilo

La prima immagine nella galleria di una persona viene utilizzata come foto profilo. In modalità modifica, è contrassegnata con un'etichetta "Foto profilo". Per utilizzare un'immagine diversa, spostala nella prima posizione con i pulsanti freccia sulle miniature della galleria.

Se una persona non ha ancora file multimediali, la modalità modifica mostra un segnaposto **Aggiungi foto profilo**. Fai clic su di esso per caricare un nuovo file multimediale o selezionarne uno esistente.

## Collega file multimediali esistenti quando crei un oggetto

Quando crei una nuova persona, famiglia, evento, luogo, fonte o citazione, il modulo ha una sezione "Media". Lì puoi selezionare uno o più oggetti multimediali esistenti, che saranno collegati al nuovo oggetto quando lo salvi.

Quando crei una persona insieme ai suoi eventi di nascita e morte, gli oggetti multimediali selezionati sono collegati solo alla persona, non agli eventi.

## Riconoscimento del testo (OCR)

Se l'amministratore del server ha abilitato il supporto OCR, un pulsante "Riconoscimento del testo" appare sotto l'immagine nella vista dettagliata di un oggetto multimediale.

Fai clic su "Riconoscimento del testo", scegli la lingua del testo mostrato nell'immagine, quindi fai clic su "Esegui". L'immagine viene elaborata con [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) e il testo riconosciuto viene visualizzato sotto.

Se il tuo utente ha permessi di modifica, fai clic su "Salva come Nota" per creare una nuova nota (di tipo "Trascrizione") contenente il testo riconosciuto e collegarla all'oggetto multimediale.

!!! tip
    L'accuratezza dell'OCR dipende fortemente dalla qualità dell'immagine e dalla lingua selezionata. Se il risultato sembra errato, prova una lingua diversa – ad esempio, i documenti storici tedeschi spesso necessitano della variante Fraktur piuttosto che del tedesco semplice.
