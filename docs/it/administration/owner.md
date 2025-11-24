# Crea un account per il proprietario dell'albero

Prima di poter iniziare a utilizzare Gramps Web, è necessario creare un account per il proprietario dell'albero. Se non esiste alcun account utente per un determinato albero, verrà mostrato un modulo per creare un account. Il modulo dipende dalla configurazione del server, che può essere per un singolo albero o per più alberi.

## Configurazione a singolo albero: crea account admin

Su un server con configurazione a singolo albero, quando non esiste ancora alcun account utente, aprendo Gramps Web viene mostrato un modulo per creare un account admin. L'utente admin sarà sia il proprietario dell'albero (singolo) che l'amministratore dell'installazione. Il modulo consente anche di impostare la configurazione e-mail necessaria per le notifiche via e-mail (ad esempio, il ripristino di una password utente). Se la configurazione e-mail è già stata aggiunta tramite un file di configurazione o variabili d'ambiente sul server, questa parte del modulo può essere lasciata vuota.

## Configurazione multi-albero: crea account admin

In una configurazione multi-albero, verrà mostrato lo stesso modulo per creare un account admin se non esistono utenti *in alcun albero*, cioè quando il server è stato appena creato.

## Configurazione multi-albero: crea account proprietario dell'albero

In una configurazione multi-albero, ogni utente è legato a un singolo albero. Anche se gli utenti esistono già in altri alberi, un proprietario dell'albero può essere creato nell'interfaccia web se non esiste ancora alcun proprietario *per questo albero*.

Tuttavia, il modulo di creazione del proprietario non verrà visualizzato automaticamente nella home page di Gramps Web, che è la stessa per tutti gli alberi. Invece, può essere raggiunto all'indirizzo `https://my-gramps-instance/firstrun/my-tree-id`, dove `https://my-gramps-instance` è l'indirizzo base della tua installazione di Gramps Web e `my-tree-id` è l'ID del tuo albero.

Un possibile flusso di lavoro per un amministratore del sito per creare un nuovo albero è:

- Creare un albero tramite l'API REST, ottenendo l'ID dell'albero del nuovo albero
- Condividere il link al modulo di creazione del proprietario con l'ID dell'albero appropriato con il potenziale proprietario dell'albero

Il modulo di creazione del proprietario dell'albero è analogo al modulo di creazione dell'admin descritto sopra, tranne per il fatto che non consente di modificare la configurazione e-mail (che è consentita solo per gli admin).
