Pour le développement backend et frontend, il peut être utile d'envoyer des requêtes manuelles à l'API Web Gramps. En utilisant HTTPie et jq, cela peut être fait facilement, y compris l'authentification JWT.

## Installation

HTTPie est installé avec `pip` :

```bash
python3 -m pip install httpie
```

Vous aurez besoin de la version 3.0.0 ou supérieure d'HTTPie.

jq peut être installé sur Ubuntu via

```bash
sudo apt install jq
```

## Récupération d'un jeton d'accès

Pour récupérer un jeton d'accès, interrogez le point de terminaison du jeton. En supposant que votre instance de développement fonctionne sur `localhost:5555`, vous pouvez utiliser la commande

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Vous verrez les jetons JSON en sortie.

En utilisant jq, vous pouvez également stocker le jeton d'accès dans une variable d'environnement :

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Vous pouvez maintenant utiliser ce jeton dans tous les appels API qui nécessitent une authentification, par exemple :

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Notez qu'en règle générale, les jetons d'accès expireront après 15 minutes.
