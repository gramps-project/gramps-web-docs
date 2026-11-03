# Einrichtung des KI-Chats

!!! info
    Der KI-Chat erfordert die Gramps Web API Version 2.5.0 oder höher. Die Version 3.6.0 führte Funktionen zum Aufrufen von Werkzeugen für intelligentere Interaktionen ein.

Die Gramps Web API unterstützt das Stellen von Fragen zur genealogischen Datenbank mithilfe von großen Sprachmodellen (LLM) mit Werkzeugaufrufen.

## Funktionsweise

Der KI-Assistent verwendet spezialisierte Werkzeuge, um direkt auf Ihre Genealogiedaten zuzugreifen. Diese Werkzeuge ermöglichen es dem Assistenten, die Datenbank mit der Volltextsuche zu durchsuchen, Personen/Ereignisse/Familien/Orte nach spezifischen Kriterien zu filtern, Beziehungen zwischen Individuen zu berechnen und vollständige Datensätze, einschließlich Notizen, abzurufen. Der Assistent antwortet dann basierend auf den Datensätzen, die er abgerufen hat, und verlinkt in seiner Antwort darauf. Er antwortet nur aus dem Baum, nicht aus allgemeinem Wissen: Wenn der Baum etwas nicht verzeichnet, sagt der Assistent das. Links zu Objekten, die nicht existieren oder die für den Benutzer privat sind, werden durch ihren Text ersetzt.

Der KI-Chat benötigt kein Vektor-Einbettungsmodell. Versionen der Gramps Web API vor 3.24 verwendeten ebenfalls *semantische Suche* (retrieval-augmented generation, RAG), die die Bedeutung einer Frage mit einem Index von numerischen Vektoren verglich, die für alle Objekte in der Datenbank berechnet wurden. Die semantische Suche wurde in der Gramps Web API 3.25 entfernt; die Einstellungen `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` und `VECTOR_EMBEDDING_API_KEY` werden ignoriert und können aus Ihrer Konfiguration entfernt werden.

Um den Chat-Endpunkt in der Gramps Web API zu aktivieren, sind zwei Schritte erforderlich:

1. Installation der erforderlichen Abhängigkeiten,
2. Einrichtung eines LLM-Anbieters.

