# Utilizzo di Gramps Web per l'analisi Y-DNA

!!! note "Nota"
    Questa funzione richiede la versione 3.3.0 o successiva dell'API di Gramps Web e la versione 25.9.0 o successiva del frontend di Gramps Web.

La vista Y-DNA in Gramps Web può utilizzare i dati grezzi dei polimorfismi a singolo nucleotide (SNP) del cromosoma Y per determinare il più probabile haplogruppo Y-DNA di una persona e visualizzare gli antenati derivati nell'albero del cromosoma Y umano insieme a stime temporali.

## Come ottenere e memorizzare i dati SNP Y-DNA

Per ottenere i dati SNP Y-DNA, è necessario effettuare un test Y-DNA tramite un servizio di test genetici. Il risultato è rappresentato come un insieme di mutazioni (SNP), ciascuna identificata da una stringa (ad es. `R-BY44535`) e da un segno `+` o `-` che indica se la mutazione è presente o assente. Gramps Web si aspetta la stringa di tutti gli SNP testati nel formato `SNP1+, SNP2-, SNP3+,...` da memorizzare in un attributo persona di tipo personalizzato `Y-DNA` (case sensitive). Puoi creare manualmente questo attributo in Gramps Web o Gramps Desktop, oppure navigare alla vista Y-DNA in Gramps Web e fare clic sul pulsante blu "Aggiungi", selezionare la persona a cui aggiungere i dati e incollare la stringa SNP. In ogni caso, i dati saranno memorizzati come un attributo persona nel tuo database Gramps.

[Consulta qui sotto](#istruzioni-per-ottenere-dati-snp-da-servizi-di-test) per le istruzioni su come ottenere i dati SNP da vari servizi di test.

## Come funziona

Una volta che una persona ha un attributo `Y-DNA` contenente i dati SNP, Gramps Web utilizzerà la libreria Python open-source [yclade](https://github.com/DavidMStraub/yclade) per determinare la posizione più probabile della persona nell'albero del cromosoma Y umano. L'albero è stato creato dal progetto [YFull](https://www.yfull.com/) basato su decine di migliaia di test Y-DNA. Si noti che Gramps Web utilizza una copia locale dell'albero YFull, quindi nessun dato viene inviato a terzi.

L'albero viene percorso dalla radice alle foglie e, in ogni nodo, gli SNP associati a quel nodo vengono confrontati con gli SNP testati positivamente e negativamente della persona, e viene seguita la ramificazione appropriata.

Il risultato finale è una successione di cladi dalla radice dell'albero (l'[“Adamo” cromosomico Y](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) al clade più derivato che è coerente con i dati SNP della persona. Ogni clade ha un'età stimata basata sulle età dei campioni nel database YFull che appartengono a quel clade.

Poiché i cromosomi Y sono ereditati da padre a figlio, questa successione corrisponde a un estratto dell'ascendenza patrilineare della persona.

## Come interpretare i risultati

Il pezzo di informazione più importante è il più probabile haplogruppo della persona, mostrato nella parte superiore della pagina. Il nome è collegato alla pagina corrispondente sul sito web [YFull](https://www.yfull.com/), che contiene ulteriori informazioni, come il paese di origine dei campioni testati appartenenti a quel haplogruppo.

Nell'albero degli antenati patrilineari mostrato in Gramps Web, la casella direttamente sopra la persona testata è l'antenato comune più recente (MRCA) di tutti i campioni testati appartenenti all'haplogruppo della persona. La data mostrata per questo antenato è la sua data di nascita stimata. L'antenato sopra di lui è l'antenato in cui è apparsa per la prima volta la mutazione che definisce questo haplogruppo.

A causa del lento tasso di mutazione dei cromosomi Y, il MRCA può risalire a molte centinaia di anni fa. Per haplogruppi rari (cioè haplogruppi per i quali poche persone sono state testate finora), può anche risalire a migliaia di anni.

## Istruzioni per ottenere dati SNP da servizi di test

### [YSEQ](https://www.yseq.net/)

Una volta effettuato l'accesso a "Il mio account", vai su "I miei risultati / Visualizza i miei alleli" e naviga fino in fondo alla pagina. Il campo di testo "Elenco alleli compatto" è stato aggiunto specificamente per Gramps Web ed è nel formato esatto per essere incollato nell'attributo `Y-DNA`.
