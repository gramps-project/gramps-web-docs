# Einrichten des KI-Chats

!!! info
    Der KI-Chat erfordert Gramps Web API Version 2.5.0 oder höher. Version 3.6.0 führte Tool-Aufruf-Funktionen für intelligentere Interaktionen ein.


Die Gramps Web API unterstützt das Stellen von Fragen zur genealogischen Datenbank mithilfe großer Sprachmodelle (LLM) mit Tool-Aufrufen.

## Funktionsweise

Der KI-Assistent verwendet spezialisierte Tools, um deine genealogischen Daten direkt abzufragen. Diese Tools ermöglichen es dem Assistenten, die Datenbank mit der Volltextsuche zu durchsuchen, Personen/Ereignisse/Familien/Orte nach bestimmten Kriterien zu filtern, Verwandtschaftsbeziehungen zwischen Personen zu berechnen und vollständige Datensätze einschließlich Notizen abzurufen. Der Assistent antwortet anschließend auf Grundlage der Datensätze, die er abgerufen hat, und verlinkt in seiner Antwort auf diese Datensätze. Er antwortet ausschließlich aus dem Stammbaum und nicht aus allgemeinem Wissen: Wenn etwas im Stammbaum nicht erfasst ist, sagt der Assistent das. Links zu Objekten, die nicht existieren oder für den Benutzer privat sind, werden durch ihren Text ersetzt.

Der KI-Chat benötigt kein Vektoreinbettungsmodell. Versionen der Gramps Web API vor 3.24 verwendeten außerdem die *semantische Suche* (Retrieval-Augmented Generation, RAG), bei der die Bedeutung einer Frage mit einem Index numerischer Vektoren verglichen wurde, die für alle Objekte in der Datenbank berechnet wurden. Die semantische Suche wurde in Gramps Web API 3.25 entfernt; die Einstellungen `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` und `VECTOR_EMBEDDING_API_KEY` werden ignoriert und können aus deiner Konfiguration entfernt werden.

Um den Chat-Endpunkt in der Gramps Web API zu aktivieren, sind zwei Schritte erforderlich:

1. Installation der erforderlichen Abhängigkeiten,
2. Einrichten eines LLM-Anbieters.

