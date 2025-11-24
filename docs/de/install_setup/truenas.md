# TrueNAS Einrichtung

Diese Anleitung erklärt, wie man Gramps Web auf TrueNAS Community Edition 25.04 einrichtet.

!!! warning
    Diese Anleitung ist für TrueNAS Community Edition 25.04 oder später gedacht, die ein neues auf Docker Compose basierendes App-System eingeführt hat. Sie gilt nicht für frühere Versionen von TrueNAS.

## Voraussetzungen

- TrueNAS Community Edition 25.04 oder später
- Grundkenntnisse der TrueNAS-Weboberfläche
- Ein Dataset zur Speicherung der Gramps Web-Daten

## Übersicht

TrueNAS Community Edition 25.04 führte ein neues auf Docker Compose basierendes App-System ein, das den vorherigen auf Helm-Chart basierenden Ansatz ersetzt. Diese Anleitung führt Sie durch die Erstellung einer benutzerdefinierten App für Gramps Web mit Docker Compose.

## Schritt 1: Speicher vorbereiten

1. Navigieren Sie zu **Datasets** in der TrueNAS-Weboberfläche
2. Erstellen Sie ein neues Dataset für Gramps Web (z. B. `grampsweb`). Notieren Sie den vollständigen Pfad zu diesem Dataset, z. B. `/mnt/storage/grampsweb`, da Sie ihn später benötigen.

Erstellen Sie Unterverzeichnisse für die verschiedenen Komponenten:
- `users` - Benutzerdatenbank
- `database` - Gramps-Datenbankdatei(en)
- `media` - Mediendateien

## Schritt 2: Die Docker Compose App erstellen

1. Navigieren Sie zu **Apps** in der TrueNAS-Weboberfläche
2. Klicken Sie auf **Discover Apps**
3. Suchen Sie nach "Gramps Web" und klicken Sie darauf
4. Klicken Sie auf "Installieren"

Dies bringt Sie zur Konfigurationsseite der App.

## Schritt 3: Die App konfigurieren

### Gramps Web-Konfiguration

- **Zeitzone:** Stellen Sie Ihre lokale Zeitzone ein (z. B. `Europe/Berlin`)
- **Redis-Passwort:** Legen Sie ein Passwort für Redis fest. Dies wird nur intern von der App verwendet.
- **Telemetrie deaktivieren:** Bitte lassen Sie dieses Kästchen ungeprüft – siehe [hier für Details](telemetry.md).
- **Geheimer Schlüssel:** Es ist entscheidend, dass Sie dies auf einen starken, einzigartigen Wert setzen. Siehe [Serverkonfiguration](configuration.md#existing-configuration-settings) für Anweisungen, wie man einen zufälligen Schlüssel generiert.
- **Zusätzliche Umgebungsvariablen:** Sie müssen alle zusätzlichen [Konfigurationsoptionen](configuration.md) als Umgebungsvariablen mit dem Präfix `GRAMPSWEB_` festlegen. Bitte überprüfen Sie die [Konfigurationsdokumentation](configuration.md) im Detail – zum Beispiel, dass boolesche Werte als `true` oder `false` (alles klein geschrieben) im Fall von Umgebungsvariablen gesetzt werden müssen, ein häufiger Fallstrick.

Bitte setzen Sie **mindestens** die `GRAMPSWEB_BASE_URL` auf die URL, unter der Ihre Gramps Web-Instanz erreichbar sein wird – dies ist für den ordnungsgemäßen Betrieb erforderlich.

Sie möchten möglicherweise auch die E-Mail-Konfiguration zu diesem Zeitpunkt einrichten. Wenn Sie dies tun, können Sie den Schritt zur E-Mail-Konfiguration im Onboarding-Assistenten überspringen. Die relevanten Umgebungsvariablen sind:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Alle Konfigurationseinstellungen können später durch Klicken auf "Bearbeiten" in der TrueNAS Apps-Oberfläche geändert werden.

### Speicher-Konfiguration

- **Benutzerspeicher:** Wählen Sie den Pfad zum `users`-Verzeichnis, das Sie zuvor erstellt haben.
- **Indexspeicher:** Sie können die Standardeinstellung "ixVolume (Dataset wurde automatisch vom System erstellt)" belassen.
- **Thumbnail-Cache-Speicher:** Sie können die Standardeinstellung "ixVolume (Dataset wurde automatisch vom System erstellt)" belassen.
- **Cache-Speicher:** Sie können die Standardeinstellung "ixVolume (Dataset wurde automatisch vom System erstellt)" belassen.
- **Medien-Speicher:** Wählen Sie den Pfad zum `media`-Verzeichnis, das Sie zuvor erstellt haben.
- **Gramps-Datenbankspeicher:** Wählen Sie den Pfad zum `database`-Verzeichnis, das Sie zuvor erstellt haben.

### Ressourcen-Konfiguration

Wir empfehlen, mindestens 2 CPUs und 4096 MB RAM zuzuweisen, um einen reibungslosen Betrieb sicherzustellen.

## Schritt 4: Gramps Web aufrufen

Sobald die App bereitgestellt ist, können Sie Gramps Web aufrufen, indem Sie auf die Schaltfläche "Web UI" in der TrueNAS Apps-Oberfläche klicken. Sie sollten den Onboarding-Assistenten "Willkommen bei Gramps Web" sehen.

Wenn Sie Benutzern den Zugriff auf Ihre Gramps Web-Oberfläche ermöglichen möchten, **stellen Sie** die App nicht direkt ins Internet, sondern fahren Sie mit dem nächsten Schritt fort.

## Schritt 5: Einen Reverse-Proxy einrichten

Um Ihre Gramps Web-Instanz sicher für Benutzer zugänglich zu machen, wird empfohlen, einen Reverse-Proxy einzurichten. Dies ermöglicht es Ihnen, SSL/TLS-Zertifikate zu verwalten und den Zugriff zu steuern.

Die einfachste Option ist die Verwendung der offiziellen TrueNAS Nginx Proxy Manager-App. Suchen Sie die App in der TrueNAS Apps-Oberfläche und installieren Sie sie. Sie können alle Einstellungen auf ihren Standardwerten belassen, aber wir empfehlen, eine zusätzliche Umgebungsvariable festzulegen: `DISABLE_IPV6` mit dem Wert `true`, um potenzielle IPv6-bezogene Probleme zu vermeiden.

Sobald die App bereitgestellt ist, öffnen Sie die Weboberfläche des Nginx Proxy Managers und erstellen Sie einen neuen Proxy-Host mit den folgenden Einstellungen:

- Scheme: `http`
- Forward Hostname / IP: der Hostname Ihres TrueNAS-Servers (z. B. `truenas`)
- Forward Port: der Port, der Ihrer Gramps Web-App zugewiesen ist (überprüfen Sie die TrueNAS Apps-Oberfläche für den genauen Port)
- Im Tab "SSL" aktivieren Sie "Force SSL"
- Unter "SSL-Zertifikate" wählen Sie "SSL-Zertifikat hinzufügen" > "Let's Encrypt", um ein neues Let's Encrypt-Zertifikat für Ihre Domain zu erstellen.

Bitte beachten Sie die [Nginx Proxy Manager-Dokumentation](https://nginxproxymanager.com/guide/) für weitere Details zur Konfiguration Ihres Routers und zum Erhalt von SSL-Zertifikaten.
