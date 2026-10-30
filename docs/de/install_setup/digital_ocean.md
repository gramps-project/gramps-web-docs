# Gramps Web DigitalOcean 1-Click App

Statt [Gramps Web selbst einzurichten](deployment.md), können Sie auch die [Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) verwenden. Digital Ocean hostet die Demoversion von Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Im Rahmen des Einrichtungsverfahrens müssen Sie sich ein Konto bei DigitalOcean erstellen und einen kostenpflichtigen Plan für den "Droplet" (virtuelle Maschine) auswählen.

Man könnte sagen, dass dies derzeit der einfachste Weg ist, Ihre eigene, selbst gehostete Gramps Web-Instanz mit SSL-Schutz bereitzustellen, ohne eigene Hardware zu verwenden.

!!! info
    Beachten Sie, dass Sie DigitalOcean für die Hosting-Dienste bezahlen werden. Das Gramps-Open-Source-Projekt bietet keinen kostenpflichtigen Support an.

## Schritt 1: Erstellen Sie ein DigitalOcean-Konto

Erstellen Sie ein Konto bei [DigitalOcean](https://www.digitalocean.com/), wenn Sie noch keins haben.

## Schritt 2: Erstellen Sie den Droplet

- Gehen Sie zur [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) und klicken Sie auf "Gramps Web Droplet erstellen".
- Wählen Sie einen Plan mit mindestens 2 GB RAM.
- Richten Sie die Authentifizierung für Ihren Droplet ein.
- Klicken Sie auf "Droplet erstellen".

## Schritt 3: Richten Sie einen Domainnamen ein

Sie benötigen einen Domainnamen (oder Subdomain). Wenn Sie eine Domain besitzen, weisen Sie sie auf die IP-Adresse Ihres Droplets. Andernfalls können Sie einen kostenlosen Dienst wie [DuckDNS](https://www.duckdns.org/) verwenden.

## Schritt 4: Melden Sie sich bei Ihrem Droplet an

SSH in Ihren Droplet. Ihnen sollte die Nachricht "Willkommen beim Gramps Web DigitalOcean 1-Click App Setup!" angezeigt werden. Wenn dies nicht der Fall ist, warten Sie ein paar Minuten und versuchen Sie es erneut (die Installation ist noch nicht abgeschlossen).

Das Einrichtungs-Skript wird Sie nach dem Domainnamen (z. B. `mygrampswebinstance.duckdns.org`) und einer E-Mail-Adresse (benötigt für das Let's Encrypt-Zertifikat) fragen. Optional wird es auch nach den SMTP-Einstellungen fragen, die Gramps Web zum Versenden von E-Mails verwendet, z. B. für Passwortzurücksetzungen; lassen Sie den SMTP-Host leer, um dies zu überspringen.

Wenn dies erledigt ist, warten Sie, bis die Einrichtung im Hintergrund abgeschlossen ist.

## Schritt 5: Starten Sie Gramps Web

Ihre Gramps Web-Instanz sollte jetzt im Root-Bereich Ihrer Domain mit einem gültigen SSL-Zertifikat zugänglich sein und den Assistenten für die erste Ausführung anzeigen.

## Ändern der Konfiguration später

Das Einrichtungs-Skript speichert die Basis-URL und die E-Mail-Einstellungen in der Datei `/root/letsencrypt.env` als [Konfigurationsoptionen](configuration.md), die mit `GRAMPSWEB_` vorangestellt sind, z. B.

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Um Einstellungen hinzuzufügen oder zu ändern, bearbeiten Sie diese Datei auf dem Droplet und wenden Sie die Änderung mit

```bash
cd /opt/grampsweb && docker compose up -d
