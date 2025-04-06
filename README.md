# Steinweg-Portfolios
Tim Schacht, Daniel Bonath, Quirin Barth

<iframe width="560" height="315" src="https://www.youtube.com/embed/inkn4Th2x5E?si=XbmOyCI8xN9ohWt6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## REQUIREMENTS

- Python 3.10 or above
- pypdf (install via `pip install pypdf`)


## Funktion

[`main.py`](main.py) gibt bei Ausführung die Strukturbilanz und mehrere Kennzahlen für zwei verschiedene **Gastro-Unternehmen** aus.


*Disclaimer: Der code ist auf Gastrounternehmen angepasst, und funktioniert mit anderen Bilanzen möglicherweise nicht ganz richtig.*

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
PDFs einlesen, hat fast auf anhieb gut funktioniert, und auch das Parsen vom Text lief gut nachdem wir uns konsequent auf eine Bilanzstruktur spezialisiert haben, anstatt zu versuchen alle möglichen Formatierungen einlesen zu können. Berechnen der Kennzahlen und hinzufügen einer "Ampel" bei den Kennzahlen, waren einfache Übungen.


### Was hat Probleme bereitet
Anfangs wollten wir mit OCR Arbeiten, jedoch ergaben sich dadurch viele kleine Schriebfehler, welche wiederrum das Parsing beinahe unmöglich gemacht haben. Nach viel rumprobieren mit höheren Bildauflösungen und anderem, haben wir uns irgendwann zu direkter PDF auslese entschieden, das die vorherigen Bilder für das OCR sowieso schon aus PDFs entnommen wurden. Durch das direkte Auslesen vom text selbst wurden damit lese-fehler durch OCR komplett umgangen.

Vor allem die Formatierung der Bilanzen in den verschiedenen verwendeten berichten, hat sich von Brache zu Branche stark verändert. Das hat dafür gesorgt dass das parsen vom Text viele Sonderfälle abfangen musste, und dadurch schnell unübersichtlich wurde. Zudem hat es nicht lange gedauert bis besagte besonderheiten einer Bilanz, und die dazugehörigen Parsingmethoden, den Methoden für eine andere Bilanz direkt wiedersprochen haben.\
Deshalb haben wir entschieden, uns nur auf Gastrounternehmen zu spezifizieren, das die Bilanzen in diesen oft einem einfacher einlesbaren Schema folgen.


### Potentielle Verbesserungen
- Möglichkeit zur betrachtung eines Unternehmens über einen Zeitraum, durch einlesen mehrerer Zeitlich aufeinander abfolgenden Bilanzen
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
