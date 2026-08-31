---
hide:
  - toc
  - navigation
---

# Fonctionnalités


![Image title](screenshots/sync.png){ align=left width="300"}

## Intégration complète avec Gramps Desktop

Gramps Web utilise la même structure **Modèle / Base de données** que [Gramps Desktop](https://gramps-project.org/) pour stocker les données généalogiques. Vous pouvez parcourir tous les mêmes [Types d'enregistrements](https://gramps-project.org/wiki/index.php/Gramps_Data_Model) que dans Gramps Desktop : ***personnes, familles, événements, lieux, dépôts, sources, citations, objets multimédias et notes.***

En utilisant le [Gramps Web Sync Add-on](../administration/sync.md) pour Gramps Desktop, les données peuvent être synchronisées dans les deux sens entre Gramps Web et Gramps Desktop ! N'hésitez pas à modifier vos données avec Gramps Web ou l'application Gramps Desktop que vous connaissez et aimez – elles fonctionnent ensemble sans problème !

<div style="clear:both;"></div>

---

![Image title](screenshots/fan.png){ align=right width="400"}

## Graphiques interactifs d'arbre généalogique

Naviguez dans votre arbre généalogique sous forme d'arbre d'ancêtres, d'arbre de descendants, de graphique en sablier, de graphique de relations ou de graphique en éventail, avec des graphiques interactifs de haute qualité et un nombre de générations configurable.

Survolez n'importe quelle personne pour voir une carte de prévisualisation avec ses faits clés, et passez directement du graphique à la page de détails complète.

<div style="clear:both;"></div>

---

![Image title](screenshots/tree-edit.png){ align=left width="400"}

## Construisez votre arbre directement dans le graphique

Passez le mode de vue de l'arbre en mode édition et développez votre arbre généalogique sans quitter le graphique. Chaque carte de personne dispose d'un bouton **+** pour ajouter un père, une mère, un enfant ou un conjoint – soit en liant quelqu'un déjà dans votre base de données, soit en créant une toute nouvelle personne sur le champ. Chaque changement est enregistré immédiatement.

Voir [Édition de l'arbre généalogique](../user-guide/tree-edit.md).

<div style="clear:both;"></div>

---

![Image title](screenshots/timeline.png){ align=right width="400"}

## Chronologie chronologique

Voyez chaque événement dans votre arbre généalogique disposé sur une chronologie horizontale et zoomable. Faites défiler et zoomez à travers les siècles, puis filtrez pour une seule personne – ou pour tous ses ancêtres ou descendants – ou pour tout ce qui s'est passé à un endroit donné.

Voir [Chronologie](../user-guide/timeline.md).

<div style="clear:both;"></div>

---

![Image title](screenshots/map.png){ align=left width="400"}

## Carte puissante

Affichez tous les lieux de votre arbre sur une carte interactive et recherchable. Recherchez de nouveaux lieux directement sur OpenStreetMap lors de la création d'un lieu, tracez les personnes de votre base de données géographiquement et retracez la vie d'une seule personne en reliant ses événements par des lignes sur la carte.

<div style="clear:both;"></div>

---

![Image title](screenshots/ohm.png){ align=right width="400"}

## Cartes historiques

Transformez une carte historique stockée en tant qu'objet multimédia dans Gramps en une superposition de carte personnalisée.

De plus, les cartes vectorielles historiques créées par le projet [OpenHistoricalMap](https://www.openhistoricalmap.org/) sont le complément parfait à la cartographie généalogique. Utilisez le curseur temporel pour faire défiler l'évolution des lieux dans votre histoire familiale et afficher les lieux où vivaient vos ancêtres ou où se sont déroulés des événements.

<div style="clear:both;"></div>

---

![Image title](screenshots/search.png){ align=left width="400"}

## Trouvez n'importe quoi

Le moteur de recherche en texte intégral couvre tous les types d'objets Gramps, y compris le contenu des notes textuelles, et prend en charge les jokers et les opérateurs logiques.

Si votre serveur l'a activé, la **recherche sémantique** répond à des requêtes en langage naturel comme "fermier en Bavière au 19ème siècle" par le sens plutôt que par des mots exacts. Pour des requêtes précises, les vues de liste d'objets offrent un mode de filtre avancé basé sur le [Gramps Query Language](../user-guide/gql.md), ainsi que des filtres rapides par texte, étiquette et confidentialité.

Depuis la page de n'importe quelle personne, [Recherche externe](../user-guide/external-search.md) ouvre une recherche pré-remplie sur FamilySearch, Ancestry, CompGen et d'autres sites – et vous pouvez ajouter les vôtres.

<div style="clear:both;"></div>

---

![Image title](screenshots/chat.png){ align=right width="400"}

## Assistant AI intégré

Propulsé par l'IA, Gramps Web vous permet de discuter avec votre arbre généalogique – dans votre langue maternelle !

L'assistant ne se contente pas de rechercher : il interroge directement votre base de données avec un ensemble d'outils, filtrant les personnes, événements, familles et lieux, et calculant les relations entre les individus. Vous pouvez voir quels outils il utilise pendant qu'il construit une réponse, et les questions plus longues s'exécutent en arrière-plan afin que vous puissiez naviguer ailleurs et revenir.

<div style="clear:both;"></div>

---

![Image title](screenshots/dna.png){ align=left width="400"}

## Correspondances ADN, navigateur de chromosomes & Y-ADN

Si vous avez des données de correspondance ADN provenant d'un des fournisseurs de généalogie ADN, téléchargez-les et stockez-les de manière pérenne et visualisez vos correspondances dans un navigateur de chromosomes interactif.

Les données brutes SNP du chromosome Y peuvent être utilisées pour déterminer le [haplogroupe Y-ADN](../user-guide/y-dna.md) le plus probable d'une personne et afficher ses ancêtres patrilinéaires dans l'arbre du chromosome Y humain, avec des estimations de temps. L'analyse s'exécute entièrement sur votre propre serveur – aucune donnée n'est envoyée à un tiers.

<div style="clear:both;"></div>

---

![Image title](screenshots/tag.png){ align=right width="400"}

## Taguer des personnes sur des photos avec détection automatique des visages

Collaborez avec vos proches pour identifier des ancêtres sur de vieilles photos de famille. Grâce à la détection automatique des visages, le marquage des personnes ne nécessite que deux clics.

<div style="clear:both;"></div>

---

![Image title](screenshots/revisions.png){ align=left width="400"}

## Historique complet des révisions – avec annulation

Chaque modification de votre arbre généalogique est enregistrée. Parcourez l'historique complet regroupé par transaction, examinez tout changement individuel pour voir exactement quels champs ont été ajoutés, supprimés ou modifiés, et annulez une transaction si cela s'avère être une erreur.

Voir [Historique des révisions](../user-guide/revisions.md).

<div style="clear:both;"></div>

---

![Image title](screenshots/list.png){ align=right width="400"}

## Niveaux de confidentialité & accès utilisateur

De nombreuses personnes souhaitent garder certains détails privés et nous respectons cela ! Vous pouvez marquer des enregistrements comme privés et contrôler quels utilisateurs sont autorisés à voir des enregistrements privés. Les enregistrements privés sont filtrés au niveau de la base de données pour une sécurité maximale. De plus, vous pouvez contrôler ce que les utilisateurs peuvent ajouter et modifier.

Les utilisateurs peuvent se connecter avec un mot de passe, ou via un fournisseur d'identité externe utilisant [OpenID Connect](../install_setup/oidc.md) – Google et Microsoft par défaut, ainsi que des fournisseurs personnalisés tels que Keycloak, Authentik et Authelia.

<div style="clear:both;"></div>

---

![Image title](screenshots/blog.png){ align=left width="400"}

## Blog de généalogie inclus

Résumez vos recherches sous forme d'histoires de blog avec des images, et partagez-les avec vos proches. Un éditeur dédié rend l'écriture d'un nouveau post simple. Toutes les données sont stockées dans la base de données Gramps.

<div style="clear:both;"></div>

---

![Image title](screenshots/tasks.png){ align=right width="400"}

## Application de gestion des tâches intégrée

Gramps Web est livré avec une application de gestion des tâches intégrée pour organiser et planifier vos recherches généalogiques. Donnez à chaque tâche un statut, une priorité et des étiquettes, documentez vos progrès dans une description en texte enrichi, et joignez les médias que vous avez rassemblés en cours de route.

Les tâches sont stockées en tant que sources dans la base de données Gramps, elles font donc partie de vos données généalogiques et peuvent être accessibles et modifiées dans Gramps Desktop également.

<div style="clear:both;"></div>

---

![Image title](screenshots/report.png){ align=left width="400"}

## Générer des rapports imprimables

Puisqu'il est construit directement sur le noyau alimentant Gramps Desktop, vous pouvez générer presque tous les [rapports](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Reports) que l'application de bureau prend en charge directement depuis le navigateur, y compris des graphiques de relations ou des rapports de livres au format PDF.

<div style="clear:both;"></div>

---

![Image title](screenshots/export.png){ align=right width="300"}

## Pas de verrouillage – importation et exportation de données

En plus de pouvoir importer des données dans divers formats, y compris Gramps XML et GEDCOM, Gramps Web facilite aux utilisateurs le téléchargement de toutes leurs données (données de l'arbre généalogique, fichiers multimédias, comptes utilisateurs) à tout moment, à des fins de sauvegarde ou pour passer à un autre serveur. Vos données vous appartiennent !

Les imports peuvent être prévisualisés comme un essai avant que quoi que ce soit ne soit écrit, et une sauvegarde complète peut être restaurée dans l'arbre.

<div style="clear:both;"></div>

---

![Image title](screenshots/mobile.png){ align=left width="400"}

## Fonctionne sur tous les appareils

Accédez à Gramps Web depuis n'importe quel appareil connecté à Internet. Vous pouvez télécharger des photos, créer ou modifier des enregistrements, montrer votre arbre généalogique à d'autres, ou rechercher ces noms de membres de la famille que vous ne pouvez pas vous souvenir lors de votre prochaine réunion de famille !

Gramps Web est une application web progressive : installez-la sur votre écran d'accueil ou votre bureau et elle se comporte comme une application native. Sur le bureau, des [raccourcis clavier](../user-guide/shortcuts.md) vous permettent d'accéder à n'importe où en quelques frappes – appuyez sur `?` pour les voir tous.

<div style="clear:both;"></div>

---

![Image title](screenshots/lang.png){ align=right width="300"}

## Entièrement internationalisé

Changez la langue de l'interface entre l'une des plus de 50 langues traduites par la communauté Gramps.

<div style="clear:both;"></div>

---

## Et plus

- **Notifications et tâches en arrière-plan** – les imports, exports, rapports et reconstructions d'index s'exécutent en arrière-plan, avec le progrès et les erreurs collectées en un seul endroit
- **Étiquettes, signets et historique** – organisez les objets avec des étiquettes codées par couleur et revenez à ce sur quoi vous travailliez
- **Édition en masse** – sélectionnez plusieurs objets dans les vues de liste pour les supprimer en une seule fois, ou fusionnez des objets en double
- **Vues de liste personnalisables** – choisissez quelles colonnes afficher, et filtrez par texte, étiquette ou confidentialité
- **Reconnaissance de texte (OCR)** – extrayez du texte à partir de documents numérisés dans votre galerie multimédia
- **Vérification des données** – vérifiez votre arbre pour des dates peu plausibles et d'autres problèmes de données
- **Personnalisez-le** – donnez à votre site son propre nom, des couleurs de thème, et du texte et une image de page d'accueil

<p>&nbsp;</p>

## Démo

Pour vous connecter à la Démo, utilisez l'un des identifiants de connexion ***USER / PASS*** suivants. Chacun représente un type d'utilisateur auquel un utilisateur de Gramps Web peut être assigné.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`


[Accéder à la connexion de démonstration](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}


### Remerciements

La démo est gentiment soutenue par DigitalOcean.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
