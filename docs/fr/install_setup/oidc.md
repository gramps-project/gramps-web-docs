# Authentification OIDC

Gramps Web prend en charge l'authentification OpenID Connect (OIDC), permettant aux utilisateurs de se connecter en utilisant des fournisseurs d'identité externes. Cela inclut à la fois des fournisseurs populaires comme Google, Microsoft et GitHub, ainsi que des fournisseurs OIDC personnalisés comme Keycloak, Authentik, et d'autres.

## Aperçu

L'authentification OIDC vous permet de :

- Utiliser des fournisseurs d'identité externes pour l'authentification des utilisateurs
- Prendre en charge plusieurs fournisseurs d'authentification simultanément
- Mapper les groupes/rôles OIDC aux rôles d'utilisateur de Gramps Web
- Mettre en œuvre le Single Sign-On (SSO) et le Single Sign-Out
- Désactiver optionnellement l'authentification locale par nom d'utilisateur/mot de passe

## Configuration

Pour activer l'authentification OIDC, vous devez configurer les paramètres appropriés dans votre fichier de configuration Gramps Web ou dans les variables d'environnement. Consultez la page [Configuration du serveur](configuration.md#settings-for-oidc-authentication) pour une liste complète des paramètres OIDC disponibles.

!!! info
    Lors de l'utilisation de variables d'environnement, n'oubliez pas de préfixer chaque nom de paramètre par `GRAMPSWEB_` (par exemple, `GRAMPSWEB_OIDC_ENABLED`). Consultez [Fichier de configuration vs. variables d'environnement](configuration.md#configuration-file-vs-environment-variables) pour plus de détails.

### Fournisseurs intégrés

Gramps Web prend en charge les fournisseurs d'identité populaires. Pour les utiliser, vous devez simplement fournir l'ID client et le secret client :

- **Google** : `OIDC_GOOGLE_CLIENT_ID` et `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft** : `OIDC_MICROSOFT_CLIENT_ID` et `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub** : `OIDC_GITHUB_CLIENT_ID` et `OIDC_GITHUB_CLIENT_SECRET`

Vous pouvez configurer plusieurs fournisseurs simultanément. Le système détectera automatiquement quels fournisseurs sont disponibles en fonction des valeurs de configuration.

### Fournisseurs OIDC personnalisés

Pour les fournisseurs OIDC personnalisés (comme Keycloak, Authentik ou tout fournisseur conforme à la norme OIDC), utilisez ces paramètres :

Clé | Description
----|-------------
`OIDC_ENABLED` | Booléen, indique si l'authentification OIDC doit être activée. Défini sur `True`.
`OIDC_ISSUER` | L'URL de l'émetteur de votre fournisseur
`OIDC_CLIENT_ID` | ID client pour votre fournisseur OIDC
`OIDC_CLIENT_SECRET` | Secret client pour votre fournisseur OIDC
`OIDC_NAME` | Nom d'affichage personnalisé (optionnel, par défaut "OIDC")
`OIDC_SCOPES` | Scopes OAuth (optionnel, par défaut "openid email profile")

## URI de redirection requises

Lorsque vous configurez votre fournisseur OIDC, vous devez enregistrer l'URI de redirection suivante :

**Pour les fournisseurs OIDC qui prennent en charge les jokers : (par exemple, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Où `*` est un joker regex. Selon l'interpréteur regex de votre fournisseur, cela pourrait également être un `.*` ou similaire. Assurez-vous que le regex est activé si votre fournisseur l'exige (par exemple, Authentik).

**Pour les fournisseurs OIDC qui ne prennent pas en charge les jokers : (par exemple, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Mapping des rôles

Gramps Web peut mapper automatiquement les groupes ou rôles OIDC de votre fournisseur d'identité aux rôles d'utilisateur de Gramps Web. Cela vous permet de gérer les autorisations des utilisateurs de manière centralisée dans votre fournisseur d'identité.

### Configuration

Utilisez ces paramètres pour configurer le mapping des rôles :

Clé | Description
----|-------------
`OIDC_ROLE_CLAIM` | Le nom de la revendication dans le jeton OIDC qui contient les groupes/rôles de l'utilisateur. Par défaut "groups"
`OIDC_GROUP_ADMIN` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Admin" de Gramps
`OIDC_GROUP_OWNER` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Owner" de Gramps
`OIDC_GROUP_EDITOR` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Editor" de Gramps
`OIDC_GROUP_CONTRIBUTOR` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Contributor" de Gramps
`OIDC_GROUP_MEMBER` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Member" de Gramps
`OIDC_GROUP_GUEST` | Le nom du groupe/rôle de votre fournisseur OIDC qui correspond au rôle "Guest" de Gramps

### Comportement du mapping des rôles

- Si aucun mapping de rôle n'est configuré (aucune variable `OIDC_GROUP_*` définie), les rôles d'utilisateur existants sont préservés
- Les utilisateurs se voient attribuer le rôle le plus élevé auquel ils ont droit en fonction de leur appartenance à un groupe
- Le mapping des rôles est sensible à la casse par défaut (dépend de votre fournisseur OIDC)

## Déconnexion OIDC

Gramps Web prend en charge la déconnexion Single Sign-Out (SSO) pour les fournisseurs OIDC. Lorsqu'un utilisateur se déconnecte de Gramps Web après s'être authentifié via OIDC, il sera automatiquement redirigé vers la page de déconnexion du fournisseur d'identité si le fournisseur prend en charge le `end_session_endpoint`.

### Déconnexion en arrière-plan

Gramps Web met en œuvre la spécification de déconnexion en arrière-plan OpenID Connect. Cela permet aux fournisseurs d'identité de notifier Gramps Web lorsqu'un utilisateur se déconnecte d'une autre application ou du fournisseur d'identité lui-même.

#### Configuration

Pour configurer la déconnexion en arrière-plan avec votre fournisseur d'identité :

1. **Enregistrez l'endpoint de déconnexion en arrière-plan** dans la configuration du client de votre fournisseur d'identité :
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Configurez votre fournisseur** pour envoyer des notifications de déconnexion. Les étapes exactes dépendent de votre fournisseur :

   **Keycloak :**

   - Dans la configuration de votre client, accédez à "Paramètres"
   - Définissez "URL de déconnexion en arrière-plan" sur `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Activez "Déconnexion en arrière-plan requise pour la session" si vous souhaitez une déconnexion basée sur la session

   **Authentik :**

   - Dans la configuration de votre fournisseur, ajoutez l'URL de déconnexion en arrière-plan
   - Assurez-vous que le fournisseur est configuré pour envoyer des jetons de déconnexion

!!! warning "Expiration du jeton"
    En raison de la nature sans état des jetons JWT, la déconnexion en arrière-plan enregistre actuellement l'événement de déconnexion mais ne peut pas révoquer immédiatement les jetons JWT déjà émis. Les jetons resteront valides jusqu'à leur expiration (par défaut : 15 minutes pour les jetons d'accès).

    Pour une sécurité accrue, envisagez de :

    - Réduire le temps d'expiration des jetons JWT (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Éduquer les utilisateurs à se déconnecter manuellement de Gramps Web lorsqu'ils se déconnectent de votre fournisseur d'identité

!!! tip "Comment ça fonctionne"
    Lorsqu'un utilisateur se déconnecte de votre fournisseur d'identité ou d'une autre application :

    1. Le fournisseur envoie un `logout_token` JWT à l'endpoint de déconnexion en arrière-plan de Gramps Web
    2. Gramps Web valide le jeton et enregistre l'événement de déconnexion
    3. Le JTI du jeton de déconnexion est ajouté à une liste noire pour prévenir les attaques par rejeu
    4. Toute nouvelle requête API avec le JWT de l'utilisateur sera refusée une fois les jetons expirés

## Exemples de configurations

### Fournisseur OIDC personnalisé (Keycloak)

```python
TREE="Mon Arbre Généalogique"
BASE_URL="https://monarbre.exemple.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////chemin/vers/utilisateurs.sqlite"

# Configuration OIDC personnalisée
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.exemple.com/realms/monrealm"
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

EMAIL_HOST="mail.exemple.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@exemple.com"
EMAIL_HOST_PASSWORD="..." # votre mot de passe SMTP
DEFAULT_FROM_EMAIL="gramps@exemple.com"
```

### Fournisseur intégré (Google)

```python
TREE="Mon Arbre Généalogique"
BASE_URL="https://monarbre.exemple.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////chemin/vers/utilisateurs.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="votre-id-client-google"
OIDC_GOOGLE_CLIENT_SECRET="votre-secret-client-google"
```

### Plusieurs fournisseurs

Vous pouvez activer plusieurs fournisseurs OIDC simultanément :

```python
TREE="Mon Arbre Généalogique"
BASE_URL="https://monarbre.exemple.com"
SECRET_KEY="..."  # votre clé secrète
USER_DB_URI="sqlite:////chemin/vers/utilisateurs.sqlite"

# Fournisseur personnalisé
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.exemple.com/realms/monrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="votre-secret-client"
OIDC_NAME="SSO d'Entreprise"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="votre-id-client-google"
OIDC_GOOGLE_CLIENT_SECRET="votre-secret-client-google"

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="votre-id-client-github"
OIDC_GITHUB_CLIENT_SECRET="votre-secret-client-github"
```

### Authelia

Un guide de configuration OIDC réalisé par la communauté pour Gramps Web est disponible sur le [site officiel de la documentation d'Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).
