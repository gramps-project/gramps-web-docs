---
hide:
  - toc
---

# Guida dell'utente

Questa sezione documenta le funzionalità disponibili per gli utenti di Gramps Web.

!!! note "Non vedi tutte le funzionalità?"
    Gramps Web utilizza un sistema di permessi basato sui ruoli. Alcune funzionalità – come la modifica dei dati, la gestione dei tag o la visualizzazione di record privati – sono disponibili solo per gli utenti con permessi sufficienti. Puoi controllare il tuo ruolo attuale in [Impostazioni utente](settings.md). Se hai bisogno di maggior accesso, contatta il proprietario del tuo albero o l'amministratore. Vedi [Sistema utente](../install_setup/users.md) per una descrizione di tutti i ruoli.

## Navigare nell'interfaccia

### Navigazione principale

La barra laterale (o menu hamburger su mobile) è il modo principale per spostarsi tra le sezioni:

- **Home** – la dashboard (vedi sotto)
- **Blog** – storie di storia familiare scritte come post del blog
- **Albero genealogico** – grafici interattivi dell'albero
- **Cronologia** – vista cronologica degli eventi nell'albero (richiede una versione API di Gramps Web sufficientemente recente)
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

### Barra superiore dell'app

La barra in cima a ogni pagina contiene:

- **Aggiungi** (icona del più, visibile ai collaboratori e superiori) – apre un menu per creare un nuovo oggetto: Persona, Famiglia, Evento, Luogo, Fonte, Citazione, Archivio, Nota, Oggetto multimediale o Attività
- **Cerca** (lente di ingrandimento) – apre la pagina di ricerca
- **Icona utente** – apre il menu delle impostazioni: Impostazioni utente, Amministrazione (solo per i proprietari), Gestisci utenti (solo per i proprietari), Informazioni di sistema

## La pagina principale (dashboard)

La dashboard viene mostrata quando accedi per la prima volta. Ha due colonne:

**Colonna sinistra:**

- **Scheda persona principale** – mostra il nome, la foto (se disponibile) e i fatti chiave della persona principale scelta, con un link al loro profilo completo e navigazione rapida all'albero genealogico. Clicca sul pulsante **Imposta persona principale** sulla scheda per cercare e selezionare un'altra persona.
- **Anniversari** – compleanni e anniversari imminenti dall'albero, basati sulla data odierna.
- **Modifiche recenti** – un breve elenco degli oggetti modificati di recente, utile per tenere traccia delle modifiche collaborative.

**Colonna destra:**

- **Post recenti del blog** – le ultime voci dal [blog](blog.md), se esistono.
- **Statistiche** – un riepilogo dei conteggi degli oggetti nell'albero (numero di persone, famiglie, eventi, ecc.).

Se l'amministratore dell'albero ha configurato una **nota della pagina principale** e/o un **immagine della pagina principale**, queste vengono visualizzate in modo prominente sopra le colonne principali. L'immagine appare accanto al testo della nota quando entrambi sono impostati. Vedi [Impostazioni di amministrazione](../administration/settings.md#customization) per come configurare questi elementi.

!!! tip
    Se l'albero è vuoto e hai permessi di modifica, la dashboard mostra un messaggio "Inizia" con pulsanti per aggiungere la tua prima persona o importare un file di albero genealogico.
