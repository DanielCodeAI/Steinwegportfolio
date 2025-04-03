import Bilanzklassen

def eigenkapitalquote(strk_bilanz: Bilanzklassen.Strukturbilant) -> float:
    try:
        return (strk_bilanz.passiva["Eigenkapital"] / strk_bilanz.gesamtkapital) * 100
    except:
        return 0.0


def fremdkapitalquote(strk_bilanz: Bilanzklassen.Strukturbilant) -> float:
    try:
        return ((strk_bilanz.passiva["kurzfristiges Fremdkapital"] + strk_bilanz.passiva["langfristiges Fremdkapital"]) / strk_bilanz.gesamtkapital) * 100
    except:
        return 0.0


def verschuldungsgrad(strk_bilanz: Bilanzklassen.Strukturbilant) -> float:
    try:
        return ((strk_bilanz.passiva["kurzfristiges Fremdkapital"] + strk_bilanz.passiva["langfristiges Fremdkapital"]) / strk_bilanz.passiva["Eigenkapital"]) * 100
    except:
        return 0.0


def umlaufquote(strk_bilanz: Bilanzklassen.Strukturbilant) -> float:
    try:
        return (strk_bilanz.aktiva["kurzfristig gebundenes Vermögen"] / strk_bilanz.gesamtkapital) * 100
    except:
        return 0.0
    

def anlagenintensität(strk_bilanz: Bilanzklassen.Strukturbilant) -> float:
    try:
        return (strk_bilanz.aktiva["langfristig gebundenes Vermögen"] / strk_bilanz.gesamtkapital) * 100
    except:
        return 0.0


def anlagendeckung(strk_bilanz: Bilanzklassen.Strukturbilant) -> float:
    try:
        return ((strk_bilanz.passiva["Eigenkapital"] + strk_bilanz.passiva["langfristiges Fremdkapital"]) / strk_bilanz.aktiva["langfristig gebundenes Vermögen"]) * 100
    except:
        return 0.0


def liquiditätsgrad_3(strk_bilanz: Bilanzklassen.Strukturbilant) -> float:
    try:
        return (strk_bilanz.aktiva["kurzfristig gebundenes Vermögen"] / strk_bilanz.passiva["kurzfristiges Fremdkapital"]) * 100
    except:
        return 0.0


def nettoumlaufvermögen(strk_bilanz: Bilanzklassen.Strukturbilant) -> float:
    return strk_bilanz.aktiva["kurzfristig gebundenes Vermögen"] - strk_bilanz.passiva["kurzfristiges Fremdkapital"]
