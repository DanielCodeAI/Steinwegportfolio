import Bilanzklassen

def eigenkapitalquote(strk_bilanz: Bilanzklassen.Strukturbilanz) -> float:
    try:
        return (strk_bilanz.passiva["Eigenkapital"] / strk_bilanz.gesamtkapital) * 100
    except:
        return 0.0


def fremdkapitalquote(strk_bilanz: Bilanzklassen.Strukturbilanz) -> float:
    try:
        return ((strk_bilanz.passiva["kurzfristiges Fremdkapital"] + strk_bilanz.passiva["langfristiges Fremdkapital"]) / strk_bilanz.gesamtkapital) * 100
    except:
        return 0.0


def verschuldungsgrad(strk_bilanz: Bilanzklassen.Strukturbilanz) -> float:
    try:
        return ((strk_bilanz.passiva["kurzfristiges Fremdkapital"] + strk_bilanz.passiva["langfristiges Fremdkapital"]) / strk_bilanz.passiva["Eigenkapital"]) * 100
    except:
        return 0.0


def umlaufquote(strk_bilanz: Bilanzklassen.Strukturbilanz) -> float:
    try:
        return (strk_bilanz.aktiva["kurzfristig gebundenes Vermögen"] / strk_bilanz.gesamtkapital) * 100
    except:
        return 0.0
    

def anlagenintensität(strk_bilanz: Bilanzklassen.Strukturbilanz) -> float:
    try:
        return (strk_bilanz.aktiva["langfristig gebundenes Vermögen"] / strk_bilanz.gesamtkapital) * 100
    except:
        return 0.0


def anlagendeckung(strk_bilanz: Bilanzklassen.Strukturbilanz) -> float:
    try:
        return ((strk_bilanz.passiva["Eigenkapital"] + strk_bilanz.passiva["langfristiges Fremdkapital"]) / strk_bilanz.aktiva["langfristig gebundenes Vermögen"]) * 100
    except:
        return 0.0


def liquiditätsgrad_3(strk_bilanz: Bilanzklassen.Strukturbilanz) -> float:
    try:
        return (strk_bilanz.aktiva["kurzfristig gebundenes Vermögen"] / strk_bilanz.passiva["kurzfristiges Fremdkapital"]) * 100
    except:
        return 0.0


def nettoumlaufvermögen(strk_bilanz: Bilanzklassen.Strukturbilanz) -> float:
    return strk_bilanz.aktiva["kurzfristig gebundenes Vermögen"] - strk_bilanz.passiva["kurzfristiges Fremdkapital"]


def alle_kennzahlen_auf_einmal(strk_bilanz: Bilanzklassen.Strukturbilanz):
    kennzahlen = {
        "Eigenkapitalquote": eigenkapitalquote(strk_bilanz),
        "Fremdkapitalquote": fremdkapitalquote(strk_bilanz),
        "Verschuldungsgrad": verschuldungsgrad(strk_bilanz),
        "Umlaufquote": umlaufquote(strk_bilanz),
        "Anlagenintensität": anlagenintensität(strk_bilanz),
        "Anlagendeckung": anlagendeckung(strk_bilanz),
        "Liquiditätsgrad 3": liquiditätsgrad_3(strk_bilanz),
        "Nettoumlaufvermögen": nettoumlaufvermögen(strk_bilanz)
    }

    ampel = {
        "Eigenkapitalquote": "grün" if kennzahlen["Eigenkapitalquote"] > 25 else "rot", # 30 gilt als solide, aber Gastro kann schwanken, deshalb 25
        "Fremdkapitalquote": "grün" if kennzahlen["Fremdkapitalquote"] < 50 else "rot", # 50 also Solide, aber kurzzeitig höher möglich
        "Verschuldungsgrad": "grün" if kennzahlen["Verschuldungsgrad"] < 185 else "rot", # Sollte unter 200 liegen
        "Umlaufquote": "grün" if kennzahlen["Umlaufquote"] > 60 else "rot", # 50 zählt als gut, aber Gastro hat durch Lebensmittel und Lagerbestände oft mehr Umlaufvermögen        "Anlagenintensität": "grün" if kennzahlen["Anlagenintensität"] > 50 else "rot", # 
        "Anlagenintensität": "grün" if kennzahlen["Anlagenintensität"] < 55 else "rot", # Zwischen 40 und 70, also ist 55 die Mitter
        "Anlagendeckung": "grün" if kennzahlen["Anlagendeckung"] > 100 else "rot", # Mehr als 100, um langzeitige Kosten zu decken
        "Liquiditätsgrad 3": "grün" if kennzahlen["Liquiditätsgrad 3"] > 110 else "rot", # 120 gilt also optimal
        "Nettoumlaufvermögen": "grün" if kennzahlen["Nettoumlaufvermögen"] > 0 else "rot" # Es sollte immer etwas geld zur hand sein
    }

    ampel = {}
    for key, value in kennzahlen.items():
        match key:
            case "Eigenkapitalquote":
                if value > 25:
                    ampel[key] = "grün"
                elif 20 <= value <= 25:
                    ampel[key] = "gelb"
                else:
                    ampel[key] = "rot"

            case "Fremdkapitalquote":
                if value < 50:
                    ampel[key] = "grün"
                elif 50 <= value <= 60:
                    ampel[key] = "gelb"
                else:
                    ampel[key] = "rot"

            case "Verschuldungsgrad":
                if value < 200:
                    ampel[key] = "grün"
                elif 200 <= value <= 225:
                    ampel[key] = "gelb"
                else:
                    ampel[key] = "rot"

            case "Umlaufquote":
                if value > 60:
                    ampel[key] = "grün"
                elif 50 <= value <= 60:
                    ampel[key] = "gelb"
                else:
                    ampel[key] = "rot"

            case "Anlagenintensität":
                if 40 <= value <= 70:
                    ampel[key] = "grün"
                elif (35 < value < 40) or (70 < value <= 75):
                    ampel[key] = "gelb"
                else:
                    ampel[key] = "rot"

            case "Anlagendeckung":
                if value > 100:
                    ampel[key] = "grün"
                elif 90 <= value <= 100:
                    ampel[key] = "gelb"
                else:
                    ampel[key] = "rot"

            case "Liquiditätsgrad 3":
                if value > 110:
                    ampel[key] = "grün"
                elif 100 <= value <= 110:
                    ampel[key] = "gelb"
                else:
                    ampel[key] = "rot"

            case "Nettoumlaufvermögen":
                if value > 0:
                    ampel[key] = "grün"
                else:
                    ampel[key] = "rot"

    for key, value in kennzahlen.items():
        print(f"{key.rjust(20)}: {value:.3f} - {ampel[key]}")
