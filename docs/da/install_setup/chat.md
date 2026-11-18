# Opsætning af AI-chat

!!! info
    AI-chat kræver Gramps Web API version 2.5.0 eller højere. Version 3.6.0 introducerede værktøjsopkaldsfunktioner for mere intelligente interaktioner.

Gramps Web API understøtter at stille spørgsmål om den genealogiske database ved hjælp af store sprogmodeller (LLM) med værktøjsopkald.

## Hvordan det fungerer

AI-assistenten bruger specialiserede værktøjer til at forespørge dine slægtsdata direkte. Disse værktøjer gør det muligt for assistenten at søge i databasen med fuldtekst-søgning, filtrere personer/begivenheder/familier/steder efter specifikke kriterier, beregne forhold mellem individer og hente komplette poster, inklusive noter. Assistenten svarer derefter baseret på de poster, den har set op, og linker til dem i sit svar. Den svarer kun fra træet, ikke fra generel viden: hvis træet ikke registrerer noget, siger assistenten det. Links til objekter, der ikke eksisterer, eller som er private for brugeren, erstattes med deres tekst.

AI-chat har ikke brug for en vektorindlejringsmodel. Versioner af Gramps Web API før 3.24 brugte også *semantisk søgning* (retrieval-augmented generation, RAG), som sammenlignede betydningen af et spørgsmål med et indeks af numeriske vektorer beregnet for alle objekter i databasen. Semantisk søgning blev fjernet i Gramps Web API 3.25; indstillingerne `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` og `VECTOR_EMBEDDING_API_KEY` ignoreres og kan fjernes fra din konfiguration.

For at aktivere chat-endpointet i Gramps Web API er to trin nødvendige:

1. Installation af nødvendige afhængigheder,
2. Opsætning af en LLM-udbyder.

