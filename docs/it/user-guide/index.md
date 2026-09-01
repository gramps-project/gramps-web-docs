---
hide:
  - toc
---

# Guida dell'utente

Questa sezione documenta le funzionalità disponibili per gli utenti di Gramps Web.

!!! note "Non vedi tutte le funzionalità?"
    Gramps Web utilizza un sistema di autorizzazioni basato sui ruoli. Alcune funzionalità – come la modifica dei dati, la gestione dei tag o la visualizzazione dei record privati – sono disponibili solo per gli utenti con autorizzazioni sufficienti. Puoi controllare il tuo ruolo attuale in [Impostazioni utente](settings.md). Se hai bisogno di maggiore accesso, contatta il proprietario del tuo albero o l'amministratore. Vedi [Sistema utenti](../install_setup/users.md) per una descrizione di tutti i ruoli.

## Navigare nell'interfaccia

### Navigazione principale

La barra laterale (o menu hamburger su mobile) è il modo principale per spostarsi tra le sezioni:

- **Home** – la dashboard (vedi sotto)
- **Blog** – storie di storia familiare scritte come post del blog
- **Albero genealogico** – grafici interattivi dell'albero
- **Cronologia** – vista cronologica degli eventi nell'albero (richiede una versione sufficientemente recente dell'API di Gramps Web)
- **Mappa** – vista geografica dei luoghi nell'albero
- **DNA** – strumenti di analisi delle corrispondenze del DNA
- **Elenco** – sfoglia tutti gli oggetti di ciascun tipo: Persone, Famiglie, Eventi, Luoghi, Fonti, Citazioni, Archivi, Note
- **Media** – sfoglia tutti i file multimediali (foto, documenti, ecc.)
- **Assistente** – assistente chat AI (se abilitato dall'amministratore)
- **Storia** – oggetti recentemente modificati
- **Segnalibri** – i tuoi segnalibri salvati
- **Attività** – attività di ricerca
- **Report** – genera report
- **Esporta** – esporta l'albero genealogico
- **Revisioni** – cronologia completa delle transazioni (visibile ai membri e superiori)
- **Notifiche** – notifiche passate

!!! note
    I tag non sono più gestiti dalla barra laterale – la gestione dei tag è stata spostata in [Impostazioni di amministrazione](../administration/settings.md#tags) (solo Proprietario/Amministratore). Vedi [Tag](tags.md) per come vengono utilizzati i tag.

### Barra dell'app in alto

La barra in cima a ogni pagina contiene:

- **Aggiungi** (icona del segno più, visibile ai collaboratori e superiori) – apre un menu per creare un nuovo oggetto: Persona, Famiglia, Evento, Luogo, Fonte, Citazione, Archivio, Nota, Oggetto multimediale o Attività
- **Cerca** (lente di ingrandimento) – apre la pagina di ricerca
- **Icona utente** – apre il menu delle impostazioni: Impostazioni utente, Amministrazione (solo per i proprietari), Gestisci utenti (solo per i proprietari), Informazioni di sistema

## La pagina iniziale (dashboard)

La dashboard viene mostrata quando accedi per la prima volta. Ha due colonne:

**Colonna sinistra:**

- **Scheda persona principale** – mostra il nome, la foto (se disponibile) e i fatti chiave della persona principale scelta, con un link al loro profilo completo e navigazione rapida all'albero genealogico. Clicca sul pulsante **Imposta persona principale** sulla scheda per cercare e selezionare un'altra persona.
- **Anniversari** – compleanni e anniversari imminenti dall'albero, basati sulla data odierna.
- **Recentemente modificati** – un breve elenco degli oggetti modificati più di recente, utile per tenere traccia delle modifiche collaborative.

**Colonna destra:**

- **Post recenti del blog** – le ultime voci dal [blog](blog.md), se esistono.
- **Statistiche** – un riepilogo dei conteggi degli oggetti nell'albero (numero di persone, famiglie, eventi, ecc.).

Se l'amministratore dell'albero ha configurato una **nota della pagina iniziale** e/o un **immagine della pagina iniziale**, queste vengono visualizzate in modo prominente sopra le colonne principali. L'immagine appare accanto al testo della nota quando entrambi sono impostati. Vedi [Impostazioni di amministrazione](../administration/settings.md#customization) per come configurare questi elementi.

!!! tip
    Se l'albero è vuoto e hai permessi di modifica, la dashboard mostra un messaggio "Inizia" con pulsanti per aggiungere la tua prima persona o importare un file dell'albero genealogico.

## Installare Gramps Web come app

Gramps Web è un'app web progressiva (PWA), il che significa che il tuo browser può installarla insieme alle altre applicazioni invece di tenerla in una scheda del browser. Ottiene quindi la sua icona e si apre in una finestra propria, senza la barra degli indirizzi e le barre degli strumenti del browser.

Come la installi dipende dal tuo browser:

- **Android (Chrome)** – apri il menu e scegli "Installa app" o "Aggiungi alla schermata principale".
- **iOS/iPadOS (Safari)** – tocca il pulsante di condivisione e scegli "Aggiungi alla schermata principale".
- **Desktop (Chrome, Edge)** – clicca sull'icona di installazione all'estremità destra della barra degli indirizzi, o usa l'entry "Installa" nel menu del browser.
- **Desktop (Firefox, Safari)** – l'installazione non è supportata; usa una normale scheda o finestra del browser.

Non cambia nulla su come funziona Gramps Web e nessun dato viene memorizzato in modo diverso – è la stessa applicazione, solo presentata come un'app autonoma.

!!! note
    Gramps Web deve comunque raggiungere il tuo server per mostrare i tuoi dati, quindi un'app installata non ti consente di navigare nel tuo albero genealogico offline.
