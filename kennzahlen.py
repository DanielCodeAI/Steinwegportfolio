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

    for key, value in kennzahlen.items():
        print(f"{key}: {value:.3f}")
