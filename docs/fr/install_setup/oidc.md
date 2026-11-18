# Authentification OIDC

Gramps Web prend en charge l'authentification OpenID Connect (OIDC), permettant aux utilisateurs de se connecter en utilisant des fournisseurs d'identité externes. Cela inclut les fournisseurs intégrés Google et Microsoft, ainsi que des fournisseurs OIDC personnalisés comme Keycloak, Authentik et Authelia.

!!! warning "GitHub en tant que fournisseur OIDC n'est plus pris en charge"
    Si vous avez `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` définis à partir d'une version antérieure, supprimez-les – ils sont désormais ignorés, et les utilisateurs qui se sont précédemment connectés via GitHub ne peuvent plus se connecter de cette manière. GitHub est un fournisseur OAuth 2.0, pas un fournisseur OpenID Connect, et n'a jamais renvoyé la revendication sur laquelle Gramps Web s'appuie pour l'identité, donc il n'a jamais été totalement fiable.

## Vue d'ensemble

L'authentification OIDC vous permet de :

- Utiliser des fournisseurs d'identité externes pour l'authentification des utilisateurs
- Prendre en charge plusieurs fournisseurs d'authentification simultanément
- Mapper les groupes/rôles OIDC aux rôles d'utilisateur de Gramps Web
- Mettre en œuvre l'authentification unique (SSO) et la déconnexion unique
- Désactiver optionnellement l'authentification locale par nom d'utilisateur/mot de passe

## Configuration

