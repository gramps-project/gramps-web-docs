Para desenvolvimento de backend e frontend, pode ser útil enviar consultas manuais à API Web do Gramps. Usando HTTPie e jq, isso pode ser feito de forma conveniente, incluindo autenticação JWT.

## Instalação

HTTPie é instalado com `pip`:

```bash
python3 -m pip install httpie
```

Você precisará da versão 3.0.0 ou mais recente do HTTPie.

jq pode ser instalado no Ubuntu via

```bash
sudo apt install jq
```

## Obtendo um token de acesso

Para obter um token de acesso, consulte o endpoint do token. Supondo que sua instância de desenvolvimento esteja rodando em `localhost:5555`, você pode usar o comando

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Você verá os tokens JSON como saída.

Usando jq, você também pode armazenar o token de acesso em uma variável de ambiente:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Agora você pode usar esse token em todas as chamadas da API que requerem autenticação, por exemplo:

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Observe que, por padrão, os tokens de acesso expirarão após 15 minutos.
