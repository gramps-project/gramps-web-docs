---
hide:
  - toc
  - navigation
---

# Fonctionnalités

Gramps Web est une application web pour la généalogie collaborative. Elle est construite sur [Gramps](https://gramps-project.org/), le programme de généalogie open-source, et fonctionne avec les mêmes données. Vous pouvez l'exécuter sur votre propre serveur ou utiliser un fournisseur d'hébergement.

[Essayez la démo](#demo){ .md-button .md-button--primary } [Commencer](../install_setup/setup.md){ .md-button }

## Explorez votre arbre généalogique { .feature-group }

![Diagramme en éventail montrant sept générations d'ancêtres](screenshots/fan.png){ align=right width="400"}

### Graphiques interactifs de l'arbre généalogique

Naviguez dans votre arbre généalogique sous forme d'arbre d'ancêtres, d'arbre de descendants, de graphique en sablier, de graphique de relations ou de diagramme en éventail, avec des graphiques interactifs de haute qualité et un nombre configurable de générations.

Survolez n'importe quelle personne pour voir une carte de prévisualisation avec ses faits clés, et accédez directement à la page de détails complète depuis le graphique.

<div style="clear:both;"></div>

---

![Chronologie des événements familiaux entre les années 1940 et 1970](screenshots/timeline.png){ align=left width="400"}

### Chronologie chronologique

Voyez chaque événement dans votre arbre généalogique disposé sur une chronologie horizontale et zoomable. Faites défiler et zoomez à travers les siècles, puis filtrez pour une seule personne – ou pour tous ses ancêtres ou descendants – ou pour tout ce qui s'est passé à un endroit donné.

Voir [Chronologie](../user-guide/timeline.md).

<div style="clear:both;"></div>

---

![Carte de Londres avec un lieu sélectionné, montrant sa photo et ses événements](screenshots/map.png){ align=right width="400"}

### Carte interactive

Affichez tous les lieux de votre arbre sur une carte interactive et consultable. Recherchez de nouveaux lieux directement sur OpenStreetMap lors de la création d'un lieu, tracez les personnes de votre base de données géographiquement, et retracez la vie d'une personne en reliant ses événements par des lignes sur la carte.

<div style="clear:both;"></div>

---

![Londres sur la couche OpenHistoricalMap, avec le curseur temporel réglé sur 1707](screenshots/ohm.png){ align=left width="400"}

### Cartes historiques

Transformez une carte historique stockée en tant qu'objet multimédia dans Gramps en une superposition de carte personnalisée.

Vous pouvez également passer aux cartes vectorielles historiques du projet [OpenHistoricalMap](https://www.openhistoricalmap.org/). Utilisez le curseur temporel pour faire défiler l'évolution des lieux dans votre histoire familiale et afficher les lieux où vivaient vos ancêtres ou où se sont déroulés des événements.

<div style="clear:both;"></div>

---

![Résultats de recherche pour "Albert" parmi les personnes, événements et médias](screenshots/search.png){ align=right width="400"}

### Trouvez n'importe quoi

Le moteur de recherche en texte intégral couvre tous les types d'objets Gramps, y compris le contenu des notes textuelles, et prend en charge les caractères génériques et les opérateurs logiques.

Pour des requêtes précises, les vues de liste d'objets offrent un mode filtre avancé basé sur le [Gramps Object Query Language](../user-guide/goql.md), ainsi que des filtres rapides par texte, tag et confidentialité.

Depuis la page de n'importe quelle personne, [Recherche externe](../user-guide/external-search.md) ouvre une recherche pré-remplie sur FamilySearch, Ancestry, CompGen et d'autres sites – et vous pouvez ajouter les vôtres.

<div style="clear:both;"></div>

## Construire et rechercher { .feature-group }

![Arbre d'ancêtres en mode édition avec la boîte de dialogue pour ajouter un membre de la famille](screenshots/tree-edit.png){ align=left width="400"}

### Construisez votre arbre directement dans le graphique

Passez la vue de l'arbre en mode édition et développez votre arbre généalogique sans quitter le graphique. Chaque carte de personne dispose d'un bouton **+** pour ajouter un père, une mère, un enfant ou un conjoint – soit en liant quelqu'un déjà dans votre base de données, soit en créant une toute nouvelle personne sur le champ. Chaque changement est enregistré immédiatement.

Voir [Édition de l'arbre généalogique](../user-guide/tree-edit.md).

<div style="clear:both;"></div>

---

![L'assistant IA lisant un certificat de naissance et proposant de nouveaux enregistrements](screenshots/chat.png){ align=right width="400"}

### Assistant IA intégré

Posez des questions sur votre arbre généalogique dans votre propre langue et obtenez des réponses basées sur vos données.

L'assistant ne se contente pas de rechercher : il interroge directement votre base de données avec un ensemble d'outils, filtrant les personnes, événements, familles et lieux, et calculant les relations entre les individus. Vous pouvez voir quels outils il utilise pendant qu'il construit une réponse, et les questions plus longues s'exécutent en tant que tâches en arrière-plan, vous permettant de naviguer ailleurs et de revenir.

L'assistant est optionnel et doit être [configuré par l'administrateur du serveur](../install_setup/chat.md) avec un fournisseur de modèle IA.

<div style="clear:both;"></div>

---

![Navigateur de chromosomes montrant les segments d'ADN partagés de onze correspondances](screenshots/dna.png){ align=left width="400"}

### Correspondances ADN, navigateur de chromosomes & Y-ADN

Téléchargez des données de correspondance ADN de votre fournisseur de tests ADN, stockez-les aux côtés de votre arbre généalogique, et visualisez vos correspondances dans un navigateur de chromosomes interactif.

Les données brutes des SNP du chromosome Y peuvent être utilisées pour déterminer le [haplogroupe Y-ADN](../user-guide/y-dna.md) le plus probable d'une personne et afficher ses ancêtres patrilinéaires dans l'arbre du chromosome Y humain, avec des estimations de temps. L'analyse s'exécute entièrement sur votre propre serveur – aucune donnée n'est envoyée à un tiers.

<div style="clear:both;"></div>

---

![Peinture avec deux personnes étiquetées et les autres visages détectés entourés](screenshots/tag.png){ align=right width="400"}

### Étiquetez les personnes sur les photos avec détection de visage automatisée

Identifiez les ancêtres dans de vieilles photos de famille avec vos proches. Les visages sont détectés automatiquement, donc étiqueter une personne ne prend que deux clics.

<div style="clear:both;"></div>

---

![Liste des tâches de recherche avec statut, priorité et étiquettes](screenshots/tasks.png){ align=left width="400"}

### Application de gestion des tâches intégrée

Gramps Web est livré avec une application de gestion des tâches intégrée pour organiser et planifier votre recherche généalogique. Donnez à chaque tâche un statut, une priorité et des étiquettes, documentez vos progrès dans une description en texte enrichi, et attachez les médias que vous avez rassemblés en cours de route.

Les tâches sont stockées en tant que sources dans la base de données Gramps, elles font donc partie de vos données généalogiques et peuvent être consultées et modifiées dans Gramps Desktop également.

<div style="clear:both;"></div>

---

![Article de blog sur l'identification des personnes dans une photographie de famille](screenshots/blog.png){ align=right width="400"}

### Blog de généalogie inclus

Résumez votre recherche sous forme d'histoires de blog avec des images, et partagez-les avec vos proches. Un éditeur dédié rend l'écriture d'un nouvel article simple. Toutes les données sont stockées dans la base de données Gramps.

<div style="clear:both;"></div>

## Travailler ensemble { .feature-group }

![Liste des personnes dans l'arbre généalogique](screenshots/list.png){ align=left width="400"}

### Niveaux de confidentialité & accès utilisateur

Vous pouvez [marquer des enregistrements comme privés](../user-guide/privacy.md) – jusqu'à un seul nom, lien d'événement ou correspondance ADN – et contrôler quels utilisateurs sont autorisés à voir des enregistrements privés. Les enregistrements privés sont filtrés au niveau de la base de données pour une sécurité maximale. De plus, vous pouvez contrôler ce que les utilisateurs peuvent ajouter et modifier.

Les utilisateurs peuvent se connecter avec un mot de passe, ou via un fournisseur d'identité externe utilisant [OpenID Connect](../install_setup/oidc.md) – Google et Microsoft par défaut, ainsi que des fournisseurs personnalisés tels que Keycloak, Authentik et Authelia.

<div style="clear:both;"></div>

---

![Une révision montrant les champs modifiés dans un enregistrement de personne](screenshots/revisions.png){ align=right width="400"}

### Historique complet des révisions – avec annulation

Chaque modification de votre arbre généalogique est enregistrée. Parcourez l'historique complet regroupé par transaction, explorez tout changement individuel pour voir exactement quels champs ont été ajoutés, supprimés ou modifiés, et annulez une transaction si cela s'avère être une erreur. La page de chaque objet a également son propre onglet de révision montrant qui l'a modifié et quand.

Voir [Historique des révisions](../user-guide/revisions.md).

<div style="clear:both;"></div>

---

![Menu Outils de Gramps Desktop avec l'entrée Gramps Web Sync](screenshots/sync.png){ align=left width="300"}

### Intégration complète avec Gramps Desktop

Gramps Web utilise le même modèle de données et la même base de données que [Gramps Desktop](https://gramps-project.org/). Vous pouvez parcourir et modifier tous les mêmes [types d'enregistrements](https://gramps-project.org/wiki/index.php/Gramps_Data_Model) : personnes, familles, événements, lieux, dépôts, sources, citations, objets multimédias et notes.

Avec l'[add-on Gramps Web Sync](../administration/sync.md) pour Gramps Desktop, vous pouvez synchroniser vos données dans les deux sens, afin que vous puissiez continuer à travailler dans Gramps Desktop et dans Gramps Web côte à côte.

<div style="clear:both;"></div>

## Rapports et exportation de données { .feature-group }

![Rapport d'ancêtres généré au format PDF](screenshots/report.png){ align=right width="400"}

### Générer des rapports imprimables

Gramps Web est construit sur le même noyau que Gramps Desktop, donc vous pouvez générer presque tous les [rapports](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports) que l'application de bureau prend en charge directement depuis le navigateur, y compris des graphiques de relations ou des rapports de livre au format PDF.

<div style="clear:both;"></div>

---

![Page d'exportation avec la liste des formats de fichiers disponibles](screenshots/export.png){ align=left width="300"}

### Pas de verrouillage – importation et exportation de données

Importez des données dans divers formats, y compris Gramps XML et GEDCOM, et téléchargez toutes vos données à tout moment – données d'arbre généalogique, fichiers multimédias et comptes utilisateurs – pour des sauvegardes ou pour passer à un autre serveur.

Les importations peuvent être prévisualisées comme un essai avant que quoi que ce soit ne soit écrit, et une sauvegarde complète peut être restaurée dans l'arbre.

<div style="clear:both;"></div>

## Utilisez-le partout { .feature-group }

![La même page de personne sur un bureau et sur un téléphone](screenshots/mobile.png){ align=right width="400"}

### Fonctionne sur tous les appareils

Utilisez Gramps Web sur n'importe quel appareil avec un navigateur web : téléchargez des photos, créez ou modifiez des enregistrements, ou montrez votre arbre généalogique à vos proches lors de la prochaine réunion de famille.

Gramps Web est une application web progressive : installez-la sur votre écran d'accueil ou votre bureau et elle se comporte comme une application native. Sur le bureau, des [raccourcis clavier](../user-guide/shortcuts.md) vous permettent d'accéder à tout en quelques frappes – appuyez sur `?` pour les voir tous.

<div style="clear:both;"></div>

---

![Menu de sélection de la langue](screenshots/lang.png){ align=left width="300"}

### Entièrement internationalisé

Utilisez l'interface dans l'une des plus de 50 langues traduites par la communauté Gramps.

<div style="clear:both;"></div>

## Et plus

- **Notifications et tâches en arrière-plan** – les importations, exportations, rapports et reconstructions d'index s'exécutent en arrière-plan, avec les progrès et les erreurs collectés en un seul endroit
- **Étiquettes, signets et historique** – organisez les objets avec des étiquettes codées par couleur et revenez à ce sur quoi vous travailliez
- **Édition en masse** – sélectionnez plusieurs objets dans les vues de liste pour les supprimer en une seule fois, ou fusionnez des objets en double
- **Vues de liste personnalisables** – choisissez quelles colonnes afficher, et filtrez par texte, étiquette ou confidentialité
- **Reconnaissance de texte (OCR)** – extrayez du texte à partir de documents numérisés dans votre galerie multimédia
- **Vérification des données** – vérifiez votre arbre pour des dates invraisemblables et d'autres problèmes de données
- **Calendriers** – saisissez des dates dans le calendrier grégorien, julien, hébreu, républicain français, persan, islamique ou suédois
- **Personnalisez-le** – donnez à votre site son propre nom, ses couleurs de thème, et son texte et image de page d'accueil

## Démo

Pour vous connecter à la démo, utilisez l'une des paires nom d'utilisateur/mot de passe suivantes. Chacune représente l'un des rôles d'utilisateur dans Gramps Web.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

La démo est réinitialisée toutes les deux heures, donc tous les changements que vous faites sont temporaires.

[Aller à la connexion de la démo](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### Remerciements

La démo est gentiment soutenue par DigitalOcean.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="Badge de parrainage DigitalOcean" /></a>
