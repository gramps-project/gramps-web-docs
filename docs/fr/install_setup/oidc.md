# Authentification OIDC

Gramps Web prend en charge l'authentification OpenID Connect (OIDC), permettant aux utilisateurs de se connecter en utilisant des fournisseurs d'identité externes. Cela inclut les fournisseurs intégrés Google et Microsoft, ainsi que des fournisseurs OIDC personnalisés comme Keycloak, Authentik et Authelia.

!!! warning "GitHub en tant que fournisseur OIDC n'est plus pris en charge"
    Si vous avez `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` définis à partir d'une version antérieure, supprimez-les – ils sont désormais ignorés, et les utilisateurs qui se connectaient auparavant via GitHub ne peuvent plus se connecter de cette manière. GitHub est un fournisseur OAuth 2.0, pas un fournisseur OpenID Connect, et n'a jamais renvoyé la revendication sur laquelle Gramps Web s'appuie pour l'identité, donc il n'a jamais été entièrement fiable.

## Vue d'ensemble

L'authentification OIDC vous permet de :

- Utiliser des fournisseurs d'identité externes pour l'authentification des utilisateurs
- Prendre en charge plusieurs fournisseurs d'authentification simultanément
- Mapper les groupes/rôles OIDC aux rôles d'utilisateur de Gramps Web
- Mettre en œuvre l'authentification unique (SSO) et la déconnexion unique
- Désactiver optionnellement l'authentification par nom d'utilisateur/mot de passe local

## Configuration

