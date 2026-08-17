# Synchroniser Gramps Web et Gramps Desktop

*Gramps Web Sync* est un addon pour Gramps qui synchronise la base de données Gramps sur votre ordinateur de bureau avec Gramps Web, y compris les fichiers multimédias. Les modifications apportées de chaque côté sont transférées à l'autre, vous permettant de travailler localement et sur le web sur le même arbre généalogique.

Comme tout outil de synchronisation, ce n'est pas une sauvegarde : si vous supprimez quelque chose d'un côté, cela sera également supprimé de l'autre côté. Gardez des sauvegardes régulières de votre arbre généalogique au format XML de Gramps.

## Installation

L'addon nécessite Gramps 6.0 fonctionnant sur Python 3.10 ou version ultérieure. Il est disponible dans Gramps Desktop et peut être installé [de la manière habituelle](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps). Cette documentation décrit la dernière version de l'addon ; utilisez le gestionnaire d'addons de Gramps pour le mettre à jour si nécessaire.

Votre ordinateur de bureau et votre serveur doivent exécuter la même version de Gramps. La version a la forme `MAJOR.MINOR.PATCH`, et `MAJOR` et `MINOR` doivent correspondre. Consultez [Obtenir de l'aide](../help/help.md) pour savoir quelle version de Gramps votre serveur utilise.

### Exigences du serveur

L'addon vérifie deux choses sur votre serveur dès qu'il se connecte, avant que quoi que ce soit ne soit téléchargé, et s'arrête avec un message si l'une d'elles n'est pas remplie :

- **Version de l'API Gramps Web 3.x.** Cette version de l'addon, pour Gramps 6.0, fonctionne avec l'API Gramps Web 3. Un serveur plus ancien doit être mis à jour ; un serveur exécutant une version majeure de l'API *plus récente* nécessite une version plus récente de Gramps, pas un addon plus récent, car chaque ligne de version de Gramps est associée à une version d'API. Vous pouvez trouver la version de votre serveur sous *Paramètres ▸ Informations sur la version* dans Gramps Web.
- **Une file d'attente de tâches en arrière-plan.** Les modifications sont appliquées sur le serveur en tant que tâche en arrière-plan. Sans file d'attente de tâches, cela s'exécuterait de manière synchrone et se bloquerait sur tout vrai arbre généalogique.

Pour appliquer des modifications à la base de données distante, vous avez besoin d'un compte avec le rôle d'éditeur, de propriétaire ou d'administrateur.

### Stockage de votre mot de passe (optionnel)

Installez `keyring` (par exemple, `sudo apt install python3-keyring` ou `sudo dnf install python3-keyring`) pour stocker le mot de passe de l'API dans le gestionnaire de mots de passe de votre système. Si le keyring ne peut pas être utilisé, l'addon le signale et continue sans lui – vous serez simplement invité à entrer votre mot de passe à chaque fois.

Sur le paquet **Snap** de Gramps, le keyring système est bloqué par confinement jusqu'à ce que vous connectiez l'interface une fois. L'addon affiche cette commande lorsqu'il détecte la situation :

```bash
snap connect gramps:password-manager-service
```

Sur de nombreuses configurations de bureau Gnome, un [bug dans python keyring](https://github.com/jaraco/keyring/issues/496) signifie que vous devez créer le fichier de configuration `~/.config/python_keyring/keyringrc.cfg` avec le contenu suivant :

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Utilisation

L'addon est disponible dans Gramps sous *Outils ▸ Traitement de l'arbre généalogique ▸ Gramps&nbsp;Web&nbsp;Sync*. Après avoir confirmé la boîte de dialogue avertissant que l'historique des annulations sera supprimé, la fenêtre de synchronisation s'ouvre. Aucune modification n'est appliquée à votre arbre local ou au serveur tant que vous ne les confirmez pas explicitement.

Une bande le long du haut de la fenêtre nomme l'arbre généalogique avec lequel vous vous synchronisez, le compte et l'adresse auxquels il appartient, et quand il a été synchronisé pour la dernière fois. En bas, la version de l'addon et de l'API Web du serveur sont affichées, ce qui est utile lors du signalement d'un problème.

### Connexion

Si vous avez déjà synchronisé cet arbre généalogique auparavant et que votre mot de passe est stocké, l'addon se connecte dès son ouverture et passe directement à la comparaison. Sinon, il vous demande l'URL de base de votre instance Gramps Web (exemple : `https://mygrampsweb.com/`), votre nom d'utilisateur et votre mot de passe.

L'URL et le nom d'utilisateur sont stockés en texte clair dans votre répertoire utilisateur Gramps. Le mot de passe est stocké dans le gestionnaire de mots de passe de votre système uniquement si vous laissez **Se souvenir du mot de passe** coché ; le décocher supprime tout mot de passe déjà stocké pour ce serveur. Si vous entrez une adresse commençant par `http://` plutôt que `https://`, l'addon vous avertit pendant que vous tapez, car votre mot de passe serait envoyé en texte clair.

Chaque serveur avec lequel vous vous synchronisez est stocké séparément, avec son propre enregistrement de la dernière synchronisation, vous permettant d'alterner entre deux serveurs sans perturber l'un ou l'autre. Chaque entrée enregistre également quel arbre généalogique local il a été synchronisé pour la dernière fois. L'addon ne se connecte de lui-même que lorsque cela correspond à l'arbre que vous avez ouvert ; sinon, il affiche les détails de connexion et attend que vous appuyiez sur *Connecter*.

Deux actions sont disponibles tant que rien n'est écrit :

- **Changer de serveur…**, sur la bande supérieure, retourne aux détails de connexion afin que vous puissiez pointer cet arbre vers un autre serveur. Cela interrompt une comparaison en cours au lieu de vous faire attendre qu'elle se termine.
- **Oublier ce serveur**, sur le panneau de connexion, supprime l'adresse, le nom d'utilisateur et le mot de passe stockés, ainsi que l'enregistrement de la dernière synchronisation de cet arbre. La prochaine synchronisation compare alors les deux arbres depuis le début.

### Révision des modifications

L'addon compare les bases de données locales et distantes et montre les actions qu'il propose d'effectuer, regroupées par quelle base de données elles changent :

```
▾ Changera sur cet ordinateur (7 objets)
    ▾ Ajouter 3 objets
        Personne   John Smith        I0123
    ▾ Mettre à jour 4 objets
        …
▾ Changera sur le serveur (5 objets)
    …
```

Chaque ligne nomme l'objet, vous permettant de savoir qui ou quoi est affecté plutôt que de voir uniquement un ID Gramps. Si quelque chose doit être supprimé, une note au-dessus de la liste indique combien d'objets et de quel côté.

Appuyez sur **Appliquer** pour effectuer ce que la liste décrit.

La fenêtre de synchronisation ne bloque pas le reste de Gramps, vous pouvez donc continuer à travailler pendant que la liste est ouverte. Si vous modifiez un objet affecté entre-temps, l'addon le remarque lorsque vous appuyez sur Appliquer, s'arrête sans rien changer et vous demande de comparer à nouveau.

#### Mode de synchronisation

Le mode de synchronisation est sélectionné au-dessus de la liste des modifications. Le changer reconstruit la liste, car le mode détermine ce que chaque différence devient.

- **Synchronisation bidirectionnelle** (par défaut) – les modifications des deux côtés sont combinées. Les objets modifiés aux deux endroits sont fusionnés.
- **Réinitialiser le serveur pour correspondre à cet ordinateur** – le serveur est fait pour correspondre à cet ordinateur. Tout ce qui a été modifié uniquement sur le serveur est supprimé.
- **Réinitialiser cet ordinateur pour correspondre au serveur** – cet ordinateur est fait pour correspondre au serveur. Tout ce qui a été modifié uniquement ici est supprimé.

Le mode **fusion** disponible dans les versions précédant 1.5 a été supprimé. Il différait de la synchronisation bidirectionnelle uniquement en restaurant les objets supprimés d'un côté au lieu de propager la suppression. Si vous comptiez dessus, utilisez la synchronisation bidirectionnelle et restaurez tout ce que vous souhaitez conserver à partir d'une sauvegarde.

### Fichiers multimédias

Les fichiers multimédias sont traités dans le cadre de la même confirmation, pas comme une étape séparée. Si des fichiers doivent être transférés, une case à cocher sous la liste propose de les déplacer :

```
[x] Transférer également 12 fichiers multimédias (4 à télécharger, 8 à télécharger)
```

Décochez-la pour synchroniser les modifications d'objet sans toucher aux fichiers.

Les fichiers manquants sur *les deux* côtés sont listés séparément, car rien ne peut être fait à leur sujet :

```
2 fichiers multimédias sont manquants des deux côtés et ne peuvent pas être transférés.
```

La synchronisation des fichiers multimédias a deux limitations :

- Si un fichier local a un checksum différent de celui stocké dans la base de données Gramps (cela peut se produire par exemple pour des fichiers Word modifiés après avoir été ajoutés à Gramps), le téléchargement échouera avec un message d'erreur.
- L'outil ne vérifie pas l'intégrité de tous les fichiers locaux. Si un fichier existe sous le chemin stocké pour l'objet multimédia mais diffère du fichier sur le serveur, l'outil ne le détectera pas. Utilisez l'addon Media Verify pour trouver des fichiers avec des checksums incorrects.

### Si une synchronisation échoue

Si une synchronisation échoue en cours de route – une connexion interrompue, par exemple – l'addon signale ce qu'il avait déjà appliqué et propose **Réessayer**, ce qui reprend à l'étape qui a échoué plutôt que de recommencer. La copie téléchargée de l'arbre distant est conservée, donc réessayer ne le télécharge pas et ne le compare pas une seconde fois.

Les détails techniques de l'échec sont disponibles derrière un expandeur *Détails*, avec un bouton pour les copier pour un rapport de bogue.

## Dépannage

**Modifications inattendues.** Si l'addon propose un nombre alarmant de suppressions, vérifiez d'abord la bande supérieure : elle nomme l'arbre généalogique sur le serveur sur lequel vous êtes sur le point d'écrire. Synchroniser un arbre contre un serveur contenant un arbre *différent* produit exactement ce symptôme.

Sinon, des différences que vous n'attendiez pas peuvent provenir d'incohérences dans l'une des bases de données, ou d'horloges qui ne sont pas synchronisées entre votre ordinateur et votre serveur. Vérifiez que les deux horloges sont correctement réglées (le fuseau horaire n'a pas d'importance, car l'outil utilise des timestamps Unix) et exécutez l'outil de vérification et de réparation sur votre base de données locale. En dernier recours, exportez votre base de données locale au format XML de Gramps et réimportez-la dans une nouvelle base de données vide. C'est une opération sans perte, mais cela garantit que toutes les données sont stockées de manière cohérente.

**Erreurs de fichiers multimédias.** Un téléchargement échoué est souvent causé par un décalage entre le checksum du fichier sur le disque et le checksum dans la base de données Gramps locale, ce qui se produit avec des fichiers modifiables tels que des documents bureautiques modifiés en dehors de Gramps. Utilisez l'addon Gramps Media Verify pour corriger les checksums.

**Erreurs de permission.** Vérifiez le rôle de votre compte utilisateur Gramps Web : seuls les éditeurs, propriétaires et administrateurs peuvent appliquer des modifications à la base de données distante.

### Demander de l'aide

Si rien de ce qui précède n'aide, demandez de l'aide à la communauté en postant dans la [catégorie Gramps Web du forum Gramps](https://gramps.discourse.group/c/gramps-web/28). Veuillez fournir :

- la version de l'addon Gramps Web Sync, affichée en bas de la fenêtre de synchronisation à côté de la version de l'API Web du serveur (et veuillez utiliser la dernière version publiée)
- la version de Gramps Desktop que vous utilisez
- les informations de version de Gramps Web, trouvées sous *Paramètres ▸ Informations sur la version*
- tout détail concernant votre installation Gramps Web (auto-hébergé, Grampshub, ...)
- la sortie des journaux de votre serveur Gramps Web, si vous y avez accès (lors de l'utilisation de Docker : `docker compose logs --tail 100 grampsweb` et `docker compose logs --tail 100 grampsweb-celery`)

Si on vous demande un journal de débogage, démarrez Gramps [depuis la ligne de commande](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) avec la journalisation de débogage activée et reproduisez le problème :

```bash
gramps --debug grampswebsync
```

## Contexte : comment fonctionne l'addon

L'addon est conçu pour maintenir une base de données Gramps locale synchronisée avec une base de données Gramps Web distante, permettant à la fois des modifications locales et distantes (édition collaborative).

Il **n'est pas adapté**

- pour synchroniser avec une base de données qui n'est pas un dérivé direct (à partir d'une copie de base de données ou d'une exportation/importation XML de Gramps) de la base de données locale,
- pour fusionner deux bases de données avec un grand nombre de modifications des deux côtés nécessitant une attention manuelle pour la fusion. Utilisez l'excellent [Outil de fusion d'importation](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) à cette fin.

Les principes de fonctionnement sont simples :

- Il compare les bases de données locales et distantes.
- S'il y a des différences, il vérifie l'horodatage du dernier objet identique, appelons-le **t**.
- Si un objet a changé plus récemment que **t** existe dans une base de données mais pas dans l'autre, il est synchronisé vers les deux (supposons un nouvel objet).
- Si un objet a changé la dernière fois avant **t** est absent dans une base de données, il est supprimé dans les deux (supposons un objet supprimé).
- Si un objet est différent mais a changé après **t** uniquement dans une base de données, synchronisez-le avec l'autre (supposons un objet modifié).
- Si un objet est différent mais a changé après **t** dans les deux bases de données, fusionnez-les (supposons une modification conflictuelle).

Le temps de la dernière synchronisation réussie est également enregistré, séparément pour chaque serveur, et utilisé comme **t** lorsqu'il est plus récent que le nouvel objet identique.

Cet algorithme est simple et robuste car il ne nécessite pas de suivi de l'historique de synchronisation. Cependant, il fonctionne mieux lorsque vous *synchronisez souvent*.
