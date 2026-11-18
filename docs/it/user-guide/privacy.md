# Registrazioni private

Qualsiasi registrazione nell'albero può essere contrassegnata come privata. Insieme ai [ruoli utente](../install_setup/users.md#user-roles), questo decide chi vede cosa.

## Chi può vedere cosa

Gramps Web non è mai aperto al pubblico: solo gli utenti con un account possono vedere qualcosa. "Pubblico" in Gramps significa semplicemente "non privato", cioè visibile a ogni utente autenticato dell'albero.

| Ruolo | Registrazioni pubbliche | Registrazioni private |
|---|---|---|
| Ospite | visualizza | – |
| Membro | visualizza | visualizza |
| Collaboratore | visualizza, aggiungi | visualizza, aggiungi |
| Editore, Proprietario, Amministratore | visualizza, aggiungi, modifica, elimina | visualizza, aggiungi, modifica, elimina |

Per gli ospiti, le registrazioni private non esistono: vengono escluse da pagine, elenchi, risultati di ricerca, grafici, rapporti, esportazioni e risposte dell'assistente AI. Questo è applicato dove il server legge il database, non nascondendo le cose nell'app, quindi un ospite non può accedere ai dati privati in nessun altro modo.

Gli account che non sono stati ancora approvati (dopo la [autoregistrazione](registration.md)) non possono accedere affatto.

Quindi, se parenti o altre persone con un account ospite non devono vedere determinate informazioni, contrassegnale come private. Se tutti gli utenti di un albero possono vedere tutto, assegna loro il ruolo di membro (o superiore) e non c'è bisogno di contrassegnare nulla come privato.

## Le persone viventi non sono automaticamente private

Niente viene reso privato automaticamente – nemmeno le persone che sono ancora vive. I dati delle persone viventi sono visibili agli ospiti fino a quando non li contrassegni come privati. Questo si applica anche agli alberi importati.

Per rendere private le persone che probabilmente sono vive in Gramps Web:

1. Nella lista delle persone, apri il [filtro avanzato](lists.md#advanced-filter) e aggiungi la condizione "Persone probabilmente vive" (lascia la data vuota per oggi). Applica il filtro.
2. Clicca su **Seleziona**, spunta la casella nell'intestazione e scegli **Seleziona tutto**.
3. Scegli l'azione **Privacy** e contrassegna le registrazioni come private.

"Probabilmente vive" è stimato dalle date della persona e dei loro parenti. Le persone senza date utilizzabili sono considerate vive. Controlla il risultato e tieni presente che la stima può cambiare man mano che aggiungi dati.

Contrassegnare una persona come privata nasconde la persona, ma non i loro eventi, note, media o famiglie – vedi sotto. Gramps Desktop ha più strumenti per impostare la privacy di molte registrazioni correlate contemporaneamente, che puoi utilizzare con l'[addon Sync](../administration/sync.md).

Le persone che muoiono in seguito non diventano automaticamente pubbliche. Se lo desideri è a tua discrezione – molti ricercatori preferiscono mantenere private le informazioni raccolte per un certo periodo.

## Lettura delle icone di blocco

Gli utenti che possono visualizzare dati privati vedono un lucchetto accanto agli elementi privati. Ci sono due tipi:

- **Lucchetto pieno** – la registrazione stessa è privata. Ad esempio, nella pagina di una persona, un lucchetto pieno accanto a un evento significa che l'evento è privato, e accanto a un bambino che il bambino è privato.
- **Lucchetto contornato** – solo il *collegamento* è privato, non la registrazione a cui porta. Ad esempio, il collegamento di una persona a un evento può essere privato mentre l'evento stesso è pubblico. L'evento è quindi nascosto dalla pagina di quella persona ma rimane visibile altrove, come nelle pagine di altri partecipanti o nell'elenco degli eventi.

Se sia la registrazione che il suo collegamento sono privati, viene mostrato il lucchetto pieno.

La stessa distinzione si applica ai bambini (il bambino o il collegamento del bambino alla famiglia), associazioni, collegamenti di repository di una fonte e media in una galleria. Nomi, attributi, indirizzi e URL appartengono alla loro registrazione e hanno solo il lucchetto pieno.

## Rendere qualcosa privato

Hai bisogno di permessi di modifica per cambiare la privacy.

- **Un'intera registrazione**: apri la sua pagina, entra in modalità modifica e clicca sul pulsante del lucchetto nella barra degli strumenti.
- **Parte di una registrazione** – un nome alternativo, attributo, indirizzo, URL, associazione, collegamento a un bambino o collegamento a un repository: apri la finestra di modifica di quell'elemento e attiva l'interruttore **Privato**. Il nome principale non ha interruttore, poiché la persona altrimenti verrebbe mostrata come "Privata".
- **Un evento dalla pagina di una persona o di una famiglia**: la finestra di modifica dell'evento ha un interruttore di privacy per l'evento stesso. Se l'evento è condiviso con altre persone, diventa modificabile solo dopo **Modifica per tutti**, poiché è privato per tutti loro.
- **Il collegamento di una persona a un evento**: nella pagina dell'evento, apri la riga del partecipante in modalità modifica. L'interruttore di privacy lì si applica solo al collegamento di quel partecipante, quindi l'evento rimane visibile per gli altri partecipanti.
- **Un oggetto media in una galleria**: in modalità modifica, clicca sul lucchetto nell'angolo della tessera.
- **Molte registrazioni contemporaneamente**: selezionale in un elenco e utilizza l'azione **Privacy**, vedi [Elenchi](lists.md#tags-and-privacy).

Per controllare quali registrazioni in un elenco sono private, attiva la colonna **Privacy** nel selettore di colonne dell'elenco.

## Cose da tenere a mente

- Rendere una registrazione privata non rende private le registrazioni a cui è collegata. Se una persona è privata, i loro eventi, le famiglie a cui appartengono e le note ad esse collegate sono ancora visibili a meno che non siano private esse stesse. Usa il filtro avanzato o la colonna **Privacy** per controllare le registrazioni correlate.
- Rendere una famiglia o un evento privato lo nasconde, ma non le persone in esso.
- [Le corrispondenze DNA e i dati Y-DNA](dna-matches.md#private-matches) hanno il loro interruttore **Privato** nelle loro finestre.
- Le esportazioni e gli archivi media effettuati da un utente che non può visualizzare dati privati non contengono registrazioni o file privati.
- La privacy è una funzionalità di Gramps, quindi le registrazioni contrassegnate come private in Gramps Desktop sono private anche in Gramps Web e viceversa.
