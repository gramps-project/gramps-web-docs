# Usa il blog integrato

Il blog è destinato a presentare storie sulla tua ricerca genealogica.

Nel database di Gramps, i post del blog sono rappresentati come fonti con una nota allegata, contenente il testo del blog e, facoltativamente, file multimediali per le immagini del post del blog. Gramps Web tratta ogni fonte con un'etichetta `Blog` come articolo del blog.

## Aggiungi un post al blog

Il modo più veloce per scrivere un post è il modulo dedicato **Nuovo Post del Blog** in Gramps Web. Aprilo sia dal pulsante blu **+** nella pagina del Blog, sia dal menu **Aggiungi** (icona del segno più) nella barra superiore dell'app selezionando **Post del Blog**.

Il modulo ha campi per:

- **Titolo** – il titolo del post (obbligatorio)
- **Autore** – chi l'ha scritto
- **Contenuto** – un editor di testo arricchito per il post stesso
- **Media** – uno o più oggetti multimediali. Il primo diventa l'immagine di anteprima mostrata sopra il testo; tutti appaiono come una galleria sotto di esso.
- **Tag** e un interruttore **privato**, come per qualsiasi altro oggetto

Salvando il modulo, vengono creati per te la fonte sottostante, la nota e l'etichetta `Blog`, come descritto [di seguito](#relation-between-blog-and-sources).

### Aggiungere un post manualmente

Puoi anche creare un post costruendo tu stesso gli oggetti sottostanti. Questo è l'unico modo per farlo in Gramps Desktop ([synchronizzato](../administration/sync.md) con Gramps Web), e i passaggi sono gli stessi in entrambe le applicazioni:

- Aggiungi una nuova fonte. Il titolo della fonte sarà il titolo del tuo post del blog, l'autore della fonte sarà l'autore del post.
- Facoltativamente, associa la fonte a un repository corrispondente al tuo blog di Gramps Web.
- Aggiungi una nuova nota alla fonte. Scrivi il tuo post del blog e copia il testo nella nota.
- Facoltativamente, aggiungi uno o più file multimediali alla tua fonte. Il primo file multimediale sarà preso come immagine di anteprima del post mostrata sopra il testo. Tutti i file multimediali saranno mostrati sotto il testo come una galleria.
- Aggiungi l'etichetta `Blog` alla fonte (creala se non esiste).

## Relazione tra blog e fonti

Poiché i post del blog sono solo fonti, tutti gli articoli del blog appaiono anche nell'elenco delle fonti e si mostrano come fonti nelle ricerche. Nella vista della fonte, c'è un pulsante "mostra nel blog" che ti porterà alla vista del blog per quel post del blog. L'URL del post del blog contiene anche l'ID Gramps della fonte corrispondente, quindi un articolo su `yourdomain.com/blog/S0123` corrisponde alla fonte su `yourdomain.com/source/S0123`.

In fondo a ogni post del blog, c'è un pulsante "dettagli" che ti porterà alla vista della fonte.
