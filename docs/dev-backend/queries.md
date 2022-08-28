For backend and frontend development, it can be useful to send manual queries to the Gramps Web API. Using HTTPie and jq, this can be done conveniently including JWT authentication.

## Installation

HTTPie is installed with `pip`:

```bash
python3 -m pip install httpie
```

You will need HTTPie version 3.0.0 or newer.

jq can be installed in Ubuntu via

```bash
sudo apt install jq
```

## Fetching an access token

To fetch an access token, query the token endpoint:

Assuming your development instance is running on `localhost:5555`, you can use the command

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

You will see the JSON tokens as output.

Using jq, you can also store the access token in an environment variable:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

You can now use this token in all API calls that require authentication, e.g.

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```