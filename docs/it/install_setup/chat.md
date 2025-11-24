# Configurazione della chat AI

!!! info
    La chat AI richiede la versione 2.5.0 o superiore dell'API Web di Gramps.


L'API Web di Gramps supporta la possibilità di porre domande sul database genealogico utilizzando modelli di linguaggio di grandi dimensioni (LLM) tramite una tecnica chiamata generazione aumentata da recupero (RAG).

RAG funziona come segue. Prima, un *modello di embedding vettoriale* viene utilizzato per creare un indice di tutti gli oggetti nel database di Gramps sotto forma di vettori numerici che codificano il significato degli oggetti. Questo processo è simile alla creazione dell'indice di ricerca full-text, ma più costoso dal punto di vista computazionale.

Successivamente, quando un utente pone una domanda tramite l'endpoint della chat, anche quella domanda viene convertita in un vettore, dallo stesso modello di embedding, e confrontata con gli oggetti nel database di Gramps. Questa *ricerca semantica* restituirà oggetti nel database che sono semanticamente più simili alla domanda.

Nell'ultimo passaggio, la domanda e gli oggetti recuperati vengono inviati a un LLM per formulare una risposta basata sulle informazioni fornite. In questo modo, il chatbot ha accesso a informazioni dettagliate sui contenuti del database genealogico invece di fare affidamento esclusivamente su conoscenze preesistenti.

Per abilitare l'endpoint della chat nell'API Web di Gramps, sono necessari tre passaggi:

1. Installazione delle dipendenze richieste,
2. Abilitazione della ricerca semantica,
3. Configurazione di un fornitore LLM.

