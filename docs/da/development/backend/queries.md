For backend- og frontend-udvikling kan det være nyttigt at sende manuelle forespørgsler til Gramps Web API. Ved at bruge HTTPie og jq kan dette gøres bekvemt, herunder JWT-godkendelse.

## Installation

HTTPie installeres med `pip`:

```bash
python3 -m pip install httpie
```

Du skal bruge HTTPie version 3.0.0 eller nyere.

jq kan installeres i Ubuntu via

```bash
sudo apt install jq
```

## Hentning af en adgangstoken

For at hente en adgangstoken skal du forespørge token-endepunktet. Forudsat at din udviklingsinstans kører på `localhost:5555`, kan du bruge kommandoen

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Du vil se JSON-tokens som output.

Ved at bruge jq kan du også gemme adgangstoken i en miljøvariabel:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Du kan nu bruge denne token i alle API-opkald, der kræver godkendelse, f.eks.

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Bemærk, at adgangstokens som standard udløber efter 15 minutter.
