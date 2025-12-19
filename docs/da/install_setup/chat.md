# Opsætning af AI-chat

!!! info
    AI-chat kræver Gramps Web API version 2.5.0 eller højere. Version 3.6.0 introducerede værktøjsopkaldsfunktioner for mere intelligente interaktioner.

Gramps Web API understøtter at stille spørgsmål om den genealogiske database ved hjælp af store sprogmodeller (LLM) via en teknik kaldet retrieval-augmented generation (RAG) kombineret med værktøjsopkald.

## Sådan fungerer det

AI-assistenten bruger to komplementære tilgange:

**Retrieval-Augmented Generation (RAG)**: En *vektorindlejringsmodel* opretter et indeks over alle objekter i Gramps-databasen i form af numeriske vektorer, der koder objekternes betydning. Når en bruger stiller et spørgsmål, konverteres det spørgsmål også til en vektor og sammenlignes med objekterne i databasen. Denne *semantiske søgning* returnerer objekter, der er mest semantisk ens med spørgsmålet.

**Værktøjsopkald (v3.6.0+)**: AI-assistenten kan nu bruge specialiserede værktøjer til direkte at forespørge dine slægtsdata. Disse værktøjer giver assistenten mulighed for at søge i databasen, filtrere personer/begivenheder/familier/steder efter specifikke kriterier, beregne relationer mellem individer og hente detaljerede objektinformationer. Dette gør assistenten meget mere i stand til præcist at besvare komplekse genealogiske spørgsmål.

For at aktivere chat-endpointet i Gramps Web API er tre trin nødvendige:

1. Installation af nødvendige afhængigheder,
2. Aktivering af semantisk søgning,
3. Opsætning af en LLM-udbyder.

