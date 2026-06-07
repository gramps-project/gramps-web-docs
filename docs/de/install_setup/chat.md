# Einrichtung des KI-Chat

!!! info
    Der KI-Chat erfordert die Gramps Web API Version 2.5.0 oder höher. Die Version 3.6.0 führte Funktionen zum Aufrufen von Werkzeugen für intelligentere Interaktionen ein.

Die Gramps Web API unterstützt das Stellen von Fragen zur genealogischen Datenbank mithilfe von großen Sprachmodellen (LLM) über eine Technik namens retrieval-augmented generation (RAG) in Kombination mit dem Aufrufen von Werkzeugen.

## Funktionsweise

Der KI-Assistent verwendet zwei komplementäre Ansätze:

**Retrieval-Augmented Generation (RAG)**: Ein *Vektor-Einbettungsmodell* erstellt einen Index aller Objekte in der Gramps-Datenbank in Form von numerischen Vektoren, die die Bedeutung der Objekte kodieren. Wenn ein Benutzer eine Frage stellt, wird diese Frage ebenfalls in einen Vektor umgewandelt und mit den Objekten in der Datenbank verglichen. Diese *semantische Suche* gibt Objekte zurück, die der Frage semantisch am ähnlichsten sind.

**Tool Calling (v3.6.0+)**: Der KI-Assistent kann jetzt spezialisierte Werkzeuge verwenden, um direkt auf Ihre genealogischen Daten zuzugreifen. Diese Werkzeuge ermöglichen es dem Assistenten, die Datenbank zu durchsuchen, Personen/Ereignisse/Familien/Orte nach bestimmten Kriterien zu filtern, Beziehungen zwischen Individuen zu berechnen und detaillierte Objektinformationen abzurufen. Dies macht den Assistenten viel fähiger, komplexe genealogische Fragen genau zu beantworten.

Um den Chat-Endpunkt in der Gramps Web API zu aktivieren, sind drei Schritte erforderlich:

1. Installation der erforderlichen Abhängigkeiten,
2. Aktivierung der semantischen Suche,
3. Einrichtung eines LLM-Anbieters.

