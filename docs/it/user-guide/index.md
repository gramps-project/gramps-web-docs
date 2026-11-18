---
hide:
  - toc
---

# Guida dell'utente

Questa sezione documenta le funzionalità disponibili per gli utenti di Gramps Web.

!!! note "Non vedi tutte le funzionalità?"
    Gramps Web utilizza un sistema di autorizzazioni basato sui ruoli. Alcune funzionalità – come la modifica dei dati, la gestione delle etichette o la visualizzazione di registri privati – sono disponibili solo per gli utenti con autorizzazioni sufficienti. Puoi controllare il tuo ruolo attuale in [Impostazioni utente](settings.md). Se hai bisogno di maggiori accessi, contatta il proprietario del tuo albero o l'amministratore. Vedi [Sistema utenti](../install_setup/users.md) per una descrizione di tutti i ruoli.

## Navigare nell'interfaccia

### Navigazione principale

La barra laterale (o menu hamburger su mobile) è il modo principale per muoversi tra le sezioni:

- **Home** – la dashboard (vedi sotto)
- **Blog** – storie di storia familiare scritte come post del blog
- **Albero genealogico** – grafici ad albero interattivi
- **Cronologia** – visualizzazione cronologica degli eventi nell'albero (richiede una versione sufficientemente recente dell'API Gramps Web)
- **Mappa** – visualizzazione geografica dei luoghi nell'albero
- **DNA** – strumenti di analisi delle corrispondenze del DNA
- **Elenco** – esplora tutti gli oggetti di ciascun tipo: Persone, Famiglie, Eventi, Luoghi, Fonti, Citazioni, Repositories, Note
- **Media** – esplora tutti i file multimediali (foto, documenti, ecc.)
- **Assistente** – assistente chat AI (se abilitato dall'amministratore)
- **Storia** – oggetti recentemente modificati
- **Segnalibri** – i tuoi segnalibri salvati
- **Attività** – attività di ricerca
- **Report** – genera report
- **Esporta** – esporta l'albero genealogico
- **Revisioni** – cronologia completa delle transazioni (visibile ai membri e superiori)

!!! note
    Le etichette non sono più gestite dalla barra laterale – la gestione delle etichette è stata spostata in [Impostazioni di amministrazione](../administration/settings.md#tags) (solo Proprietario/Amministratore). Vedi [Etichette](tags.md) per come vengono utilizzate le etichette.

### Barra superiore dell'app

La barra in cima a ogni pagina contiene:

- **Aggiungi** (icona del più, visibile ai collaboratori e superiori) – apre un menu per creare un nuovo oggetto: Persona, Famiglia, Evento, Luogo, Fonte, Citazione, Repository, Nota, Oggetto multimediale o Attività
- **Cerca** (lente d'ingrandimento) – apre la pagina di ricerca
- **Campana** – apre le [notifiche](notifications.md), inclusi i cambiamenti da parte di altri utenti e i compiti in background completati
- **Icona utente** – apre il menu delle impostazioni: Impostazioni utente, Amministrazione (solo per i proprietari), Gestisci utenti (solo per i proprietari), Informazioni di sistema

## La pagina principale (dashboard)

La dashboard viene mostrata quando accedi per la prima volta. Ha due colonne:

**Colonna sinistra:**

- **Scheda persona principale** – mostra il nome, la foto (se disponibile) e i fatti chiave della persona principale scelta, con un link al loro profilo completo e navigazione rapida all'albero genealogico. Clicca sul pulsante **Imposta persona principale** sulla scheda per cercare e selezionare un'altra persona.
- **Anniversari** – compleanni e anniversari imminenti dall'albero, basati sulla data odierna.
- **Modifiche recenti** – un breve elenco degli oggetti modificati più di recente, utile per tenere traccia delle modifiche collaborative.

**Colonna destra:**

- **Post recenti del blog** – le ultime voci dal [blog](blog.md), se ce ne sono.
- **Statistiche** – un riepilogo dei conteggi degli oggetti nell'albero (numero di persone, famiglie, eventi, ecc.).

Mentre l'albero è ancora vuoto, la dashboard nasconde i pannelli che non avrebbero nulla da mostrare e invece visualizza una scheda **Inizia** per gli utenti con permessi di modifica: offre prima di creare una persona o importare un file di albero genealogico, e una volta che esistono persone, di collegarle creando una famiglia. La scheda scompare non appena l'albero contiene una famiglia.

Se l'amministratore dell'albero ha configurato una **nota della pagina principale** e/o un **immagine della pagina principale**, queste vengono visualizzate in modo prominente sopra le colonne principali. L'immagine appare accanto al testo della nota quando entrambe sono impostate. Vedi [Impostazioni di amministrazione](../administration/customization.md) per come configurarle.

!!! tip
    Se l'albero è vuoto e hai permessi di modifica, la dashboard mostra un messaggio "Inizia" con pulsanti per aggiungere la tua prima persona o importare un file di albero genealogico.

## Installare Gramps Web come app

Gramps Web è un'app web progressiva (PWA), il che significa che il tuo browser può installarla insieme alle tue altre applicazioni invece di tenerla in una scheda del browser. Ottiene quindi la sua icona e si apre in una propria finestra, senza la barra degli indirizzi e le barre degli strumenti del browser.

Come la installi dipende dal tuo browser:

- **Android (Chrome)** – apri il menu e scegli "Installa app" o "Aggiungi alla schermata principale".
- **iOS/iPadOS (Safari)** – tocca il pulsante di condivisione e scegli "Aggiungi alla schermata principale".
- **Desktop (Chrome, Edge)** – clicca sull'icona di installazione all'estremità destra della barra degli indirizzi, o usa l'entrata "Installa" nel menu del browser.
- **Desktop (Firefox, Safari)** – l'installazione non è supportata; usa una normale scheda o finestra del browser.

Nulla cambia nel modo in cui funziona Gramps Web e nessun dato viene memorizzato in modo diverso – è la stessa applicazione, semplicemente presentata come un'app autonoma.

!!! note
    Gramps Web ha ancora bisogno di raggiungere il tuo server per mostrare i tuoi dati, quindi un'app installata non ti consente di navigare nel tuo albero genealogico offline.
