# Verwende den integrierten Blog

Der Blog dient dazu, Geschichten über deine Familienforschung zu präsentieren.

In der Gramps-Datenbank werden Blogbeiträge als Quellen mit einer angehängten Notiz dargestellt, die den Text des Blogs enthält, sowie optional mit Mediendateien für die Bilder des Blogbeitrags. Gramps Web behandelt jede Quelle mit dem Etikett `Blog` als Blogartikel.

## Einen Blogbeitrag hinzufügen

Am schnellsten verfasst du einen Beitrag über das spezielle Formular **Neuer Blogbeitrag** in Gramps Web. Öffne es entweder über die blaue Schaltfläche **+** auf der Blogseite oder über das Menü **Hinzufügen** (Plus-Symbol) in der oberen App-Leiste, indem du **Blogbeitrag** auswählst.

Das Formular enthält folgende Felder:

- **Titel** – der Titel des Beitrags (erforderlich)
- **Autor** – wer ihn verfasst hat
- **Inhalt** – ein Rich-Text-Editor für den Beitrag selbst
- **Medien** – ein oder mehrere Medienobjekte. Das erste wird zum Vorschaubild, das über dem Text angezeigt wird; alle werden darunter als Galerie angezeigt.
- **Etiketten** und ein Schalter für **privat**, wie bei jedem anderen Objekt

Beim Speichern des Formulars werden die zugrunde liegende Quelle, Notiz und das Etikett `Blog` für dich erstellt, wie [weiter unten](#relation-between-blog-and-sources) beschrieben.

### Einen Beitrag manuell hinzufügen

Du kannst einen Beitrag auch erstellen, indem du die zugrunde liegenden Objekte selbst anlegst. Dies ist die einzige Möglichkeit, dies in Gramps Desktop zu tun ([synchronisiert](../administration/sync.md) mit Gramps Web), und die Schritte sind in beiden Anwendungen gleich:

- Füge eine neue Quelle hinzu. Der Titel der Quelle wird zum Titel deines Blogbeitrags, der Autor der Quelle zum Autor des Beitrags.
- Verknüpfe die Quelle optional mit einem Archiv, das deinem Gramps-Web-Blog entspricht.
- Füge der Quelle eine neue Notiz hinzu. Verfasse deinen Blogbeitrag und kopiere den Text in die Notiz.
- Füge deiner Quelle optional eine oder mehrere Mediendateien hinzu. Die erste Mediendatei wird als Vorschaubild des Beitrags verwendet und über dem Text angezeigt. Alle Mediendateien werden unter dem Text als Galerie angezeigt.
- Füge der Quelle das Etikett `Blog` hinzu (erstelle es, falls es nicht vorhanden ist).

## Beziehung zwischen Blog und Quellen

Da Blogbeiträge einfach Quellen sind, erscheinen alle Blogartikel auch in der Quellenliste und werden bei Suchen als Quellen angezeigt. In der Quellenansicht gibt es eine Schaltfläche „im Blog anzeigen“, über die du zur Blogansicht dieses Blogbeitrags gelangst. Die URL des Blogbeitrags enthält ebenfalls die Gramps-ID der entsprechenden Quelle. Ein Artikel unter `yourdomain.com/blog/S0123` entspricht daher der Quelle unter `yourdomain.com/source/S0123`.

Am Ende jedes Blogbeitrags gibt es eine Schaltfläche „Details“, über die du zur Quellenansicht gelangst.
