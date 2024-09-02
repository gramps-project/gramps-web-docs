For backend and frontend development, it can be useful to send manual queries to the Gramps Web API. Using HTTPie and jq, this can be done conveniently including JWT authentication. You can also test the API queries using a tool such as [Postman](https://www.postman.com/).

## Installation

### Testing with HTTPie and jq

HTTPie is installed with `pip`:

```bash
python3 -m pip install httpie
```

You will need HTTPie version 3.0.0 or newer.

jq can be installed in Ubuntu via

```bash
sudo apt install jq
```

### Testing with Postman

Postman can be used on the web, or via the Desktop app, or as an extension for VSCode, or even via the CLI.

See the Postman [Downloads page](https://www.postman.com/downloads/) for all the options.

## Fetching an access token

To fetch an access token, query the token endpoint `/api/token/` (note: the trailing slash is required). We'll assume your development instance is running on `localhost:5555`. Adjust the port accordingly if it's running on any other port, such as port **5000** (default port for Flask apps).

### Using HTTPie and jq
You can use the command

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

You will see the JSON tokens as output.

Using jq, you can also store the access token in an environment variable:

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

### Using Postman

First we'll name the Workspace for all of our requests to the Gramps Web API.

![Name the Workspace](postman-workspace.png)

Next we'll create an Environment which will allow us to store our API token for usage in further requests to the API. We can also name this environment accordingly, so it will be easier to remember that it will be the environment for our Gramps Web API requests.

![Create an Environment](postman-environment.png)

Set the Environment to our newly created Gramps Web API environment.

![Set the Environment](postman-set-environment.png)

Let's store our Gramps Web API password in a secure manner to the Postman Vault. Click on **Vault** at the bottom of the window, and create a key `gramps_localhost_password` and set the value to your password. Using the Vault to save sensitive data is an extra protection that will prevent your password from being synchronized to any cloud service.

!!! info
    When using this for a remote connection we can also restrict this variable to the domain or IP using the **Allowed domains** field, but for localhost we'll just leave the URL field blank, since Postman doesn't always like to deal with ports here, and for requests on ports other than the implicit 80 or 443 ports the Vault will only work if the URL is set WITH the port. There is a little workaround, by **tabbing** out of the URL field after setting the port rather than clicking to lose focus; this will keep the port but you also have to make sure that **http://localhost** or **http://127.0.0.1** correspond exactly with the request, they are not interchangeable. Seeing the slight complications, it's perhaps easier just to leave this blank for localhost connections.

![Store Password in Vault](postman-set-vault.png)

Now we'll prepare a `POST` type request to `http://localhost:5555/api/token/`.

Click on the `+` icon in the tabs section, enter the URL for the request, and click on the default `GET` method to change it to `POST`.

![Set the Request type to POST](postman-post-request.png)

Now we'll set the **Body** to type **raw** (make sure **JSON** is set in the dropdown on the right), and the Body contents to:

```json
{
    "username": "owner",
    "password": "{{vault:gramps_localhost_password}}"
}
```

![Set the Request Body](postman-json-body.png)

!!! info
    Postman has some nice autocomplete features, if you first type `{{}}` and then start typing a variable name within the curly brackets, it will suggest available variables. When you select the previously saved `gramps_localhost_password` variable it will also automatically prepend `vault:` to the variable.

Before clicking on **Send**, we will also create a **Post-response script** which will automatically store the token from the response to our Environment. Click on **Scripts** next to **Body**, select **Post-response**, and set the script to:

```js
pm.environment.set("jwt_token", pm.response.json().access_token);
```

![Set the Post-response script](postman-set-script.png)

Now when you click on **Send**, the access token will be retrieved from the reponse and set as an Environment variable which you can use for further requests.

If you open your **Gramps Web API** Environment again you will see that the `jwt_token` key has been set with the value of the `access_token` from the response. You can optionally further protect the value of this token by changing the **type** from **default** to **secret**.

![Set the Environment variable to type secret](postman-set-env-to-secret.png)

If you go back to the POST request tab, you can also **Save** the request to a **Collection** so that you can easily send the request again in the future. Click on the **Save** button, then click on **New Collection** at the bottom of the **Save to Collection** dialog and name the collection, for example **Gramps Web API localhost**. You can later make other collections, for example to save requests to a remote production instance.

![Save request to collection](postman-save-to-collection.png)

## Making further requests

You can now use this token in all API calls that require authentication.

Note that, by default, access tokens will expire after 15 minutes.

### Using HTTPie and jq

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

### Using Postman

Click on `+` to create a new Request, it will default to the `GET` method. Set the URL to `http://localhost:5555/api/metadata/`. Then set **Authorization** → **Auth Type** to **Bearer token** and set the **Token** value to `{{jwt_token}}`.

![Authorization](postman-authorization.png)

Now when you click on **Send** you should correctly see the Response body. You can again save this Request to your **Gramps Web API localhost** collection for future use. Whenever your `access_token` expires resulting in a failed request, just open your `/api/token/` request from the saved collection and click **Send**, then go back to the initial request and click **Send**.
