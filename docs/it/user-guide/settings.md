# Impostazioni utente

Le Impostazioni utente sono accessibili tramite l'icona dell'utente nella barra superiore dell'app, quindi **Impostazioni utente**. La pagina è organizzata in sezioni espandibili. Le modifiche hanno effetto immediato, a meno che non sia specificato diversamente.

!!! note
    Le modifiche nelle Impostazioni utente influenzano solo il tuo account. Le impostazioni che influenzano tutti gli utenti dell'albero sono gestite nelle [Impostazioni di amministrazione](../administration/settings.md).

## Account

Copre le informazioni del tuo profilo, le credenziali e la sicurezza dell'account.

### Informazioni utente

Mostra il tuo **nome utente** e il **ruolo utente** attuale (ad es. Ospite, Membro, Editore). Questi sono in sola lettura.

### Cambia e-mail

Inserisci un nuovo indirizzo e-mail e fai clic su **Invia** per aggiornare l'indirizzo associato al tuo account. L'indirizzo e-mail è utilizzato per il ripristino della password e (se configurato) per le notifiche.

### Cambia password

Inserisci la tua password attuale e una nuova password, quindi fai clic su **Invia**. Se hai dimenticato la tua password attuale, utilizza il link **Password dimenticata** nella pagina di accesso.

### Metodi di accesso collegati

Se il tuo server offre il single sign-on (vedi [autenticazione OIDC](../install_setup/oidc.md)), puoi collegare un account di un fornitore, come Google o il login della tua organizzazione, al tuo account Gramps Web. Puoi quindi accedere con quel fornitore e atterrare nel tuo account esistente, con il tuo ruolo e le tue modifiche. Questa sezione appare solo quando il single sign-on è abilitato e il server supporta il collegamento (Gramps Web API 3.24 e versioni successive).

Per collegare un account, fai clic su **Collega con** e il nome del fornitore, accedi presso il fornitore e verrai riportato alle tue impostazioni. Se non hai effettuato l'accesso di recente, ti verrà chiesto di accedere di nuovo prima.

Un account fornitore può essere collegato solo a un account Gramps Web. Se vedi "Questo accesso è già collegato a un altro account", è collegato altrove, ad esempio a un account che è stato creato quando hai effettuato l'accesso per la prima volta con quel fornitore. Un amministratore può eliminare quell'altro account, dopo di che puoi collegarlo al tuo.

Per scollegare un account, fai clic su **Scollega**. Se è il tuo ultimo metodo di accesso collegato, dovrai anche inserire la tua password, in modo da poter ancora accedere successivamente. Se il tuo account è stato creato tramite single sign-on e non hai mai impostato una password, utilizza **Password dimenticata** nella pagina di accesso per impostarne una prima (questo richiede che il server invii e-mail). Se il server consente solo l'accesso tramite un fornitore, l'ultimo account collegato non può essere scollegato.

## Aspetto

Controlla le preferenze di visualizzazione salvate sul tuo dispositivo.

### Lingua

Seleziona la lingua per l'interfaccia di Gramps Web. L'impostazione della lingua è memorizzata nella memoria locale del browser e si applica solo al dispositivo attuale.

### Tema

Scegli tra:

- **Sistema** – segue la preferenza chiaro/scuro del sistema operativo (predefinito)
- **Chiaro** – utilizza sempre il tema chiaro
- **Scuro** – utilizza sempre il tema scuro

L'impostazione del tema è memorizzata nella memoria locale del browser.

### Preferenze dell'albero genealogico

#### Vista predefinita dell'albero genealogico

Imposta quale tipo di grafico si apre per impostazione predefinita quando navighi alla pagina [Albero genealogico](tree.md). Le opzioni sono Albero degli antenati, Albero dei discendenti, Grafico a clessidra, Grafico delle relazioni e Grafico a ventaglio.

Questa preferenza è memorizzata nella memoria locale del browser.

## Strumenti per sviluppatori

### Token API

Copia il tuo token di sessione attuale negli appunti. Il token può essere utilizzato per autenticarsi direttamente contro l'API REST, ad esempio nell'interfaccia Swagger interattiva fornita dalla tua istanza di Gramps Web a `/api/swagger-ui`.

Fai clic su **Avvia Swagger** per aprire l'interfaccia Swagger in una nuova scheda con la tua sessione già disponibile.

!!! note
    Il token di sessione ha una durata limitata. Copialo immediatamente prima di utilizzarlo in Swagger, poiché potrebbe scadere.
