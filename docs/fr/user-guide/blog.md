# Utiliser le blog intégré

Le blog est destiné à présenter des histoires sur vos recherches en histoire familiale.

Dans la base de données Gramps, les articles de blog sont représentés comme des sources avec une note jointe, contenant le texte du blog, et éventuellement, des fichiers multimédias pour les images de l'article de blog. Gramps Web traite chaque source avec un tag `Blog` comme un article de blog.

## Ajouter un article de blog

Pour ajouter un article de blog, vous pouvez utiliser Gramps Web ou Gramps Desktop ([synchronisé](../administration/sync.md) avec Gramps Web), les étapes sont les mêmes dans les deux cas :

- Ajoutez une nouvelle source. Le titre de la source sera le titre de votre article de blog, l'auteur de la source sera l'auteur de l'article.
- Optionnellement, associez la source à un dépôt correspondant à votre blog Gramps Web.
- Ajoutez une nouvelle note à la source. Écrivez votre article de blog et copiez le texte dans la note.
- Optionnellement, ajoutez un ou plusieurs fichiers multimédias à votre source. Le premier fichier multimédia sera pris comme l'image d'aperçu de l'article affichée au-dessus du texte. Tous les fichiers multimédias seront affichés en dessous du texte sous forme de galerie.
- Ajoutez l'étiquette `Blog` à la source (créez-la si elle n'existe pas).

## Relation entre le blog et les sources

Puisque les articles de blog ne sont que des sources, tous les articles de blog apparaissent également sur la liste des sources et se présentent comme des sources dans les recherches. Dans la vue de la source, il y a un bouton "montrer dans le blog" qui vous amènera à la vue du blog pour cet article de blog. L'URL de l'article de blog contient également l'ID Gramps de la source correspondante, donc un article à `yourdomain.com/blog/S0123` correspond à la source à `yourdomain.com/source/S0123`.

Au bas de chaque article de blog, il y a un bouton "détails" qui vous amènera à la vue de la source.
