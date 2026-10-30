# Gramps Web DigitalOcean 1-Click App

Au lieu de [configurer Gramps Web vous-même](deployment.md), vous pouvez également utiliser l'[application Gramps Web DigitalOcean 1-Click](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean héberge la version Démo de Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="Badge de parrainage DigitalOcean" /></a>

Dans le cadre de la procédure de configuration, vous devrez créer un compte chez DigitalOcean et sélectionner un plan payant pour le "droplet" (machine virtuelle) à utiliser.

On peut dire que c'est actuellement la manière la plus simple de déployer votre propre instance de Gramps Web auto-hébergée, sécurisée par SSL, sans utiliser votre propre matériel.

!!! info
    Notez que vous paierez DigitalOcean pour les services d'hébergement. Le projet open source Gramps ne fournit pas de support payant.

## Étape 1 : Créer un compte DigitalOcean

Créez un compte sur [DigitalOcean](https://www.digitalocean.com/) si vous n'en avez pas encore.

## Étape 2 : Créer le droplet

- Allez sur [l'application Gramps Web 1-Click](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) et cliquez sur "Créer un Droplet Gramps Web".
- Choisissez un plan avec au moins 2 Go de RAM.
- Configurez l'authentification pour votre droplet.
- Cliquez sur "Créer Droplet".

!!! info
    Vous devrez peut-être attendre jusqu'à dix minutes pour que l'application 1-Click installe la dernière version de `docker-compose`.
    Utiliser la dernière version de `docker-compose` peut atténuer les erreurs faisant référence à `firstlogin.sh`.

## Étape 3 : Configurer un nom de domaine

Vous aurez besoin d'un nom de domaine (ou sous-domaine). Si vous possédez un domaine, pointez-le vers l'adresse IP de votre droplet. Sinon, vous pouvez utiliser un service gratuit tel que [DuckDNS](https://www.duckdns.org/).

## Étape 4 : Connectez-vous à votre droplet

Connectez-vous en SSH à votre droplet. Vous devriez voir le message "Bienvenue dans la configuration de l'application Gramps Web DigitalOcean 1-click !". Si ce n'est pas le cas, attendez quelques minutes et réessayez (l'installation n'est pas encore terminée).

Le script de configuration vous demandera le nom de domaine (par exemple, `mygrampswebinstance.duckdns.org`) et une adresse e-mail (nécessaire pour le certificat Let's Encrypt). En option, il vous demandera également les paramètres SMTP que Gramps Web utilise pour envoyer des e-mails, par exemple pour les réinitialisations de mot de passe ; laissez le champ hôte SMTP vide pour ignorer cela.

Une fois cela fait, attendez que la configuration soit terminée en arrière-plan.

## Étape 5 : Lancer Gramps Web

Votre instance Gramps Web devrait maintenant être accessible à la racine de votre domaine, avec un certificat SSL valide, et elle devrait afficher l'assistant de première exécution.

## Changer la configuration plus tard

Le script de configuration stocke l'URL de base et les paramètres d'e-mail dans le fichier `/root/letsencrypt.env` en tant qu'[options de configuration](configuration.md) préfixées par `GRAMPSWEB_`, par exemple :

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Pour ajouter ou modifier des paramètres, éditez ce fichier sur le droplet et appliquez le changement avec

```bash
cd /opt/grampsweb && docker compose up -d