Pour activer l'authentification OIDC, vous devez configurer les paramètres appropriés dans votre fichier de configuration Gramps Web ou dans les variables d'environnement. Consultez la page [Configuration du serveur](configuration.md#settings-for-oidc-authentication) pour une liste complète des paramètres OIDC disponibles.

!!! info
    Lorsque vous utilisez des variables d'environnement, n'oubliez pas de préfixer chaque nom de paramètre avec `GRAMPSWEB_` (par exemple, `GRAMPSWEB_OIDC_ENABLED`). Consultez [Fichier de configuration vs. variables d'environnement](configuration.md#configuration-file-vs-environment-variables) pour plus de détails.

### Fournisseurs intégrés

Gramps Web prend en charge les fournisseurs d'identité populaires intégrés. Pour les utiliser, vous devez simplement fournir l'ID client et le secret client :

- **Google** : `OIDC_GOOGLE_CLIENT_ID` et `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft** : `OIDC_MICROSOFT_CLIENT_ID` et `OIDC_MICROSOFT_CLIENT_SECRET`

Vous pouvez configurer plusieurs fournisseurs simultanément. Le système détectera automatiquement quels fournisseurs sont disponibles en fonction des valeurs de configuration.

!!! tip "Microsoft : déploiements à locataire unique"
    Le fournisseur Microsoft intégré utilise le point de terminaison multi-locataire `/common` et accepte les connexions de tout compte Microsoft par conception. Si vous souhaitez uniquement autoriser les utilisateurs de votre propre locataire, utilisez le [fournisseur OIDC personnalisé](#custom-oidc-providers) avec l'URL de l'émetteur spécifique à votre locataire à la place, ce qui maintient la validation de l'émetteur active et restreint les connexions à ce locataire.

### Fournisseurs OIDC personnalisés

Pour les fournisseurs OIDC personnalisés (comme Keycloak, Authentik, Authelia, ou un locataire Microsoft Entra à locataire unique), utilisez ces paramètres :

Clé | Description
----|-------------
`OIDC_ENABLED` | Booléen, si l'authentification OIDC doit être activée. Défini sur `True`.
`OIDC_ISSUER` | L'URL de l'émetteur de votre fournisseur. La découverte est récupérée à partir de `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID client pour votre fournisseur OIDC
`OIDC_CLIENT_SECRET` | Secret client pour votre fournisseur OIDC
`OIDC_NAME` | Nom d'affichage personnalisé (optionnel, par défaut "OIDC")
`OIDC_SCOPES` | Scopes OAuth (optionnel, par défaut "openid email profile")
`OIDC_USERNAME_CLAIM` | Revendication utilisée pour générer le nom d'utilisateur (optionnel, par défaut "preferred_username")
`OIDC_PKCE` | Si PKCE doit être utilisé, voir [PKCE](#pkce) (optionnel, activé automatiquement si le fournisseur le prend en charge)

### PKCE

Depuis l'API Gramps Web 3.23, Gramps Web prend en charge [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, méthode `S256`) pour le flux de code d'autorisation. Certains fournisseurs d'identité, tels que Pocket ID, peuvent être configurés pour *exiger* PKCE pour un client, et refuser les connexions qui ne l'utilisent pas. Les anciennes versions de l'API Gramps Web n'utilisent jamais PKCE, donc les connexions avec un tel client échouent.

La décision d'utiliser PKCE est prise lors de la connexion comme suit :

- Si `OIDC_PKCE` est défini sur `True`, PKCE est utilisé.
- Si `OIDC_PKCE` est défini sur `False`, PKCE n'est pas utilisé, même si le fournisseur le prend en charge.
- Si `OIDC_PKCE` n'est pas défini, ou défini mais vide, PKCE est utilisé si le document de découverte du fournisseur (`/.well-known/openid-configuration`) liste `S256` dans `code_challenge_methods_supported`, et n'est pas utilisé sinon.

Pour la plupart des configurations, vous n'avez pas besoin de définir quoi que ce soit. Définissez `OIDC_PKCE` sur `True` si votre fournisseur exige PKCE mais ne fait pas de publicité pour `S256` dans son document de découverte, et sur `False` si votre fournisseur fait de la publicité pour `S256` mais le gère mal. En tant que variables d'environnement, les booléens doivent être en minuscules (`GRAMPSWEB_OIDC_PKCE=true`), voir [Configuration](configuration.md).

Pour les fournisseurs intégrés, les options correspondantes sont `OIDC_GOOGLE_PKCE` et `OIDC_MICROSOFT_PKCE`.

Le vérificateur de code PKCE est conservé dans la session de l'utilisateur entre la redirection vers le fournisseur et le rappel, donc cela ne nécessite aucun changement dans les URI de redirection.

### Configurations multi-arbres

Sur un serveur multi-arbres, un utilisateur qui se connecte avec une identité déjà liée à un compte Gramps Web est connecté à l'arbre de ce compte, donc la page de connexion simple fonctionne pour eux.

Pour créer un compte *nouveau* avec une identité OIDC, Gramps Web doit savoir à quel arbre il doit appartenir. Les nouveaux utilisateurs doivent donc commencer par le lien d'enregistrement de l'arbre (`/register/<tree_id>`, voir [Lien d'enregistrement](../administration/users.md#registration-link-multi-tree-setup-only)), ou depuis la page de connexion de l'arbre (`/login/<tree_id>`). Les deux offrent les fournisseurs configurés. Se connecter avec une identité inconnue depuis la page de connexion simple est refusé avec un message pointant vers le lien d'enregistrement. Cela nécessite l'API Gramps Web 3.25.3 et Gramps Web 26.11.2 ou plus récent.

En coulisses, la connexion commence par :

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

où `tree` est optionnel sauf si un nouveau compte est créé. Passer l'ID d'un arbre qui n'existe pas échoue la connexion. Sur un serveur à arbre unique, `tree` est optionnel, mais s'il est donné, il doit correspondre à l'`TREE` configuré.

Une identité OIDC est liée à exactement un compte Gramps Web, qui appartient à son tour à exactement un arbre – se connecter à un arbre différent échoue plutôt que de déplacer le compte. Il n'y a aucun moyen de lier une seule identité au fournisseur à des comptes dans plusieurs arbres ; les utilisateurs qui ont besoin d'accéder à plusieurs arbres ont besoin d'identités distinctes chez le fournisseur (par exemple, des noms d'utilisateur ou des comptes distincts).

!!! warning
    Un compte administrateur de site sans arbre associé (voir [création d'un compte admin](../administration/owner.md)) ne peut pas être créé via OIDC, car un compte créé par une connexion OIDC appartient toujours à un arbre. Créez de tels comptes avec un nom d'utilisateur et un mot de passe locaux.

### Applications natives

Les applications natives, telles que les applications mobiles pour Gramps Web, peuvent permettre à l'utilisateur de se connecter dans le navigateur du système et de recevoir le résultat à un lien `https` de l'application. Depuis l'API Gramps Web 3.26, cela fonctionne si le lien est répertorié dans `OIDC_ALLOWED_REDIRECT_URIS`, par exemple :

```
GRAMPSWEB_OIDC_ALLOWED_REDIRECT_URIS='["https://app.example.com/oidc-callback"]'
```

La documentation de l'application vous indique quel lien ajouter. Les URI de redirection enregistrées auprès du fournisseur d'identité restent les mêmes.

## URI de redirection requises

Lorsque vous configurez votre fournisseur OIDC, vous devez enregistrer l'URI de redirection suivante :

**Pour les fournisseurs OIDC qui prennent en charge les jokers : (par exemple, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Où `*` est un joker regex. Selon l'interpréteur regex de votre fournisseur, cela pourrait également être un `.*` ou similaire. Assurez-vous que le regex est activé si votre fournisseur l'exige (par exemple, Authentik).

**Pour les fournisseurs OIDC qui ne prennent pas en charge les jokers : (par exemple, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

L'arbre ne fait jamais partie de l'URI de redirection, même sur des serveurs multi-arbres – il voyage séparément dans la session, puisque les fournisseurs exigent que l'URI de redirection corresponde exactement à celle enregistrée.

## Mapping des rôles

Gramps Web peut mapper automatiquement les groupes ou rôles OIDC de votre fournisseur d'identité aux rôles d'utilisateur de Gramps Web. Cela vous permet de gérer les autorisations des utilisateurs de manière centralisée dans votre fournisseur d'identité. Le mapping des rôles fonctionne de la même manière pour tous les fournisseurs, intégrés ou personnalisés.

### Configuration

Utilisez ces paramètres pour configurer le mapping des rôles :

Clé | Description
----|-------------
`OIDC_ROLE_CLAIM` | Le nom de la revendication dans le jeton OIDC qui contient les groupes/rôles de l'utilisateur. Par défaut "groups". Les chemins avec des points sont pris en charge, par exemple `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Admin" de Gramps
`OIDC_GROUP_OWNER` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Owner" de Gramps
`OIDC_GROUP_EDITOR` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Editor" de Gramps
`OIDC_GROUP_CONTRIBUTOR` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Contributor" de Gramps
`OIDC_GROUP_MEMBER` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Member" de Gramps
`OIDC_GROUP_GUEST` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Guest" de Gramps

### Comportement du mapping des rôles

Si aucun paramètre `OIDC_GROUP_*` n'est configuré, le mapping des rôles est désactivé et les rôles sont gérés manuellement dans Gramps Web ; de nouveaux comptes OIDC sont alors créés désactivés et doivent être approuvés par un propriétaire ou un administrateur existant (voir [Première connexion et initialisation](#first-login-and-bootstrapping) ci-dessous).

Une fois le mapping des rôles configuré, à chaque connexion :

- Si la revendication de rôle est présente et que l'utilisateur appartient à un groupe mappé, il obtient le rôle correspondant.
- Si la revendication de rôle est présente mais que l'utilisateur n'appartient à aucun groupe mappé, son rôle est défini sur désactivé. C'est un défaut de sécurité, pas un bug – Gramps Web ne peut pas déduire un rôle pour un groupe qu'il ne reconnaît pas.
- Si la revendication de rôle est complètement absente du jeton, le rôle existant reste inchangé ; un nouveau compte est toujours par défaut désactivé.

!!! warning "Google n'envoie pas de revendication de groupes"
    Les jetons de Google n'incluent jamais de revendication `groups`, donc avec le mapping des rôles activé, les connexions Google tombent sous "revendication absente" ci-dessus : les utilisateurs existants conservent leur rôle, mais les nouveaux utilisateurs Google sont créés désactivés et nécessitent une approbation manuelle. Gardez cela à l'esprit avant d'activer le mapping des rôles uniquement pour un autre fournisseur – cela ne désactive pas, en soi, les utilisateurs Google existants.

Microsoft Entra renvoie des rôles d'application et des adhésions de groupe uniquement dans le jeton ID, pas depuis le point de terminaison userinfo. Gramps Web fusionne les revendications du jeton ID dans la réponse userinfo afin que `OIDC_ROLE_CLAIM` fonctionne de la même manière que pour les autres fournisseurs ; lorsque les deux contiennent une revendication, la valeur userinfo prend le pas.

## Première connexion et initialisation

Les nouveaux comptes créés via OIDC commencent désactivés à moins que le mapping des rôles ne leur attribue un rôle (voir ci-dessus). Sur une instance toute neuve, personne ne peut approuver un compte désactivé, et si `OIDC_DISABLE_LOCAL_AUTH` est également activé, il n'y a pas de connexion par mot de passe sur laquelle se rabattre.

!!! warning "Configurez un groupe propriétaire/admin avant la première connexion"
    Avant que quiconque ne se connecte via OIDC pour la première fois, définissez `OIDC_GROUP_OWNER` (ou `OIDC_GROUP_ADMIN`) et assurez-vous que le premier utilisateur appartient à ce groupe chez le fournisseur. Sinon, l'instance ne peut pas être initialisée via OIDC.

## Comptes et noms d'utilisateur

Les comptes créés via OIDC obtiennent un nom d'utilisateur généré, attribué une fois à la création du compte et jamais changé lors des connexions ultérieures :

- Fournisseurs intégrés : `<provider>_<valeur de revendication>`, par exemple `microsoft_alice@contoso.com`
- Fournisseur personnalisé : la valeur de revendication brute, par exemple `alice`

Un suffixe numérique est ajouté en cas de collision. Il n'y a aucun moyen de renommer le nom d'utilisateur d'un compte créé par OIDC par la suite ; en revanche, le nom complet et l'adresse e-mail sont actualisés à chaque connexion.

Une connexion OIDC ne s'attache jamais à un compte local existant qui partage par hasard son adresse e-mail – c'est délibéré, car lier des comptes par e-mail est un vecteur de prise de contrôle de compte. Un utilisateur qui a déjà un compte local obtient un deuxième compte distinct la première fois qu'il se connecte via OIDC, à moins qu'il ne lie d'abord le fournisseur à son compte.

Depuis l'API Gramps Web 3.24, les utilisateurs peuvent lier des identités OIDC à leur compte existant, et les lister et les dissocier, sous [Paramètres utilisateur > Méthodes de connexion liées](../user-guide/settings.md#linked-sign-in-methods). Le lien nécessite une connexion récente et est confirmé avec le propre jeton de l'utilisateur, donc cela fonctionne également lorsque le frontend est sur une origine différente de l'API. Une identité ne peut appartenir qu'à un seul compte ; pour lier une identité qui a déjà son propre compte, un administrateur doit d'abord supprimer ce compte (ses modifications restent, mais l'historique des révisions ne montre plus son nom). La dernière identité liée ne peut être dissociée qu'avec le mot de passe actuel du compte, et pas du tout si `OIDC_DISABLE_LOCAL_AUTH` est défini.

Les adresses e-mail du fournisseur ne sont stockées que si le fournisseur les marque comme vérifiées (ou omet complètement la revendication `email_verified`) ; sinon, la connexion se poursuit sans stocker d'adresse e-mail. Étant donné que les adresses e-mail n'ont pas à être uniques (depuis l'API Gramps Web 3.22), une adresse est stockée même si un autre compte l'utilise déjà.

## Déconnexion OIDC

Gramps Web prend en charge la déconnexion unique (déconnexion SSO) pour les fournisseurs OIDC. `GET /api/oidc/logout/` recherche le `end_session_endpoint` du fournisseur et le renvoie comme `logout_url` dans la réponse ; c'est le frontend de Gramps Web qui navigue vers cette URL pour mettre réellement fin à la session auprès du fournisseur d'identité. `logout_url` est `null` lorsque le fournisseur n'a pas de `end_session_endpoint`.

!!! warning "Les jetons ne sont pas révoqués lors de la déconnexion"
    Se déconnecter ne met fin qu'à la session du navigateur ; il n'y a actuellement aucun moyen de révoquer un jeton Gramps Web qui a déjà été émis. Les jetons restent valides jusqu'à leur expiration (`JWT_ACCESS_TOKEN_EXPIRES`, par défaut 15 minutes pour les jetons d'accès), peu importe si l'utilisateur s'est depuis déconnecté de Gramps Web ou du fournisseur d'identité.

## Dépannage

Commencez au point où la connexion s'arrête et suivez la branche. Gramps Web enregistre la raison d'un rappel échoué (recherchez `OIDC callback error for provider` dans le journal du serveur), qui est généralement plus spécifique que le message affiché dans le navigateur.

**1. Le bouton de connexion est-il manquant ?**

- Vérifiez `<BASE_URL>/api/oidc/config/`. Si `enabled` est `false` ou si `providers` est vide, OIDC n'est pas configuré : `OIDC_ENABLED` doit être `True`, et un fournisseur personnalisé a besoin à la fois de `OIDC_ISSUER` et `OIDC_CLIENT_ID`.
- Un fournisseur intégré (Google, Microsoft) n'est enregistré que si son ID client et son secret client sont tous deux définis.
- Regardez dans le journal du serveur au démarrage pour `Could not load discovery document`. Cela signifie que le serveur n'a pas pu atteindre `<issuer>/.well-known/openid-configuration` (ou `OIDC_OPENID_CONFIG_URL`). Il réessaie lors de la première utilisation, mais le conteneur Gramps Web doit être capable de résoudre et d'atteindre l'URL de l'émetteur lui-même, pas seulement votre navigateur.

**2. Le navigateur reçoit-il une erreur juste après avoir été envoyé au fournisseur ?**

L'erreur est affichée par le fournisseur d'identité, avant que vous ne vous connectiez.

- *"mismatch d'URI de redirection"* (ou similaire) : l'URI de redirection enregistrée auprès du fournisseur doit correspondre exactement, y compris le schéma, l'hôte, le port et l'ID du fournisseur. Voir [URI de redirection requises](#required-redirect-uris). Notez qu'elle est construite à partir de `BASE_URL`, donc un mauvais `BASE_URL` donne une mauvaise URI de redirection.
- *Une erreur PKCE* (par exemple `invalid_request`, "code challenge required", ou un paramètre `code_challenge` manquant) : le fournisseur exige PKCE mais Gramps Web ne l'a pas envoyé. Allez à [la branche PKCE](#pkce-branch) ci-dessous.

**3. Le fournisseur accepte la connexion mais Gramps Web affiche ensuite une erreur ?**

- *`mismatching_state`, ou l'erreur mentionne la session ou l'état* : le navigateur n'a pas renvoyé le cookie de session que Gramps Web a défini lorsque la connexion a commencé. Ce cookie transporte également le vérificateur de code PKCE. Assurez-vous que l'adresse dans le navigateur correspond à `BASE_URL` (même schéma et hôte), qu'un proxy inverse passe les cookies et l'hôte d'origine, et que la connexion est commencée et terminée dans le même onglet ou fenêtre du navigateur.
- *`OIDC authentication failed for <provider>` (HTTP 401)* : vérifiez le journal du serveur pour la raison sous-jacente. Les causes courantes sont un mauvais secret client, une URL d'émetteur qui ne correspond pas à la revendication `iss` des jetons, et le fournisseur renvoyant une erreur au rappel (par exemple PKCE, voir ci-dessous).
- *Trop de tentatives* : les points de terminaison de connexion et de rappel sont limités en fréquence (5 demandes par minute). Attendez une minute et réessayez.

**4. La connexion réussit mais vous voyez "Compte en cours d'examen", ou vous ne pouvez rien faire ?**

De nouveaux comptes sont créés désactivés à moins que le mapping des rôles n'attribue un rôle. Voir [Première connexion et initialisation](#first-login-and-bootstrapping) et [Comportement du mapping des rôles](#role-mapping-behavior). Un administrateur peut également activer le compte sous Paramètres > Administration > Gérer les utilisateurs.

### Branche PKCE

Gramps Web décide d'utiliser PKCE lorsque le processus de connexion commence (voir [PKCE](#pkce)). Pour savoir ce qui s'est passé pour votre configuration, suivez ces questions dans l'ordre :

1. **`OIDC_PKCE` est-il défini ?** (Pour les fournisseurs intégrés, `OIDC_GOOGLE_PKCE` ou `OIDC_MICROSOFT_PKCE`.)
    - `True` : PKCE est utilisé. Passez à la question 3.
    - `False` : PKCE est délibérément désactivé, et le document de découverte du fournisseur est ignoré. Si votre fournisseur exige PKCE, supprimez le paramètre ou définissez-le sur `True`.
    - Non défini, ou vide : continuez avec la question 2.
2. **Le document de découverte liste-t-il `S256` ?** Ouvrez `<issuer>/.well-known/openid-configuration` et recherchez `S256` dans `code_challenge_methods_supported`.
    - Oui : PKCE est utilisé automatiquement. Continuez avec la question 3.
    - Non, ou le champ est manquant : PKCE est **non** utilisé. Définissez `OIDC_PKCE` sur `True` si votre fournisseur l'exige. Vérifiez également le journal du serveur pour `Could not check the provider for PKCE support`, ce qui signifie que le document de découverte n'a pas pu être récupéré et que PKCE a donc été laissé de côté.
3. **PKCE a-t-il vraiment été envoyé ?** Commencez une connexion et regardez l'adresse de la page de connexion du fournisseur (ou la première redirection dans l'onglet réseau de votre navigateur). Elle devrait contenir `code_challenge=` et `code_challenge_method=S256`.
    - Présent, mais la connexion échoue toujours au rappel : le fournisseur a rejeté le vérificateur de code. Le cookie de session peut avoir été perdu entre la redirection et le rappel (voir la branche 3 ci-dessus), ou le fournisseur ne prend pas en charge `S256`, auquel cas définissez `OIDC_PKCE` sur `False` si le fournisseur n'exige pas PKCE.
    - Absent : les paramètres ci-dessus n'ont pas été appliqués. Vérifiez que la variable d'environnement a le bon préfixe et une valeur en minuscules (par exemple `GRAMPSWEB_OIDC_PKCE=true` dans Docker ; `True` n'est pas lu comme un booléen), redémarrez le serveur et vérifiez à nouveau la configuration.

!!! note
    Avec PKCE activé chez le fournisseur comme *optionnel*, ou pas activé du tout, les connexions fonctionnent que Gramps Web envoie ou non un défi. Seuls les fournisseurs (ou clients) configurés pour *exiger* PKCE rendent ce paramètre important.

## Exemples de configurations

### Fournisseur OIDC personnalisé (Keycloak)

```python
TREE="Mon Arbre Familial"
BASE_URL="https://monarbre.example.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Configuration OIDC personnalisée
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="votre-secret-client"
OIDC_NAME="SSO Familial"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Optionnel : rediriger automatiquement vers la connexion SSO
OIDC_DISABLE_LOCAL_AUTH=True  # Optionnel : désactiver la connexion par nom d'utilisateur/mot de passe

# Optionnel : Mapping des rôles des groupes OIDC aux rôles Gramps
OIDC_ROLE_CLAIM="groups"  # ou "roles" selon votre fournisseur
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Utiliser SSL implicite pour le port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # votre mot de passe SMTP
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Fournisseur intégré (Google)

```python
TREE="Mon Arbre Familial"
BASE_URL="https://monarbre.example.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////path/to/users.sqlite"

# OAuth Google
OIDC_GOOGLE_CLIENT_ID="votre-id-client-google"
OIDC_GOOGLE_CLIENT_SECRET="votre-secret-client-google"
```

### Plusieurs fournisseurs

Vous pouvez activer plusieurs fournisseurs OIDC simultanément :

```python
TREE="Mon Arbre Familial"
BASE_URL="https://monarbre.example.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Fournisseur personnalisé
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="votre-secret-client"
OIDC_NAME="SSO d'Entreprise"

# OAuth Google
OIDC_GOOGLE_CLIENT_ID="votre-id-client-google"
OIDC_GOOGLE_CLIENT_SECRET="votre-secret-client-google"

# OAuth Microsoft
OIDC_MICROSOFT_CLIENT_ID="votre-id-client-microsoft"
OIDC_MICROSOFT_CLIENT_SECRET="votre-secret-client-microsoft"
```

### Pocket ID

Créez un client OIDC dans Pocket ID avec l'URI de redirection `<BASE_URL>/api/oidc/callback/custom` (voir [URI de redirection requises](#required-redirect-uris)). Si vous activez "Exiger PKCE" pour le client, aucune configuration supplémentaire de Gramps Web n'est nécessaire, car Pocket ID fait de la publicité pour le support PKCE dans son document de découverte. Ensuite, configurez :

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<id client>
GRAMPSWEB_OIDC_CLIENT_SECRET=<secret client>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Un guide de configuration OIDC créé par la communauté pour Gramps Web est disponible sur le [site officiel de documentation d'Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

La plupart de la configuration pour Keycloak peut être laissée à ses valeurs par défaut (*Client → Créer un client → Authentification du client ACTIVÉ*).
Il y a quelques exceptions :

1. **Scope OpenID** – Le scope `openid` n'est pas inclus par défaut dans toutes les versions de Keycloak. Pour éviter des problèmes, ajoutez-le manuellement : *Client → [Client Gramps] → Scopes de client → Ajouter un scope → Nom : `openid` → Définir comme défaut.*
2. **Rôles** – Les rôles peuvent être attribués soit au niveau du client, soit globalement par royaume.

    * Si vous utilisez des rôles de client, définissez l'option de configuration `OIDC_ROLE_CLAIM` sur : `resource_access.[nom-du-client-gramps].roles`
    * Pour rendre les rôles visibles à Gramps, accédez à *Scopes de client* (la section de niveau supérieur, pas sous le client spécifique), puis : *Rôles → Mappers → rôles de client → Ajouter à userinfo → ACTIVÉ.*
