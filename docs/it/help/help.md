---
hide:
  - navigation
---

Se riscontri problemi o hai bisogno di aiuto con Gramps Web, ti preghiamo di scegliere una delle seguenti opzioni.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Problemi backend :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Problemi frontend :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Vedi di seguito alcune indicazioni su dove dirigerti per prima cosa.

## Porre domande

Il forum ufficiale di Gramps Discourse ha una [categoria separata per Gramps Web](https://gramps.discourse.group/c/gramps-web/). Ti preghiamo di utilizzarla per porre qualsiasi domanda tu possa avere su Gramps Web, ad esempio

- Domande sull'uso di Gramps Web
- Domande sulla configurazione di Gramps Web
- Risoluzione dei problemi di un'implementazione di Gramps Web
- Idee per miglioramenti a Gramps Web
- ...

## Segnalare problemi

Se incontri un problema che ritieni sia un bug in Gramps Web, ti preghiamo di segnalarlo tramite GitHub.

Ci sono due repository GitHub separati per il codice utilizzato in Gramps Web, uno per l'interfaccia utente (“frontend”) e uno per il codice del server (“backend”):

- [Problemi frontend](https://github.com/gramps-project/gramps-web/issues)
- [Problemi backend](https://github.com/gramps-project/gramps-web-api/issues)

Se non sei sicuro di dove segnalare un problema, non preoccuparti e scegli semplicemente uno dei due – i manutentori saranno in grado di trasferire il problema se necessario.

In entrambi i casi, ti preghiamo di includere sempre le seguenti informazioni nella tua segnalazione:

- Dettagli sulla tua configurazione (ad es. un file docker-compose con valori sensibili oscurati, o se stai utilizzando una versione ospitata, come Grampshub, o un'immagine preconfigurata, come DigitalOcean)
- Informazioni sulla versione. Per ottenerle, vai alla scheda "Informazioni di sistema" nella pagina delle impostazioni in Gramps Web e copia/incolla i valori nella casella, che dovrebbe apparire simile a questo:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: it
multi-tree: false
task queue: true
```

## Suggerire miglioramenti

Per idee generali e discussioni su futuri miglioramenti, sentiti libero di aprire una discussione nel [forum](https://gramps.discourse.group/c/gramps-web/). Potresti anche voler controllare le pagine dei problemi (vedi i link sopra) se una particolare funzionalità è già pianificata o in fase di sviluppo.

Per miglioramenti specifici con un ambito limitato, sentiti libero di aprire direttamente un problema con una richiesta di funzionalità nel repository GitHub frontend o backend appropriato.