Die beiden Schritte werden im Folgenden nacheinander beschrieben. Schließlich muss ein Eigentümer oder Administrator [konfigurieren, welche Benutzer auf die Chat-Funktion zugreifen können](users.md#configuring-who-can-use-ai-chat) in den Einstellungen zur Benutzerverwaltung.

## Installation der erforderlichen Abhängigkeiten

Die Standard-Docker-Images für Gramps Web haben bereits alle erforderlichen Abhängigkeiten für den KI-Chat vorinstalliert.

Bei der Installation der Gramps Web API über `pip` (dies ist bei der Verwendung der Docker-Images nicht erforderlich) werden die notwendigen Abhängigkeiten mit

```bash
pip install gramps_webapi[ai]
```

installiert.

## Einrichtung eines LLM-Anbieters

Die Kommunikation mit dem LLM verwendet das Pydantic AI-Framework, das OpenAI-kompatible APIs unterstützt. Dies ermöglicht die Verwendung eines lokal bereitgestellten LLM über Ollama (siehe [Ollama OpenAI-Kompatibilität](https://ollama.com/blog/openai-compatibility)) oder gehostete APIs wie OpenAI, Anthropic oder Hugging Face TGI (Text Generation Inference). Das LLM wird über die Konfigurationsparameter `LLM_MODEL` und `LLM_BASE_URL` konfiguriert.

Neben OpenAI-kompatiblen APIs können die anbieter-spezifischen Modellpräfixe von Pydantic AI für OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock und Ollama verwendet werden. Andere Anbieter wie Cohere, Hugging Face und xAI sind nicht installiert; Hugging Face Inference Providers können jedoch weiterhin über ihren OpenAI-kompatiblen Endpunkt verwendet werden (`LLM_BASE_URL` auf `https://router.huggingface.co/v1` gesetzt).

Wenn Ihr Modellserver die Länge einer Antwort nicht begrenzt, setzen Sie `LLM_MAX_OUTPUT_TOKENS` auf die maximale Anzahl von Tokens, die das Modell pro Antwort generieren darf (siehe [Konfiguration](configuration.md)).

### Verwendung eines gehosteten LLM über die OpenAI API

Bei der Verwendung der OpenAI API kann `LLM_BASE_URL` ungesetzt bleiben, während `LLM_MODEL` auf eines der OpenAI-Modelle gesetzt werden muss, z.B. `gpt-4o-mini`. Das LLM verwendet Werkzeugaufrufe, um Fragen zu beantworten: Es fragt die Datenbank direkt mit spezialisierten Werkzeugen ab und antwortet basierend auf den Datensätzen, die es findet. Es erfordert kein tiefes genealogisches oder historisches Wissen. Daher können Sie ausprobieren, ob ein kleines/günstiges Modell ausreicht.

Sie müssen sich auch für ein Konto anmelden, einen API-Schlüssel erhalten und ihn in der Umgebungsvariable `OPENAI_API_KEY` speichern.

!!! info
    `LLM_MODEL` ist ein Konfigurationsparameter; wenn Sie ihn über eine Umgebungsvariable setzen möchten, verwenden Sie `GRAMPSWEB_LLM_MODEL` (siehe [Konfiguration](configuration.md)). `OPENAI_API_KEY` ist kein Konfigurationsparameter, sondern eine Umgebungsvariable, die direkt von der Pydantic AI-Bibliothek verwendet wird, daher sollte sie nicht mit einem Präfix versehen werden.

### Verwendung von Mistral AI

Um die gehosteten Modelle von Mistral AI zu verwenden, prefixen Sie den Modellnamen mit `mistral:`, wenn Sie `LLM_MODEL` setzen.

Sie müssen sich für ein Mistral AI-Konto anmelden, einen API-Schlüssel erhalten und ihn in der Umgebungsvariable `MISTRAL_API_KEY` speichern. Es ist nicht erforderlich, `LLM_BASE_URL` zu setzen, da Pydantic AI automatisch den richtigen Mistral API-Endpunkt verwendet.

Beispielkonfiguration bei Verwendung von Docker Compose mit Umgebungsvariablen:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Verwendung eines lokalen LLM über Ollama

[Ollama](https://ollama.com/) ist eine bequeme Möglichkeit, LLMs lokal auszuführen. Bitte konsultieren Sie die Ollama-Dokumentation für Details. Bitte beachten Sie, dass LLMs erhebliche Rechenressourcen benötigen und alle außer den kleinsten Modellen wahrscheinlich ohne GPU-Unterstützung zu langsam sein werden. Da der Assistent auf Werkzeugaufrufen basiert, wählen Sie ein Modell, das Werkzeuge unterstützt, wie z.B. [`qwen2.5`](https://ollama.com/library/qwen2.5). Beginnen Sie mit einer kleinen Variante wie `qwen2.5:7b` und probieren Sie ein größeres Modell, wenn die Antworten nicht gut genug sind. Bitte teilen Sie Ihre Erfahrungen mit der Community!

Beim Bereitstellen von Gramps Web mit Docker Compose können Sie einen Ollama-Dienst hinzufügen und Gramps Web darauf verweisen:

```yaml
services:
  grampsweb: &grampsweb
    # ... bestehende Konfiguration ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... bestehende Konfiguration ...
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

Nachdem Sie die Dienste gestartet haben, ziehen Sie das Modell in Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Einige Dinge, die zu beachten sind:

- Setzen Sie `LLM_MODEL` auf den Ollama-Modellnamen, einschließlich seines Tags (dem Teil nach dem Doppelpunkt, z.B. `7b`), vorangestellt mit `ollama:`. Das Präfix sorgt dafür, dass Pydantic AI seine Ollama-spezifischen Einstellungen für das Modell verwendet, was die empfohlene Konfiguration ist.
- `LLM_BASE_URL` muss mit `/v1/` enden, z.B. `http://ollama:11434/v1/`.
- Mit dem `ollama:`-Präfix sind weder `OPENAI_API_KEY` noch die Umgebungsvariable `OLLAMA_BASE_URL` erforderlich. Wenn `LLM_BASE_URL` nicht gesetzt ist, fällt Gramps Web auf `OLLAMA_BASE_URL` zurück.
- Alternativ können Sie das Präfix weglassen (z.B. `LLM_MODEL: qwen2.5:7b`) und Ollama über seine generische OpenAI-kompatible API verwenden. In diesem Fall müssen Sie auch die Umgebungsvariable `OPENAI_API_KEY` auf `ollama` setzen (jeder nicht leere Wert funktioniert).

Um Probleme mit Ollama zu beheben, können Sie das Debug-Logging aktivieren, indem Sie die Umgebungsvariable `OLLAMA_DEBUG=1` in der Umgebung des Ollama-Dienstes setzen.

!!! info
    Wenn Sie Ollama für den Gramps Web KI-Chat verwenden, unterstützen Sie bitte die Community, indem Sie diese Dokumentation mit fehlenden Details vervollständigen.

### Verwendung anderer Anbieter

Bitte zögern Sie nicht, Dokumentationen für andere Anbieter einzureichen und Ihre Erfahrungen mit der Community zu teilen!
