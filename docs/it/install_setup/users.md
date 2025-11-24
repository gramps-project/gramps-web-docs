# Sistema utente

Gramps Web non è destinato ad essere esposto a Internet per accesso pubblico, ma solo da parte di utenti autenticati. Gli account utente possono essere creati dal proprietario del sito tramite la riga di comando o l'interfaccia web, oppure tramite auto-registrazione e successiva approvazione da parte del proprietario del sito.

## Ruoli utente

I seguenti ruoli utente sono attualmente definiti.

Ruolo | ID Ruolo | Permessi
-----|---------|------------
Ospite | 0 | Visualizza oggetti non privati
Membro | 1 | Ospite + visualizza oggetti privati
Contributore* | 2 | Membro + aggiungi oggetti
Editore | 3 | Contributore + modifica e elimina oggetti
Proprietario | 4 | Editore + gestisci utenti
Amministratore | 5 | Proprietario + modifica altri alberi in configurazione multi-albero

\* Si noti che il ruolo di "Contributore" è attualmente solo parzialmente supportato; ad esempio, gli oggetti familiari non possono essere aggiunti poiché implicano una modifica degli oggetti persona di Gramps sottostanti dei membri della famiglia. Si raccomanda di utilizzare gli altri ruoli ogni volta che è possibile.

## Configurare chi può utilizzare la chat AI

Se hai [configurato la chat AI](chat.md), vedrai un'opzione qui per scegliere quali gruppi di utenti sono autorizzati a utilizzare la funzione di chat.

## Gestione utenti

Ci sono due modi per gestire gli utenti:

- Con permessi di proprietario utilizzando l'interfaccia web
- Dalla riga di comando sul server

L'account proprietario necessario per accedere per la prima volta all'app web può essere aggiunto nella procedura guidata di onboarding che viene avviata automaticamente quando si accede a Gramps Web con un database utente vuoto.

### Gestione utenti dalla riga di comando

Quando si utilizza [Docker Compose](deployment.md), il comando di base è

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

Il `COMMAND` può essere `add` o `delete`. Usa `--help` per `[ARGS]` per mostrare la sintassi e le possibili opzioni di configurazione.

### Approvazione utenti auto-registrati

Quando un utente si auto-registra, non ottiene accesso immediato. Un'email viene inviata al proprietario dell'albero riguardo la nuova registrazione dell'utente e all'utente viene inviata una richiesta via email per confermare il proprio indirizzo email. Confermare con successo il proprio indirizzo email cambia il loro ruolo da `unconfirmed` a `disabled`. Mentre l'account utente è in uno di questi due ruoli, l'utente non può accedere. Il proprietario dell'albero deve esaminare la richiesta dell'utente e assegnare all'utente un ruolo appropriato prima che gli sia consentito accedere.
