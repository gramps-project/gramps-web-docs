# Opsætning af AI-chat

!!! info
    AI-chat kræver Gramps Web API version 2.5.0 eller højere. Version 3.6.0 introducerede værktøjsopkaldsmuligheder for mere intelligente interaktioner.

Gramps Web API understøtter at stille spørgsmål om den genealogiske database ved hjælp af store sprogmodeller (LLM) via en teknik kaldet retrieval-augmented generation (RAG) kombineret med værktøjsopkald.

## Sådan fungerer det

AI-assistenten bruger to komplementære tilgange:

**Retrieval-Augmented Generation (RAG)**: En *vektorindlejringsmodel* opretter et indeks over alle objekter i Gramps-databasen i form af numeriske vektorer, der koder objekternes betydning. Når en bruger stiller et spørgsmål, konverteres dette spørgsmål også til en vektor og sammenlignes med objekterne i databasen. Denne *semantiske søgning* returnerer objekter, der er mest semantisk lignende spørgsmålet.

**Værktøjsopkald (v3.6.0+)**: AI-assistenten kan nu bruge specialiserede værktøjer til at forespørge dine slægtshistoriske data direkte. Disse værktøjer giver assistenten mulighed for at søge i databasen, filtrere personer/begivenheder/familier/steder efter specifikke kriterier, beregne relationer mellem individer og hente detaljerede objektinformationer. Dette gør assistenten meget mere i stand til at besvare komplekse slægtshistoriske spørgsmål præcist.

For at aktivere chat-endpointet i Gramps Web API er tre trin nødvendige:

1. Installation af nødvendige afhængigheder,
2. Aktivering af semantisk søgning,
3. Opsætning af en LLM-udbyder.

