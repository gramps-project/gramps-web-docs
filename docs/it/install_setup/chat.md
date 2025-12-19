# Impostare la chat AI

!!! info
    La chat AI richiede la Gramps Web API versione 2.5.0 o superiore. La versione 3.6.0 ha introdotto capacità di chiamata degli strumenti per interazioni più intelligenti.

La Gramps Web API supporta la possibilità di porre domande sul database genealogico utilizzando modelli linguistici di grandi dimensioni (LLM) tramite una tecnica chiamata generazione aumentata da recupero (RAG) combinata con la chiamata degli strumenti.

## Come funziona

L'assistente AI utilizza due approcci complementari:

**Generazione Aumentata da Recupero (RAG)**: Un *modello di embedding vettoriale* crea un indice di tutti gli oggetti nel database di Gramps sotto forma di vettori numerici che codificano il significato degli oggetti. Quando un utente pone una domanda, anche quella domanda viene convertita in un vettore e confrontata con gli oggetti nel database. Questa *ricerca semantica* restituisce gli oggetti che sono semanticamente più simili alla domanda.

**Chiamata degli Strumenti (v3.6.0+)**: L'assistente AI può ora utilizzare strumenti specializzati per interrogare direttamente i tuoi dati genealogici. Questi strumenti consentono all'assistente di cercare nel database, filtrare persone/eventi/famiglie/luoghi in base a criteri specifici, calcolare relazioni tra individui e recuperare informazioni dettagliate sugli oggetti. Questo rende l'assistente molto più capace di rispondere con precisione a domande genealogiche complesse.

Per abilitare l'endpoint della chat nella Gramps Web API, sono necessari tre passaggi:

1. Installare le dipendenze richieste,
2. Abilitare la ricerca semantica,
3. Configurare un fornitore di LLM.

