# Importa file multimediali

Se hai [importato un albero genealogico](import.md) e hai bisogno di caricare i file multimediali corrispondenti, utilizza **Importa file multimediali** nella [pagina di importazione](import.md), sotto l'importazione dell'albero genealogico. Si aspetta un file ZIP contenente i file multimediali mancanti. Il caricamento è possibile solo una volta che l'albero contiene oggetti multimediali, poiché i file sono abbinati agli oggetti multimediali esistenti – un file di albero genealogico si riferisce solo ai suoi file multimediali, quindi importalo prima.

I file sono abbinati agli oggetti multimediali nel tuo albero in uno dei due modi:

- **Per checksum.** Per gli oggetti multimediali che hanno un checksum – come nel caso degli alberi importati da Gramps Desktop – il file con il checksum corrispondente viene utilizzato, indipendentemente dal suo nome o dalla struttura delle cartelle nel file ZIP. Questo funziona solo se i checksum nel database di Gramps sono corretti, cosa che l'esecuzione dello strumento di controllo e riparazione garantisce.
- **Per percorso o nome file.** Gli oggetti multimediali senza un checksum – come è tipico dopo un'importazione GEDCOM – vengono abbinati in base al percorso relativo memorizzato nell'oggetto multimediale. Se nessun file nel ZIP ha quel percorso, vengono abbinati solo per nome file, ignorando maiuscole e minuscole (dalla versione 3.26 dell'API Web di Gramps). Questo funziona anche per percorsi assoluti da altri programmi, come `C:\Users\...\Family\grandpa.jpg`, quindi puoi semplicemente mettere tutti i file nel file ZIP. Un nome file viene utilizzato solo se è unico, sia nel file ZIP che tra gli oggetti multimediali ancora senza un file.

Dopo il caricamento, il risultato indica per quanti oggetti multimediali è stato trovato un file e elenca quelli per i quali il file ZIP non conteneva alcun file, con il loro ID Gramps e percorso memorizzato. Usa questo elenco per trovare i file mancanti, quindi carica un altro file ZIP con solo questi – i file già presenti sul server non sono interessati.

Se diversi oggetti multimediali hanno lo stesso nome file in cartelle diverse, l'abbinamento per nome file non funziona per loro. Ricrea la struttura delle cartelle dai percorsi memorizzati nel file ZIP, oppure importa tutto in Gramps Desktop prima, che ha più opzioni per associare file multimediali esistenti con un albero importato, e poi passa a Gramps Web come descritto in [Provenienza da Gramps Desktop](import.md#coming-from-gramps-desktop).

## Stato del file multimediale

La sezione **Dati** delle [Impostazioni di amministrazione](settings.md) mostra:

- Il numero totale di oggetti multimediali nell'albero e se alcuni mancano di un checksum
- Il numero di oggetti multimediali il cui file associato è mancante dal server

Un segno di spunta verde indica che tutto è in ordine. Se vengono rilevati problemi, vengono mostrati i collegamenti agli oggetti interessati. I checksum mancanti si verificano tipicamente quando i dati sono stati importati da un formato come GEDCOM che include riferimenti multimediali ma non i file effettivi. I file mancanti possono essere caricati come descritto sopra.