Die beiden Schritte werden im Folgenden nacheinander beschrieben. Anschließend muss ein Eigentümer oder Administrator in den Einstellungen zur Benutzerverwaltung [konfigurieren, welche Benutzer auf die Chat-Funktion zugreifen können](users.md#configuring-who-can-use-ai-chat).

## Installation der erforderlichen Abhängigkeiten

Die standardmäßigen Docker-Images für Gramps Web enthalten bereits alle für den KI-Chat erforderlichen Abhängigkeiten.

Bei der Installation der Gramps Web API über `pip` (dies ist bei Verwendung der Docker-Images nicht erforderlich) werden die notwendigen Abhängigkeiten mit folgendem Befehl installiert:

```bash
pip install gramps_webapi[ai]
```


## Einrichten eines LLM-Anbieters

Die Kommunikation mit dem LLM erfolgt über das Pydantic-AI-Framework, das OpenAI-kompatible APIs unterstützt. Dadurch kann ein lokal über Ollama bereitgestelltes LLM verwendet werden (siehe [Ollama OpenAI compatibility](https://ollama.com/blog/openai-compatibility)) oder gehostete APIs wie OpenAI, Anthropic oder Hugging Face TGI (Text Generation Inference). Das LLM wird über die Konfigurationsparameter `LLM_MODEL` und `LLM_BASE_URL` konfiguriert.

Neben OpenAI-kompatiblen APIs können die anbieterspezifischen Modellpräfixe von Pydantic AI für OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock und Ollama verwendet werden. Andere Anbieter wie Cohere, Hugging Face und xAI sind nicht installiert; Hugging Face Inference Providers können weiterhin über ihren OpenAI-kompatiblen Endpunkt verwendet werden (`LLM_BASE_URL` wird auf `https://router.huggingface.co/v1` gesetzt).

Wenn dein Modellserver die Länge einer Antwort nicht begrenzt, setze `LLM_MAX_OUTPUT_TOKENS` auf die maximale Anzahl von Token, die das Modell pro Antwort generieren darf (siehe [Konfiguration](configuration.md)).


### Verwenden eines gehosteten LLM über die OpenAI-API

Bei Verwendung der OpenAI-API kann `LLM_BASE_URL` nicht gesetzt werden, während `LLM_MODEL` auf eines der OpenAI-Modelle gesetzt werden muss, z. B. `gpt-4o-mini`. Das LLM verwendet Tool-Aufrufe, um Fragen zu beantworten: Es fragt die Datenbank direkt mithilfe spezialisierter Tools ab und antwortet auf Grundlage der gefundenen Datensätze. Es benötigt kein tiefgreifendes genealogisches oder historisches Wissen. Daher kannst du ausprobieren, ob ein kleines/kostengünstiges Modell ausreicht.

Du musst außerdem ein Konto erstellen, einen API-Schlüssel abrufen und ihn in der Umgebungsvariable `OPENAI_API_KEY` speichern.

!!! info
    `LLM_MODEL` ist ein Konfigurationsparameter; wenn du ihn über eine Umgebungsvariable setzen möchtest, verwende `GRAMPSWEB_LLM_MODEL` (siehe [Konfiguration](configuration.md)). `OPENAI_API_KEY` ist kein Konfigurationsparameter, sondern eine direkt von der Pydantic-AI-Bibliothek verwendete Umgebungsvariable und sollte daher nicht mit einem Präfix versehen werden.


### Verwenden von Mistral AI

Um die gehosteten Modelle von Mistral AI zu verwenden, stelle dem Modellnamen beim Setzen von `LLM_MODEL` das Präfix `mistral:` voran.

Du musst ein Mistral-AI-Konto erstellen, einen API-Schlüssel abrufen und ihn in der Umgebungsvariable `MISTRAL_API_KEY` speichern. `LLM_BASE_URL` muss nicht gesetzt werden, da Pydantic AI automatisch den richtigen Mistral-API-Endpunkt verwendet.

Beispielkonfiguration bei Verwendung von Docker Compose mit Umgebungsvariablen:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```


### Verwenden eines lokalen LLM über Ollama

[Ollama](https://ollama.com/) ist eine praktische Möglichkeit, LLMs lokal auszuführen. Einzelheiten findest du in der Ollama-Dokumentation. Beachte, dass LLMs erhebliche Rechenressourcen benötigen und alle außer den kleinsten Modellen ohne GPU-Unterstützung wahrscheinlich zu langsam sind. Da der Assistent auf Tool-Aufrufen basiert, solltest du ein Modell wählen, das Tools unterstützt, beispielsweise [`qwen2.5`](https://ollama.com/library/qwen2.5). Beginne mit einer kleinen Variante wie `qwen2.5:7b` und probiere ein größeres Modell aus, wenn die Antworten nicht gut genug sind. Teile deine Erfahrungen gerne mit der Community!

Bei der Bereitstellung von Gramps Web mit Docker Compose kannst du einen Ollama-Dienst hinzufügen und Gramps Web darauf verweisen:

```yaml
services:
  grampsweb: &grampsweb
    # ... existing config ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... existing config ...
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

Nachdem die Dienste gestartet wurden, lade das Modell in Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Einige wichtige Hinweise:

- Setze `LLM_MODEL` auf den Ollama-Modellnamen einschließlich seines Etiketts (der Teil nach dem Doppelpunkt, z. B. `7b`) und stelle ihm `ollama:` voran. Durch das Präfix verwendet Pydantic AI die Ollama-spezifischen Einstellungen für das Modell, was der empfohlenen Einrichtung entspricht.
- `LLM_BASE_URL` muss mit `/v1/` enden, z. B. `http://ollama:11434/v1/`.
- Mit dem Präfix `ollama:` werden weder `OPENAI_API_KEY` noch die Umgebungsvariable `OLLAMA_BASE_URL` benötigt. Wenn `LLM_BASE_URL` nicht gesetzt ist, verwendet Gramps Web ersatzweise `OLLAMA_BASE_URL`.
- Alternativ kannst du das Präfix weglassen (z. B. `LLM_MODEL: qwen2.5:7b`) und Ollama über seine generische OpenAI-kompatible API verwenden. In diesem Fall musst du außerdem die Umgebungsvariable `OPENAI_API_KEY` auf `ollama` setzen (jeder nichtleere Wert funktioniert).

Zur Fehlerbehebung bei Problemen mit Ollama kannst du die Debug-Protokollierung aktivieren, indem du die Umgebungsvariable `OLLAMA_DEBUG=1` in der Umgebung des Ollama-Dienstes setzt.

!!! info
    Wenn du Ollama für den KI-Chat von Gramps Web verwendest, unterstütze bitte die Community, indem du diese Dokumentation um fehlende Details ergänzt.

### Verwenden anderer Anbieter

Du kannst gerne Dokumentation für andere Anbieter einreichen und deine Erfahrungen mit der Community teilen!

## Optionale Funktionen

### Bilder in Fragen

Wenn dein Modell Bilder akzeptiert, setze `LLM_VISION` auf `True`, damit Benutzer Bilder an ihre Fragen anhängen können, beispielsweise Scans von Dokumenten (Gramps Web API 3.26+). Bilder werden auf höchstens 1568 Pixel an der langen Seite verkleinert, bevor sie an das Modell gesendet werden. Überprüfe, ob das Modell die Bildeingabe tatsächlich unterstützt: Viele kleine lokale Modelle tun dies nicht, woraufhin der Anbieter Fragen mit Bildern ablehnt.

### Den Assistenten Änderungen vorschlagen lassen

Wenn `LLM_ALLOW_WRITE_PROPOSALS` auf `True` gesetzt ist (Gramps Web API 3.26+), kann der Assistent [Änderungen am Stammbaum vorschlagen](../user-guide/chat.md#letting-the-assistant-change-your-tree), die Benutzer nach ihrer Überprüfung anwenden. Der Assistent selbst schreibt niemals in die Datenbank. Vorschläge werden nur Benutzern angeboten, die Objekte hinzufügen, bearbeiten und löschen dürfen, also Editoren und Benutzern mit höheren Rechten, und die den Chat verwenden dürfen.

Das Erstellen korrekter Vorschläge ist für ein Modell schwieriger als das Beantworten von Fragen. Teste die Funktion daher mit deinem Modell, bevor du sie für deine Benutzer aktivierst. Die zusätzlichen Tools machen außerdem jede Anfrage an das Modell etwas größer.
