Backend- ja frontend-kehityksessä voi olla hyödyllistä lähettää manuaalisia kyselyitä Gramps Web API:lle. HTTPien ja jq:n avulla tämä voidaan tehdä kätevästi, mukaan lukien JWT-todennus.

## Asennus

HTTPie asennetaan komennolla `pip`:

```bash
python3 -m pip install httpie
```

Tarvitset HTTPie-version 3.0.0 tai uudemman.

jq voidaan asentaa Ubuntussa komennolla

```bash
sudo apt install jq
```

## Pääsytokenin hakeminen

Pääsytokenin hakemiseksi kysy token-päätepistettä. Oletetaan, että kehitysympäristösi toimii osoitteessa `localhost:5555`, voit käyttää komentoa

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Näet JSON-tokenit tulosteena.

Käyttämällä jq:ta voit myös tallentaa pääsytokenin ympäristömuuttujaan:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Voit nyt käyttää tätä tokenia kaikissa API-kutsuissa, jotka vaativat todennusta, esim.

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Huomaa, että oletusarvoisesti pääsytokenit vanhenevat 15 minuutin kuluttua.
