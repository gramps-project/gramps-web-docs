# Personalizza l'albero

I proprietari e gli amministratori dell'albero possono adattare il nome e l'aspetto dell'albero, così come la sua home page, per tutti gli utenti. Queste impostazioni si trovano nelle sezioni **Impostazioni dell'albero** e **Personalizzazione** delle [Impostazioni di amministrazione](settings.md).

## Nome dell'albero genealogico

!!! note
    Rinominare l'albero funziona solo in una [configurazione multi-albero](../install_setup/multi-tree.md) o quando `TREE_ID` è esplicitamente impostato nella [configurazione del server](../install_setup/configuration.md). In un'installazione predefinita a singolo albero senza `TREE_ID` impostato, questo genererà un errore.

Questo consente di cambiare il nome del database sottostante dell'albero genealogico di Gramps. Inserisci un nuovo nome e fai clic su **Rinomina** per applicare.

!!! tip
    Se desideri solo cambiare il nome visualizzato nella barra dell'app senza rinominare il database, utilizza invece l'impostazione [Titolo dell'app](#app-title).

## Informazioni sul ricercatore

Imposta il nome, l'indirizzo e i dettagli di contatto del ricercatore principale. Queste informazioni sono incorporate nelle esportazioni (ad es. file GEDCOM).

## Colori del tema

Imposta un **colore primario** e un **colore d'accento** personalizzati per l'interfaccia web di Gramps. Questi colori vengono applicati a tutti gli utenti di questo albero e hanno effetto immediato dopo il salvataggio.

Utilizza i selettori di colore per scegliere i colori, quindi fai clic su **Salva**. Fai clic su **Ripristina** per tornare ai valori predefiniti.

## Titolo dell'app

Imposta un titolo personalizzato per l'applicazione. Se impostato, questo sovrascrive il nome dell'albero genealogico nella barra del titolo del browser e nella barra superiore dell'app.

Inserisci un titolo e fai clic su **Salva**. Lascia vuoto per utilizzare il predefinito (il nome dell'albero genealogico).

## Nota della home page

Seleziona un oggetto **Nota** di Gramps da visualizzare sulla home page del dashboard. Il contenuto della nota viene visualizzato sotto le colonne principali del dashboard ed è visibile a tutti gli utenti con accesso all'albero.

Utilizza il selettore di oggetti per cercare e scegliere una nota, quindi salva. Fai clic su **Rimuovi** per cancellare l'attuale nota della home page.

## Immagine della home page

Seleziona un oggetto **Media** di Gramps da visualizzare come immagine sulla home page del dashboard. Quando combinato con una nota della home page, l'immagine appare accanto al testo della nota. Senza una nota, viene mostrata solo l'immagine.

Utilizza il selettore di oggetti per cercare e scegliere un oggetto multimediale, quindi salva. Fai clic su **Rimuovi** per cancellare l'attuale immagine della home page.

## Impostazioni di esportazione/importazione

Le impostazioni a livello di albero (titolo dell'app, colori del tema, nota/immagine della home page, ecc.) possono essere esportate come file JSON per backup o per copiare in un'altra istanza di Gramps Web.

- Fai clic su **Esporta impostazioni** per scaricare le impostazioni attuali come file JSON.
- Fai clic su **Importa impostazioni dell'albero** per caricare un file JSON precedentemente esportato e applicare le impostazioni.
