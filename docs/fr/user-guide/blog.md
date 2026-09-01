# Utiliser le blog intégré

Le blog est destiné à présenter des histoires sur vos recherches en histoire familiale.

Dans la base de données Gramps, les articles de blog sont représentés comme des sources avec une note jointe, contenant le texte du blog, et éventuellement, des fichiers multimédias pour les images de l'article de blog. Gramps Web traite chaque source avec une étiquette `Blog` comme un article de blog.

## Ajouter un article de blog

Le moyen le plus rapide d'écrire un article est le formulaire dédié **Nouvel Article de Blog** dans Gramps Web. Ouvrez-le soit à partir du bouton bleu **+** sur la page Blog, soit à partir du menu **Ajouter** (icône plus) dans la barre d'application en haut en choisissant **Article de Blog**.

Le formulaire contient des champs pour :

- **Titre** – le titre de l'article (obligatoire)
- **Auteur** – qui l'a écrit
- **Contenu** – un éditeur de texte enrichi pour l'article lui-même
- **Média** – un ou plusieurs objets multimédias. Le premier devient l'image d'aperçu affichée au-dessus du texte ; tous apparaissent comme une galerie en dessous.
- **Tags** et un interrupteur **privé**, comme pour tout autre objet

En enregistrant le formulaire, cela crée la source sous-jacente, la note et l'étiquette `Blog` pour vous, comme décrit [ci-dessous](#relation-entre-blog-et-sources).

### Ajouter un article manuellement

Vous pouvez également créer un article en construisant vous-même les objets sous-jacents. C'est le seul moyen de le faire dans Gramps Desktop ([synchronisé](../administration/sync.md) avec Gramps Web), et les étapes sont les mêmes dans les deux applications :

- Ajoutez une nouvelle source. Le titre de la source sera le titre de votre article de blog, l'auteur de la source sera l'auteur de l'article.
- Optionnellement, associez la source à un dépôt correspondant à votre blog Gramps Web.
- Ajoutez une nouvelle note à la source. Écrivez votre article de blog et copiez le texte dans la note.
- Optionnellement, ajoutez un ou plusieurs fichiers multimédias à votre source. Le premier fichier multimédia sera pris comme l'image d'aperçu de l'article affichée au-dessus du texte. Tous les fichiers multimédias seront affichés en dessous du texte sous forme de galerie.
- Ajoutez l'étiquette `Blog` à la source (créez-la si elle n'existe pas).

## Relation entre blog et sources

Puisque les articles de blog ne sont que des sources, tous les articles de blog apparaissent également sur la liste des sources et se présentent comme des sources dans les recherches. Dans la vue de la source, il y a un bouton "afficher dans le blog" qui vous amènera à la vue du blog pour cet article de blog. L'URL de l'article de blog contient également l'ID Gramps de la source correspondante, donc un article à `yourdomain.com/blog/S0123` correspond à la source à `yourdomain.com/source/S0123`.

Au bas de chaque article de blog, il y a un bouton "détails" qui vous amènera à la vue de la source.
