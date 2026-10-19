# Albero Genealogico

La pagina dell'Albero Genealogico è accessibile dalla barra laterale e visualizza grafici interattivi centrati su una persona selezionata. Cinque tipi di grafico sono disponibili tramite schede nella parte superiore della pagina.

## Selezionare la persona di partenza

Tutti i grafici partono dalla persona attualmente selezionata nell'albero (mostrata nella barra degli strumenti). La persona attualmente centrata è evidenziata con un'ombra. Usa il pulsante **Persona Home** per tornare alla tua persona di casa, o il pulsante **Indietro** per tornare alla persona visualizzata in precedenza. Cliccando sulla scheda di una persona in qualsiasi grafico si ricentra il grafico su quella persona.

Se non è stata impostata alcuna persona di casa, la pagina offre un pulsante **Imposta Persona Home** per cercarne e selezionarne una direttamente. Se l'albero non contiene ancora persone, gli utenti con il ruolo di Editor o superiore vedono invece un pulsante **Nuova Persona** – la prima persona creata in un albero vuoto diventa automaticamente la tua persona di casa, quindi il grafico viene mostrato immediatamente.

## Tipi di grafico

### Albero degli Antenati

Un grafico genealogico che mostra gli antenati della persona selezionata. I genitori appaiono a sinistra (o a destra, a seconda del layout), i nonni più lontano, e così via.

### Albero dei Discendenti

Mostra i discendenti della persona selezionata – figli, nipoti, e così via.

### Grafico a Clessidra

Combina gli antenati sopra e i discendenti sotto la persona selezionata in un'unica vista.

### Grafico delle Relazioni

Mostra il percorso di relazione tra due persone. La persona selezionata è un estremo; clicca su qualsiasi altra persona nel grafico per impostare il secondo estremo e visualizzare il percorso di relazione più breve tra di loro.

!!! nota
    La stessa persona può apparire più di una volta nel grafico – ad esempio quando qualcuno è stato sposato più volte e appare in diverse unità familiari lungo il percorso. Questo è intenzionale, non un bug.

### Grafico a Ventaglio

Un grafico genealogico circolare. Gli antenati si irradiano verso l'esterno dalla persona selezionata al centro.

## Spostarsi verso i parenti ed espandere i rami

Nell'Albero degli Antenati e nel Grafico a Ventaglio, la persona selezionata ha un pulsante a forma di chevron che apre un menu dei loro figli. Nell'Albero dei Discendenti, apre invece un menu dei loro genitori. Scegliendo una persona dal menu si centra il grafico su di essa.

Nell'Albero degli Antenati, nell'Albero dei Discendenti e nel Grafico a Clessidra, le persone ai margini del grafico i cui genitori o figli non sono mostrati hanno un chevron sul lato dove il loro ramo continua. Cliccando su di esso si aggiunge un'altra generazione a quel ramo, mentre la persona selezionata rimane la stessa. In questo modo, puoi ad esempio guardare tutti i nonni e poi seguire solo una linea più indietro. I rami espansi vengono reimpostati quando selezioni un'altra persona o cambi grafico.

## Controlli di navigazione

Tutti i tipi di grafico condividono una barra degli strumenti con i seguenti pulsanti:

- **Persona Home** – torna alla tua persona di casa
- **Indietro** – torna alla persona centrata in precedenza
- **Dettagli Persona** – apri la pagina del profilo completo della persona attualmente centrata
- **Preferenze** – apri una finestra di dialogo per regolare le opzioni di visualizzazione specifiche del grafico (vedi sotto)

Tutti i grafici supportano **pan** (clicca e trascina) e **zoom** (rotella del mouse o pizzica).

## Preferenze del grafico

La finestra di dialogo **Preferenze** (icona dell'ingranaggio nella barra degli strumenti) ti consente di regolare le seguenti opzioni, a seconda del tipo di grafico:

- **Generazioni Massime di Antenati** – quante generazioni di antenati visualizzare
- **Generazioni Massime di Discendenti** – quante generazioni di discendenti visualizzare
- **Massimo Grado di Separazione** – per il Grafico delle Relazioni, la lunghezza massima del percorso da cercare
- **Numero Massimo di Immagini visualizzate** – limita le foto profilo mostrate nel grafico per prestazioni
- **Formato di Visualizzazione del Nome** – controlla come i nomi sono mostrati sulle schede delle persone

Clicca su **Ripristina** per ripristinare le impostazioni predefinite, o **Chiudi** per applicare le tue modifiche.

Le impostazioni delle preferenze del grafico sono memorizzate nella memoria locale del browser, quindi persistono tra le sessioni sullo stesso dispositivo.

## Tipo di grafico predefinito

Il tipo di grafico mostrato quando apri per la prima volta la pagina dell'Albero Genealogico può essere configurato in [Impostazioni Utente](settings.md). La tua scelta predefinita si applica a tutti i tuoi dispositivi.

## Modifica dell'albero

Gli utenti con il ruolo di Editor o superiore possono aggiungere e collegare persone direttamente dall'Albero degli Antenati. Vedi [Modifica dell'albero genealogico](tree-edit.md) per dettagli.
