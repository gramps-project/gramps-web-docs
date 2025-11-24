# Configurazione dello sviluppo frontend

Questa pagina descrive i passaggi necessari per iniziare con lo sviluppo frontend.

## Requisiti

La configurazione di sviluppo consigliata utilizza Visual Studio Code con devcontainers. Questo approccio creerà un ambiente di sviluppo preconfigurato con tutti gli strumenti di cui hai bisogno.

Consulta [Configurazione dello sviluppo backend](../backend/setup.md#prerequisites) per i requisiti necessari.

## Iniziare

1. Apri il [repository frontend di Gramps Web](https://github.com/gramps-project/gramps-web) e clicca su "fork"
2. Clona il tuo repository forkato sulla tua macchina locale utilizzando Git
3. Apri il repository clonato in Visual Studio Code. Quando richiesto, seleziona "Reopen in Container" oppure apri manualmente il palette dei comandi (Ctrl+Shift+P o Cmd+Shift+P) e seleziona "Dev Containers: Rebuild and Reopen in Container".
4. Attendi che il dev container venga costruito e avviato. Questo potrebbe richiedere alcuni minuti, specialmente la prima volta.

## Esecuzione del server di sviluppo frontend

Per eseguire il server di sviluppo frontend e visualizzare l'impatto delle tue modifiche nel browser, puoi utilizzare i task predefiniti nel dev container.

Per farlo funzionare, devi prima avviare un'istanza del [backend API di Gramps Web](../backend/setup.md#tasks). Il modo più semplice per farlo è utilizzare il dev container del backend e [eseguire il task "Serve Web API"](../backend/setup.md#tasks) in una finestra separata di VS Code.

Una volta che il backend è in esecuzione, puoi avviare il server di sviluppo frontend selezionando "Tasks: Run Task" dal palette dei comandi (Ctrl+Shift+P o Cmd+Shift+P) e poi scegliendo "Serve Gramps Web frontend".

Questo avvierà il server di sviluppo frontend sulla porta 8001, a cui puoi accedere nel tuo browser all'indirizzo `http://localhost:8001`. Il browser si ricaricherà automaticamente quando apporti modifiche al codice frontend, permettendoti di vedere immediatamente l'impatto delle tue modifiche.