Pour activer l'authentification OIDC, vous devez configurer les paramètres appropriés dans votre fichier de configuration Gramps Web ou dans les variables d'environnement. Consultez la page [Configuration du serveur](configuration.md#settings-for-oidc-authentication) pour une liste complète des paramètres OIDC disponibles.

!!! info
    Lors de l'utilisation de variables d'environnement, n'oubliez pas de préfixer chaque nom de paramètre avec `GRAMPSWEB_` (par exemple, `GRAMPSWEB_OIDC_ENABLED`). Consultez [Fichier de configuration vs. variables d'environnement](configuration.md#configuration-file-vs-environment-variables) pour plus de détails.

### Fournisseurs intégrés

Gramps Web prend en charge les fournisseurs d'identité populaires intégrés. Pour les utiliser, vous devez simplement fournir l'ID client et le secret client :

- **Google** : `OIDC_GOOGLE_CLIENT_ID` et `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft** : `OIDC_MICROSOFT_CLIENT_ID` et `OIDC_MICROSOFT_CLIENT_SECRET`

Vous pouvez configurer plusieurs fournisseurs simultanément. Le système détectera automatiquement quels fournisseurs sont disponibles en fonction des valeurs de configuration.

!!! tip "Microsoft : déploiements à locataire unique"
    Le fournisseur Microsoft intégré utilise le point de terminaison multi-locataire `/common` et accepte les connexions de n'importe quel compte Microsoft par conception. Si vous souhaitez uniquement autoriser les utilisateurs de votre propre locataire, utilisez le [fournisseur OIDC personnalisé](#custom-oidc-providers) avec votre URL d'émetteur spécifique au locataire à la place, ce qui maintient la validation de l'émetteur active et restreint les connexions à ce locataire.

### Fournisseurs OIDC personnalisés

Pour les fournisseurs OIDC personnalisés (comme Keycloak, Authentik, Authelia, ou un locataire Microsoft Entra à locataire unique), utilisez ces paramètres :

Clé | Description
----|-------------
`OIDC_ENABLED` | Booléen, pour activer l'authentification OIDC. Défini sur `True`.
`OIDC_ISSUER` | L'URL de l'émetteur de votre fournisseur. La découverte est récupérée à partir de `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID client pour votre fournisseur OIDC
`OIDC_CLIENT_SECRET` | Secret client pour votre fournisseur OIDC
`OIDC_NAME` | Nom d'affichage personnalisé (facultatif, par défaut "OIDC")
`OIDC_SCOPES` | Scopes OAuth (facultatif, par défaut "openid email profile")
`OIDC_USERNAME_CLAIM` | Revendication utilisée pour générer le nom d'utilisateur (facultatif, par défaut "preferred_username")

### Configurations multi-arbres

Sur un serveur multi-arbres, l'arbre dans lequel l'utilisateur se connecte doit être connu avant que Gramps Web ne redirige vers le fournisseur d'identité, donc la connexion commence par :

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` est requis dans les configurations multi-arbres ; l'omettre ou passer l'ID d'un arbre qui n'existe pas échoue la connexion. Sur un serveur à arbre unique, `tree` est optionnel, mais s'il est donné, il doit correspondre à l'`ARBRE` configuré.

Une identité OIDC est liée à exactement un compte Gramps Web, qui appartient à son tour à exactement un arbre – se connecter à un arbre différent échoue plutôt que de déplacer le compte. Il n'y a aucun moyen de lier une seule identité au fournisseur à des comptes dans plusieurs arbres ; les utilisateurs qui ont besoin d'accéder à plusieurs arbres ont besoin d'identités distinctes chez le fournisseur (par exemple, des noms d'utilisateur ou des comptes distincts).

!!! warning
    Un compte administrateur de site sans arbre associé (voir [création d'un compte admin](../administration/owner.md)) ne peut pas se connecter via OIDC, car la connexion OIDC nécessite toujours un arbre. De tels comptes doivent être créés et authentifiés avec un nom d'utilisateur/mot de passe local à la place.

## URIs de redirection requises

Lorsque vous configurez votre fournisseur OIDC, vous devez enregistrer l'URI de redirection suivante :

**Pour les fournisseurs OIDC qui prennent en charge les jokers : (par exemple, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Où `*` est un joker regex. Selon l'interpréteur regex de votre fournisseur, cela pourrait également être un `.*` ou similaire. Assurez-vous que le regex est activé si votre fournisseur l'exige (par exemple, Authentik).

**Pour les fournisseurs OIDC qui ne prennent pas en charge les jokers : (par exemple, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

L'arbre ne fait jamais partie de l'URI de redirection, même sur des serveurs multi-arbres – il voyage séparément dans la session, car les fournisseurs exigent que l'URI de redirection corresponde exactement à celle enregistrée.

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

Si aucun paramètre `OIDC_GROUP_*` n'est configuré, le mapping des rôles est désactivé et les rôles sont gérés manuellement dans Gramps Web ; de nouveaux comptes OIDC sont alors créés désactivés et doivent être approuvés par un propriétaire ou un administrateur existant (voir [Première connexion et démarrage](#first-login-and-bootstrapping) ci-dessous).

Une fois le mapping des rôles configuré, à chaque connexion :

- Si la revendication de rôle est présente et que l'utilisateur appartient à un groupe mappé, il obtient le rôle correspondant.
- Si la revendication de rôle est présente mais que l'utilisateur n'appartient à aucun groupe mappé, son rôle est défini sur désactivé. C'est un défaut de fermeture, pas un bug – Gramps Web ne peut pas inférer un rôle pour un groupe qu'il ne reconnaît pas.
- Si la revendication de rôle est complètement absente du jeton, le rôle existant reste inchangé ; un nouveau compte est toujours par défaut désactivé.

!!! warning "Google n'envoie pas de revendication de groupes"
    Les jetons de Google n'incluent jamais de revendication `groups`, donc avec le mapping des rôles activé, les connexions Google relèvent de "revendication absente" ci-dessus : les utilisateurs existants conservent leur rôle, mais les nouveaux utilisateurs Google sont créés désactivés et nécessitent une approbation manuelle. Gardez cela à l'esprit avant d'activer le mapping des rôles uniquement pour un autre fournisseur – cela ne désactive pas, en soi, les utilisateurs Google existants.

Microsoft Entra renvoie des rôles d'application et des adhésions de groupe uniquement dans le jeton ID, pas à partir du point de terminaison userinfo. Gramps Web fusionne les revendications du jeton ID dans la réponse userinfo afin que `OIDC_ROLE_CLAIM` fonctionne de la même manière que pour d'autres fournisseurs ; lorsque les deux contiennent une revendication, la valeur userinfo a la priorité.

## Première connexion et démarrage

Les nouveaux comptes créés via OIDC commencent désactivés à moins que le mapping des rôles ne leur attribue un rôle (voir ci-dessus). Sur une instance toute nouvelle, personne ne peut approuver un compte désactivé, et si `OIDC_DISABLE_LOCAL_AUTH` est également activé, il n'y a pas de connexion par mot de passe sur laquelle se rabattre non plus.

!!! warning "Configurez un groupe propriétaire/admin avant la première connexion"
    Avant que quiconque ne se connecte via OIDC pour la première fois, définissez `OIDC_GROUP_OWNER` (ou `OIDC_GROUP_ADMIN`) et assurez-vous que le premier utilisateur appartient à ce groupe chez le fournisseur. Sinon, l'instance ne peut pas être démarrée via OIDC.

## Comptes et noms d'utilisateur

Les comptes créés via OIDC obtiennent un nom d'utilisateur généré, attribué une fois à la création du compte et jamais changé lors des connexions ultérieures :

- Fournisseurs intégrés : `<provider>_<claim value>`, par exemple `microsoft_alice@contoso.com`
- Fournisseur personnalisé : la valeur de revendication brute, par exemple `alice`

Un suffixe numérique est ajouté en cas de collision. Il n'y a aucun moyen de renommer le nom d'utilisateur d'un compte créé par OIDC par la suite ; le nom complet et l'adresse e-mail, en revanche, sont actualisés à chaque connexion.

Une connexion OIDC ne s'attache jamais à un compte local existant qui partage par hasard son adresse e-mail – c'est délibéré, car lier des comptes par e-mail est un vecteur de prise de contrôle de compte. Un utilisateur qui a déjà un compte local obtient un deuxième compte distinct la première fois qu'il se connecte via OIDC.

Les adresses e-mail du fournisseur ne sont stockées que si le fournisseur les marque comme vérifiées (ou omet complètement la revendication `email_verified`) et si l'adresse n'est pas déjà utilisée par un autre compte ; sinon, la connexion se poursuit sans stocker d'adresse e-mail.

## Déconnexion OIDC

Gramps Web prend en charge la déconnexion unique (déconnexion SSO) pour les fournisseurs OIDC. `GET /api/oidc/logout/` recherche le `end_session_endpoint` du fournisseur et le renvoie en tant que `logout_url` dans la réponse ; c'est le frontend de Gramps Web qui navigue le navigateur là-bas pour réellement mettre fin à la session auprès du fournisseur d'identité. `logout_url` est `null` lorsque le fournisseur n'a pas de `end_session_endpoint`.

!!! warning "Les jetons ne sont pas révoqués lors de la déconnexion"
    Se déconnecter met uniquement fin à la session du navigateur ; il n'y a actuellement aucun moyen de révoquer un jeton Gramps Web qui a déjà été émis. Les jetons restent valides jusqu'à leur expiration (`JWT_ACCESS_TOKEN_EXPIRES`, par défaut 15 minutes pour les jetons d'accès), peu importe si l'utilisateur s'est depuis déconnecté de Gramps Web ou du fournisseur d'identité.

## Exemples de configurations

### Fournisseur OIDC personnalisé (Keycloak)

```python
TREE="Mon Arbre Familial"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Configuration OIDC personnalisée
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
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
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////path/to/users.sqlite"

# OAuth Google
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Plusieurs fournisseurs

Vous pouvez activer plusieurs fournisseurs OIDC simultanément :

```python
TREE="Mon Arbre Familial"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Fournisseur personnalisé
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="SSO d'Entreprise"

# OAuth Google
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# OAuth Microsoft
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Authelia

Un guide de configuration OIDC réalisé par la communauté pour Gramps Web est disponible sur le [site officiel de la documentation d'Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

La plupart de la configuration pour Keycloak peut être laissée à ses valeurs par défaut (*Client → Créer un client → Authentification du client ACTIVÉ*). Il y a quelques exceptions :

1. **Scope OpenID** – Le scope `openid` n'est pas inclus par défaut dans toutes les versions de Keycloak. Pour éviter des problèmes, ajoutez-le manuellement : *Client → [Client Gramps] → Scopes de client → Ajouter un scope → Nom : `openid` → Définir comme par défaut.*
2. **Rôles** – Les rôles peuvent être attribués soit au niveau du client, soit globalement par royaume.

    * Si vous utilisez des rôles de client, définissez l'option de configuration `OIDC_ROLE_CLAIM` sur : `resource_access.[gramps-client-name].roles`
    * Pour rendre les rôles visibles pour Gramps, naviguez vers *Scopes de client* (la section de niveau supérieur, pas sous le client spécifique), puis : *Rôles → Mappers → rôles de client → Ajouter à userinfo → ACTIVÉ.*
