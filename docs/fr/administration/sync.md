# Synchroniser Gramps Web et Gramps Desktop

*Gramps Web Sync* est un addon pour Gramps qui permet de synchroniser votre base de données Gramps sur votre ordinateur de bureau avec Gramps Web, y compris les fichiers multimédias.

!!! warning
    Comme avec tout outil de synchronisation, veuillez ne pas considérer cela comme un outil de sauvegarde. Une suppression accidentelle d'un côté sera propagée à l'autre côté. Assurez-vous de créer des sauvegardes régulières (au format XML de Gramps) de votre arbre généalogique.

!!! info
    La documentation fait référence à la dernière version de l'addon Gramps Web Sync. Veuillez utiliser le gestionnaire d'addons Gramps pour mettre à jour l'addon vers la dernière version si nécessaire.

!!! note "Qu'est-ce qui a changé dans la version 1.5"
    L'interface de l'addon a été réécrite dans la version 1.5. L'assistant étape par étape a disparu, remplacé par une seule fenêtre, et les fichiers multimédias sont maintenant confirmés avec les changements d'objet au lieu d'une page séparée par la suite. Si vous cherchez le sélecteur de mode de synchronisation, il se trouve maintenant **au-dessus** de la liste des changements plutôt qu'en dessous. Le mode de synchronisation **fusion** a été supprimé ; voir [Mode de synchronisation](#sync-mode) ci-dessous.

## Installation

L'addon nécessite Gramps 6.0 fonctionnant sur Python 3.10 ou une version plus récente.
Il est disponible dans Gramps Desktop et peut être installé [de la manière habituelle](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warning
    Veuillez vous assurer d'utiliser la même version de Gramps sur votre bureau que celle qui fonctionne sur votre serveur. Consultez la section [Obtenir de l'aide](../help/help.md) pour savoir comment trouver la version de Gramps que votre serveur utilise. La version de Gramps a la forme `MAJOR.MINOR.PATCH`, et `MAJOR` et `MINOR` doivent être les mêmes sur le web et le bureau.

### Exigences du serveur

L'addon vérifie deux choses concernant votre serveur dès qu'il se connecte, et refuse de continuer si l'une d'elles n'est pas remplie. Les deux vérifications se font avant que quoi que ce soit soit téléchargé.

- **Version de l'API Gramps Web 3.x.** Cette version de l'addon, pour Gramps 6.0, fonctionne avec l'API Gramps Web 3. Un serveur plus ancien doit être mis à jour ; un serveur fonctionnant avec une version majeure de l'API *plus récente* nécessite une version plus récente de Gramps, pas un addon plus récent, car chaque ligne de version de Gramps est associée à une version d'API. Vous pouvez trouver la version de votre serveur sous *Paramètres ▸ Informations sur la version* dans Gramps Web.
- **Une file d'attente de tâches en arrière-plan.** La synchronisation soumet ses changements en tant que tâche en arrière-plan. Sur un serveur sans file d'attente de tâches configurée, l'application des changements s'exécuterait de manière synchrone et se bloquerait sur un arbre généalogique réel, donc l'addon refuse de démarrer plutôt que d'échouer en cours de route.

Vous avez également besoin d'un compte avec au moins des privilèges d'éditeur pour appliquer des changements à la base de données distante.

Étape optionnelle :

??? note inline end "Bug du trousseau de clés Gnome"
    Il y a actuellement un [bug dans python keyring](https://github.com/jaraco/keyring/issues/496) qui affecte de nombreuses configurations de bureau Gnome. Vous devrez peut-être créer le fichier de configuration `~/.config/python_keyring/keyringrc.cfg` et le modifier pour qu'il ressemble à ceci :

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Installez `keyring` (par exemple `sudo apt install python3-keyring` ou `sudo dnf install python3-keyring`) pour permettre le stockage du mot de passe API en toute sécurité dans le gestionnaire de mots de passe de votre système.

Si le trousseau de clés ne peut pas être utilisé, l'addon le signale et continue sans lui — vous serez simplement invité à entrer votre mot de passe à chaque fois. Sur le paquet **Snap** de Gramps, le trousseau de clés système est bloqué par confinement jusqu'à ce que vous connectiez l'interface une fois :

```bash
snap connect gramps:password-manager-service
```

L'addon affiche cette commande exacte lorsqu'il détecte la situation.

## Utilisation

Une fois installé, l'addon est disponible dans Gramps sous *Outils ▸ Traitement de l'arbre généalogique ▸ Gramps&nbsp;Web&nbsp;Sync*. Après avoir confirmé le message d'avertissement indiquant que l'historique des annulations sera supprimé, la fenêtre de synchronisation s'ouvre.

**Aucun changement n'est appliqué à votre arbre local ou au serveur tant que vous ne les confirmez pas explicitement.**

La fenêtre a une bande en haut nommant l'arbre généalogique avec lequel vous synchronisez, le compte et l'adresse auxquels il appartient, et la dernière fois qu'il a été synchronisé. En bas, la version de l'addon et de l'API Web du serveur sont affichées — utiles lors du signalement d'un problème.

### Connexion

Si vous avez déjà synchronisé cet arbre généalogique auparavant et que votre mot de passe est stocké, l'addon se connecte dès son ouverture et passe directement à la comparaison. Sinon, il demande l'URL de base de votre instance Gramps Web (exemple : `https://mygrampsweb.com/`), votre nom d'utilisateur et votre mot de passe.

L'URL et le nom d'utilisateur sont stockés en texte clair dans votre répertoire utilisateur Gramps. Le mot de passe est stocké dans le gestionnaire de mots de passe de votre système uniquement si vous laissez **Se souvenir du mot de passe** coché ; le décocher supprime tout mot de passe déjà stocké pour ce serveur.

!!! tip "Plusieurs arbres généalogiques, plusieurs serveurs"
    Chaque serveur avec lequel vous synchronisez est stocké séparément, avec son propre enregistrement de la dernière synchronisation. Alterner entre deux serveurs ne perturbe plus aucun d'eux.

    Chaque entrée enregistre également **quel arbre généalogique local** il a été synchronisé pour la dernière fois. L'addon ne se connecte de lui-même que lorsque cela correspond à l'arbre que vous avez ouvert ; sinon, il affiche les détails de connexion et attend que vous appuyiez sur *Connecter*, avec un avertissement si les identifiants stockés appartiennent à un arbre différent. Cela est important car synchroniser un arbre contre un serveur contenant un arbre *différent* proposerait de supprimer le contenu des deux.

Deux actions sont disponibles tant que rien n'est écrit :

- **Changer de serveur…**, sur la bande supérieure, retourne aux détails de connexion afin que vous puissiez pointer cet arbre vers un autre serveur. Cela interrompt une comparaison en cours plutôt que de vous faire attendre qu'elle se termine.
- **Oublier ce serveur**, sur le panneau de connexion, supprime l'adresse, le nom d'utilisateur et le mot de passe stockés, ainsi que l'enregistrement de la dernière synchronisation de cet arbre. La prochaine synchronisation compare alors les deux arbres à partir de zéro.

Si vous entrez une adresse commençant par `http://` plutôt que `https://`, un avertissement apparaît au fur et à mesure que vous tapez. Votre mot de passe serait envoyé en texte clair, donc utilisez-le uniquement pour des tests locaux.

### Révision des changements

L'addon compare les bases de données locales et distantes et montre ce qu'il propose de faire. Contrairement aux versions précédentes, qui énuméraient les différences brutes entre les deux arbres, la liste montre maintenant les **actions** qui seront effectuées, regroupées par quelle base de données elles changent :

```
▾ Changera sur cet ordinateur (7 objets)
    ▾ Ajouter 3 objets
        Personne   John Smith        I0123
    ▾ Mettre à jour 4 objets
        …
▾ Changera sur le serveur (5 objets)
    …
```

Chaque ligne nomme l'objet, vous pouvez donc savoir qui ou quoi est affecté plutôt que de voir uniquement un ID Gramps.

Si quoi que ce soit doit être supprimé, un avertissement au-dessus de la liste indique combien d'objets et de quel côté. Cela apparaît chaque fois que des suppressions sont impliquées, y compris lors d'une synchronisation bidirectionnelle ordinaire qui propage une suppression que vous avez effectuée vous-même.

Appuyez sur **Appliquer** pour effectuer ce que la liste décrit.

!!! warning "Ne pas éditer pendant la révision"
    La fenêtre de synchronisation ne bloque pas le reste de Gramps, donc vous pouvez continuer à travailler pendant que la liste est ouverte. Si vous éditez un objet affecté, l'addon le détecte lorsque vous appuyez sur Appliquer, s'arrête sans rien changer et vous demande de comparer à nouveau. Rien n'est perdu, mais la comparaison doit être répétée.

#### Mode de synchronisation

Le mode de synchronisation est sélectionné **au-dessus** de la liste des changements. Le changement reconstruit la liste, car le mode décide de ce que chaque différence devient réellement.

- **Synchronisation bidirectionnelle** (par défaut) — les changements des deux côtés sont combinés. Les objets modifiés aux deux endroits sont fusionnés.
- **Réinitialiser le serveur pour correspondre à cet ordinateur** — le serveur est fait pour correspondre à cet ordinateur. Tout ce qui a été changé uniquement sur le serveur est supprimé.
- **Réinitialiser cet ordinateur pour correspondre au serveur** — cet ordinateur est fait pour correspondre au serveur. Tout ce qui a été changé uniquement ici est supprimé.

!!! note
    Le mode **fusion** disponible dans les versions précédentes a été supprimé. Il différait de la synchronisation bidirectionnelle uniquement en restaurant des objets supprimés d'un côté au lieu de propager la suppression, ce qui n'était pas une distinction que l'interface pouvait expliquer utilement. Si vous comptiez dessus, utilisez la synchronisation bidirectionnelle et restaurez tout ce que vous souhaitez conserver à partir d'une sauvegarde.

### Fichiers multimédias

Les fichiers multimédias sont traités dans le cadre de la même confirmation, pas comme une étape séparée. Si des fichiers doivent être transférés, une case à cocher en dessous de la liste propose de les déplacer :

```
[x] Transférer également 12 fichiers multimédias (4 à télécharger, 8 à télécharger)
```

Décochez-la pour synchroniser les changements d'objet sans toucher aux fichiers.

Les fichiers manquants sur *les deux* côtés sont listés séparément, car rien ne peut être fait à leur sujet :

```
2 fichiers multimédias sont manquants des deux côtés et ne peuvent pas être transférés.
```

Notez les limitations suivantes de la synchronisation des fichiers multimédias :

- Si un fichier local a un checksum différent de celui stocké dans la base de données Gramps (cela peut arriver par exemple pour des fichiers Word lorsqu'ils sont modifiés après avoir été ajoutés à Gramps), le téléchargement échouera avec un message d'erreur.
- L'outil ne vérifie pas l'intégrité de tous les fichiers locaux, donc si un fichier local existe sous le chemin stocké pour l'objet multimédia, mais que le fichier est différent de celui sur le serveur, l'outil ne le détectera pas. Utilisez l'addon Media Verify pour détecter les fichiers avec des checksums incorrects.

### Quand quelque chose ne va pas

Si une synchronisation échoue en cours de route — une connexion interrompue, par exemple — l'addon signale ce qu'il avait déjà appliqué et propose **Réessayer**, ce qui reprend à l'étape qui a échoué plutôt que de recommencer. La copie téléchargée de l'arbre distant est conservée, donc réessayer ne télécharge pas et ne compare pas une seconde fois.

Les détails techniques de l'échec sont disponibles derrière un *Détails* extensible, avec un bouton pour les copier pour un rapport de bug.

## Dépannage

### Journalisation de débogage

Si vous rencontrez des problèmes avec l'addon Sync, veuillez démarrer Gramps avec la journalisation de débogage activée en [démarrant Gramps depuis la ligne de commande](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) avec l'option suivante :

```bash
gramps --debug grampswebsync
```

Cela imprimera de nombreuses déclarations de journalisation utiles dans la ligne de commande qui vous aideront à identifier la cause du problème.

### Identifiants du serveur

Si la connexion échoue, veuillez vérifier à nouveau l'URL du serveur, votre nom d'utilisateur et votre mot de passe.

### L'addon refuse de se connecter

Si l'addon signale que la version de l'API Gramps Web du serveur est trop ancienne ou trop récente, ou qu'aucune file d'attente de tâches en arrière-plan n'est configurée, consultez [Exigences du serveur](#server-requirements) ci-dessus. Ces vérifications sont effectuées avant toute autre chose, donc le message nomme directement le problème.

### Problèmes de permissions

Si vous rencontrez une erreur impliquant des permissions, veuillez vérifier le rôle utilisateur de votre compte utilisateur Gramps Web. Vous ne pouvez appliquer des changements à la base de données distante que si vous êtes un utilisateur avec le rôle d'éditeur, de propriétaire ou d'administrateur.

### Changements inattendus dans la base de données

Si l'outil de synchronisation détecte des changements que vous pensez ne pas avoir eu lieu, il se peut qu'il y ait des incohérences dans l'une des bases de données qui trompent Gramps en détectant une différence, ou que l'heure ne soit pas synchronisée entre votre ordinateur local et votre serveur.

Veuillez vérifier que les horloges des deux machines sont correctement réglées (notez que le fuseau horaire n'a pas d'importance car l'outil utilise des timestamps Unix, qui sont indépendants du fuseau horaire).

Vous pouvez également exécuter l'outil de vérification et de réparation sur votre base de données locale et voir si cela aide.

Une méthode brute mais efficace pour s'assurer que les incohérences dans votre base de données locale ne causent pas de faux positifs est d'exporter votre base de données au format XML de Gramps et de la réimporter dans une nouvelle base de données vide. C'est une opération sans perte mais qui garantit que toutes les données sont importées de manière cohérente.

!!! tip
    Si l'addon propose un nombre alarmant de suppressions, vérifiez d'abord la bande supérieure : elle nomme l'arbre généalogique sur le serveur vers lequel vous vous apprêtez à écrire. Synchroniser contre un serveur qui contient un arbre *différent* produit exactement ce symptôme.

### Erreurs de délai d'attente

La synchronisation vers le serveur est traitée par un travailleur en arrière-plan, donc les synchronisations longues ne devraient pas expirer. Un serveur sans file d'attente de tâches configurée est refusé au moment de la connexion pour cette raison — voir [Exigences du serveur](#server-requirements).

Les demandes de l'addon au serveur expirent après 60 secondes sans réponse, donc un serveur inaccessible signale une erreur de connexion au lieu de rester bloqué indéfiniment.

### Erreurs inattendues de fichiers multimédias

Si le téléchargement d'un fichier multimédia échoue, cela est souvent causé par un décalage dans le checksum du fichier réel sur le disque et le checksum dans la base de données Gramps locale. Cela se produit souvent avec des fichiers modifiables, comme des documents de bureau, modifiés en dehors de Gramps. Veuillez utiliser l'addon Gramps Media Verify pour corriger les checksums de tous les fichiers multimédias.

### Demander de l'aide

Si tout ce qui précède ne vous aide pas, vous pouvez demander de l'aide à la communauté en postant dans la [catégorie Gramps Web du forum Gramps](https://gramps.discourse.group/c/gramps-web/28). Veuillez vous assurer de fournir :

- la version de l'addon Gramps Web Sync (et utilisez la dernière version publiée s'il vous plaît) — elle est affichée en bas de la fenêtre de synchronisation, à côté de la version de l'API Web du serveur
- la version de Gramps Desktop que vous utilisez
- la sortie de la journalisation de débogage de Gramps, activée comme décrit ci-dessus
- les informations de version de Gramps Web (vous pouvez les trouver sous Paramètres/Informations sur la version)
- tous les détails que vous pouvez fournir sur votre installation Gramps Web (auto-hébergée, Grampshub, ...)
- la sortie des journaux de votre serveur Gramps Web, si vous y avez accès (lors de l'utilisation de docker : `docker compose logs --tail 100 grampsweb` et `docker compose logs --tail 100 grampsweb-celery`)

## Contexte : comment fonctionne l'addon

Si vous êtes curieux de savoir comment l'addon fonctionne réellement, vous pouvez trouver plus de détails dans cette section.

L'addon est conçu pour garder une base de données Gramps locale synchronisée avec une base de données Gramps Web distante, permettant à la fois des modifications locales et distantes (édition collaborative).

Il n'est **pas adapté**

- Pour synchroniser avec une base de données qui n'est pas un dérivé direct (commençant par une copie de base de données ou une exportation/importation XML de Gramps) de la base de données locale
- Pour fusionner deux bases de données avec un grand nombre de changements des deux côtés nécessitant une attention manuelle pour la fusion. Utilisez l'excellent [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) à cet effet.

Les principes de fonctionnement de l'outil sont très simples :

- Il compare les bases de données locales et distantes
- S'il y a des différences, il vérifie le timestamp du dernier objet identique, appelons-le **t**
- Si un objet a changé plus récemment que **t** existe dans une base de données mais pas dans l'autre, il est synchronisé vers les deux (supposons un nouvel objet)
- Si un objet a changé la dernière fois avant **t** est absent dans une base de données, il est supprimé dans les deux (supposons un objet supprimé)
- Si un objet est différent mais a changé après **t** uniquement dans une base de données, synchronisez-le avec l'autre (supposons un objet modifié)
- Si un objet est différent mais a changé après **t** dans les deux bases de données, fusionnez-les (supposons une modification conflictuelle)

Le temps de la dernière synchronisation réussie est également enregistré, séparément pour chaque serveur, et utilisé comme **t** lorsqu'il est plus récent que le nouvel objet identique.

Cet algorithme est simple et robuste car il ne nécessite pas de suivre l'historique de synchronisation. Cependant, il fonctionne mieux lorsque vous *synchronisez souvent*.