I tre passaggi sono descritti di seguito a turno. Infine, un proprietario o un amministratore deve [configurare quali utenti possono accedere alla funzione di chat](users.md#configuring-who-can-use-ai-chat) nelle impostazioni Gestisci Utenti.

## Installare le dipendenze richieste

La chat AI richiede che le librerie Sentence Transformers e PyTorch siano installate.

Le immagini docker standard per Gramps Web le hanno già pre-installate per le architetture `amd64` (ad esempio, PC desktop a 64 bit) e `arm64` (ad esempio, Raspberry Pi a 64 bit). Sfortunatamente, la chat AI non è supportata sull'architettura `armv7` (ad esempio, Raspberry Pi a 32 bit) a causa della mancanza di supporto per PyTorch.

Quando si installa la Gramps Web API tramite `pip` (questo non è necessario quando si utilizzano le immagini Docker), le dipendenze necessarie vengono installate con

```bash
pip install gramps_webapi[ai]
```

## Abilitare la ricerca semantica

Se le dipendenze necessarie sono installate, abilitare la ricerca semantica può essere semplice come impostare l'opzione di configurazione `VECTOR_EMBEDDING_MODEL` (ad esempio, impostando la variabile di ambiente `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), vedere [Configurazione del Server](configuration.md). Questo può essere qualsiasi stringa di un modello supportato dalla libreria [Sentence Transformers](https://sbert.net/). Vedi la documentazione di questo progetto per dettagli e modelli disponibili.

!!! warning
    Nota che le immagini docker predefinite non includono una versione di PyTorch con supporto GPU. Se hai accesso a una GPU (che accelererà significativamente l'indicizzazione semantica), ti preghiamo di installare una versione di PyTorch abilitata per GPU.

Ci sono diverse considerazioni da fare quando si sceglie un modello.

- Quando cambi il modello, devi ricreare manualmente l'indice di ricerca semantica per il tuo albero (o per tutti gli alberi in una configurazione multi-albero), altrimenti incontrerai errori o risultati privi di significato.
- I modelli sono un compromesso tra accuratezza/generalità da un lato e tempo di calcolo/spazio di archiviazione dall'altro. Se non stai eseguendo la Gramps Web API su un sistema che ha accesso a una potente GPU, i modelli più grandi sono solitamente troppo lenti nella pratica.
- A meno che l'intero database non sia in inglese e tutti i tuoi utenti non siano previsti per porre domande in chat solo in inglese, avrai bisogno di un modello di embedding multilingue, che è più raro rispetto ai modelli puramente in inglese.

Se il modello non è presente nella cache locale, verrà scaricato quando la Gramps Web API viene avviata per la prima volta con la nuova configurazione. Il modello `sentence-transformers/distiluse-base-multilingual-cased-v2` è già disponibile localmente quando si utilizzano le immagini docker standard. Questo modello è un buon punto di partenza e supporta input multilingue.

Ti preghiamo di condividere le esperienze sui diversi modelli con la comunità!

!!! info
    La libreria sentence transformers consuma una quantità significativa di memoria, il che potrebbe causare l'uccisione dei processi worker. Come regola generale, con la ricerca semantica abilitata, ogni worker Gunicorn consuma circa 200 MB di memoria e ogni worker celery circa 500 MB di memoria anche quando inattivo, e fino a 1 GB quando calcola gli embedding. Vedi [Limitare l'uso della CPU e della memoria](cpu-limited.md) per le impostazioni che limitano l'uso della memoria. Inoltre, è consigliabile fornire una partizione di swap sufficientemente grande per prevenire errori OOM a causa di picchi temporanei nell'uso della memoria.

## Configurare un fornitore di LLM

La comunicazione con il LLM utilizza il framework Pydantic AI, che supporta API compatibili con OpenAI. Questo consente di utilizzare un LLM distribuito localmente tramite Ollama (vedi [Compatibilità OpenAI di Ollama](https://ollama.com/blog/openai-compatibility)) o API ospitate come OpenAI, Anthropic o Hugging Face TGI (Text Generation Inference). Il LLM è configurato tramite i parametri di configurazione `LLM_MODEL` e `LLM_BASE_URL`.

### Utilizzare un LLM ospitato tramite l'API OpenAI

Quando si utilizza l'API OpenAI, `LLM_BASE_URL` può essere lasciato non impostato, mentre `LLM_MODEL` deve essere impostato su uno dei modelli OpenAI, ad esempio `gpt-4o-mini`. Il LLM utilizza sia RAG che chiamata degli strumenti per rispondere alle domande: seleziona informazioni pertinenti dai risultati della ricerca semantica e può interrogare direttamente il database utilizzando strumenti specializzati. Non richiede una profonda conoscenza genealogica o storica. Pertanto, puoi provare se un modello piccolo/economico è sufficiente.

Dovrai anche registrarti per un account, ottenere una chiave API e memorizzarla nella variabile di ambiente `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` è un parametro di configurazione; se desideri impostarlo tramite una variabile di ambiente, utilizza `GRAMPSWEB_LLM_MODEL` (vedi [Configurazione](configuration.md)). `OPENAI_API_KEY` non è un parametro di configurazione ma una variabile di ambiente utilizzata direttamente dalla libreria Pydantic AI, quindi non dovrebbe essere preceduta da alcun prefisso.

### Utilizzare Mistral AI

Per utilizzare i modelli ospitati di Mistral AI, anteponi il nome del modello con `mistral:` quando imposti `LLM_MODEL`.

Dovrai registrarti per un account Mistral AI, ottenere una chiave API e memorizzarla nella variabile di ambiente `MISTRAL_API_KEY`. Non è necessario impostare `LLM_BASE_URL` poiché Pydantic AI utilizzerà automaticamente l'endpoint API corretto di Mistral.

Esempio di configurazione quando si utilizza docker compose con variabili di ambiente:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Utilizzare un LLM locale tramite Ollama

[Ollama](https://ollama.com/) è un modo conveniente per eseguire LLM localmente. Ti preghiamo di consultare la documentazione di Ollama per dettagli. Si prega di notare che gli LLM richiedono risorse computazionali significative e tutti tranne i modelli più piccoli saranno probabilmente troppo lenti senza supporto GPU. Puoi provare se [`tinyllama`](https://ollama.com/library/tinyllama) soddisfa le tue esigenze. In caso contrario, prova uno dei modelli più grandi. Ti preghiamo di condividere qualsiasi esperienza con la comunità!

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

e poi impostare il parametro di configurazione `LLM_BASE_URL` su `http://ollama:11434/v1`. Imposta `LLM_MODEL` su un modello supportato da Ollama e scaricalo nel tuo contenitore con `ollama pull <model>`. Infine, imposta `OPENAI_API_KEY` su `ollama`.

Per risolvere problemi con Ollama, puoi abilitare il logging di debug impostando la variabile di ambiente `OLLAMA_DEBUG=1` nell'ambiente del servizio Ollama.

!!! info
    Se stai utilizzando Ollama per la chat AI di Gramps Web, ti preghiamo di supportare la comunità completando questa documentazione con eventuali dettagli mancanti.

### Utilizzare altri fornitori

Sentiti libero di inviare documentazione per altri fornitori e condividere la tua esperienza con la comunità!
