class Bilanz:
    def __init__(self):  # GPT nach Inhalten gefragt, muss bestimmt noch angepasst werden
        self.aktiva = {
            "Anlagevermögen": 0,
            "Umlaufvermögen": 0,
            "C. Rechnungsabgrenzungsposten": 0,
        }
        
        self.passiva = {
            "Eigenkapital": 0,
            "Rückstellungen": 0,
            "Verbindlichkeiten": 0,
            "D. Rechnungsabgrenzungsposten": 0
        }
    
    def show(self):
        print("\n--- AKTIVA ---")
    
        for categorie, value in self.aktiva.items():
            print(f"{categorie}: {value} EUR")
        
        print("\n--- PASSIVA ---")
        for categorie, value in self.passiva.items():
            print(f"{categorie}: {value} EUR")


class Strukturbilanz:
    def __init__(self):
        self.aktiva = {
            "Langfristiges Vermögen": {
                "Anlagevermögen": None
            },
            "Kurzfristiges Vermögen": {
                "Umlaufvermögen": None
            }
        }
        
        self.passiva = {
            "Langfristiges Kapital": {
                "Eigenkapital": None,
                "Langfristiges Fremdkapital": None
            },
            "Kurzfristiges Kapital": {
                "Kurzfristiges Fremdkapital": None
            }
        }
    
    def show(self):
        print("\n--- STRUKTURBILANZ AKTIVA ---")
        for categorie, value in self.aktiva.items():
            print(f"{categorie}:")
            if isinstance(value, dict):
                for subcategory in value:
                    print(f"  - {subcategory}")
        
        print("\n--- STRUKTURBILANZ PASSIVA ---")
        for categorie, value in self.passiva.items():
            print(f"{categorie}:")
            if isinstance(value, dict):
                for subcategory in value:
                    print(f"  - {subcategory}")

if __name__ == "__main__":
    bilanz = Bilanz()
    bilanz.show()
    strukturbilanz = Strukturbilanz()
    strukturbilanz.show()
