class KPIs:  # I'm a lazy bum, used GPT for this, cause no Brian for searching possible KPIs, but it could help.
    def __init__(self, strukturbilanz):
        self.strukturbilanz = strukturbilanz
    
    def eigenkapitalquote(self):
        eigenkapital = self.strukturbilanz.passiva["Langfristiges Kapital"].get("Eigenkapital", 0) or 0
        gesamtkapital = sum((v or 0) for k, v in self.strukturbilanz.passiva.items())
        return eigenkapital / gesamtkapital if gesamtkapital else 0
    
    def verschuldungsgrad(self):
        fremdkapital = self.strukturbilanz.passiva["Langfristiges Kapital"].get("Langfristiges Fremdkapital", 0) or 0
        eigenkapital = self.strukturbilanz.passiva["Langfristiges Kapital"].get("Eigenkapital", 0) or 0
        return fremdkapital / eigenkapital if eigenkapital else 0
    
    def anlagendeckungsgrad(self):
        eigenkapital = self.strukturbilanz.passiva["Langfristiges Kapital"].get("Eigenkapital", 0) or 0
        langfristiges_fremdkapital = self.strukturbilanz.passiva["Langfristiges Kapital"].get("Langfristiges Fremdkapital", 0) or 0
        anlagevermoegen = self.strukturbilanz.aktiva["Langfristiges Vermögen"].get("Anlagevermögen", 0) or 0
        return (eigenkapital + langfristiges_fremdkapital) / anlagevermoegen if anlagevermoegen else 0
    
    def liquiditaetsgrad(self):
        umlaufvermoegen = self.strukturbilanz.aktiva["Kurzfristiges Vermögen"].get("Umlaufvermögen", 0) or 0
        kurzfristiges_fremdkapital = self.strukturbilanz.passiva["Kurzfristiges Kapital"].get("Kurzfristiges Fremdkapital", 0) or 0
        return umlaufvermoegen / kurzfristiges_fremdkapital if kurzfristiges_fremdkapital else 0
    
    def anzeigen(self):
        print("\n--- KPIs ---")
        print(f"Eigenkapitalquote: {self.eigenkapitalquote():.2%}")
        print(f"Verschuldungsgrad: {self.verschuldungsgrad():.2f}")
        print(f"Anlagendeckungsgrad: {self.anlagendeckungsgrad():.2%}")
        print(f"Liquiditätsgrad: {self.liquiditaetsgrad():.2%}")

if __name__ == "__main__":
   # kpi = KPIs(strukturbilanz)
   # kpi.anzeigen()