I tre passaggi sono descritti di seguito a turno. Infine, un proprietario o un amministratore deve [configurare quali utenti possono accedere alla funzione di chat](users.md#configuring-who-can-use-ai-chat) nelle impostazioni di gestione utenti.

## Installazione delle dipendenze richieste

La chat AI richiede che le librerie Sentence Transformers e PyTorch siano installate.

Le immagini Docker standard per Gramps Web le hanno già preinstallate per le architetture `amd64` (ad es. PC desktop a 64 bit) e `arm64` (ad es. Raspberry Pi a 64 bit). Sfortunatamente, la chat AI non è supportata sull'architettura `armv7` (ad es. Raspberry Pi a 32 bit) a causa della mancanza di supporto per PyTorch.

Quando si installa l'API Web di Gramps tramite `pip` (questo non è necessario quando si utilizzano le immagini Docker), le dipendenze necessarie vengono installate con

```bash
pip install gramps_webapi[ai]
```


## Abilitazione della ricerca semantica

Se le dipendenze necessarie sono installate, abilitare la ricerca semantica può essere semplice come impostare l'opzione di configurazione `VECTOR_EMBEDDING_MODEL` (ad es. impostando la variabile d'ambiente `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), vedere [Configurazione del server](configuration.md). Questo può essere qualsiasi stringa di un modello supportato dalla libreria [Sentence Transformers](https://sbert.net/). Consultare la documentazione di questo progetto per dettagli e modelli disponibili.


!!! warning
    Si noti che le immagini Docker predefinite non includono una versione di PyTorch con supporto GPU. Se hai accesso a una GPU (che accelererà significativamente l'indicizzazione semantica), ti preghiamo di installare una versione di PyTorch abilitata per GPU.

Ci sono diverse considerazioni da fare quando si sceglie un modello.

- Quando cambi il modello, devi ricreare manualmente l'indice di ricerca semantica per il tuo albero (o per tutti gli alberi in una configurazione multi-albero), altrimenti incontrerai errori o risultati privi di significato.
- I modelli sono un compromesso tra accuratezza/generalità da un lato e tempo di calcolo/spazio di archiviazione dall'altro. Se non stai eseguendo l'API Web di Gramps su un sistema che ha accesso a una potente GPU, modelli più grandi sono generalmente troppo lenti nella pratica.
- A meno che il tuo intero database non sia in inglese e tutti i tuoi utenti non siano previsti per porre domande in chat solo in inglese, avrai bisogno di un modello di embedding multilingue, che sono più rari rispetto ai modelli puramente inglesi.


Se il modello non è presente nella cache locale, verrà scaricato quando l'API Web di Gramps viene avviata per la prima volta con la nuova configurazione. Il modello `sentence-transformers/distiluse-base-multilingual-cased-v2` è già disponibile localmente quando si utilizzano le immagini Docker standard. Questo modello è un buon punto di partenza e supporta input multilingue.

Ti preghiamo di condividere le esperienze sui diversi modelli con la comunità!

!!! info
    La libreria sentence transformers consuma una quantità significativa di memoria, il che potrebbe causare l'uccisione dei processi worker. Come regola generale, con la ricerca semantica abilitata, ogni worker di Gunicorn consuma circa 200 MB di memoria e ogni worker di celery circa 500 MB di memoria anche quando inattivo, e fino a 1 GB quando calcola gli embedding. Vedi [Limitare l'uso della CPU e della memoria](cpu-limited.md) per le impostazioni che limitano l'uso della memoria. Inoltre, è consigliabile fornire una partizione di swap sufficientemente grande per prevenire errori OOM a causa di picchi transitori nell'uso della memoria.

## Configurazione di un fornitore LLM

La comunicazione con il LLM utilizza un'API compatibile con OpenAI tramite la libreria `openai-python`. Questo consente di utilizzare un LLM distribuito localmente tramite Ollama (vedi [Compatibilità di Ollama con OpenAI](https://ollama.com/blog/openai-compatibility)) o un'API come OpenAI o Hugging Face TGI (Text Generation Inference). Il LLM è configurato tramite i parametri di configurazione `LLM_MODEL` e `LLM_BASE_URL`.


### Utilizzo di un LLM ospitato tramite l'API OpenAI

Quando si utilizza l'API OpenAI, `LLM_BASE_URL` può essere lasciato non impostato, mentre `LLM_MODEL` deve essere impostato su uno dei modelli OpenAI, ad es. `gpt-4o-mini`. Si noti che, a causa dell'approccio RAG, il LLM è "solo" utilizzato per selezionare le informazioni corrette dai risultati della ricerca semantica e formulare una risposta, non richiede una profonda conoscenza genealogica o storica. Pertanto, puoi provare se un modello piccolo/economico è sufficiente.

Dovrai anche registrarti per un account, ottenere una chiave API e memorizzarla nella variabile d'ambiente `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` è un parametro di configurazione; se desideri impostarlo tramite una variabile d'ambiente, utilizza `GRAMPSWEB_LLM_MODEL` (vedi [Configurazione](configuration.md)). `OPENAI_API_KEY` non è un parametro di configurazione ma una variabile d'ambiente utilizzata direttamente dalla libreria `openai-python`, quindi non dovrebbe essere preceduta da alcun prefisso.


### Utilizzo di un LLM locale tramite Ollama

[Ollama](https://ollama.com/) è un modo conveniente per eseguire LLM localmente. Ti preghiamo di consultare la documentazione di Ollama per ulteriori dettagli. Si prega di notare che gli LLM richiedono risorse computazionali significative e tutti tranne i modelli più piccoli saranno probabilmente troppo lenti senza supporto GPU. Puoi provare se [`tinyllama`](https://ollama.com/library/tinyllama) soddisfa le tue esigenze. In caso contrario, prova uno dei modelli più grandi. Ti preghiamo di condividere eventuali esperienze con la comunità!

Quando distribuisci Gramps Web con Docker Compose, puoi aggiungere un servizio Ollama

```yaml
services:
  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
    ollama_data:
```

e poi impostare il parametro di configurazione `LLM_BASE_URL` su `http://ollama:11434/v1`. Imposta `LLM_MODEL` su un modello supportato da Ollama e scaricalo nel tuo container con `ollama pull <model>`. Infine, imposta `OPENAI_API_KEY` su `ollama`.

Per risolvere problemi con Ollama, puoi abilitare il logging di debug impostando la variabile d'ambiente `OLLAMA_DEBUG=1` nell'ambiente del servizio Ollama.

!!! info
    Se stai utilizzando Ollama per la chat AI di Gramps Web, ti preghiamo di supportare la comunità completando questa documentazione con eventuali dettagli mancanti.

### Utilizzo di altri fornitori

Sentiti libero di inviare documentazione per altri fornitori e condividere la tua esperienza con la comunità!
