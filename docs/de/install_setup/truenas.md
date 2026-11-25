# TrueNAS-Einrichtung

Diese Anleitung erklärt, wie du Gramps Web unter TrueNAS Community Edition 25.04 einrichtest.

!!! warning
    Diese Anleitung ist für TrueNAS Community Edition 25.04 oder höher vorgesehen, das ein neues Docker-Compose-basiertes Apps-System eingeführt hat. Sie gilt nicht für frühere Versionen von TrueNAS.

## Voraussetzungen

- TrueNAS Community Edition 25.04 oder höher
- Grundlegende Vertrautheit mit der TrueNAS-Weboberfläche
- Ein Dataset zum Speichern der Gramps-Web-Daten

## Übersicht

TrueNAS Community Edition 25.04 hat ein neues Docker-Compose-basiertes Apps-System eingeführt, das den bisherigen Helm-Chart-basierten Ansatz ersetzt. Diese Anleitung führt dich durch die Erstellung einer benutzerdefinierten App für Gramps Web mit Docker Compose.

## Schritt 1: Speicher vorbereiten

1. Navigiere in der TrueNAS-Weboberfläche zu **Datasets**
2. Erstelle ein neues Dataset für Gramps Web (z. B. `grampsweb`). Notiere den vollständigen Pfad zu diesem Dataset, z. B. `/mnt/storage/grampsweb`, da du ihn später benötigen wirst.

Erstelle Unterverzeichnisse für die verschiedenen Komponenten:
- `users` – Benutzerdatenbank
- `database` – Gramps-Datenbankdatei(en)
- `media` – Mediendateien



## Schritt 2: Die Docker-Compose-App erstellen

1. Navigiere in der TrueNAS-Weboberfläche zu **Apps**
2. Klicke auf **Discover Apps**
3. Suche nach „Gramps Web“ und klicke darauf
4. Klicke auf „Installieren“

Dadurch gelangst du zur Konfigurationsseite der App.

## Schritt 3: Die App konfigurieren

### Gramps-Web-Konfiguration

- **Zeitzone:** Lege deine lokale Zeitzone fest (z. B. `Europe/Berlin`)
- **Redis-Passwort:** Lege ein Passwort für Redis fest. Dieses wird nur intern von der App verwendet.
- **Telemetrie deaktivieren:** Bitte lasse dieses Kästchen deaktiviert – siehe [hier für weitere Informationen](telemetry.md).
- **Geheimer Schlüssel:** Es ist entscheidend, dass du hier einen starken, eindeutigen Wert festlegst. Anweisungen zum Generieren eines zufälligen Schlüssels findest du unter [Serverkonfiguration](configuration.md#existing-configuration-settings).
- **Zusätzliche Umgebungsvariablen:** Du musst alle zusätzlichen [Konfigurationsoptionen](configuration.md) als Umgebungsvariablen festlegen, denen `GRAMPSWEB_` vorangestellt wird. Lies die [Konfigurationsdokumentation](configuration.md) sorgfältig durch – insbesondere ist zu beachten, dass boolesche Werte bei Umgebungsvariablen als `true` oder `false` (alles kleingeschrieben) festgelegt werden müssen. Dies ist eine häufige Fehlerquelle.

Lege **mindestens** `GRAMPSWEB_BASE_URL` auf die URL fest, unter der deine Gramps-Web-Instanz erreichbar sein wird – dies ist für den ordnungsgemäßen Betrieb erforderlich.

Du kannst in diesem Schritt auch die E-Mail-Konfiguration einrichten, die beispielsweise für das Zurücksetzen von Passwörtern benötigt wird. Die relevanten Umgebungsvariablen sind:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Alle Konfigurationseinstellungen können später geändert werden, indem du in der TrueNAS-Apps-Oberfläche auf „Bearbeiten“ klickst.


### Speicherkonfiguration

- **Benutzerspeicher:** Wähle den Pfad zu dem zuvor erstellten Verzeichnis `users` aus.
- **Indexspeicher:** Du kannst die Standardeinstellung „ixVolume (Dataset created automatically by the system)“ beibehalten.
- **Speicher für den Vorschaubild-Cache:** Du kannst die Standardeinstellung „ixVolume (Dataset created automatically by the system)“ beibehalten.
- **Cache-Speicher:** Du kannst die Standardeinstellung „ixVolume (Dataset created automatically by the system)“ beibehalten.
- **Medienspeicher:** Wähle den Pfad zu dem zuvor erstellten Verzeichnis `media` aus.
- **Gramps-Datenbankspeicher:** Wähle den Pfad zu dem zuvor erstellten Verzeichnis `database` aus.

### Ressourcenkonfiguration

Wir empfehlen, mindestens 2 CPUs und 4096 MB RAM zuzuweisen, um einen reibungslosen Betrieb sicherzustellen.


## Schritt 4: Auf Gramps Web zugreifen

Sobald die App bereitgestellt wurde, kannst du auf Gramps Web zugreifen, indem du in der TrueNAS-Apps-Oberfläche auf die Schaltfläche „Web UI“ klickst. Du solltest den Einrichtungsassistenten „Welcome to Gramps Web“ sehen.

Wenn du Benutzern den Zugriff auf deine Gramps-Web-Oberfläche ermöglichen möchtest, **darfst du die App nicht direkt dem Internet aussetzen**, sondern fahre mit dem nächsten Schritt fort.


## Schritt 5: Einen Reverse Proxy einrichten

Um deine Gramps-Web-Instanz sicher für Benutzer zugänglich zu machen, wird empfohlen, einen Reverse Proxy einzurichten. Damit kannst du SSL/TLS-Zertifikate verwalten und den Zugriff kontrollieren.

Am einfachsten ist es, die offizielle TrueNAS-App Nginx Proxy Manager zu verwenden. Suche in der TrueNAS-Apps-Oberfläche nach der App und installiere sie. Du kannst alle Einstellungen auf ihren Standardwerten belassen, aber wir empfehlen, eine zusätzliche Umgebungsvariable festzulegen: `DISABLE_IPV6` mit dem Wert `true`, um mögliche Probleme im Zusammenhang mit IPv6 zu vermeiden.

Öffne nach der Bereitstellung die Weboberfläche von Nginx Proxy Manager und erstelle einen neuen Proxy-Host mit den folgenden Einstellungen:

- Schema: `http`
- Weiterleitungs-Hostname / IP: der Hostname deines TrueNAS-Servers (z. B. `truenas`)
- Weiterleitungsport: der deiner Gramps-Web-App zugewiesene Port (sieh in der TrueNAS-Apps-Oberfläche nach, um den genauen Port zu ermitteln)
- Aktiviere im Tab „SSL“ die Option „SSL erzwingen“
- Wähle unter „SSL-Zertifikate“ die Option „SSL-Zertifikat hinzufügen“ > „Let's Encrypt“ aus, um ein neues Let's-Encrypt-Zertifikat für deine Domain zu erstellen.

Weitere Informationen zur Konfiguration deines Routers und zum Abrufen von SSL-Zertifikaten findest du in der [Dokumentation von Nginx Proxy Manager](https://nginxproxymanager.com/guide/).