De tre trin beskrives nedenfor i rækkefølge. Endelig skal en ejer eller administrator [konfigurere, hvilke brugere der kan få adgang til chatfunktionen](users.md#configuring-who-can-use-ai-chat) i indstillingerne for Administrer brugere.

## Installation af nødvendige afhængigheder

AI-chat kræver, at Sentence Transformers og PyTorch-bibliotekerne er installeret.

De standard docker-billeder for Gramps Web har allerede disse forudinstalleret til `amd64` (f.eks. 64-bit desktop PC) og `arm64` (f.eks. 64-bit Raspberry Pi) arkitekturerne. Desværre understøttes AI-chat ikke på `armv7` (f.eks. 32-bit Raspberry Pi) arkitekturen på grund af manglende PyTorch-understøttelse.

Når du installerer Gramps Web API via `pip` (dette er ikke nødvendigt, når du bruger Docker-billederne), installeres de nødvendige afhængigheder med

```bash
pip install gramps_webapi[ai]
```

## Aktivering af semantisk søgning

Hvis de nødvendige afhængigheder er installeret, kan aktivering af semantisk søgning være så simpel som at indstille konfigurationsmuligheden `VECTOR_EMBEDDING_MODEL` (f.eks. ved at indstille miljøvariablen `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), se [Serverkonfiguration](configuration.md). Dette kan være en hvilken som helst streng af en model, der understøttes af [Sentence Transformers](https://sbert.net/) biblioteket. Se dokumentationen for dette projekt for detaljer og de tilgængelige modeller.

!!! warning
    Bemærk, at de standard docker-billeder ikke inkluderer en PyTorch-version med GPU-understøttelse. Hvis du har adgang til en GPU (som vil fremskynde den semantiske indeksering betydeligt), skal du installere en GPU-aktiveret version af PyTorch.

Der er flere overvejelser at gøre, når du vælger en model.

- Når du ændrer modellen, skal du manuelt genskabe den semantiske søgeindeks for dit træ (eller alle træer i en multi-træ opsætning), ellers vil du støde på fejl eller meningsløse resultater.
- Modellerne er et kompromis mellem nøjagtighed/generelhed på den ene side og beregningstid/lagerplads på den anden. Hvis du ikke kører Gramps Web API på et system, der har adgang til en kraftfuld GPU, er større modeller normalt for langsomme i praksis.
- Medmindre din hele database er på engelsk, og alle dine brugere kun forventes at stille chatspørgsmål på engelsk, vil du have brug for en flersproget indlejringsmodel, som er mere sjælden end rene engelske modeller.

Hvis modellen ikke er til stede i den lokale cache, vil den blive downloadet, når Gramps Web API startes for første gang med den nye konfiguration. Modellen `sentence-transformers/distiluse-base-multilingual-cased-v2` er allerede tilgængelig lokalt, når du bruger de standard docker-billeder. Denne model er et godt udgangspunkt og understøtter flersproget input.

Del venligst erfaringer om forskellige modeller med fællesskabet!

!!! info
    Sentence transformers-biblioteket bruger en betydelig mængde hukommelse, hvilket kan medføre, at arbejdsgange bliver dræbt. Som en tommelfingerregel, med semantisk søgning aktiveret, bruger hver Gunicorn-arbejder omkring 200 MB hukommelse, og hver celery-arbejder omkring 500 MB hukommelse, selv når de er inaktive, og op til 1 GB, når de beregner indlejringer. Se [Begræns CPU- og hukommelsesforbrug](cpu-limited.md) for indstillinger, der begrænser hukommelsesforbruget. Derudover er det tilrådeligt at tilvejebringe en tilstrækkeligt stor swap-partition for at forhindre OOM-fejl på grund af midlertidige hukommelsesforbrugs-spidser.

## Opsætning af en LLM-udbyder

Kommunikationen med LLM bruger Pydantic AI-rammen, som understøtter OpenAI-kompatible API'er. Dette gør det muligt at bruge en lokalt implementeret LLM via Ollama (se [Ollama OpenAI-kompatibilitet](https://ollama.com/blog/openai-compatibility)) eller hostede API'er som OpenAI, Anthropic eller Hugging Face TGI (Text Generation Inference). LLM'en konfigureres via konfigurationsparametrene `LLM_MODEL` og `LLM_BASE_URL`.

### Brug af en hostet LLM via OpenAI API

Når du bruger OpenAI API, kan `LLM_BASE_URL` efterlades uindstillet, mens `LLM_MODEL` skal indstilles til en af OpenAI-modellerne, f.eks. `gpt-4o-mini`. LLM'en bruger både RAG og værktøjsopkald til at besvare spørgsmål: den vælger relevant information fra semantiske søgeresultater og kan direkte forespørge databasen ved hjælp af specialiserede værktøjer. Den kræver ikke dyb genealogisk eller historisk viden. Derfor kan du prøve, om en lille/billig model er tilstrækkelig.

Du skal også tilmelde dig en konto, få en API-nøgle og gemme den i miljøvariablen `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` er en konfigurationsparameter; hvis du vil indstille den via en miljøvariabel, skal du bruge `GRAMPSWEB_LLM_MODEL` (se [Konfiguration](configuration.md)). `OPENAI_API_KEY` er ikke en konfigurationsparameter, men en miljøvariabel, der bruges direkte af Pydantic AI-biblioteket, så den bør ikke have et præfiks.

### Brug af Mistral AI

For at bruge Mistral AIs hostede modeller, skal du præfixe modelnavnet med `mistral:` når du indstiller `LLM_MODEL`.

Du skal tilmelde dig en Mistral AI-konto, få en API-nøgle og gemme den i miljøvariablen `MISTRAL_API_KEY`. Der er ikke behov for at indstille `LLM_BASE_URL`, da Pydantic AI automatisk vil bruge den korrekte Mistral API-endpoint.

Eksempelkonfiguration, når du bruger docker compose med miljøvariabler:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Brug af en lokal LLM via Ollama

[Ollama](https://ollama.com/) er en bekvem måde at køre LLM'er lokalt. Konsulter venligst Ollama-dokumentationen for detaljer. Vær opmærksom på, at LLM'er kræver betydelige beregningsressourcer, og alle undtagen de mindste modeller vil sandsynligvis være for langsomme uden GPU-understøttelse. Du kan prøve, om [`tinyllama`](https://ollama.com/library/tinyllama) opfylder dine behov. Hvis ikke, så prøv en af de større modeller. Del venligst eventuelle erfaringer med fællesskabet!

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
    Hvis du bruger Ollama til Gramps Web AI-chat, bedes du støtte fællesskabet ved at udfylde denne dokumentation med eventuelle manglende detaljer.

### Brug af andre udbydere

Du er meget velkommen til at indsende dokumentation for andre udbydere og dele dine erfaringer med fællesskabet!
