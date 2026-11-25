Für die Backend- und Frontend-Entwicklung kann es nützlich sein, manuelle Abfragen an die Gramps-Web-API zu senden. Mit HTTPie und jq ist dies bequem einschließlich JWT-Authentifizierung möglich.

## Installation

HTTPie wird mit `pip` installiert:

```bash
python3 -m pip install httpie
```

Du benötigst HTTPie in Version 3.0.0 oder höher.

jq kann unter Ubuntu folgendermaßen installiert werden:

```bash
sudo apt install jq
```

## Abrufen eines Zugriffstokens

Um ein Zugriffstoken abzurufen, frage den Token-Endpunkt ab. Vorausgesetzt, deine Entwicklungsinstanz läuft auf `localhost:5555`, kannst du den folgenden Befehl verwenden:

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Die JSON-Token werden als Ausgabe angezeigt.

Mit jq kannst du das Zugriffstoken auch in einer Umgebungsvariablen speichern:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Du kannst dieses Token nun in allen API-Aufrufen verwenden, die eine Authentifizierung erfordern, z. B.

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Beachte, dass Zugriffstoken standardmäßig nach 15 Minuten ablaufen.
