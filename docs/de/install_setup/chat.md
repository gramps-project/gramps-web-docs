# Einrichtung des KI-Chats

!!! info
    Der KI-Chat erfordert die Gramps Web API Version 2.5.0 oder höher. Die Version 3.6.0 führte Funktionen zum Aufrufen von Werkzeugen für intelligentere Interaktionen ein.

Die Gramps Web API unterstützt das Stellen von Fragen zur genealogischen Datenbank mithilfe von großen Sprachmodellen (LLM) mit Werkzeugaufrufen.

## Funktionsweise

Der KI-Assistent verwendet spezialisierte Werkzeuge, um direkt auf Ihre Genealogiedaten zuzugreifen. Diese Werkzeuge ermöglichen es dem Assistenten, die Datenbank mit einer Volltextsuche zu durchsuchen, Personen/Ereignisse/Familien/Orte nach bestimmten Kriterien zu filtern, Beziehungen zwischen Individuen zu berechnen und vollständige Datensätze, einschließlich Notizen, abzurufen. Der Assistent beantwortet dann basierend auf den Datensätzen, die er abgerufen hat, und verlinkt in seiner Antwort auf diese.

Seit Gramps Web API 3.24 benötigt der KI-Chat kein Vektor-Einbettungsmodell mehr. Frühere Versionen verwendeten ebenfalls *semantische Suche* (retrieval-augmented generation, RAG), die die Bedeutung einer Frage mit einem Index numerischer Vektoren vergleicht, die für alle Objekte in der Datenbank berechnet wurden. Die semantische Suche ist veraltet und wird in Gramps Web API 3.25 entfernt, siehe [Semantische Suche (veraltet)](#semantische-suche-veraltet) unten.

Um den Chat-Endpunkt in der Gramps Web API zu aktivieren, sind zwei Schritte erforderlich:

1. Installation der erforderlichen Abhängigkeiten,
2. Einrichtung eines LLM-Anbieters.

Die beiden Schritte werden im Folgenden nacheinander beschrieben. Schließlich muss ein Eigentümer oder Administrator [konfigurieren, welche Benutzer auf die Chat-Funktion zugreifen können](users.md#configuring-who-can-use-ai-chat) in den Einstellungen zur Benutzerverwaltung.

## Installation der erforderlichen Abhängigkeiten

Die Standard-Docker-Images für Gramps Web haben bereits alle für den KI-Chat benötigten Abhängigkeiten vorinstalliert.

Bei der Installation der Gramps Web API über `pip` (dies ist bei der Verwendung der Docker-Images nicht erforderlich) werden die notwendigen Abhängigkeiten mit

```bash
pip install gramps_webapi[ai]
```

installiert.

## Semantische Suche (veraltet)

!!! warning "Semantische Suche ist veraltet"
    Die semantische Suche ist seit Gramps Web API 3.24 veraltet und wird in Version 3.25 entfernt. Der KI-Chat und die [Volltextsuche](../user-guide/search.md) benötigen sie nicht. Nach der Entfernung wird die Einstellung `VECTOR_EMBEDDING_MODEL` weiterhin akzeptiert, aber ignoriert. Wenn Sie sie nur zur Aktivierung des KI-Chats gesetzt haben, können Sie sie jetzt zusammen mit den anderen `VECTOR_EMBEDDING_*`-Einstellungen entfernen, was auch den Speicher spart, den das Einbettungsmodell benötigt.

Der Rest dieses Abschnitts beschreibt die semantische Suche für Server, die sie weiterhin mit Gramps Web API 3.24 verwenden.

Wenn die erforderlichen Abhängigkeiten installiert sind, kann die Aktivierung der semantischen Suche so einfach sein wie das Setzen der Konfigurationsoption `VECTOR_EMBEDDING_MODEL` (z. B. durch Setzen der Umgebungsvariable `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), siehe [Serverkonfiguration](configuration.md). Dies kann jeder String eines Modells sein, das von der [Sentence Transformers](https://sbert.net/) Bibliothek unterstützt wird. Siehe die Dokumentation dieses Projekts für Details und die verfügbaren Modelle.

!!! warning
    Beachten Sie, dass die Standard-Docker-Images keine PyTorch-Version mit GPU-Unterstützung enthalten. Wenn Sie Zugriff auf eine GPU haben (was die semantische Indizierung erheblich beschleunigt), installieren Sie bitte eine GPU-fähige Version von PyTorch.

Es gibt mehrere Überlegungen, die bei der Auswahl eines Modells zu beachten sind.

- Wenn Sie das Modell ändern, müssen Sie den semantischen Suchindex für Ihren Baum (oder alle Bäume in einer Multi-Baum-Konfiguration) manuell neu erstellen, andernfalls treten Fehler oder sinnlose Ergebnisse auf. Gramps Web erkennt, wenn das konfigurierte Einbettungsmodell nicht mehr mit dem vorhandenen Index übereinstimmt, und zeigt eine dauerhafte Benachrichtigung an Administratoren an, die sie auffordert, eine vollständige Neuindizierung über die [Verwaltungseinstellungen](../administration/settings.md#semantic-search-index) auszulösen.
- Die Modelle sind ein Kompromiss zwischen Genauigkeit/Allgemeinheit einerseits und Rechenzeit/Speicherplatz andererseits. Wenn Sie Gramps Web API nicht auf einem System ausführen, das Zugriff auf eine leistungsstarke GPU hat, sind größere Modelle in der Praxis normalerweise zu langsam.
- Es sei denn, Ihre gesamte Datenbank ist auf Englisch und alle Ihre Benutzer werden nur erwartet, Fragen im Chat auf Englisch zu stellen, benötigen Sie ein mehrsprachiges Einbettungsmodell, das seltener ist als reine englische Modelle.

Wenn das Modell nicht im lokalen Cache vorhanden ist, wird es heruntergeladen, wenn die Gramps Web API zum ersten Mal mit der neuen Konfiguration gestartet wird. Das Modell `sentence-transformers/distiluse-base-multilingual-cased-v2` ist bereits lokal verfügbar, wenn die Standard-Docker-Images verwendet werden. Dieses Modell ist ein guter Ausgangspunkt und unterstützt mehrsprachige Eingaben.

Bitte teilen Sie Erkenntnisse über verschiedene Modelle mit der Community!

!!! info
    Die Sentence Transformers-Bibliothek verbraucht eine erhebliche Menge an Speicher, was dazu führen kann, dass Arbeitsprozesse beendet werden. Als Faustregel gilt: Bei aktivierter semantischer Suche verbraucht jeder Gunicorn-Arbeiter etwa 200 MB Speicher und jeder Celery-Arbeiter etwa 500 MB Speicher, selbst im Leerlauf, und bis zu 1 GB, wenn Einbettungen berechnet werden. Siehe [CPU- und Speichernutzung begrenzen](cpu-limited.md) für Einstellungen, die die Speichernutzung begrenzen. Darüber hinaus ist es ratsam, eine ausreichend große Swap-Partition bereitzustellen, um OOM-Fehler aufgrund vorübergehender Speicherverbrauchsspitzen zu vermeiden.

### Verwendung einer Remote-Einbettungs-API

Als Alternative zum Ausführen eines lokalen Sentence Transformers-Modells können Sie eine Remote-API für Einbettungen verwenden, die mit OpenAI kompatibel ist, um die semantische Suche durchzuführen. Dies ist nützlich, wenn Sie die Berechnung von Einbettungen an einen separaten Dienst (z. B. [Ollama](https://ollama.com/)) auslagern, einen Cloud-Einbettungsanbieter (z. B. OpenAI) verwenden oder das Laden der Sentence Transformers- und PyTorch-Bibliotheken in den Speicher vermeiden möchten.

Die Remote-API muss mit dem [OpenAI-Einbettungsendpunkt](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`) kompatibel sein.

Um eine Remote-Einbettungs-API zu verwenden, setzen Sie die folgenden Konfigurationsoptionen (siehe [Serverkonfiguration](configuration.md)):

Schlüssel | Beschreibung
----|-------------
`VECTOR_EMBEDDING_MODEL` | Der Modellname, der an den Remote-Anbieter übergeben werden soll
`VECTOR_EMBEDDING_BASE_URL` | Basis-URL der Remote-API
`VECTOR_EMBEDDING_API_KEY` | API-Schlüssel (nur erforderlich, wenn der Anbieter eine Authentifizierung erfordert)

#### Verwendung von Ollama für Einbettungen

Bei der Bereitstellung von Gramps Web mit Docker Compose können Sie einen Ollama-Dienst hinzufügen und ihn sowohl für Einbettungen als auch (optional) für das LLM verwenden:

```yaml
services:
  grampsweb: &grampsweb
    # ... vorhandene Konfiguration ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... vorhandene Konfiguration ...
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

Nachdem Sie die Dienste gestartet haben, ziehen Sie das Einbettungsmodell in Ollama:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Bei der Verwendung von Ollama für Einbettungen sind die Sentence Transformers- und PyTorch-Bibliotheken nicht erforderlich, was den Speicherverbrauch der Gramps Web API-Arbeiter erheblich reduziert.

#### Verwendung von OpenAI für Einbettungen

Um die OpenAI-Einbettungs-API zu verwenden, setzen Sie die Basis-URL auf die OpenAI-API und geben Sie Ihren API-Schlüssel an:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Das Ändern des Einbettungsmodells erfordert eine Neuindizierung aller Datensätze für Ihren Baum (oder alle Bäume in einer Multi-Baum-Konfiguration), da unterschiedliche Modelle Vektoren mit unterschiedlichen Dimensionen erzeugen.

## Einrichtung eines LLM-Anbieters

Die Kommunikation mit dem LLM verwendet das Pydantic AI-Framework, das OpenAI-kompatible APIs unterstützt. Dies ermöglicht die Verwendung eines lokal bereitgestellten LLM über Ollama (siehe [Ollama OpenAI-Kompatibilität](https://ollama.com/blog/openai-compatibility)) oder gehostete APIs wie OpenAI, Anthropic oder Hugging Face TGI (Text Generation Inference). Das LLM wird über die Konfigurationsparameter `LLM_MODEL` und `LLM_BASE_URL` konfiguriert.

### Verwendung eines gehosteten LLM über die OpenAI-API

Bei der Verwendung der OpenAI-API kann `LLM_BASE_URL` ungesetzt bleiben, während `LLM_MODEL` auf eines der OpenAI-Modelle gesetzt werden muss, z. B. `gpt-4o-mini`. Das LLM verwendet Werkzeugaufrufe, um Fragen zu beantworten: Es fragt die Datenbank direkt mit spezialisierten Werkzeugen ab und antwortet basierend auf den Datensätzen, die es findet. Es erfordert kein tiefes genealogisches oder historisches Wissen. Daher können Sie ausprobieren, ob ein kleines/günstiges Modell ausreicht.

Sie müssen sich auch für ein Konto anmelden, einen API-Schlüssel erhalten und ihn in der Umgebungsvariable `OPENAI_API_KEY` speichern.

!!! info
    `LLM_MODEL` ist ein Konfigurationsparameter; wenn Sie ihn über eine Umgebungsvariable setzen möchten, verwenden Sie `GRAMPSWEB_LLM_MODEL` (siehe [Konfiguration](configuration.md)). `OPENAI_API_KEY` ist kein Konfigurationsparameter, sondern eine Umgebungsvariable, die direkt von der Pydantic AI-Bibliothek verwendet wird, daher sollte sie nicht mit einem Präfix versehen werden.

### Verwendung von Mistral AI

Um die gehosteten Modelle von Mistral AI zu verwenden, setzen Sie den Modellnamen beim Festlegen von `LLM_MODEL` mit `mistral:` voran.

Sie müssen sich für ein Mistral AI-Konto anmelden, einen API-Schlüssel erhalten und ihn in der Umgebungsvariable `MISTRAL_API_KEY` speichern. Es ist nicht erforderlich, `LLM_BASE_URL` festzulegen, da Pydantic AI automatisch den richtigen Mistral-API-Endpunkt verwendet.

Beispielkonfiguration bei Verwendung von Docker Compose mit Umgebungsvariablen:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Verwendung eines lokalen LLM über Ollama

[Ollama](https://ollama.com/) ist eine bequeme Möglichkeit, LLMs lokal auszuführen. Bitte konsultieren Sie die Ollama-Dokumentation für Details. Bitte beachten Sie, dass LLMs erhebliche Rechenressourcen benötigen und alle außer den kleinsten Modellen wahrscheinlich zu langsam sein werden, wenn keine GPU-Unterstützung vorhanden ist. Da der Assistent auf Werkzeugaufrufe angewiesen ist, wählen Sie ein Modell, das Werkzeuge unterstützt, wie z. B. [`qwen2.5`](https://ollama.com/library/qwen2.5). Beginnen Sie mit einer kleinen Variante wie `qwen2.5:7b` und versuchen Sie ein größeres, wenn die Antworten nicht gut genug sind. Bitte teilen Sie Ihre Erfahrungen mit der Community!

Bei der Bereitstellung von Gramps Web mit Docker Compose können Sie einen Ollama-Dienst hinzufügen und Gramps Web darauf verweisen:

```yaml
services:
  grampsweb: &grampsweb
    # ... vorhandene Konfiguration ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... vorhandene Konfiguration ...
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

Einige Dinge sind zu beachten:

- Setzen Sie `LLM_MODEL` auf den Ollama-Modellnamen, einschließlich seines Tags (dem Teil nach dem Doppelpunkt, z. B. `7b`), vorangestellt mit `ollama:`. Das Präfix sorgt dafür, dass Pydantic AI die ollama-spezifischen Einstellungen für das Modell verwendet, was die empfohlene Konfiguration ist.
- `LLM_BASE_URL` muss mit `/v1/` enden, z. B. `http://ollama:11434/v1/`.
- Mit dem `ollama:`-Präfix sind weder `OPENAI_API_KEY` noch die Umgebungsvariable `OLLAMA_BASE_URL` erforderlich. Wenn `LLM_BASE_URL` nicht gesetzt ist, fällt Gramps Web auf `OLLAMA_BASE_URL` zurück.
- Alternativ können Sie das Präfix weglassen (z. B. `LLM_MODEL: qwen2.5:7b`) und Ollama über seine generische OpenAI-kompatible API verwenden. In diesem Fall müssen Sie auch die Umgebungsvariable `OPENAI_API_KEY` auf `ollama` setzen (ein beliebiger nicht leerer Wert funktioniert).

Um Probleme mit Ollama zu beheben, können Sie das Debug-Logging aktivieren, indem Sie die Umgebungsvariable `OLLAMA_DEBUG=1` in der Umgebung des Ollama-Dienstes setzen.

!!! info
    Wenn Sie Ollama für den Gramps Web KI-Chat verwenden, unterstützen Sie bitte die Community, indem Sie diese Dokumentation mit fehlenden Details vervollständigen.

### Verwendung anderer Anbieter

Bitte zögern Sie nicht, Dokumentationen für andere Anbieter einzureichen und Ihre Erfahrungen mit der Community zu teilen!
