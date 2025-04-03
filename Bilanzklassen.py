class Bilanz:
    def __init__(self):  # GPT nach Inhalten gefragt, muss bestimmt noch angepasst werden
        self.aktiva = {
            "anlagevermögen": 0,
            "umlaufvermögen": 0,
            "c. rechnungsabgrenzungsposten": 0,
            "aktive latente steuern": 0,
            "unterschiedsbetrag": 0,
            "fehlbetrag": 0
        }
        
        self.passiva = {
            "a. eigenkapital": 0,
            "rückstellungen": 0,
            "verbindlichkeiten": 0,
            "d. rechnungsabgrenzungsposten": 0,
            "passive latente steuern": 0
        }
    

    def show(self):
        print("\n--- AKTIVA ---")
    
        for categorie, value in self.aktiva.items():
            print(f"{categorie}: {value} EUR")
        
        print("\n--- PASSIVA ---")
        for categorie, value in self.passiva.items():
            print(f"{categorie}: {value} EUR")


class Strukturbilanz:
    def __init__(self, bilanz:Bilanz=None):
        if bilanz is None:
            raise Exception("Alter du musst eine Bilanz übergeben!")
        
        self.aktiva = {
            "langfristig gebundenes Vermögen": bilanz.aktiva["anlagevermögen"],
            "kurzfristig gebundenes Vermögen": bilanz.aktiva["umlaufvermögen"] + bilanz.aktiva["c. rechnungsabgrenzungsposten"],
            "sonstige Aktiva": bilanz.aktiva["aktive latente steuern"] + bilanz.aktiva["unterschiedsbetrag"] + bilanz.aktiva["fehlbetrag"]
        }
        
        self.passiva = {
            "Eigenkapital": bilanz.passiva["a. eigenkapital"],
            "langfristiges Fremdkapital": bilanz.passiva["rückstellungen"] + bilanz.passiva["passive latente steuern"],
            "kurzfristiges Fremdkapital": bilanz.passiva["verbindlichkeiten"] + bilanz.passiva["d. rechnungsabgrenzungsposten"],
        }
    
        self.gesamtkapital = self.aktiva["langfristig gebundenes Vermögen"] + self.aktiva["kurzfristig gebundenes Vermögen"] + self.aktiva["sonstige Aktiva"]

    def show(self):
        print("\n--- STRUKTURBILANZ AKTIVA ---")
    
        for categorie, value in self.aktiva.items():
            print(f"{categorie}: {value} EUR")
        
        print("\n--- STRUKTURBILANZ PASSIVA ---")
        for categorie, value in self.passiva.items():
            print(f"{categorie}: {value} EUR")


if __name__ == "__main__":
    bilanz = Bilanz()
    bilanz.show()
    strukturbilanz = Strukturbilanz(bilanz=bilanz)
    strukturbilanz.show()
