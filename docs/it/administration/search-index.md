# Indice di ricerca

La sezione **Indice di ricerca** delle [Impostazioni di amministrazione](settings.md) mostra lo stato dell'indice di ricerca full-text e consente di ricostruirlo.

## Gestisci indice di ricerca

Gramps Web mantiene un indice di ricerca full-text che viene normalmente aggiornato automaticamente ogni volta che i dati cambiano. L'indicatore di stato mostra quanti oggetti sono attualmente indicizzati rispetto al conteggio totale degli oggetti.

Clicca su **Aggiorna indice di ricerca** per attivare una ricostruzione completa. Un indicatore di progresso viene mostrato mentre il compito viene eseguito in background. Questo è raramente necessario.

Se un albero non ha ancora un indice di ricerca, ad esempio dopo un aggiornamento del server che ha cambiato il formato dell'indice, Gramps Web lo costruisce in background la prima volta che l'albero viene aperto. Mentre viene costruito, la sezione mostra "L'indice di ricerca è in fase di costruzione." invece dei conteggi, **Aggiorna indice di ricerca** è disabilitato e i risultati della ricerca potrebbero essere incompleti. La costruzione appare nelle [Notifiche](../user-guide/notifications.md) come il compito "Aggiorna indice di ricerca".
