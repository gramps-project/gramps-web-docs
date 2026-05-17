# Paramètres utilisateur

Les paramètres utilisateur sont accessibles via l'icône utilisateur dans la barre d'application en haut, puis **Paramètres utilisateur**. La page est organisée en sections repliables. Les modifications prennent effet immédiatement, sauf indication contraire.

!!! note
    Les modifications des paramètres utilisateur n'affectent que votre propre compte. Les paramètres qui affectent tous les utilisateurs de l'arbre sont gérés dans les [Paramètres d'administration](../administration/settings.md).

## Compte

Couvre vos informations de profil, vos identifiants et la sécurité de votre compte.

### Informations utilisateur

Affiche votre **nom d'utilisateur** et votre **rôle utilisateur** actuel (par exemple, Invité, Membre, Éditeur). Ceux-ci sont en lecture seule.

### Changer d'e-mail

Entrez une nouvelle adresse e-mail et cliquez sur **Soumettre** pour mettre à jour l'adresse associée à votre compte. L'adresse e-mail est utilisée pour les réinitialisations de mot de passe et (si configuré) pour les notifications.

### Changer de mot de passe

Entrez votre mot de passe actuel et un nouveau mot de passe, puis cliquez sur **Soumettre**. Si vous avez oublié votre mot de passe actuel, utilisez le lien **Mot de passe oublié** sur la page de connexion à la place.

## Apparence

Contrôle les préférences d'affichage enregistrées sur votre appareil.

### Langue

Sélectionnez la langue pour l'interface Web de Gramps. Le paramètre de langue est stocké dans le stockage local du navigateur et s'applique uniquement à l'appareil actuel.

### Thème

Choisissez entre :

- **Système** – suit la préférence de lumière/sombre du système d'exploitation (par défaut)
- **Clair** – utilise toujours le thème clair
- **Sombre** – utilise toujours le thème sombre

Le paramètre de thème est stocké dans le stockage local du navigateur.

### Préférences de l'arbre généalogique

#### Vue par défaut de l'arbre généalogique

Détermine quel type de graphique s'ouvre par défaut lorsque vous naviguez vers la page [Arbre généalogique](tree.md). Les options sont Arbre des ancêtres, Arbre des descendants, Graphique en sablier, Graphique de relation et Graphique en éventail.

Cette préférence est stockée dans le stockage local du navigateur.

## Outils de développement

### Jeton API

Copie votre jeton de session actuel dans le presse-papiers. Le jeton peut être utilisé pour s'authentifier directement contre l'API REST, par exemple dans l'interface Swagger interactive servie par votre instance Gramps Web à `/api/swagger-ui`.

Cliquez sur **Lancer Swagger** pour ouvrir l'interface Swagger dans un nouvel onglet avec votre session déjà disponible.

!!! note
    Le jeton de session est de courte durée. Copiez-le immédiatement avant de l'utiliser dans Swagger, car il peut expirer.
