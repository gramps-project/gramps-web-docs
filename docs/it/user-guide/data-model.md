# Come Gramps organizza i dati

Gramps Web memorizza un albero genealogico non come un grafico, ma come oggetti separati – persone, famiglie, eventi, luoghi, fonti, e così via – che sono collegati tra loro. Una volta che sai come questi oggetti si incastrano, inserire dati diventa prevedibile: qualsiasi cosa tu voglia collegare deve esistere prima.

Gramps Web utilizza lo stesso modello di dati di Gramps Desktop, quindi tutto ciò che è presente in questa pagina si applica a entrambi.

## I mattoni fondamentali

| Oggetto | Cosa rappresenta | Esempi |
|---|---|---|
| Persona | Un individuo | Tu, tua nonna |
| Famiglia | Una coppia, i loro figli, o entrambi | I tuoi genitori e i loro figli |
| Evento | Qualcosa che è accaduto, con una data e un luogo | Nascita, matrimonio, censimento, emigrazione |
| Luogo | Una località geografica | Un villaggio, una parrocchia, un paese |
| Fonte | Un documento o una raccolta di informazioni | Un registro parrocchiale, un censimento, un libro |
| Citazione | Un riferimento specifico all'interno di una fonte | Pagina 12, voce 3 del registro parrocchiale |
| Repositorio | Dove è conservata una fonte | Un archivio, una biblioteca, un sito web |
| Nota | Testo libero | Una trascrizione, osservazioni di ricerca |
| Oggetto multimediale | Un file | Una foto, un certificato scansionato |

Ogni tipo di oggetto ha la propria lista in Gramps Web, vedi [Liste](lists.md).

## Persone e famiglie

I genitori e i figli non sono collegati direttamente tra loro, ma attraverso una **famiglia**. Una famiglia ha fino a due partner e un numero qualsiasi di figli:

- I tuoi genitori e tu siete collegati attraverso la famiglia in cui sei un figlio.
- I tuoi fratelli e sorelle sono gli altri figli della stessa famiglia.
- Tu e il tuo coniuge formate un'altra famiglia, in cui sei un partner, insieme ai vostri figli.

Una persona può essere un figlio in una famiglia e un partner in diverse. Ogni figlio ha una relazione con ciascuno dei genitori, come nascita, adozione o figliastro, e ogni famiglia ha un tipo di relazione, come sposato o unione civile.

Questo è il motivo per cui "aggiungere genitori" a una persona significa aggiungere la persona come figlio a una famiglia – cosa che il [grafico ad albero](tree-edit.md) fa per te in un solo passaggio.

## Eventi

Una nascita, una morte o un matrimonio non sono un campo di una persona, ma un **evento** a sé stante, con un tipo, una data, un luogo e una descrizione. Le persone sono collegate a un evento con un **ruolo**: la persona di cui è la nascita ha il ruolo di "Primario", mentre qualcun altro potrebbe essere collegato allo stesso evento come testimone.

Gli eventi che riguardano una coppia, come un matrimonio, appartengono alla famiglia piuttosto che a uno dei partner. Un evento può anche essere condiviso da più persone – ad esempio, un record di censimento che elenca un'intera famiglia – invece di essere inserito una volta per persona.

## Oggetti condivisi: luoghi e fonti

Luoghi, fonti, citazioni, repository, note e oggetti multimediali esistono di per sé, e un numero qualsiasi di altri oggetti può fare riferimento allo stesso. Questo ha alcune conseguenze:

- **Crea una volta, seleziona molte volte.** Il villaggio dove sono nati dieci dei tuoi antenati è un luogo, selezionato in dieci eventi di nascita. Se correggi il suo nome o le coordinate, la correzione si applica ovunque.
- **Crealo prima di selezionarlo.** I moduli in Gramps Web selezionano luoghi e fonti che già esistono. Crea prima un nuovo luogo o una nuova fonte utilizzando il pulsante **+** (Aggiungi) nella barra dell'app in alto.
- **I luoghi sono nidificati.** Un luogo può essere racchiuso da uno più grande – un villaggio da una contea, la contea da un paese – così non devi ripetere l'intera gerarchia per ogni villaggio.
- **Fonti e citazioni sono separate.** Una fonte è il registro parrocchiale nel suo insieme; una citazione è l'entry specifica che supporta un fatto, con la sua pagina, data e la tua fiducia in essa. Molte citazioni possono puntare alla stessa fonte.

