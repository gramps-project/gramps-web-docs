# Synchroniser Gramps Web et Gramps Desktop

*Gramps Web Sync* est un addon pour Gramps qui permet de synchroniser votre base de données Gramps sur votre ordinateur de bureau avec Gramps Web, y compris les fichiers multimédias.

!!! warning
    Comme avec tout outil de synchronisation, veuillez ne pas considérer cela comme un outil de sauvegarde. Une suppression accidentelle d'un côté sera propagée à l'autre côté. Assurez-vous de créer des sauvegardes régulières (au format XML Gramps) de votre arbre généalogique.

!!! info
    La documentation fait référence à la dernière version de l'addon Gramps Web Sync. Veuillez utiliser le gestionnaire d'addons Gramps pour mettre à jour l'addon vers la dernière version si nécessaire.

## Installation

L'addon nécessite Gramps 6.0 fonctionnant sur Python 3.10 ou une version plus récente.  
Il est disponible dans Gramps Desktop et peut être installé [de la manière habituelle](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warn
    Veuillez vous assurer d'utiliser la même version de Gramps sur votre bureau que celle exécutée sur votre serveur. Consultez la section [Obtenir de l'aide](../help/help.md) pour savoir quelle version de Gramps votre serveur utilise. La version de Gramps a la forme `MAJOR.MINOR.PATCH`, et `MAJOR` et `MINOR` doivent être les mêmes sur le web et le bureau.

Étape optionnelle :

