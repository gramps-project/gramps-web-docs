# Créer un compte pour le propriétaire de l'arbre

Avant de pouvoir commencer à utiliser Gramps Web, vous devez créer un compte pour le propriétaire de l'arbre. Si aucun compte utilisateur n'existe pour un arbre donné, un formulaire sera affiché pour créer un compte. Le formulaire dépend de la configuration du serveur, qu'il soit pour un seul arbre ou pour plusieurs arbres.

## Configuration à arbre unique : créer un compte administrateur

Sur un serveur avec une configuration à arbre unique, lorsque aucun compte utilisateur n'existe encore, l'ouverture de Gramps Web affiche un formulaire pour créer un compte administrateur. L'utilisateur administrateur sera à la fois le propriétaire de l'arbre (unique) et l'administrateur de l'installation. Le formulaire permet également de configurer les paramètres e-mail nécessaires pour les notifications par e-mail (par exemple, la réinitialisation d'un mot de passe utilisateur). Si la configuration e-mail a déjà été ajoutée via un fichier de configuration ou des variables d'environnement sur le serveur, cette partie du formulaire peut être laissée vide.

## Configuration multi-arbres : créer un compte administrateur

Dans une configuration multi-arbres, le même formulaire pour créer un compte administrateur sera affiché si aucun utilisateur n'existe *dans aucun arbre*, c'est-à-dire lorsque le serveur vient d'être créé.

## Configuration multi-arbres : créer un compte propriétaire d'arbre

Dans une configuration multi-arbres, chaque utilisateur est lié à un seul arbre. Même si des utilisateurs existent déjà dans d'autres arbres, un propriétaire d'arbre peut être créé dans l'interface web si aucun propriétaire n'existe *pour cet arbre*.

Cependant, le formulaire de création de propriétaire ne sera pas affiché automatiquement sur la page d'accueil de Gramps Web, qui est la même pour tous les arbres. Au lieu de cela, il peut être atteint à `https://my-gramps-instance/firstrun/my-tree-id`, où `https://my-gramps-instance` est l'adresse de base de votre installation Gramps Web, et `my-tree-id` est l'ID de votre arbre.

Un flux de travail possible pour un administrateur de site pour créer un nouvel arbre est de

- Créer un arbre via l'API REST, en obtenant l'ID de l'arbre du nouvel arbre
- Partager le lien vers le formulaire de création de propriétaire avec l'ID d'arbre approprié avec le propriétaire d'arbre potentiel

Le formulaire de création de propriétaire d'arbre est analogue au formulaire de création d'administrateur décrit ci-dessus, sauf qu'il ne permet pas de modifier la configuration e-mail (ce qui n'est autorisé que pour les administrateurs).
