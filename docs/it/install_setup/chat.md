# Impostare la chat AI

!!! info
    La chat AI richiede Gramps Web API versione 2.5.0 o superiore. La versione 3.6.0 ha introdotto capacità di chiamata degli strumenti per interazioni più intelligenti.

Gramps Web API supporta la possibilità di porre domande sul database genealogico utilizzando modelli di linguaggio di grandi dimensioni (LLM) con chiamata degli strumenti.

## Come funziona

L'assistente AI utilizza strumenti specializzati per interrogare direttamente i tuoi dati genealogici. Questi strumenti consentono all'assistente di cercare nel database con la ricerca full-text, filtrare persone/eventi/famiglie/luoghi in base a criteri specifici, calcolare relazioni tra individui e recuperare record completi, comprese le note. L'assistente quindi risponde in base ai record che ha consultato e fornisce collegamenti ad essi nella sua risposta.

Dalla versione 3.24 di Gramps Web API, la chat AI non richiede più un modello di embedding vettoriale. Le versioni precedenti utilizzavano anche la *ricerca semantica* (generazione aumentata da recupero, RAG), che confronta il significato di una domanda con un indice di vettori numerici calcolati per tutti gli oggetti nel database. La ricerca semantica è deprecata e sarà rimossa nella versione 3.25 di Gramps Web API, vedere [Ricerca semantica (deprecata)](#semantic-search-deprecated) qui sotto.

Per abilitare l'endpoint della chat in Gramps Web API, sono necessari due passaggi:

1. Installare le dipendenze richieste,
2. Configurare un fornitore LLM.

I due passaggi sono descritti di seguito a turno. Infine, un proprietario o un amministratore deve [configurare quali utenti possono accedere alla funzione di chat](users.md#configuring-who-can-use-ai-chat) nelle impostazioni di gestione utenti.

## Installazione delle dipendenze richieste

Le immagini docker standard per Gramps Web hanno già tutte le dipendenze necessarie per la chat AI pre-installate.

Quando si installa Gramps Web API tramite `pip` (questo non è necessario quando si utilizzano le immagini Docker), le dipendenze necessarie vengono installate con

```bash
pip install gramps_webapi[ai]
```

## Ricerca semantica (deprecata)

!!! warning "La ricerca semantica è deprecata"
    La ricerca semantica è deprecata dalla versione 3.24 di Gramps Web API e sarà rimossa nella versione 3.25. La chat AI e la [ricerca full-text](../user-guide/search.md) non la richiedono. Dopo la rimozione, l'impostazione `VECTOR_EMBEDDING_MODEL` sarà ancora accettata ma ignorata. Se la imposti solo per abilitare la chat AI, puoi rimuoverla ora, insieme alle altre impostazioni `VECTOR_EMBEDDING_*`, il che salva anche la memoria necessaria per il modello di embedding.

Il resto di questa sezione descrive la ricerca semantica per i server che la utilizzano ancora con Gramps Web API 3.24.

Se le dipendenze necessarie sono installate, abilitare la ricerca semantica può essere semplice come impostare l'opzione di configurazione `VECTOR_EMBEDDING_MODEL` (ad esempio impostando la variabile ambiente `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), vedere [Configurazione del server](configuration.md). Questo può essere qualsiasi stringa di un modello supportato dalla libreria [Sentence Transformers](https://sbert.net/). Vedi la documentazione di questo progetto per dettagli e modelli disponibili.

!!! warning
    Nota che le immagini docker predefinite non includono una versione di PyTorch con supporto GPU. Se hai accesso a una GPU (che accelererà significativamente l'indicizzazione semantica), ti preghiamo di installare una versione di PyTorch abilitata per GPU.

Ci sono diverse considerazioni da fare quando si sceglie un modello.

- Quando cambi il modello, devi ricreare manualmente l'indice di ricerca semantica per il tuo albero (o per tutti gli alberi in una configurazione multi-albero), altrimenti incontrerai errori o risultati privi di significato. Gramps Web rileva quando il modello di embedding configurato non corrisponde più all'indice esistente e mostra una notifica persistente agli amministratori che li invita a attivare un reindicizzazione completa da [Impostazioni di amministrazione](../administration/settings.md#semantic-search-index).
- I modelli sono un compromesso tra accuratezza/generalità da un lato e tempo di calcolo/spazio di archiviazione dall'altro. Se non stai eseguendo Gramps Web API su un sistema che ha accesso a una potente GPU, i modelli più grandi sono generalmente troppo lenti in pratica.
- A meno che l'intero database non sia in inglese e tutti i tuoi utenti non siano previsti per porre domande in chat solo in inglese, avrai bisogno di un modello di embedding multilingue, che è più raro rispetto ai modelli puramente inglesi.

Se il modello non è presente nella cache locale, verrà scaricato quando Gramps Web API viene avviato per la prima volta con la nuova configurazione. Il modello `sentence-transformers/distiluse-base-multilingual-cased-v2` è già disponibile localmente quando si utilizzano le immagini docker standard. Questo modello è un buon punto di partenza e supporta input multilingue.

Ti preghiamo di condividere le esperienze sui diversi modelli con la comunità!

!!! info
    La libreria sentence transformers consuma una quantità significativa di memoria, il che potrebbe causare l'uccisione dei processi worker. Come regola generale, con la ricerca semantica abilitata, ogni worker Gunicorn consuma circa 200 MB di memoria e ogni worker celery circa 500 MB di memoria anche quando inattivo, e fino a 1 GB quando calcola gli embedding. Vedi [Limitare l'uso della CPU e della memoria](cpu-limited.md) per le impostazioni che limitano l'uso della memoria. Inoltre, è consigliabile prevedere una partizione di swap sufficientemente grande per prevenire errori OOM a causa di picchi temporanei nell'uso della memoria.

### Utilizzare un'API di embedding remota

Come alternativa all'esecuzione di un modello Sentence Transformers locale, puoi utilizzare un'API di embedding remota compatibile con OpenAI per la ricerca semantica. Questo è utile se desideri scaricare il calcolo degli embedding a un servizio separato (ad esempio, [Ollama](https://ollama.com/)), utilizzare un fornitore di embedding cloud (ad esempio OpenAI) o evitare di caricare le librerie Sentence Transformers e PyTorch in memoria.

L'API remota deve essere compatibile con l'[endpoint di embedding di OpenAI](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`).

Per utilizzare un'API di embedding remota, imposta le seguenti opzioni di configurazione (vedi [Configurazione del server](configuration.md)):

Chiave | Descrizione
----|-------------
`VECTOR_EMBEDDING_MODEL` | Il nome del modello da passare al fornitore remoto
`VECTOR_EMBEDDING_BASE_URL` | URL di base dell'API remota
`VECTOR_EMBEDDING_API_KEY` | Chiave API (necessaria solo se il fornitore richiede autenticazione)

#### Utilizzare Ollama per gli embedding

Quando distribuisci Gramps Web con Docker Compose, puoi aggiungere un servizio Ollama e utilizzarlo sia per gli embedding che (opzionalmente) per il LLM:

```yaml
services:
  grampsweb: &grampsweb
    # ... configurazione esistente ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... configurazione esistente ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

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

Dopo aver avviato i servizi, scarica il modello di embedding in Ollama:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Quando utilizzi Ollama per gli embedding, le librerie Sentence Transformers e PyTorch non sono necessarie, il che riduce significativamente l'uso della memoria dei worker di Gramps Web API.

#### Utilizzare OpenAI per gli embedding

Per utilizzare l'API di embedding di OpenAI, imposta l'URL di base sull'API di OpenAI e fornisci la tua chiave API:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Cambiare il modello di embedding richiede di reindicizzare tutti i record per il tuo albero (o per tutti gli alberi in una configurazione multi-albero), poiché modelli diversi producono vettori con dimensioni diverse.

## Impostare un fornitore LLM

La comunicazione con il LLM utilizza il framework Pydantic AI, che supporta API compatibili con OpenAI. Questo consente di utilizzare un LLM distribuito localmente tramite Ollama (vedi [Compatibilità di Ollama con OpenAI](https://ollama.com/blog/openai-compatibility)) o API ospitate come OpenAI, Anthropic o Hugging Face TGI (Text Generation Inference). Il LLM è configurato tramite i parametri di configurazione `LLM_MODEL` e `LLM_BASE_URL`.

### Utilizzare un LLM ospitato tramite l'API di OpenAI

Quando utilizzi l'API di OpenAI, `LLM_BASE_URL` può essere lasciato non impostato, mentre `LLM_MODEL` deve essere impostato su uno dei modelli OpenAI, ad esempio `gpt-4o-mini`. Il LLM utilizza la chiamata degli strumenti per rispondere alle domande: interroga direttamente il database utilizzando strumenti specializzati e risponde in base ai record che trova. Non richiede una profonda conoscenza genealogica o storica. Pertanto, puoi provare se un modello piccolo/economico è sufficiente.

Dovrai anche registrarti per un account, ottenere una chiave API e memorizzarla nella variabile ambiente `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` è un parametro di configurazione; se desideri impostarlo tramite una variabile ambiente, utilizza `GRAMPSWEB_LLM_MODEL` (vedi [Configurazione](configuration.md)). `OPENAI_API_KEY` non è un parametro di configurazione ma una variabile ambiente utilizzata direttamente dalla libreria Pydantic AI, quindi non dovrebbe essere preceduta da alcun prefisso.

### Utilizzare Mistral AI

Per utilizzare i modelli ospitati di Mistral AI, anteponi il nome del modello con `mistral:` quando imposti `LLM_MODEL`.

Dovrai registrarti per un account Mistral AI, ottenere una chiave API e memorizzarla nella variabile ambiente `MISTRAL_API_KEY`. Non è necessario impostare `LLM_BASE_URL` poiché Pydantic AI utilizzerà automaticamente l'endpoint API corretto di Mistral.

Esempio di configurazione quando si utilizza docker compose con variabili ambiente:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Utilizzare un LLM locale tramite Ollama

[Ollama](https://ollama.com/) è un modo conveniente per eseguire LLM localmente. Ti preghiamo di consultare la documentazione di Ollama per dettagli. Si prega di notare che gli LLM richiedono risorse computazionali significative e tutti tranne i modelli più piccoli saranno probabilmente troppo lenti senza supporto GPU. Poiché l'assistente si basa sulla chiamata degli strumenti, scegli un modello che supporti gli strumenti, come [`qwen2.5`](https://ollama.com/library/qwen2.5). Inizia con una variante piccola come `qwen2.5:7b` e prova un modello più grande se le risposte non sono sufficientemente buone. Ti preghiamo di condividere qualsiasi esperienza con la comunità!

Quando distribuisci Gramps Web con Docker Compose, puoi aggiungere un servizio Ollama e puntare Gramps Web ad esso:

```yaml
services:
  grampsweb: &grampsweb
    # ... configurazione esistente ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... configurazione esistente ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

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

Dopo aver avviato i servizi, scarica il modello in Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Alcune cose da notare:

- Imposta `LLM_MODEL` sul nome del modello Ollama, inclusa la sua etichetta (la parte dopo i due punti, ad esempio `7b`), preceduta da `ollama:`. Il prefisso fa sì che Pydantic AI utilizzi le impostazioni specifiche di Ollama per il modello, che è la configurazione consigliata.
- `LLM_BASE_URL` deve terminare con `/v1/`, ad esempio `http://ollama:11434/v1/`.
- Con il prefisso `ollama:`, né `OPENAI_API_KEY` né la variabile ambiente `OLLAMA_BASE_URL` sono necessarie. Se `LLM_BASE_URL` non è impostato, Gramps Web torna a `OLLAMA_BASE_URL`.
- In alternativa, puoi omettere il prefisso (ad esempio `LLM_MODEL: qwen2.5:7b`) e utilizzare Ollama tramite la sua API generica compatibile con OpenAI. In questo caso, devi anche impostare la variabile ambiente `OPENAI_API_KEY` su `ollama` (qualsiasi valore non vuoto funziona).

Per risolvere problemi con Ollama, puoi abilitare il logging di debug impostando la variabile ambiente `OLLAMA_DEBUG=1` nell'ambiente del servizio Ollama.

!!! info
    Se stai utilizzando Ollama per la chat AI di Gramps Web, ti preghiamo di supportare la comunità completando questa documentazione con eventuali dettagli mancanti.

### Utilizzare altri fornitori

Sentiti libero di inviare documentazione per altri fornitori e condividere la tua esperienza con la comunità!
