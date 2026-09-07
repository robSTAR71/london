# London für Melanie

Reise-Begleiter für die Geschwisterreise nach London, **9.–12. Oktober 2026** –
anlässlich Melanies Charity-Halbmarathon (Royal Parks Half Marathon) am 11. Oktober,
im Gedenken an Mama.

Für: Robert, Heidi, Evelin und Steffi.

## Inhalt

Eine einzelne statische Seite (`index.html`, kein Build, keine Abhängigkeiten):

- Countdown bis Abflug und bis Melanies Start
- Flüge (Ryanair), Unterkunft und privater Flughafentransfer
- Tagesplan Freitag bis Montag
- Melanies Lauf: Eckdaten, schematische Strecke, Anfeuer-Plan
- Checkliste mit Fortschrittsbalken
- Notizfelder für Transfer, Treffpunkt und Startnummer

Checkliste und Notizen werden nur lokal im jeweiligen Browser gespeichert
(`localStorage`) – es gibt keinen Server und keine geteilten Daten.

## Veröffentlichen (GitHub Pages)

1. Repository auf GitHub anlegen und diese Dateien pushen.
2. **Settings → Pages → Build and deployment**: Source „Deploy from a branch",
   Branch `main`, Ordner `/ (root)`, speichern.
3. Nach ein bis zwei Minuten ist die Seite unter
   `https://<benutzername>.github.io/<repo>/` erreichbar.

Die Seite trägt `noindex` und eine `robots.txt`, damit Suchmaschinen sie nicht
aufnehmen. Der Link ist trotzdem für alle erreichbar, die ihn kennen –
also nur an die Geschwister weitergeben.

## Anpassen

Alle Inhalte stehen direkt in `index.html`. Häufige Änderungen:

- **Checklisten-Punkte**: Array `groups` im `<script>`-Block.
- **Countdown-Ziele**: `departure` und `raceStart` im `<script>`-Block.
- **Startnummer / Tracking-Link**: direkt im Abschnitt „Melanies Lauf" eintragen
  oder das Notizfeld nutzen.