De to trin beskrives nedenfor i rækkefølge. Endelig skal en ejer eller administrator [konfigurere, hvilke brugere der kan få adgang til chatfunktionen](users.md#configuring-who-can-use-ai-chat) i indstillingerne for Administrer brugere.

## Installation af nødvendige afhængigheder

De standard docker-billeder for Gramps Web har allerede alle de nødvendige afhængigheder til AI-chat forudinstalleret.

Når du installerer Gramps Web API via `pip` (dette er ikke nødvendigt, når du bruger Docker-billederne), installeres de nødvendige afhængigheder med

```bash
pip install gramps_webapi[ai]
```

## Opsætning af en LLM-udbyder

Kommunikationen med LLM bruger Pydantic AI-rammen, som understøtter OpenAI-kompatible API'er. Dette gør det muligt at bruge en lokalt implementeret LLM via Ollama (se [Ollama OpenAI-kompatibilitet](https://ollama.com/blog/openai-compatibility)) eller hostede API'er som OpenAI, Anthropic eller Hugging Face TGI (Text Generation Inference). LLM'en konfigureres via konfigurationsparametrene `LLM_MODEL` og `LLM_BASE_URL`.

Udover OpenAI-kompatible API'er kan udbyder-specifikke modelpræfikser fra Pydantic AI bruges til OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock og Ollama. Andre udbydere, såsom Cohere, Hugging Face og xAI, er ikke installeret; Hugging Face Inference Providers kan stadig bruges gennem deres OpenAI-kompatible endpoint (`LLM_BASE_URL` sat til `https://router.huggingface.co/v1`).

Hvis din modelserver ikke begrænser længden af et svar, skal `LLM_MAX_OUTPUT_TOKENS` sættes til det maksimale antal tokens, modellen må generere pr. svar (se [Konfiguration](configuration.md)).

### Brug af en hostet LLM via OpenAI API

Når du bruger OpenAI API, kan `LLM_BASE_URL` efterlades usat, mens `LLM_MODEL` skal sættes til en af OpenAI-modellerne, f.eks. `gpt-4o-mini`. LLM'en bruger værktøjsopkald til at besvare spørgsmål: den forespørger databasen direkte ved hjælp af specialiserede værktøjer og svarer baseret på de poster, den finder. Den kræver ikke dyb genealogisk eller historisk viden. Derfor kan du prøve, om en lille/billig model er tilstrækkelig.

Du skal også tilmelde dig en konto, få en API-nøgle og gemme den i miljøvariablen `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` er en konfigurationsparameter; hvis du vil sætte den via en miljøvariabel, skal du bruge `GRAMPSWEB_LLM_MODEL` (se [Konfiguration](configuration.md)). `OPENAI_API_KEY` er ikke en konfigurationsparameter, men en miljøvariabel, der bruges direkte af Pydantic AI-biblioteket, så den bør ikke præfikses.

### Brug af Mistral AI

For at bruge Mistral AIs hostede modeller skal modelnavnet præfikses med `mistral:` når `LLM_MODEL` sættes.

Du skal tilmelde dig en Mistral AI-konto, få en API-nøgle og gemme den i miljøvariablen `MISTRAL_API_KEY`. Der er ikke behov for at sætte `LLM_BASE_URL`, da Pydantic AI automatisk vil bruge den korrekte Mistral API-endpoint.

Eksempelkonfiguration ved brug af docker compose med miljøvariabler:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Brug af en lokal LLM via Ollama

[Ollama](https://ollama.com/) er en bekvem måde at køre LLM'er lokalt. Konsulter venligst Ollama-dokumentationen for detaljer. Vær opmærksom på, at LLM'er kræver betydelige computerressourcer, og alle undtagen de mindste modeller vil sandsynligvis være for langsomme uden GPU-understøttelse. Da assistenten er afhængig af værktøjsopkald, skal du vælge en model, der understøtter værktøjer, såsom [`qwen2.5`](https://ollama.com/library/qwen2.5). Start med en lille variant som `qwen2.5:7b` og prøv en større, hvis svarene ikke er gode nok. Del venligst eventuelle erfaringer med fællesskabet!

Når du implementerer Gramps Web med Docker Compose, kan du tilføje en Ollama-tjeneste og pege Gramps Web mod den:

```yaml
services:
  grampsweb: &grampsweb
    # ... eksisterende konfiguration ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... eksisterende konfiguration ...
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

Efter at have startet tjenesterne, skal du hente modellen ind i Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Nogle ting at bemærke:

- Sæt `LLM_MODEL` til Ollama-modelnavnet, inklusive dets tag (den del efter kolon, f.eks. `7b`), præfiks med `ollama:`. Præfikset får Pydantic AI til at bruge sine Ollama-specifikke indstillinger for modellen, hvilket er den anbefalede opsætning.
- `LLM_BASE_URL` skal ende med `/v1/`, f.eks. `http://ollama:11434/v1/`.
- Med `ollama:` præfikset er hverken `OPENAI_API_KEY` eller miljøvariablen `OLLAMA_BASE_URL` nødvendig. Hvis `LLM_BASE_URL` ikke er sat, falder Gramps Web tilbage på `OLLAMA_BASE_URL`.
- Alternativt kan du undlade præfikset (f.eks. `LLM_MODEL: qwen2.5:7b`) og bruge Ollama gennem dens generiske OpenAI-kompatible API. I dette tilfælde skal du også sætte miljøvariablen `OPENAI_API_KEY` til `ollama` (enhver ikke-tom værdi fungerer).

For at fejlfinde problemer med Ollama kan du aktivere debug-logning ved at sætte miljøvariablen `OLLAMA_DEBUG=1` i Ollama-tjenestens miljø.

!!! info
    Hvis du bruger Ollama til Gramps Web AI-chat, bedes du støtte fællesskabet ved at fuldføre denne dokumentation med eventuelle manglende detaljer.

### Brug af andre udbydere

Du er velkommen til at indsende dokumentation for andre udbydere og dele dine erfaringer med fællesskabet!

## Valgfri funktioner

### Billeder i spørgsmål

Hvis din model accepterer billeder, skal du sætte `LLM_VISION` til `True` for at lade brugerne vedhæfte billeder til deres spørgsmål, f.eks. scanninger af optegnelser (Gramps Web API 3.26+). Billeder skaleres ned til højst 1568 pixels på den lange side, før de sendes til modellen. Tjek at modellen virkelig understøtter billedeindgang: mange små lokale modeller gør ikke, og udbyderen afviser derefter spørgsmål med billeder.

### Lad assistenten foreslå ændringer

Med `LLM_ALLOW_WRITE_PROPOSALS` sat til `True` (Gramps Web API 3.26+) kan assistenten [foreslå ændringer til træet](../user-guide/chat.md#letting-the-assistant-change-your-tree), som brugerne anvender efter at have gennemgået dem. Assistenten skriver aldrig til databasen. Forslag tilbydes kun til brugere, der har tilladelse til at tilføje, redigere og slette objekter, dvs. redaktører og derover, og som har tilladelse til at bruge chatten.

At skrive korrekte forslag er sværere for en model end at besvare spørgsmål, så test det med din model, før du aktiverer det for dine brugere. De ekstra værktøjer gør også hver anmodning til modellen noget større.
