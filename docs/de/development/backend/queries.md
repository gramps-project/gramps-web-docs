Für die Backend- und Frontend-Entwicklung kann es nützlich sein, manuelle Abfragen an die Gramps Web API zu senden. Mit HTTPie und jq kann dies bequem unter Verwendung von JWT-Authentifizierung erfolgen.

## Installation

HTTPie wird mit `pip` installiert:

```bash
python3 -m pip install httpie
```

Sie benötigen HTTPie Version 3.0.0 oder neuer.

jq kann in Ubuntu über

```bash
sudo apt install jq
```

installiert werden.

## Abrufen eines Zugriffstokens

Um ein Zugriffstoken abzurufen, fragen Sie den Token-Endpunkt ab. Angenommen, Ihre Entwicklungsinstanz läuft auf `localhost:5555`, können Sie den Befehl verwenden

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Sie sehen die JSON-Tokens als Ausgabe.

Mit jq können Sie das Zugriffstoken auch in einer Umgebungsvariable speichern:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Sie können dieses Token jetzt in allen API-Aufrufen verwenden, die eine Authentifizierung erfordern, z.B.

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Bitte beachten Sie, dass Zugriffstokens standardmäßig nach 15 Minuten ablaufen.