De tre trin er beskrevet nedenfor i rækkefølge. Endelig skal en ejer eller administrator [konfigurere, hvilke brugere der kan få adgang til chatfunktionen](users.md#configuring-who-can-use-ai-chat) i indstillingerne for Administrer brugere.

## Installation af nødvendige afhængigheder

AI-chat kræver, at Sentence Transformers og PyTorch-bibliotekerne er installeret.

De standard docker-billeder for Gramps Web har allerede disse forudinstalleret til `amd64` (f.eks. 64-bit desktop PC) og `arm64` (f.eks. 64-bit Raspberry Pi) arkitekturerne. Desværre understøttes AI-chat ikke på `armv7` (f.eks. 32-bit Raspberry Pi) arkitekturen på grund af manglende PyTorch-understøttelse.

Når du installerer Gramps Web API via `pip` (dette er ikke nødvendigt, når du bruger Docker-billederne), installeres de nødvendige afhængigheder med

```bash
pip install gramps_webapi[ai]
```

## Aktivering af semantisk søgning

Hvis de nødvendige afhængigheder er installeret, kan aktivering af semantisk søgning være så enkel som at indstille konfigurationsmuligheden `VECTOR_EMBEDDING_MODEL` (f.eks. ved at indstille miljøvariablen `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), se [Serverkonfiguration](configuration.md). Dette kan være enhver streng af en model, der understøttes af [Sentence Transformers](https://sbert.net/) biblioteket. Se dokumentationen for dette projekt for detaljer og de tilgængelige modeller.

!!! warning
    Bemærk, at de standard docker-billeder ikke inkluderer en PyTorch-version med GPU-understøttelse. Hvis du har adgang til en GPU (som vil fremskynde den semantiske indeksering betydeligt), skal du installere en GPU-aktiveret version af PyTorch.

Der er flere overvejelser at gøre, når du vælger en model.

- Når du ændrer modellen, skal du manuelt genskabe den semantiske søgeindeks for dit træ (eller alle træer i en multi-træ opsætning), ellers vil du støde på fejl eller meningsløse resultater. Gramps Web registrerer, når den konfigurerede indlejringsmodel ikke længere matcher det eksisterende indeks og viser en vedholdende meddelelse til administratorer, der beder dem om at udløse en fuld reindeksering fra [Administrationsindstillinger](../administration/settings.md#semantic-search-index).
- Modellerne er et kompromis mellem nøjagtighed/generelhed på den ene side og beregningstid/lagerplads på den anden. Hvis du ikke kører Gramps Web API på et system, der har adgang til en kraftfuld GPU, er større modeller normalt for langsomme i praksis.
- Medmindre hele din database er på engelsk, og alle dine brugere kun forventes at stille chat-spørgsmål på engelsk, vil du have brug for en flersproget indlejringsmodel, som er mere sjælden end rene engelske modeller.

Hvis modellen ikke er til stede i den lokale cache, vil den blive downloadet, når Gramps Web API startes for første gang med den nye konfiguration. Modellen `sentence-transformers/distiluse-base-multilingual-cased-v2` er allerede tilgængelig lokalt, når du bruger de standard docker-billeder. Denne model er et godt udgangspunkt og understøtter flersproget input.

Del venligst erfaringer om forskellige modeller med fællesskabet!

!!! info
    Sentence transformers-biblioteket forbruger en betydelig mængde hukommelse, hvilket kan medføre, at arbejdsgange bliver dræbt. Som en tommelfingerregel, med aktiveret semantisk søgning, forbruger hver Gunicorn-arbejder omkring 200 MB hukommelse, og hver celery-arbejder omkring 500 MB hukommelse, selv når de er inaktive, og op til 1 GB, når de beregner indlejringer. Se [Begræns CPU- og hukommelsesforbrug](cpu-limited.md) for indstillinger, der begrænser hukommelsesforbruget. Derudover er det tilrådeligt at tilvejebringe en tilstrækkelig stor swap-partition for at forhindre OOM-fejl på grund af midlertidige hukommelsesforbrugsstigninger.

## Brug af en fjern indlejrings-API

Som et alternativ til at køre en lokal Sentence Transformers-model kan du bruge en fjern OpenAI-kompatibel indlejrings-API til semantisk søgning. Dette er nyttigt, hvis du ønsker at overføre indlejringsberegning til en separat tjeneste (f.eks. [Ollama](https://ollama.com/)), bruge en cloud-indlejringsudbyder (f.eks. OpenAI) eller undgå at installere Sentence Transformers og PyTorch-afhængighederne.

Den fjerne API skal være kompatibel med [OpenAI indlejrings-endpointet](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`).

For at bruge en fjern indlejrings-API skal du indstille følgende konfigurationsmuligheder (se [Serverkonfiguration](configuration.md)):

Nøgle | Beskrivelse
----|-------------
`VECTOR_EMBEDDING_MODEL` | Modellens navn, der skal sendes til den fjerne udbyder
`VECTOR_EMBEDDING_BASE_URL` | Basis-URL for den fjerne API
`VECTOR_EMBEDDING_API_KEY` | API-nøgle (kun nødvendig, hvis udbyderen kræver godkendelse)

### Brug af Ollama til indlejringer

Når du implementerer Gramps Web med Docker Compose, kan du tilføje en Ollama-tjeneste og bruge den til både indlejringer og (valgfrit) LLM:

```yaml
services:
  grampsweb: &grampsweb
    # ... eksisterende konfiguration ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... eksisterende konfiguration ...
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

Efter at have startet tjenesterne, skal du hente indlejringsmodellen til Ollama:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Når du bruger Ollama til indlejringer, er Sentence Transformers og PyTorch-bibliotekerne ikke nødvendige, hvilket reducerer hukommelsesforbruget for Gramps Web API-arbejdere betydeligt.

### Brug af OpenAI til indlejringer

For at bruge OpenAI indlejrings-API'en skal du indstille basis-URL'en til OpenAI API'en og angive din API-nøgle:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Ændring af indlejringsmodellen kræver reindeksering af alle poster for dit træ (eller alle træer i en multi-træ opsætning), da forskellige modeller producerer vektorer med forskellige dimensioner.

## Opsætning af en LLM-udbyder

Kommunikationen med LLM bruger Pydantic AI-rammen, som understøtter OpenAI-kompatible API'er. Dette muliggør brug af en lokalt implementeret LLM via Ollama (se [Ollama OpenAI-kompatibilitet](https://ollama.com/blog/openai-compatibility)) eller hostede API'er som OpenAI, Anthropic eller Hugging Face TGI (Text Generation Inference). LLM konfigureres via konfigurationsparametrene `LLM_MODEL` og `LLM_BASE_URL`.

### Brug af en hostet LLM via OpenAI API

Når du bruger OpenAI API'en, kan `LLM_BASE_URL` forblive uindstillet, mens `LLM_MODEL` skal indstilles til en af OpenAI-modellerne, f.eks. `gpt-4o-mini`. LLM bruger både RAG og værktøjsopkald til at besvare spørgsmål: den vælger relevant information fra semantiske søgeresultater og kan direkte forespørge databasen ved hjælp af specialiserede værktøjer. Den kræver ikke dyb slægtshistorisk eller historisk viden. Derfor kan du prøve, om en lille/billig model er tilstrækkelig.

Du skal også tilmelde dig en konto, få en API-nøgle og gemme den i miljøvariablen `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` er en konfigurationsparameter; hvis du vil indstille den via en miljøvariabel, skal du bruge `GRAMPSWEB_LLM_MODEL` (se [Konfiguration](configuration.md)). `OPENAI_API_KEY` er ikke en konfigurationsparameter, men en miljøvariabel, der bruges direkte af Pydantic AI-biblioteket, så den bør ikke præfikses.

### Brug af Mistral AI

For at bruge Mistral AIs hostede modeller skal du præfikse modellens navn med `mistral:`, når du indstiller `LLM_MODEL`.

Du skal tilmelde dig en Mistral AI-konto, få en API-nøgle og gemme den i miljøvariablen `MISTRAL_API_KEY`. Der er ikke behov for at indstille `LLM_BASE_URL`, da Pydantic AI automatisk vil bruge den korrekte Mistral API-endpoint.

Eksempelkonfiguration, når du bruger docker compose med miljøvariabler:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Brug af en lokal LLM via Ollama

[Ollama](https://ollama.com/) er en bekvem måde at køre LLM'er lokalt. Konsulter venligst Ollama-dokumentationen for detaljer. Vær opmærksom på, at LLM'er kræver betydelige beregningsressourcer, og alle undtagen de mindste modeller vil sandsynligvis være for langsomme uden GPU-understøttelse. Du kan prøve, om [`tinyllama`](https://ollama.com/library/tinyllama) opfylder dine behov. Hvis ikke, kan du prøve en af de større modeller. Del venligst enhver erfaring med fællesskabet!

Når du implementerer Gramps Web med Docker Compose, kan du tilføje en Ollama-tjeneste

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

og derefter indstille konfigurationsparameteren `LLM_BASE_URL` til `http://ollama:11434/v1`. Indstil `LLM_MODEL` til en model, der understøttes af Ollama, og hent den ned i din container med `ollama pull <model>`. Endelig skal du indstille `OPENAI_API_KEY` til `ollama`.

For at fejlfinde problemer med Ollama kan du aktivere debug-logning ved at indstille miljøvariablen `OLLAMA_DEBUG=1` i Ollama-tjenestens miljø.

!!! info
    Hvis du bruger Ollama til Gramps Web AI-chat, bedes du støtte fællesskabet ved at fuldføre denne dokumentation med eventuelle manglende detaljer.

### Brug af andre udbydere

Du er meget velkommen til at indsende dokumentation for andre udbydere og dele dine erfaringer med fællesskabet!
