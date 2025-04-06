# Steinweg-Portfolios
Tim Schacht, Daniel Bonath, Quirin Barth

[Hier ist das Erklär-Video: https://youtu.be/inkn4Th2x5E](https://youtu.be/inkn4Th2x5E)

## REQUIREMENTS

- Python 3.10 or above
- pypdf (install via `pip install pypdf`)


## Funktion

[`main.py`](main.py) gibt bei Ausführung die Strukturbilanz und mehrere Kennzahlen für zwei verschiedene **Gastro-Unternehmen** aus.


*Disclaimer: Der code ist auf Gastrounternehmen angepasst und funktioniert mit anderen Bilanzen möglicherweise nur eingeschränkt.*

### Automatisierungsgrad
Der Code ist so eingerichtet, dass letztenendes nur der Dateipfad des pdfs angegeben werden muss.

Vollautomatisch erkannt und ausgewertet wird:
- Die pdf Seiten welche die Bilanz enthalten
- Die Bilanz
- Die daraus entstehende Strukturbilanz
- Eigenkapitalquote
- Fremdkapitalquote
- Verschuldungsgrad
- Umlaufquote
- Anlagenintensität
- Anlagendeckung
- Liquiditätsgrad 3
- Nettoumlaufvermögen


### Was hat gut funktioniert
PDFs einlesen hat fast auf Anhieb gut funktioniert und auch das Parsen vom Text lief gut, nachdem wir uns konsequent auf eine Bilanzstruktur spezialisiert haben, anstatt zu versuchen, alle möglichen Formatierungen einlesen zu können. Berechnen der Kennzahlen und hinzufügen einer "Ampel" bei den Kennzahlen waren anschließend einfache Übungen.


### Was hat Probleme bereitet
Anfangs wollten wir mit OCR (Optical Character Recognition) arbeiten, jedoch ergaben sich dadurch viele kleine Schreibfehler, welche wiederum das Parsing beinahe unmöglich gemacht haben. Nach viel Rumprobieren mit höheren Bildauflösungen und anderem haben wir uns irgendwann zu direkter PDF-Auslese entschieden, da die vorherigen Bilder für das OCR sowieso schon aus PDFs entnommen wurden. Durch das direkte Auslesen vom Text selbst wurden damit Lese-Fehler durch OCR komplett umgangen.

Vor allem die Formatierung der Bilanzen in den verschiedenen verwendeten Berichten hat sich von Brache zu Branche stark verändert. Das hat dafür gesorgt, dass das Parsen vom Text viele Sonderfälle abfangen musste und dadurch schnell unübersichtlich wurde. Zudem hat es nicht lange gedauert, bis besagte Besonderheiten bei einer Bilanz und die dazugehörigen Parsingmethoden den Methoden für eine andere Bilanz direkt wiedersprochen haben.\
Deshalb haben wir entschieden, uns nur auf Gastrounternehmen zu spezifizieren, da die Bilanzen in diesem Sektor oft einem ähnlichen Schema folgen.


### Potentielle Verbesserungen
- Möglichkeit zur betrachtung eines Unternehmens über einen Zeitraum, durch das Einlesen mehrerer zeitlich aufeinander abfolgenden Bilanzen
- Eine Vergleichsfunktion, die nochmal direkter Werte nebeneinanderstellt
- Ein Dashboard, oder zumindest eine schönere graphische Darstellung der Daten


## The Fox!
```
        /\/\    _
       < o  \  /_|
        |  | \/ /
        |/\|<__/
```
*- Fox by Quirin*
