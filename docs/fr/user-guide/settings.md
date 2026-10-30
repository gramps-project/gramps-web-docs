# Paramètres utilisateur

Les paramètres utilisateur sont accessibles via l'icône utilisateur dans la barre d'application en haut, puis **Paramètres utilisateur**. La page est organisée en sections repliables. Les modifications prennent effet immédiatement, sauf indication contraire.

!!! note
    Les modifications des paramètres utilisateur n'affectent que votre propre compte. Les paramètres qui affectent tous les utilisateurs de l'arbre sont gérés dans [Paramètres d'administration](../administration/settings.md).

## Compte

Couvre vos informations de profil, vos identifiants et la sécurité de votre compte.

### Informations utilisateur

Affiche votre **nom d'utilisateur** et votre **rôle utilisateur** actuel (par exemple, Invité, Membre, Éditeur). Ceux-ci sont en lecture seule.

### Changer d'e-mail

Entrez une nouvelle adresse e-mail et cliquez sur **Soumettre** pour mettre à jour l'adresse associée à votre compte. L'adresse e-mail est utilisée pour les réinitialisations de mot de passe et (si configuré) les notifications.

### Changer de mot de passe

Entrez votre mot de passe actuel et un nouveau mot de passe, puis cliquez sur **Soumettre**. Si vous avez oublié votre mot de passe actuel, utilisez le lien **Mot de passe oublié** sur la page de connexion à la place.

### Méthodes de connexion liées

Si votre serveur propose une connexion unique (voir [authentification OIDC](../install_setup/oidc.md)), vous pouvez lier un compte d'un fournisseur, tel que Google ou la connexion de votre organisation, à votre compte Gramps Web. Vous pouvez ensuite vous connecter avec ce fournisseur et accéder à votre compte existant, avec votre rôle et vos modifications. Cette section n'apparaît que lorsque la connexion unique est activée et que le serveur prend en charge le lien (API Gramps Web 3.24 et ultérieure).

Pour lier un compte, cliquez sur **Lier avec** et le nom du fournisseur, connectez-vous chez le fournisseur, et vous serez ramené à vos paramètres. Si vous ne vous êtes pas connecté récemment, il vous sera demandé de vous reconnecter d'abord.

Un compte fournisseur ne peut être lié qu'à un seul compte Gramps Web. Si vous voyez "Cette connexion est déjà liée à un autre compte", cela signifie qu'elle est liée ailleurs, par exemple à un compte qui a été créé lorsque vous vous êtes d'abord connecté avec ce fournisseur. Un administrateur peut supprimer cet autre compte, après quoi vous pourrez le lier au vôtre.

Pour dissocier un compte, cliquez sur **Dissocier**. Si c'est votre dernière méthode de connexion liée, vous devez également entrer votre mot de passe, afin que vous puissiez toujours vous connecter par la suite. Si votre compte a été créé via une connexion unique et que vous n'avez jamais défini de mot de passe, utilisez **Mot de passe oublié** sur la page de connexion pour en définir un d'abord (cela nécessite que le serveur envoie des e-mails). Si le serveur n'autorise la connexion que via un fournisseur, le dernier compte lié ne peut pas être dissocié.

## Apparence

Contrôle les préférences d'affichage enregistrées sur votre appareil.

### Langue

Sélectionnez la langue pour l'interface Gramps Web. Le paramètre de langue est stocké dans le stockage local du navigateur et s'applique uniquement à l'appareil actuel.

### Thème

Choisissez entre :

- **Système** – suit la préférence claire/sombre du système d'exploitation (par défaut)
- **Clair** – utilise toujours le thème clair
- **Sombre** – utilise toujours le thème sombre

Le paramètre de thème est stocké dans le stockage local du navigateur.

### Préférences de l'arbre généalogique

#### Vue par défaut de l'arbre généalogique

Définit quel type de graphique s'ouvre par défaut lorsque vous naviguez vers la page [Arbre généalogique](tree.md). Les options sont Arbre des ancêtres, Arbre des descendants, Graphique en sablier, Graphique de relation et Graphique en éventail.

Cette préférence est stockée dans le stockage local du navigateur.

## Outils de développement

### Jeton API

Copie votre jeton de session actuel dans le presse-papiers. Le jeton peut être utilisé pour s'authentifier directement contre l'API REST, par exemple dans l'interface Swagger interactive servie par votre instance Gramps Web à `/api/swagger-ui`.

Cliquez sur **Lancer Swagger** pour ouvrir l'interface Swagger dans un nouvel onglet avec votre session déjà disponible.

!!! note
    Le jeton de session est de courte durée. Copiez-le immédiatement avant de l'utiliser dans Swagger, car il peut expirer.
