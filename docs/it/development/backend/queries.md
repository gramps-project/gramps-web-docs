Per lo sviluppo backend e frontend, può essere utile inviare query manuali all'API Web di Gramps. Utilizzando HTTPie e jq, questo può essere fatto comodamente includendo l'autenticazione JWT.

## Installazione

HTTPie si installa con `pip`:

```bash
python3 -m pip install httpie
```

Avrai bisogno della versione 3.0.0 o successiva di HTTPie.

jq può essere installato su Ubuntu tramite

```bash
sudo apt install jq
```

## Recupero di un token di accesso

Per recuperare un token di accesso, interroga l'endpoint del token. Supponendo che la tua istanza di sviluppo sia in esecuzione su `localhost:5555`, puoi utilizzare il comando

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Vedrai i token JSON come output.

Utilizzando jq, puoi anche memorizzare il token di accesso in una variabile di ambiente:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Ora puoi utilizzare questo token in tutte le chiamate API che richiedono autenticazione, ad esempio

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Nota che, per impostazione predefinita, i token di accesso scadranno dopo 15 minuti.
