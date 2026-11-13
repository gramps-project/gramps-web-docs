# Importa file multimediali

Se hai [importato un albero genealogico](import.md) e hai bisogno di caricare i file multimediali corrispondenti, utilizza **Importa file multimediali** nella sezione Dati delle [impostazioni di amministrazione](settings.md). Si aspetta un file ZIP contenente i file multimediali mancanti. I file vengono abbinati agli oggetti multimediali nel tuo albero in uno dei seguenti modi:

- **Per checksum.** Per gli oggetti multimediali che hanno un checksum – come nel caso degli alberi importati da Gramps Desktop – viene utilizzato il file con il checksum corrispondente, indipendentemente dal suo nome o dalla struttura delle cartelle nel file ZIP. Questo funziona solo se i checksum nel database di Gramps sono corretti, cosa che garantisce l'esecuzione dello strumento di controllo e riparazione.
- **Per percorso.** Gli oggetti multimediali senza un checksum – come è tipico dopo un'importazione GEDCOM – vengono abbinati in base al loro percorso: il file ZIP deve contenere il file esattamente nel percorso relativo memorizzato nell'oggetto multimediale.

Se i percorsi memorizzati nel tuo file GEDCOM sono assoluti (ad esempio `C:\Users\...\photo.jpg`), l'abbinamento per percorso non funzionerà. In questo caso, è consigliabile importare prima tutto in Gramps Desktop, che ha più opzioni per associare file multimediali esistenti con un albero importato, e poi passare a Gramps Web come descritto in [Provenendo da Gramps Desktop](import.md#coming-from-gramps-desktop).