??? note inline end "Bug du trousseau de clés Gnome"
    Il y a actuellement un [bug dans python keyring](https://github.com/jaraco/keyring/issues/496) qui affecte de nombreuses configurations de bureau Gnome. Vous devrez peut-être créer le fichier de configuration `~/.config/python_keyring/keyringrc.cfg` et l'éditer pour qu'il ressemble à ceci :

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Installez `keyring` (par exemple `sudo apt install python3-keyring` ou `sudo dnf install python3-keyring`) pour permettre le stockage du mot de passe API en toute sécurité dans le gestionnaire de mots de passe de votre système.

## Utilisation

Une fois installé, l'addon est disponible dans Gramps sous *Outils > Traitement de l'arbre généalogique > Gramps&nbsp;Web&nbsp;Sync*. Une fois démarré, et après avoir confirmé la boîte de dialogue indiquant que l'historique des annulations sera supprimé, un assistant vous guidera à travers les étapes de synchronisation. Notez qu'aucun changement ne sera appliqué à votre arbre local ou au serveur tant que vous ne les confirmez pas explicitement.

### Étape 1 : entrer les identifiants du serveur

L'outil vous demandera l'URL de base (exemple : `https://mygrampsweb.com/`) de votre instance Gramps Web, votre nom d'utilisateur et votre mot de passe. Vous avez besoin d'un compte avec au moins des privilèges d'éditeur pour synchroniser les modifications vers votre base de données distante. Le nom d'utilisateur et l'URL seront stockés en texte clair dans votre répertoire utilisateur Gramps, le mot de passe ne sera stocké que si `keyring` est installé (voir ci-dessus).

### Étape 2 : examiner les changements

Après avoir confirmé vos identifiants, l'outil compare les bases de données locales et distantes et évalue s'il y a des différences. S'il y en a, il affiche une liste des changements d'objets (où un objet peut être une personne, une famille, un événement, un lieu, etc.) appartenant à l'une des catégories suivantes :

- ajouté localement
- supprimé localement
- modifié localement
- ajouté à distance
- supprimé à distance
- modifié à distance
- modifié simultanément (c'est-à-dire, des deux côtés)

L'outil utilise des horodatages pour évaluer quel côté est le plus récent pour chaque objet (voir "Contexte" ci-dessous si vous êtes intéressé par les détails).

Si les changements semblent conformes à vos attentes, vous pouvez cliquer sur "Appliquer" pour appliquer les modifications nécessaires aux bases de données locales et distantes.

!!! tip "Avancé : Mode de synchronisation"
    En dessous de la liste des changements, vous pouvez sélectionner un mode de synchronisation.
    
    Le mode par défaut, **synchronisation bidirectionnelle**, signifie qu'il appliquera les changements des deux côtés (local et distant) en répliquant les changements détectés (les objets ajoutés localement seront ajoutés du côté distant, etc.). Les objets modifiés des deux côtés seront fusionnés et mis à jour des deux côtés également.

    L'option **réinitialiser distant à local** garantira plutôt que la base de données Gramps distante ressemble exactement à celle locale. Tous les objets détectés comme "ajoutés à distance" seront supprimés à nouveau, les objets détectés comme "supprimés à distance" seront ajoutés à nouveau, etc. *Aucun changement ne sera appliqué à la base de données Gramps locale.*

    L'option **réinitialiser local à distant** fonctionne à l'inverse et définit l'état local sur celui de la base de données distante. *Aucun changement ne sera appliqué à la base de données distante.*

    Enfin, l'option **fusionner** est similaire à la synchronisation bidirectionnelle en ce sens qu'elle modifie les deux bases de données, mais elle *ne supprime aucun objet*, mais restaure tous les objets supprimés d'un seul côté.

### Étape 3 : synchroniser les fichiers multimédias

*Après* que les bases de données ont été synchronisées, l'outil vérifie s'il y a de nouveaux fichiers multimédias ou des fichiers mis à jour. S'il en trouve, il affiche une liste et demande confirmation pour télécharger/téléverser les fichiers nécessaires.

Notez les limitations suivantes de la synchronisation des fichiers multimédias :

- Si un fichier local a un checksum différent de celui stocké dans la base de données Gramps (cela peut se produire par exemple pour des fichiers Word lorsqu'ils sont modifiés après avoir été ajoutés à Gramps), le téléchargement échouera avec un message d'erreur.
- L'outil ne vérifie pas l'intégrité de tous les fichiers locaux, donc si un fichier local existe sous le chemin stocké pour l'objet multimédia, mais que le fichier est différent de celui sur le serveur, l'outil ne le détectera pas. Utilisez l'addon Media Verify pour détecter les fichiers avec des checksums incorrects.

## Dépannage

### Journalisation de débogage

Si vous rencontrez des problèmes avec l'addon Sync, veuillez démarrer Gramps avec la journalisation de débogage activée en [démarrant Gramps depuis la ligne de commande](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) avec l'option suivante :

```bash
gramps --debug grampswebsync
```

Cela imprimera de nombreuses déclarations de journalisation utiles dans la ligne de commande qui vous aideront à identifier la cause du problème.

### Identifiants du serveur

Si la première étape échoue déjà, veuillez vérifier à nouveau l'URL du serveur, votre nom d'utilisateur et votre mot de passe.

### Problèmes de permissions

Si vous rencontrez une erreur impliquant des permissions, veuillez vérifier le rôle utilisateur de votre compte utilisateur Gramps Web. Vous ne pouvez appliquer des changements à la base de données distante que si vous êtes un utilisateur avec le rôle d'éditeur, de propriétaire ou d'administrateur.

### Changements inattendus dans la base de données

Si l'outil de synchronisation détecte des changements que vous pensez ne pas avoir eu lieu, il se peut qu'il y ait des incohérences dans l'une des bases de données qui trompent Gramps en détectant une différence, ou que l'heure ne soit pas synchronisée entre votre ordinateur local et votre serveur.

Veuillez vérifier que les horloges des deux machines sont correctement réglées (notez que le fuseau horaire n'a pas d'importance car l'outil utilise des horodatages Unix, qui sont indépendants du fuseau horaire).

Vous pouvez également exécuter l'outil de vérification et de réparation sur votre base de données locale et voir si cela aide.

Une méthode brute mais efficace pour s'assurer que les incohérences dans votre base de données locale ne causent pas de faux positifs est d'exporter votre base de données au format XML Gramps et de la réimporter dans une nouvelle base de données vide. C'est une opération sans perte mais qui garantit que toutes les données sont importées de manière cohérente.

### Erreurs de délai d'attente

Si vous rencontrez des erreurs de délai d'attente (par exemple, indiquées par une erreur de statut HTTP 408 ou un autre message d'erreur incluant le mot "délai d'attente"), cela est probablement dû à un grand nombre de changements qui doivent être synchronisés du côté distant en combinaison avec la configuration de votre serveur.

Pour les versions de l'addon de synchronisation antérieures à v1.2.0 et les versions de l'API Gramps Web antérieures à v2.7.0 (voir l'onglet d'informations sur la version dans Gramps Web), la synchronisation vers le côté serveur était traitée dans une seule requête qui pourrait expirer, en fonction de la configuration du serveur, après une à quelques minutes au maximum. Pour de grandes synchronisations (comme après l'importation de milliers d'objets dans la base de données locale ou en essayant de synchroniser une base de données locale complète vers une base de données vide côté serveur), cela peut être trop court.

Si vous utilisez l'addon de synchronisation v1.2.0 ou une version ultérieure et l'API Gramps Web v2.7.0 ou une version ultérieure, la synchronisation côté serveur est traitée par un travailleur en arrière-plan et peut fonctionner très longtemps (une barre de progression sera affichée) et les erreurs de délai d'attente ne devraient pas se produire.

### Erreurs inattendues de fichiers multimédias

Si le téléversement d'un fichier multimédia échoue, cela est souvent causé par un désaccord entre le checksum du fichier réel sur le disque et le checksum dans la base de données Gramps locale. Cela se produit souvent avec des fichiers modifiables, comme des documents de bureau, modifiés en dehors de Gramps. Veuillez utiliser l'addon Gramps Media Verify pour corriger les checksums de tous les fichiers multimédias.

### Demander de l'aide

Si tout ce qui précède ne vous aide pas, vous pouvez demander de l'aide à la communauté en publiant dans la [catégorie Gramps Web du forum Gramps](https://gramps.discourse.group/c/gramps-web/28). Veuillez vous assurer de fournir :

- la version de l'addon Gramps Web Sync (et utilisez la dernière version publiée, s'il vous plaît)
- la version de Gramps desktop que vous utilisez
- la sortie de la journalisation de débogage de Gramps, activée comme décrit ci-dessus
- les informations de version de Gramps Web (vous pouvez les trouver sous Paramètres/Informations sur la version)
- tous les détails que vous pouvez fournir sur votre installation Gramps Web (auto-hébergé, Grampshub, ...)
- la sortie des journaux de votre serveur Gramps Web, si vous y avez accès (lors de l'utilisation de docker : `docker compose logs --tail 100 grampsweb` et `docker compose logs --tail 100 grampsweb-celery`)

## Contexte : comment fonctionne l'addon

Si vous êtes curieux de savoir comment l'addon fonctionne réellement, vous pouvez trouver plus de détails dans cette section.

L'addon est conçu pour maintenir une base de données Gramps locale synchronisée avec une base de données Gramps Web distante, afin de permettre à la fois des modifications locales et distantes (édition collaborative).

Il **n'est pas adapté**

- Pour synchroniser avec une base de données qui n'est pas un dérivé direct (à partir d'une copie de base de données ou d'une exportation/importation XML Gramps) de la base de données locale
- Pour fusionner deux bases de données avec un grand nombre de changements des deux côtés nécessitant une attention manuelle pour la fusion. Utilisez l'excellent [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) à cette fin.

Les principes de fonctionnement de l'outil sont très simples :

- Il compare les bases de données locales et distantes
- S'il y a des différences, il vérifie l'horodatage du dernier objet identique, appelons-le **t**
- Si un objet a changé plus récemment que **t** existe dans une base de données mais pas dans l'autre, il est synchronisé vers les deux (supposons un nouvel objet)
- Si un objet a changé la dernière fois avant **t** est absent dans une base de données, il est supprimé dans les deux (supposons un objet supprimé)
- Si un objet est différent mais a changé après **t** uniquement dans une base de données, synchronisez-le avec l'autre (supposons un objet modifié)
- Si un objet est différent mais a changé après **t** dans les deux bases de données, fusionnez-les (supposons une modification conflictuelle)

Cet algorithme est simple et robuste car il ne nécessite pas de suivre l'historique de synchronisation. Cependant, il fonctionne mieux lorsque vous *synchronisez souvent*.
