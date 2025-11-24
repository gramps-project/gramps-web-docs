# Telemetria

A partire dalla versione 3.2.0 dell'API Web di Gramps, Gramps Web invia per impostazione predefinita dati di telemetria completamente anonimizzati ogni 24 ore a un endpoint di analisi controllato dal team di Gramps Web. Questa pagina contiene informazioni sui dati di telemetria raccolti, su come vengono utilizzati e su come disabilitarli se desiderato.

## Quali dati vengono raccolti?

I dati di telemetria sono un piccolo payload JSON della seguente forma:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Come puoi verificare [nel codice sorgente](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87), gli identificatori del server e dell'albero sono unici per il server e l'albero, ma non contengono alcuna informazione personale identificabile. Il `timestamp` è l'ora corrente come timestamp Unix.

## Perché vengono raccolti i dati?

Inviare un identificatore unico una volta al giorno consente al team di Gramps Web di monitorare quanti server unici stanno eseguendo Gramps Web e quanti alberi unici vengono utilizzati.

Questo è importante per comprendere l'impatto sui servizi esterni utilizzati da Gramps Web, come le mappe.

## Come vengono raccolti i dati?

Quando viene effettuata una richiesta al tuo server API di Gramps Web, verifica se la telemetria è stata inviata nelle ultime 24 ore (controllando una chiave nella cache locale). Se non è stato fatto, il payload sopra viene inviato a un endpoint che registra i dati.

L'endpoint di registrazione è ospitato su Google Cloud Run ed è direttamente distribuito da un [repository open source](https://github.com/DavidMStraub/cloud-run-telemetry), quindi puoi ispezionare come vengono elaborati i dati.

## Cosa verrà fatto con i dati?

Prima di tutto, nessun dato oltre al payload anonimizzato, che potrebbe ipoteticamente essere raccolto (come l'indirizzo IP del server), sarà utilizzato dal team di Gramps Web.

Gli ID anonimizzati raccolti e il timestamp saranno aggregati per produrre grafici come:

- Numero di installazioni attive di Gramps Web in funzione del tempo
- Numero di alberi attivi di Gramps Web in funzione del tempo

Questi grafici saranno pubblicati sul sito di documentazione di Gramps Web.

## Come disabilitare la telemetria?

Poiché i dati statistici sono utili per il team di Gramps Web e abbiamo garantito che non vengano inviati dati personali identificabili, **saremmo grati se non disabilitassi la telemetria!**

Tuttavia, Gramps Web mette gli utenti completamente sotto controllo, quindi ovviamente puoi scegliere di disabilitare la funzione se lo desideri.

Per farlo, basta impostare l'opzione di configurazione `DISABLE_TELEMETRY` su `True` (ad esempio impostando la variabile d'ambiente `GRAMPSWEB_DISABLE_TELEMETRY` su `true` &ndash; consulta la [documentazione di configurazione](configuration.md) per dettagli).
