# Configurazione della chat AI

!!! info
    La chat AI richiede la Gramps Web API versione 2.5.0 o superiore. La versione 3.6.0 ha introdotto capacità di chiamata degli strumenti per interazioni più intelligenti.


La Gramps Web API supporta la possibilità di porre domande sul database genealogico utilizzando modelli di linguaggio di grandi dimensioni (LLM) con chiamata degli strumenti.

## Come funziona

L'assistente AI utilizza strumenti specializzati per interrogare direttamente i tuoi dati genealogici. Questi strumenti consentono all'assistente di cercare nel database con la ricerca full-text, filtrare persone/eventi/famiglie/luoghi in base a criteri specifici, calcolare relazioni tra individui e recuperare registri completi, comprese le note. L'assistente risponde quindi in base ai registri che ha consultato e fornisce link ad essi nella sua risposta. Risponde solo in base all'albero genealogico, non da conoscenze generali: se l'albero non registra qualcosa, l'assistente lo comunica. I link a oggetti che non esistono o che sono privati per l'utente vengono sostituiti dal loro testo.

La chat AI non ha bisogno di un modello di embedding vettoriale. Le versioni della Gramps Web API precedenti alla 3.24 utilizzavano anche *ricerca semantica* (generazione aumentata da recupero, RAG), che confrontava il significato di una domanda con un indice di vettori numerici calcolati per tutti gli oggetti nel database. La ricerca semantica è stata rimossa nella Gramps Web API 3.25; le impostazioni `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` e `VECTOR_EMBEDDING_API_KEY` vengono ignorate e possono essere rimosse dalla tua configurazione.

Per abilitare l'endpoint della chat nella Gramps Web API, sono necessari due passaggi:

1. Installazione delle dipendenze richieste,
2. Configurazione di un fornitore LLM.

I due passaggi sono descritti di seguito. Infine, un proprietario o un amministratore deve [configurare quali utenti possono accedere alla funzione di chat](users.md#configuring-who-can-use-ai-chat) nelle impostazioni Gestisci Utenti.

## Installazione delle dipendenze richieste

Le immagini docker standard per Gramps Web hanno già tutte le dipendenze necessarie per la chat AI pre-installate.

Quando si installa la Gramps Web API tramite `pip` (questo non è necessario quando si utilizzano le immagini Docker), le dipendenze necessarie vengono installate con

```bash
pip install gramps_webapi[ai]
```


## Configurazione di un fornitore LLM

La comunicazione con l'LLM utilizza il framework Pydantic AI, che supporta le API compatibili con OpenAI. Questo consente di utilizzare un LLM distribuito localmente tramite Ollama (vedi [Compatibilità OpenAI di Ollama](https://ollama.com/blog/openai-compatibility)) o API ospitate come OpenAI, Anthropic o Hugging Face TGI (Text Generation Inference). L'LLM è configurato tramite i parametri di configurazione `LLM_MODEL` e `LLM_BASE_URL`.

Oltre alle API compatibili con OpenAI, i prefissi specifici del modello del fornitore di Pydantic AI possono essere utilizzati per OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock e Ollama. Altri fornitori, come Cohere, Hugging Face e xAI, non sono installati; i fornitori di inferenza di Hugging Face possono comunque essere utilizzati tramite il loro endpoint compatibile con OpenAI (`LLM_BASE_URL` impostato su `https://router.huggingface.co/v1`).

Se il tuo server di modelli non limita la lunghezza di una risposta, imposta `LLM_MAX_OUTPUT_TOKENS` al numero massimo di token che il modello può generare per risposta (vedi [Configurazione](configuration.md)).


### Utilizzo di un LLM ospitato tramite l'API OpenAI

Quando si utilizza l'API OpenAI, `LLM_BASE_URL` può essere lasciato non impostato, mentre `LLM_MODEL` deve essere impostato su uno dei modelli OpenAI, ad esempio `gpt-4o-mini`. L'LLM utilizza la chiamata degli strumenti per rispondere alle domande: interroga direttamente il database utilizzando strumenti specializzati e risponde in base ai registri che trova. Non richiede una profonda conoscenza genealogica o storica. Pertanto, puoi provare se un modello piccolo/economico è sufficiente.

Dovrai anche registrarti per un account, ottenere una chiave API e memorizzarla nella variabile di ambiente `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` è un parametro di configurazione; se desideri impostarlo tramite una variabile di ambiente, utilizza `GRAMPSWEB_LLM_MODEL` (vedi [Configurazione](configuration.md)). `OPENAI_API_KEY` non è un parametro di configurazione ma una variabile di ambiente utilizzata direttamente dalla libreria Pydantic AI, quindi non dovrebbe avere un prefisso.


### Utilizzo di Mistral AI

Per utilizzare i modelli ospitati di Mistral AI, prefissa il nome del modello con `mistral:` quando imposti `LLM_MODEL`.

Dovrai registrarti per un account Mistral AI, ottenere una chiave API e memorizzarla nella variabile di ambiente `MISTRAL_API_KEY`. Non è necessario impostare `LLM_BASE_URL` poiché Pydantic AI utilizzerà automaticamente l'endpoint API corretto di Mistral.

Esempio di configurazione quando si utilizza docker compose con variabili di ambiente:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```


### Utilizzo di un LLM locale tramite Ollama

[Ollama](https://ollama.com/) è un modo conveniente per eseguire LLM localmente. Si prega di consultare la documentazione di Ollama per i dettagli. Si noti che gli LLM richiedono risorse computazionali significative e tutti tranne i modelli più piccoli saranno probabilmente troppo lenti senza supporto GPU. Poiché l'assistente si basa sulla chiamata degli strumenti, scegli un modello che supporti gli strumenti, come [`qwen2.5`](https://ollama.com/library/qwen2.5). Inizia con una variante piccola come `qwen2.5:7b` e prova una più grande se le risposte non sono sufficientemente buone. Si prega di condividere qualsiasi esperienza con la comunità!

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

- Imposta `LLM_MODEL` sul nome del modello Ollama, inclusa la sua etichetta (la parte dopo i due punti, ad esempio `7b`), prefissata con `ollama:`. Il prefisso fa sì che Pydantic AI utilizzi le sue impostazioni specifiche per Ollama per il modello, che è la configurazione raccomandata.
- `LLM_BASE_URL` deve terminare con `/v1/`, ad esempio `http://ollama:11434/v1/`.
- Con il prefisso `ollama:`, né `OPENAI_API_KEY` né la variabile di ambiente `OLLAMA_BASE_URL` sono necessari. Se `LLM_BASE_URL` non è impostato, Gramps Web torna a `OLLAMA_BASE_URL`.
- In alternativa, puoi omettere il prefisso (ad esempio `LLM_MODEL: qwen2.5:7b`) e utilizzare Ollama tramite la sua API generica compatibile con OpenAI. In questo caso, devi anche impostare la variabile di ambiente `OPENAI_API_KEY` su `ollama` (qualsiasi valore non vuoto funziona).

Per risolvere problemi con Ollama, puoi abilitare il logging di debug impostando la variabile di ambiente `OLLAMA_DEBUG=1` nell'ambiente del servizio Ollama.

!!! info
    Se stai utilizzando Ollama per la chat AI di Gramps Web, ti preghiamo di supportare la comunità completando questa documentazione con eventuali dettagli mancanti.

### Utilizzo di altri fornitori

Sentiti libero di inviare documentazione per altri fornitori e condividere la tua esperienza con la comunità!
