# Verwenden Sie den integrierten Blog

Der Blog dient dazu, Geschichten über Ihre Familienforschung zu präsentieren.

In der Gramps-Datenbank werden Blogbeiträge als Quellen mit einer angehängten Notiz dargestellt, die den Text des Blogs enthält und optional Mediendateien für die Bilder des Blogbeitrags. Gramps Web behandelt jede Quelle mit dem Etikett `Blog` als Blogartikel.

## Fügen Sie einen Blogbeitrag hinzu

Der schnellste Weg, einen Beitrag zu schreiben, ist das spezielle **Neuer Blogbeitrag**-Formular in Gramps Web. Öffnen Sie es entweder über die blaue **+**-Schaltfläche auf der Blog-Seite oder über das **Hinzufügen**-Menü (Plus-Symbol) in der oberen App-Leiste, indem Sie **Blogbeitrag** auswählen.

Das Formular hat Felder für:

- **Titel** – der Titel des Beitrags (erforderlich)
- **Autor** – wer ihn geschrieben hat
- **Inhalt** – einen Rich-Text-Editor für den Beitrag selbst
- **Medien** – ein oder mehrere Medienobjekte. Das erste wird als Vorschaubild über dem Text angezeigt; alle erscheinen als Galerie darunter.
- **Etiketten** und einen **privat**-Schalter, wie bei jedem anderen Objekt

Das Speichern des Formulars erstellt für Sie die zugrunde liegende Quelle, Notiz und das Etikett `Blog`, wie [unten](#relation-between-blog-and-sources) beschrieben.

### Hinzufügen eines Beitrags manuell

Sie können auch einen Beitrag erstellen, indem Sie die zugrunde liegenden Objekte selbst erstellen. Dies ist der einzige Weg, es in Gramps Desktop zu tun ([synchronisiert](../administration/sync.md) mit Gramps Web), und die Schritte sind in beiden Anwendungen gleich:

- Fügen Sie eine neue Quelle hinzu. Der Titel der Quelle wird der Titel Ihres Blogbeitrags sein, der Autor der Quelle wird der Autor des Beitrags sein.
- Optional: Verknüpfen Sie die Quelle mit einem Repository, das Ihrem Gramps Web-Blog entspricht.
- Fügen Sie der Quelle eine neue Notiz hinzu. Schreiben Sie Ihren Blogbeitrag und kopieren Sie den Text in die Notiz.
- Optional: Fügen Sie ein oder mehrere Mediendateien zu Ihrer Quelle hinzu. Die erste Mediendatei wird als Vorschaubild des Beitrags über dem Text verwendet. Alle Mediendateien werden unter dem Text als Galerie angezeigt.
- Fügen Sie der Quelle das Etikett `Blog` hinzu (erstellen Sie es, wenn es nicht existiert).

## Beziehung zwischen Blog und Quellen

Da Blogbeiträge nur Quellen sind, erscheinen alle Blogartikel auch in der Liste der Quellen und werden in Suchanfragen als Quellen angezeigt. Im Quellansichtsfenster gibt es eine Schaltfläche "im Blog anzeigen", die Sie zur Blogansicht für diesen Blogbeitrag führt. Die URL des Blogbeitrags enthält auch die Gramps-ID der entsprechenden Quelle, sodass ein Artikel unter `yourdomain.com/blog/S0123` der Quelle unter `yourdomain.com/source/S0123` entspricht.

Am Ende jedes Blogbeitrags gibt es eine Schaltfläche "Details", die Sie zur Quellansicht führt.
