Para el desarrollo de backend y frontend, puede ser útil enviar consultas manuales a la API web de Gramps. Usando HTTPie y jq, esto se puede hacer de manera conveniente incluyendo la autenticación JWT.

## Instalación

HTTPie se instala con `pip`:

```bash
python3 -m pip install httpie
```

Necesitarás la versión 3.0.0 o superior de HTTPie.

jq se puede instalar en Ubuntu a través de

```bash
sudo apt install jq
```

## Obtención de un token de acceso

Para obtener un token de acceso, consulta el endpoint del token. Suponiendo que tu instancia de desarrollo está corriendo en `localhost:5555`, puedes usar el comando

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

Verás los tokens JSON como salida.

Usando jq, también puedes almacenar el token de acceso en una variable de entorno:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

Ahora puedes usar este token en todas las llamadas a la API que requieran autenticación, por ejemplo:

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

Ten en cuenta que, por defecto, los tokens de acceso expirarán después de 15 minutos.
