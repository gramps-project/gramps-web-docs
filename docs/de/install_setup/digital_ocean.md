# Gramps Web DigitalOcean 1-Klick-App

Anstatt [Gramps Web selbst einzurichten](deployment.md), kannst du auch die [Gramps Web DigitalOcean 1-Klick-App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) verwenden. DigitalOcean hostet die Demo-Version von Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Im Rahmen des Einrichtungsvorgangs musst du ein Konto bei DigitalOcean erstellen und einen kostenpflichtigen Tarif für den zu verwendenden „Droplet“ (virtuelle Maschine) auswählen.

Dies ist derzeit wohl die einfachste Möglichkeit, deine eigene, selbst gehostete Gramps-Web-Instanz bereitzustellen, die mit SSL abgesichert ist, ohne deine eigene Hardware zu verwenden.

!!! info
    Beachte, dass du DigitalOcean für die Hosting-Dienste bezahlen musst. Das Open-Source-Projekt Gramps bietet keinen kostenpflichtigen Support an.

## Schritt 1: DigitalOcean-Konto erstellen

Erstelle ein Konto bei [DigitalOcean](https://www.digitalocean.com/), falls du noch keines hast.

## Schritt 2: Droplet erstellen

- Gehe zu [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) und klicke auf „Create Gramps Web Droplet“.
- Wähle einen Tarif mit mindestens 2 GB RAM.
- Richte die Authentifizierung für dein Droplet ein
- Klicke auf „Create Droplet“

## Schritt 3: Domainnamen einrichten

Du benötigst einen Domainnamen (oder eine Subdomain). Wenn du eine Domain besitzt, verweise sie auf die IP-Adresse deines Droplets. Andernfalls kannst du einen kostenlosen Dienst wie [DuckDNS](https://www.duckdns.org/) verwenden.

## Schritt 4: Bei deinem Droplet anmelden

Melde dich per SSH bei deinem Droplet an. Dir sollte die Meldung „Welcome to the Gramps Web DigitalOcean 1-click app setup!“ angezeigt werden. Falls dies nicht der Fall ist, warte einige Minuten und versuche es erneut (die Installation ist noch nicht abgeschlossen).

Das Einrichtungsskript fragt dich nach dem Domainnamen (z. B. `mygrampswebinstance.duckdns.org`) und einer E-Mail-Adresse (die für das Let's-Encrypt-Zertifikat benötigt wird). Optional fragt es dich auch nach den SMTP-Einstellungen, die Gramps Web zum Senden von E-Mails verwendet, z. B. für das Zurücksetzen von Passwörtern. Lass den SMTP-Host leer, um dies zu überspringen.

Wenn dies erledigt ist, warte, bis die Einrichtung im Hintergrund abgeschlossen ist.

## Schritt 5: Gramps Web starten

Deine Gramps-Web-Instanz sollte jetzt am Stammverzeichnis deiner Domain mit einem gültigen SSL-Zertifikat erreichbar sein und den Assistenten für die Ersteinrichtung anzeigen.

## Konfiguration später ändern

Das Einrichtungsskript speichert die Basis-URL und die E-Mail-Einstellungen in der Datei `/root/letsencrypt.env` als [Konfigurationsoptionen](configuration.md) mit dem Präfix `GRAMPSWEB_`, z. B.

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Um Einstellungen hinzuzufügen oder zu ändern, bearbeite diese Datei auf dem Droplet und wende die Änderung mit folgendem Befehl an:

```bash
cd /opt/grampsweb && docker compose up -d
```
