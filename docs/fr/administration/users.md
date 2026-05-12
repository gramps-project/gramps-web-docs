# Gérer les utilisateurs

L'interface de gestion des utilisateurs est accessible via **Paramètres > Gérer les utilisateurs** (l'icône utilisateur dans la barre d'application en haut). Elle n'est disponible que pour les utilisateurs ayant le rôle de Propriétaire ou d'Administrateur.

## Rôles des utilisateurs

Voir [Système d'utilisateurs](../install_setup/users.md) pour une description complète des rôles d'utilisateur disponibles et de leurs permissions.

## Afficher et filtrer les utilisateurs

La page de gestion des utilisateurs affiche un tableau de tous les comptes d'utilisateur enregistrés avec les colonnes suivantes :

- **Nom d'utilisateur** — le nom de connexion
- **Nom complet** — le nom affiché
- **E-mail** — l'adresse e-mail de l'utilisateur
- **Rôle** — le rôle attribué (Invité, Membre, Contributeur, Éditeur, Propriétaire ou Administrateur)
- **Source du compte** — soit "Mot de passe" (compte local) soit le nom d'un fournisseur d'identité externe (par exemple, lors de l'utilisation d'OIDC)

Utilisez le champ de recherche et le menu déroulant des rôles en haut du tableau pour filtrer la liste. Cliquez sur le bouton de réinitialisation des filtres pour réinitialiser tous les filtres.

## Modifier un utilisateur

Cliquez sur l'icône de modification (crayon) sur n'importe quelle ligne pour ouvrir la boîte de dialogue de modification. Vous pouvez changer :

- Nom complet
- Adresse e-mail
- Rôle

C'est le moyen principal pour **activer un nouvel utilisateur auto-enregistré** : changez son rôle de *désactivé* à tout rôle actif (par exemple, Membre ou Éditeur).

## Ajouter un utilisateur manuellement

Cliquez sur l'icône **ajouter un utilisateur** (personne-ajouter) au-dessus du tableau pour créer un nouveau compte utilisateur directement sans nécessiter d'auto-enregistrement. Remplissez le nom d'utilisateur, le nom complet, l'adresse e-mail, le mot de passe et le rôle dans la boîte de dialogue et cliquez sur **Enregistrer**.

## Supprimer un utilisateur

Cliquez sur l'icône de suppression (corbeille) sur n'importe quelle ligne et confirmez dans la boîte de dialogue. Cette action ne peut pas être annulée.

## Exporter et importer des comptes utilisateurs

Ces boutons sont utiles lors de [la migration vers une autre instance de Gramps Web](export.md).

- **Exporter les détails des utilisateurs** (icône de téléchargement) — télécharge un fichier JSON contenant tous les comptes d'utilisateur (sans mots de passe, car les mots de passe sont stockés sous forme cryptée).
- **Importer des comptes utilisateurs** (icône de groupe-ajouter) — télécharge un fichier JSON précédemment exporté pour créer des comptes utilisateurs en masse. Tous les utilisateurs importés devront définir un nouveau mot de passe via le lien "Mot de passe oublié", car les mots de passe ne peuvent pas être transférés.

## Lien d'inscription (configuration multi-arbres uniquement)

Dans une configuration multi-arbres, le lien d'inscription pour les nouveaux utilisateurs est affiché en haut de la page de gestion des utilisateurs. Vous pouvez copier ce lien et le partager avec les personnes que vous souhaitez inviter à s'inscrire sur votre arbre.

!!! note
    Dans une configuration à arbre unique, il existe un lien générique "S'inscrire" sur la page de connexion ; le lien d'inscription par arbre n'est nécessaire que dans les installations multi-arbres.

## Permissions de chat AI

Si le chat AI a été activé sur le serveur, un menu déroulant en haut de la page vous permet de contrôler quels rôles d'utilisateur sont autorisés à utiliser la fonction de chat :

- Tout le monde (y compris les invités)
- Membre et au-dessus
- Contributeur et au-dessus
- Éditeur et au-dessus
- Propriétaires et administrateurs uniquement
- Personne (désactiver le chat pour tous les utilisateurs)
