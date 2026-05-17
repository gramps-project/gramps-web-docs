# Impostazioni utente

Le Impostazioni utente sono accessibili tramite l'icona dell'utente nella barra superiore dell'app, quindi **Impostazioni utente**. La pagina è organizzata in sezioni espandibili. Le modifiche hanno effetto immediato, salvo diversa indicazione.

!!! nota
    Le modifiche nelle Impostazioni utente influenzano solo il tuo account. Le impostazioni che influenzano tutti gli utenti dell'albero sono gestite nelle [Impostazioni di amministrazione](../administration/settings.md).

## Account

Copre le informazioni del tuo profilo, le credenziali e la sicurezza dell'account.

### Informazioni utente

Mostra il tuo **nome utente** e il **ruolo utente** attuale (ad es. Ospite, Membro, Editore). Questi sono in sola lettura.

### Cambia e-mail

Inserisci un nuovo indirizzo e-mail e fai clic su **Invia** per aggiornare l'indirizzo associato al tuo account. L'indirizzo e-mail viene utilizzato per il ripristino della password e (se configurato) per le notifiche.

### Cambia password

Inserisci la tua password attuale e una nuova password, quindi fai clic su **Invia**. Se hai dimenticato la tua password attuale, utilizza il link **Password dimenticata** nella pagina di accesso.

## Aspetto

Controlla le preferenze di visualizzazione salvate sul tuo dispositivo.

### Lingua

Seleziona la lingua per l'interfaccia web di Gramps. L'impostazione della lingua è memorizzata nel local storage del browser e si applica solo al dispositivo attuale.

### Tema

Scegli tra:

- **Sistema** – segue la preferenza chiara/scura del sistema operativo (predefinito)
- **Chiaro** – utilizza sempre il tema chiaro
- **Scuro** – utilizza sempre il tema scuro

L'impostazione del tema è memorizzata nel local storage del browser.

### Preferenze dell'albero genealogico

#### Vista predefinita dell'albero genealogico

Imposta quale tipo di grafico si apre per impostazione predefinita quando navighi alla pagina [Albero genealogico](tree.md). Le opzioni sono Albero degli antenati, Albero dei discendenti, Grafico a clessidra, Grafico delle relazioni e Grafico a ventaglio.

Questa preferenza è memorizzata nel local storage del browser.

## Strumenti per sviluppatori

### Token API

Copia il tuo token di sessione attuale negli appunti. Il token può essere utilizzato per autenticarsi direttamente contro l'API REST, ad esempio nell'interfaccia interattiva Swagger UI servita dalla tua istanza di Gramps Web su `/api/swagger-ui`.

Fai clic su **Avvia Swagger** per aprire l'interfaccia Swagger UI in una nuova scheda con la tua sessione già disponibile.

!!! nota
    Il token di sessione è di breve durata. Copialo immediatamente prima di utilizzarlo in Swagger, poiché potrebbe scadere.
