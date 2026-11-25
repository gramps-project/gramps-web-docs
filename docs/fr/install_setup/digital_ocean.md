# Application Gramps Web DigitalOcean en un clic

Au lieu de [configurer vous-même Gramps Web](deployment.md), vous pouvez également utiliser l’[application Gramps Web DigitalOcean en un clic](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean héberge la version de démonstration de Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="Badge de parrainage DigitalOcean" /></a>

Dans le cadre de la procédure de configuration, vous devrez créer un compte DigitalOcean et sélectionner une formule payante pour le « droplet » (machine virtuelle) à utiliser.

On peut raisonnablement considérer qu’il s’agit actuellement de la manière la plus simple de déployer votre propre instance Gramps Web auto-hébergée, sécurisée avec SSL, sans utiliser votre propre matériel.

!!! info
    Notez que vous paierez DigitalOcean pour les services d’hébergement. Le projet open source Gramps ne fournit pas d’assistance payante.

## Étape 1 : Créer un compte DigitalOcean

Créez un compte sur [DigitalOcean](https://www.digitalocean.com/) si vous n’en avez pas encore.

## Étape 2 : Créer le droplet

- Accédez à l’[application Gramps Web en un clic](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) et cliquez sur « Create Gramps Web Droplet ».
- Choisissez une formule disposant d’au moins 2 Go de RAM.
- Configurez l’authentification sur votre droplet
- Cliquez sur « Create Droplet »

## Étape 3 : Configurer un nom de domaine

Vous aurez besoin d’un nom de domaine (ou d’un sous-domaine). Si vous possédez un domaine, faites-le pointer vers l’adresse IP de votre droplet. Sinon, vous pouvez utiliser un service gratuit tel que [DuckDNS](https://www.duckdns.org/).

## Étape 4 : Se connecter à votre droplet

Connectez-vous à votre droplet via SSH. Le message « Welcome to the Gramps Web DigitalOcean 1-click app setup! » devrait s’afficher. Si ce n’est pas le cas, attendez quelques minutes, puis réessayez (l’installation n’est pas encore terminée).

Le script de configuration vous demandera le nom de domaine (par exemple, `mygrampswebinstance.duckdns.org`) ainsi qu’une adresse e-mail (nécessaire pour le certificat Let’s Encrypt). Il vous demandera également, si vous le souhaitez, les paramètres SMTP utilisés par Gramps Web pour envoyer des e-mails, par exemple pour les réinitialisations de mot de passe ; laissez l’hôte SMTP vide pour ignorer cette étape.

Une fois cette opération terminée, attendez que la configuration soit achevée en arrière-plan

## Étape 5 : Lancer Gramps Web

Votre instance Gramps Web devrait maintenant être accessible à la racine de votre domaine, avec un certificat SSL valide, et l’assistant de première exécution devrait s’afficher.

## Modifier la configuration ultérieurement

Le script de configuration enregistre l’URL de base et les paramètres d’e-mail dans le fichier `/root/letsencrypt.env` sous forme d’[options de configuration](configuration.md) préfixées par `GRAMPSWEB_`, par exemple :

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Pour ajouter ou modifier des paramètres, modifiez ce fichier sur le droplet, puis appliquez la modification avec

```bash
cd /opt/grampsweb && docker compose up -d
```
