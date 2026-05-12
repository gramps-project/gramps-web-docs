# Gestire gli Utenti

L'interfaccia di gestione degli utenti è accessibile tramite **Impostazioni > Gestisci Utenti** (l'icona dell'utente nella barra superiore dell'app). È disponibile solo per gli utenti con il ruolo di Proprietario o Amministratore.

## Ruoli degli utenti

Consulta il [Sistema degli utenti](../install_setup/users.md) per una descrizione completa dei ruoli utente disponibili e delle loro autorizzazioni.

## Visualizza e filtra gli utenti

La pagina di gestione degli utenti mostra una tabella di tutti gli account utente registrati con le seguenti colonne:

- **Nome utente** – il nome di accesso
- **Nome completo** – il nome visualizzato
- **E-mail** – l'indirizzo e-mail dell'utente
- **Ruolo** – il ruolo assegnato (Ospite, Membro, Collaboratore, Editore, Proprietario o Amministratore)
- **Fonte dell'account** – "Password" (account locale) o il nome di un fornitore di identità esterno (ad es. quando si utilizza OIDC)

Utilizza il campo di ricerca e il menu a discesa dei ruoli in cima alla tabella per filtrare l'elenco. Clicca sul pulsante per cancellare i filtri per ripristinare tutti i filtri.

## Modifica un utente

Clicca sull'icona di modifica (matita) in qualsiasi riga per aprire la finestra di dialogo di modifica. Puoi cambiare:

- Nome completo
- Indirizzo e-mail
- Ruolo

Questo è il modo principale per **abilitare un nuovo utente auto-registrato**: cambia il loro ruolo da *disabilitato* a qualsiasi ruolo attivo (ad es. Membro o Editore).

## Aggiungi un utente manualmente

Clicca sull'icona **aggiungi utente** (persona-aggiungi) sopra la tabella per creare un nuovo account utente direttamente senza richiedere auto-registrazione. Compila il nome utente, il nome completo, l'indirizzo e-mail, la password e il ruolo nella finestra di dialogo e clicca su **Salva**.

## Elimina un utente

Clicca sull'icona di eliminazione (cestino) in qualsiasi riga e conferma nella finestra di dialogo. Questa azione non può essere annullata.

## Esporta e importa account utente

Questi pulsanti sono utili quando si [migra a un'istanza Gramps Web diversa](export.md).

- **Esporta dettagli utente** (icona di download) – scarica un file JSON contenente tutti gli account utente (senza password, poiché le password sono memorizzate in forma crittografata).
- **Importa account utente** (icona di gruppo-aggiungi) – carica un file JSON precedentemente esportato per creare account utente in blocco. Tutti gli utenti importati dovranno impostare una nuova password tramite il link "Password dimenticata", poiché le password non possono essere trasferite.

## Link di registrazione (solo configurazione multi-albero)

In una configurazione multi-albero, il link di registrazione per i nuovi utenti è mostrato in cima alla pagina di gestione degli utenti. Puoi copiare questo link e condividerlo con le persone che desideri invitare a registrare un account sul tuo albero.

!!! nota
    In una configurazione a singolo albero c'è un link generico "Registrati" nella pagina di accesso; il link di registrazione per albero è necessario solo nelle installazioni multi-albero.

## Autorizzazioni chat AI

Se la chat AI è stata abilitata sul server, un menu a discesa in cima alla pagina ti consente di controllare quali ruoli utente possono utilizzare la funzione di chat:

- Tutti (inclusi gli ospiti)
- Membro e superiore
- Collaboratore e superiore
- Editore e superiore
- Solo proprietari e amministratori
- Nessuno (disabilita la chat per tutti gli utenti)
