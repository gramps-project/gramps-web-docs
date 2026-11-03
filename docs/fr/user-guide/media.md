Il existe deux façons d'ajouter un nouveau fichier multimédia (une image, un fichier audio, un fichier vidéo ou tout autre fichier), et les fichiers multimédias existants peuvent être liés à de nouveaux objets au fur et à mesure de leur création :

## Ajouter un nouveau fichier multimédia autonome

Pour ajouter un fichier multimédia autonome, cliquez sur l'icône + dans la barre d'application en haut et sélectionnez "Objet multimédia".

Cliquez sur "sélectionner un fichier" pour choisir un fichier sur votre ordinateur. Sur un appareil mobile, cliquer sur ce bouton vous donnera l'option de prendre directement une photo avec l'appareil photo de votre appareil.

En option,

- entrez une description du fichier multimédia sous "titre"
- entrez une date
- définissez le fichier multimédia comme privé (ce qui le rendra visible uniquement aux utilisateurs disposant d'une autorisation suffisante)

Cliquez sur "ajouter" pour télécharger le fichier et créer l'objet multimédia.

## Ajouter un nouveau fichier multimédia et le lier à un autre objet

Les types d'objets suivants dans Gramps peuvent avoir des objets multimédias attachés : personnes, familles, événements, lieux, sources et citations.

Dans la vue détaillée de tout objet, cliquez sur le bouton bleu d'édition en bas à droite (si vous ne le voyez pas, votre utilisateur n'a pas les autorisations d'édition). Cliquez sur l'onglet "galerie" et cliquez sur le bouton bleu +.

Une boîte de dialogue s'ouvrira proposant les mêmes champs que ceux décrits dans la section précédente. Cliquez sur "enregistrer" pour télécharger le fichier, ajouter un nouvel objet multimédia et le lier à l'objet visualisé.

## Photos de profil

La première image dans la galerie d'une personne est utilisée comme sa photo de profil. En mode d'édition, elle est marquée d'un badge "Photo de profil". Pour utiliser une image différente, déplacez-la en première position avec les boutons fléchés sur les vignettes de la galerie.

Si une personne n'a pas encore de multimédia, le mode d'édition affiche un espace réservé **Ajouter une photo de profil** à la place. Cliquez dessus pour télécharger un nouveau fichier multimédia ou sélectionner un fichier existant.

## Lier des fichiers multimédias existants lors de la création d'un objet

Lorsque vous créez une nouvelle personne, une famille, un événement, un lieu, une source ou une citation, le formulaire a une section "Média". Vous pouvez y sélectionner un ou plusieurs objets multimédias existants, qui seront liés au nouvel objet lorsque vous l'enregistrerez.

Lorsque vous créez une personne avec ses événements de naissance et de décès, les objets multimédias sélectionnés sont liés uniquement à la personne, et non aux événements.

## Parcourir les médias

La vue multimédia affiche les objets multimédias sous forme de galerie de vignettes ou sous forme de liste ; le choix est mémorisé dans votre navigateur. Comme les autres [vues de liste](lists.md), elle peut être triée (y compris par date), filtrée et utilisée pour sélectionner et supprimer des médias en masse.

Cliquer sur une tuile dans la galerie ouvre le média dans la lightbox. Utilisez les touches fléchées, faites glisser ou cliquez sur les boutons fléchés pour naviguer à travers les résultats filtrés et triés, à travers les pages. Le bouton **Détails** dans la lightbox ouvre la page de l'objet multimédia. Cliquer sur une ligne dans la mise en page de la liste ouvre directement la page de l'objet multimédia.

Les vidéos sont affichées avec une vignette et un bouton de lecture. Les fichiers audio et vidéo peuvent être lus sur la page de l'objet multimédia, dans la lightbox, dans des [articles de blog](blog.md) et lorsqu'ils sont intégrés dans des notes.

## Reconnaissance de texte (OCR)

Si l'administrateur du serveur a activé le support OCR, un bouton "Reconnaissance de texte" apparaît sous l'image dans la vue détaillée d'un objet multimédia.

Cliquez sur "Reconnaissance de texte", choisissez la langue du texte affiché dans l'image, puis cliquez sur "Exécuter". L'image est traitée avec [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) et le texte reconnu est affiché ci-dessous.

Si votre utilisateur a des autorisations d'édition, cliquez sur "Enregistrer en tant que note" pour créer une nouvelle note (de type "Transcription") contenant le texte reconnu et le lier à l'objet multimédia.

!!! astuce
    La précision de l'OCR dépend fortement de la qualité de l'image et de la langue sélectionnée. Si le résultat semble incorrect, essayez une langue différente – par exemple, les documents historiques allemands nécessitent souvent la variante Fraktur plutôt que l'allemand standard.
