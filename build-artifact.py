"""Erzeugt aus index.html die Artifact-Variante (ohne <!doctype>/<html>/<head>/<body>,
Bild als data-URI inline) fuer die Veroeffentlichung als Claude-Artifact."""
import base64, pathlib, sys

root = pathlib.Path(__file__).parent
src = (root / "index.html").read_text(encoding="utf-8")

# HTML-Geruest entfernen (das Artifact-Harness liefert charset/viewport/reset selbst)
src = src.replace('<!doctype html>\n<html lang="de">\n<head>\n', '')
for s in [
    '<meta charset="utf-8" />\n',
    '<meta name="viewport" content="width=device-width, initial-scale=1" />\n',
    '<meta name="robots" content="noindex, nofollow" />\n',
    '<meta name="referrer" content="no-referrer" />\n',
    '</head>\n', '<body>\n', '\n</body>\n</html>\n',
]:
    src = src.replace(s, '')

# lokale Assets als data-URI einbetten (Artifact-CSP erlaubt keine externen Bilder)
img = (root / "assets" / "hero.jpg").read_bytes()
data_uri = "data:image/jpeg;base64," + base64.b64encode(img).decode("ascii")
src = src.replace('src="assets/hero.jpg"', 'src="' + data_uri + '"')

out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else (root / "artifact.html")
out.write_text(src, encoding="utf-8")
print("geschrieben:", out, f"({len(src)} Zeichen)")
