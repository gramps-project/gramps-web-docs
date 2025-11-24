# Impostazione dello sviluppo backend

Questa pagina elenca i passaggi necessari per iniziare a sviluppare [Gramps Web API](https://github.com/gramps-project/gramps-web-api/), il backend (componente server) di Gramps Web.


## Requisiti

L'impostazione di sviluppo consigliata utilizza Visual Studio Code con devcontainers. Questo approccio creerà un ambiente di sviluppo preconfigurato con tutti gli strumenti necessari. Per iniziare, avrai bisogno dei seguenti ingredienti:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) con l'estensione [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installata
- [Git](https://git-scm.com)

Puoi utilizzare Linux, macOS o Windows come sistema operativo.


## Iniziare

1. Apri il [repository Gramps Web API](https://github.com/gramps-project/gramps-web-api) e fai clic su "fork"
2. Clona il tuo repository forkato sulla tua macchina locale utilizzando Git
3. Apri il repository clonato in Visual Studio Code. Quando richiesto, seleziona "Reopen in Container" oppure apri manualmente il palette dei comandi (Ctrl+Shift+P o Cmd+Shift+P) e seleziona "Dev Containers: Rebuild and Reopen in Container".
4. Attendi che il dev container venga costruito e avviato. Questo potrebbe richiedere alcuni minuti, specialmente la prima volta.


## Attività

Se stai modificando solo il codice backend, non è necessario avviare un server web - i test unitari utilizzano un client di test Flask che consente di simulare richieste all'API senza la necessità di un server in esecuzione.

Tuttavia, eseguire un server è utile se

- vuoi provare le tue modifiche con richieste HTTP reali (vedi [query manuali](queries.md)), 
- vuoi visualizzare l'impatto delle modifiche sull'intera applicazione Gramps Web, o
- vuoi anche apportare modifiche simultanee al frontend (vedi [impostazione dello sviluppo frontend](../frontend/setup.md)).

L'esecuzione del server è semplificata nel dev container da attività predefinite. Puoi eseguire queste attività dal palette dei comandi (Ctrl+Shift+P o Cmd+Shift+P) selezionando "Tasks: Run Task" e poi scegliendo una delle seguenti:
- "Serve Web API" - avvia il server di sviluppo Flask sulla porta 5555 con il logging di debug abilitato
- "Start Celery worker" - avvia un worker Celery per elaborare attività in background.


## Debugging

Il debugging può essere a volte impegnativo, specialmente quando si cerca di tracciare comportamenti complessi o identificare problemi sottili. Per semplificare questo processo, puoi eseguire il debug sia di un'istanza API in esecuzione che di singoli casi di test direttamente all'interno di Visual Studio Code.

### Debugging della Gramps Web API

Per eseguire il debug dell'API in esecuzione:

1. Apri Visual Studio Code e vai alla vista **Esegui e Debug**.  
2. Seleziona la configurazione **"Web API"** dal menu a discesa.  
3. Inizia il debugging.  
4. Quando invii richieste al backend (sia manualmente che tramite l'interfaccia grafica di Gramps Web), l'esecuzione si fermerà a qualsiasi punto di interruzione impostato nel codice.  
   Questo ti consente di ispezionare variabili, flusso di controllo e altri dettagli di runtime.

### Debugging dei Casi di Test

Per eseguire il debug di un caso di test specifico:

1. Apri il file di test che desideri eseguire in debug (ad esempio, `test_people.py`).  
2. In Visual Studio Code, apri la vista **Esegui e Debug**.  
3. Scegli la configurazione **"Current Test File"**.  
4. Inizia il debugging — l'esecuzione si fermerà a qualsiasi punto di interruzione impostato all'interno di quel file di test.  

Questa configurazione ti consente di eseguire il passo attraverso la logica del test, esaminare i valori delle variabili e comprendere meglio i fallimenti dei test o i risultati inaspettati.