Se hai accidentalmente creato lo stesso luogo o fonte due volte, puoi [unire i duplicati](lists.md#merge).

## Modifica della pagina di un oggetto

Nella pagina di una fonte, repository o oggetto multimediale, fai clic sul titolo in modalità modifica per cambiarlo (per un oggetto multimediale, la sua descrizione). Premi Invio, fai clic su ✓, o fai clic altrove per salvare; premi Esc o fai clic su ✕ per annullare.

La maggior parte delle liste nella pagina di un oggetto mantiene l'ordine che dai, ad esempio gli eventi, i nomi, gli attributi, gli indirizzi, le citazioni, o i figli di una famiglia. In modalità modifica, seleziona una riga e spostala con i pulsanti su e giù, o trascinala nella sua nuova posizione: con il mouse, premi la riga e spostala; su un touchscreen, premi e tieni premuta la riga fino a quando non viene sollevata. Premi Esc mentre trascini per annullare. I media nella galleria possono essere riordinati allo stesso modo, vedi [Foto profilo](media.md#profile-pictures).

## La Persona Principale

La Persona Principale è la persona da cui partono i grafici dell'albero genealogico e il punto di partenza predefinito per i rapporti. Vedi [Primo accesso](first-login.md) per come impostarlo.

!!! nota "Diverso da Gramps Desktop"
    In Gramps Desktop, la Persona Principale è memorizzata nel database dell'albero genealogico, quindi è la stessa per chiunque apra quel database. Gramps Web non lo utilizza. Invece, la Persona Principale è memorizzata nel tuo browser, separatamente per ogni albero: non è condivisa con altri utenti e non ti segue su un browser o dispositivo diverso. Dopo aver importato un albero da Gramps Desktop, o quando utilizzi Gramps Web su un altro dispositivo, devi impostarlo di nuovo.

## Un ordine raccomandato

Quando inserisci una nuova famiglia a mano, questo ordine evita di saltare avanti e indietro tra i moduli:

1. **Luoghi e fonti.** Crea i luoghi di cui hai bisogno e, se registri fonti, la fonte da cui stai lavorando.
2. **Persone.** Aggiungi le persone con le loro date e luoghi di nascita e morte. Questo è più veloce in modalità modifica del grafico dell'albero genealogico, che crea le famiglie per te – vedi [Inizia un nuovo albero](start-tree.md) e [Modifica l'albero genealogico](tree-edit.md).
3. **Ulteriori eventi.** Apri una famiglia (ad esempio dalla scheda Relazioni di una persona) per aggiungere il matrimonio, e una pagina di una persona per aggiungere altri eventi.
4. **Citazioni.** Nella scheda Citazioni delle Fonti della persona, evento o altro oggetto che una fonte supporta, aggiungi una nuova citazione, seleziona la fonte e inserisci la pagina.
5. **Note e media.** Allegare trascrizioni, foto e scansioni – vedi [Aggiungi file multimediali](media.md).

## Inserimento delle date

Una data è inserita come campi separati per anno, mese e giorno, che possono anche essere compilati utilizzando un selettore di date. Lascia fuori le parti che non conosci: un anno da solo è una data valida. 
Invece di indovinare un giorno esatto, descrivi ciò che sai effettivamente scegliendo il tipo di data con le chip sopra i campi. Un suggerimento sotto le chip spiega il tipo selezionato:

| Cosa sai | Tipo | Esempio |
|---|---|---|
| La data esatta, o parte di essa | Normale | 12 marzo 1850, o solo 1850 |
| Una data approssimativa | Circa | circa 1850 |
| Un limite | Prima, Dopo | prima del 1900 |
| La data si colloca in un periodo | Intervallo | tra il 1850 e il 1855 (campi "Più antico" e "Più recente") |
| Qualcosa è durato per un periodo | Intervallo | dal 1850 al 1855 |

Per un Intervallo, uno dei due date ("Da" e "A") può essere lasciato vuoto, quindi "da 1850" o "a 1855" è un Intervallo con solo una data.

I campi **Qualità** e **Calendario** sono sotto **Ulteriori opzioni**, che si apre automaticamente quando una data utilizza uno dei due. La qualità registra come sei arrivato a una data: "Stimata" per un'ipotesi informata, "Calcolata" per una data derivata da altre informazioni, come un anno di nascita calcolato da un'età al momento della morte.

!!! warning "Le date circa e stimate coprono 50 anni in entrambe le direzioni"
    Quando Gramps confronta le date, tratta una data del tipo "circa" – e qualsiasi data con la qualità "Stimata" – come un intervallo che va da 50 anni prima a 50 anni dopo la data fornita. Ad esempio, filtrando la lista delle Persone per persone nate tra il 1840 e il 1860 si trova anche una persona nata "circa 1880", perché quella data è considerata coprire il periodo dal 1830 al 1930. Allo stesso modo, "prima" e "dopo" sono considerati estendersi fino a 50 anni prima o dopo la data.

    Questo può portare a risultati sorprendenti, quindi usa "circa" e "Stimata" solo quando non puoi restringere la data. Se conosci un periodo più breve, un Intervallo come "tra il 1878 e il 1882" è più preciso.

Il calendario ti consente di inserire una data nel calendario utilizzato nel record originale, come il calendario giuliano, invece di convertirlo tu stesso.