Die drei Schritte werden im Folgenden nacheinander beschrieben. Schließlich muss ein Eigentümer oder Administrator [konfigurieren, welche Benutzer auf die Chat-Funktion zugreifen können](users.md#configuring-who-can-use-ai-chat) in den Einstellungen zur Benutzerverwaltung.

## Installation der erforderlichen Abhängigkeiten

Der KI-Chat erfordert die Installation der Bibliotheken Sentence Transformers und PyTorch.

Die Standard-Docker-Images für Gramps Web haben diese bereits für die Architekturen `amd64` (z. B. 64-Bit-Desktop-PC) und `arm64` (z. B. 64-Bit-Raspberry Pi) vorinstalliert. Leider wird der KI-Chat auf der Architektur `armv7` (z. B. 32-Bit-Raspberry Pi) aufgrund fehlender PyTorch-Unterstützung nicht unterstützt.

Bei der Installation der Gramps Web API über `pip` (dies ist bei Verwendung der Docker-Images nicht erforderlich) werden die erforderlichen Abhängigkeiten mit

```bash
pip install gramps_webapi[ai]
```

installiert.

## Aktivierung der semantischen Suche

Wenn die erforderlichen Abhängigkeiten installiert sind, kann die Aktivierung der semantischen Suche so einfach sein wie das Setzen der Konfigurationsoption `VECTOR_EMBEDDING_MODEL` (z. B. durch Setzen der Umgebungsvariable `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), siehe [Serverkonfiguration](configuration.md). Dies kann jede Zeichenfolge eines Modells sein, das von der [Sentence Transformers](https://sbert.net/) Bibliothek unterstützt wird. Siehe die Dokumentation dieses Projekts für Details und die verfügbaren Modelle.

!!! warning
    Beachten Sie, dass die Standard-Docker-Images keine PyTorch-Version mit GPU-Unterstützung enthalten. Wenn Sie Zugriff auf eine GPU haben (was die semantische Indizierung erheblich beschleunigt), installieren Sie bitte eine GPU-fähige Version von PyTorch.

Es gibt mehrere Überlegungen, die bei der Auswahl eines Modells zu beachten sind.

- Wenn Sie das Modell ändern, müssen Sie den semantischen Suchindex für Ihren Baum (oder alle Bäume in einer Multi-Baum-Konfiguration) manuell neu erstellen, andernfalls treten Fehler oder sinnlose Ergebnisse auf. Gramps Web erkennt, wenn das konfigurierte Einbettungsmodell nicht mehr mit dem vorhandenen Index übereinstimmt, und zeigt eine dauerhafte Benachrichtigung an Administratoren an, die sie auffordert, eine vollständige Neuindizierung über die [Verwaltungseinstellungen](../administration/settings.md#semantic-search-index) auszulösen.
- Die Modelle sind ein Kompromiss zwischen Genauigkeit/Allgemeinheit einerseits und Rechenzeit/Speicherplatz andererseits. Wenn Sie die Gramps Web API nicht auf einem System ausführen, das Zugriff auf eine leistungsstarke GPU hat, sind größere Modelle in der Praxis normalerweise zu langsam.
- Es sei denn, Ihre gesamte Datenbank ist auf Englisch und alle Ihre Benutzer werden nur erwartet, Fragen im Chat auf Englisch zu stellen, benötigen Sie ein mehrsprachiges Einbettungsmodell, das seltener ist als reine englische Modelle.

Wenn das Modell nicht im lokalen Cache vorhanden ist, wird es heruntergeladen, wenn die Gramps Web API zum ersten Mal mit der neuen Konfiguration gestartet wird. Das Modell `sentence-transformers/distiluse-base-multilingual-cased-v2` ist bereits lokal verfügbar, wenn die Standard-Docker-Images verwendet werden. Dieses Modell ist ein guter Ausgangspunkt und unterstützt mehrsprachige Eingaben.

Bitte teilen Sie Erkenntnisse über verschiedene Modelle mit der Community!

!!! info
    Die Sentence Transformers-Bibliothek verbraucht eine erhebliche Menge an Speicher, was dazu führen kann, dass Arbeitsprozesse beendet werden. Als Faustregel gilt, dass bei aktivierter semantischer Suche jeder Gunicorn-Arbeiter etwa 200 MB Speicher und jeder Celery-Arbeiter etwa 500 MB Speicher selbst im Leerlauf verbraucht, und bis zu 1 GB, wenn Einbettungen berechnet werden. Siehe [CPU- und Speichernutzung begrenzen](cpu-limited.md) für Einstellungen, die die Speichernutzung begrenzen. Darüber hinaus ist es ratsam, eine ausreichend große Swap-Partition bereitzustellen, um OOM-Fehler aufgrund vorübergehender Speicherverbrauchsspitzen zu vermeiden.

## Einrichtung eines LLM-Anbieters

Die Kommunikation mit dem LLM verwendet das Pydantic AI-Framework, das OpenAI-kompatible APIs unterstützt. Dies ermöglicht die Verwendung eines lokal bereitgestellten LLM über Ollama (siehe [Ollama OpenAI-Kompatibilität](https://ollama.com/blog/openai-compatibility)) oder gehostete APIs wie OpenAI, Anthropic oder Hugging Face TGI (Text Generation Inference). Das LLM wird über die Konfigurationsparameter `LLM_MODEL` und `LLM_BASE_URL` konfiguriert.

### Verwendung eines gehosteten LLM über die OpenAI API

Bei der Verwendung der OpenAI API kann `LLM_BASE_URL` ungesetzt bleiben, während `LLM_MODEL` auf eines der OpenAI-Modelle, z. B. `gpt-4o-mini`, gesetzt werden muss. Das LLM verwendet sowohl RAG als auch Tool Calling, um Fragen zu beantworten: Es wählt relevante Informationen aus den Ergebnissen der semantischen Suche aus und kann die Datenbank direkt mit spezialisierten Werkzeugen abfragen. Es erfordert kein tiefes genealogisches oder historisches Wissen. Daher können Sie ausprobieren, ob ein kleines/günstiges Modell ausreicht.

Sie müssen sich auch für ein Konto anmelden, einen API-Schlüssel erhalten und ihn in der Umgebungsvariable `OPENAI_API_KEY` speichern.

!!! info
    `LLM_MODEL` ist ein Konfigurationsparameter; wenn Sie ihn über eine Umgebungsvariable setzen möchten, verwenden Sie `GRAMPSWEB_LLM_MODEL` (siehe [Konfiguration](configuration.md)). `OPENAI_API_KEY` ist kein Konfigurationsparameter, sondern eine Umgebungsvariable, die direkt von der Pydantic AI-Bibliothek verwendet wird, daher sollte sie nicht mit einem Präfix versehen werden.

### Verwendung von Mistral AI

Um die gehosteten Modelle von Mistral AI zu verwenden, setzen Sie den Modellnamen beim Setzen von `LLM_MODEL` mit `mistral:` voraus.

Sie müssen sich für ein Mistral AI-Konto anmelden, einen API-Schlüssel erhalten und ihn in der Umgebungsvariable `MISTRAL_API_KEY` speichern. Es ist nicht erforderlich, `LLM_BASE_URL` zu setzen, da Pydantic AI automatisch den richtigen Mistral API-Endpunkt verwendet.

Beispielkonfiguration bei Verwendung von Docker Compose mit Umgebungsvariablen:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Verwendung eines lokalen LLM über Ollama

[Ollama](https://ollama.com/) ist eine bequeme Möglichkeit, LLMs lokal auszuführen. Bitte konsultieren Sie die Ollama-Dokumentation für Details. Bitte beachten Sie, dass LLMs erhebliche Rechenressourcen benötigen und alle bis auf die kleinsten Modelle wahrscheinlich zu langsam sein werden, wenn keine GPU-Unterstützung vorhanden ist. Sie können ausprobieren, ob [`tinyllama`](https://ollama.com/library/tinyllama) Ihren Anforderungen entspricht. Wenn nicht, probieren Sie eines der größeren Modelle aus. Bitte teilen Sie Ihre Erfahrungen mit der Community!

Beim Bereitstellen von Gramps Web mit Docker Compose können Sie einen Ollama-Dienst hinzufügen

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

und dann den Konfigurationsparameter `LLM_BASE_URL` auf `http://ollama:11434/v1` setzen. Setzen Sie `LLM_MODEL` auf ein von Ollama unterstütztes Modell und ziehen Sie es in Ihrem Container mit `ollama pull <model>` herunter. Schließlich setzen Sie `OPENAI_API_KEY` auf `ollama`.

Um Probleme mit Ollama zu beheben, können Sie das Debug-Logging aktivieren, indem Sie die Umgebungsvariable `OLLAMA_DEBUG=1` in der Umgebung des Ollama-Dienstes setzen.

!!! info
    Wenn Sie Ollama für den Gramps Web KI-Chat verwenden, unterstützen Sie bitte die Community, indem Sie diese Dokumentation mit fehlenden Details vervollständigen.

### Verwendung anderer Anbieter

Bitte zögern Sie nicht, Dokumentationen für andere Anbieter einzureichen und Ihre Erfahrungen mit der Community zu teilen!
