import pypdf
import re  # Kakyoin can't comprehent stopped time - if you dont get it, dont sweat it
import Bilanzklassen # don't forget the class file :3

# this was fun, so I did it myself, no cheating this time (stack overflow is fair game) :O
class Bilanz_OCR:
    def __init__(self, pdf_path:str, pdf_pages:tuple):
        self.pdf_path = pdf_path
        self.pdf_pages = pdf_pages
        self.bilanz = Bilanzklassen.Bilanz()
    
    def extract_text(self):
        reader = pypdf.PdfReader(self.pdf_path)

        page_texts = []

        for page_num in self.pdf_pages:
            page_texts.append(reader.pages[page_num].extract_text())

        return "\n".join(page_texts)
    
    def get_clean_number(self, x: str)->float:
        xclean = x.replace(".", "")
        xclean = xclean.replace(",", "")
        x_floatable = xclean[:-2] + "." + xclean[-2:]
        return float(x_floatable)
        
    def parse_text(self, text):
        active_category= ''
        for line in text.split("\n"):
            scan_category = re.findall(r"Anlagevermögen|Umlaufvermögen|Eigenkapital|Rückstellungen|Verbindlichkeiten|C. Rechnungsabgrenzungsposten|D. Rechnungsabgrenzungsposten", line)
            if scan_category:
                active_category = scan_category[0]
            
            skip_line = False
            # Hiermit ignorieren wir Summenzeilen, welche keinen MEHRWERT haben
            if (not any(char.isalpha() for char in line)) or ("EUR" in line):
                skip_line = True

            scan_money = re.findall(r"\s+(\d*[.,]*\d*[.,]*\d*[.,]*\d*[.,]*\d*[.,]*\d*[.,]*\d+[,]\d+)", line)

            print(f"In line: {line}\nWe have category: {active_category}\nMoney found: {scan_money}\nLine skipped: {skip_line}\n===============================")

            if skip_line:
                if active_category == "D. Rechnungsabgrenzungsposten":
                    break # Diese Abfrage checkt of das das Ende der Bilanz ist
                continue

            if scan_money:
                if active_category in ["Anlagevermögen", "Umlaufvermögen", "C. Rechnungsabgrenzungsposten"]: # Aktiva go in the Aktiva UwU
                    self.bilanz.aktiva[active_category] += self.get_clean_number(scan_money[0])
                else:
                    self.bilanz.passiva[active_category] += self.get_clean_number(scan_money[0])
                continue
             
    def computer_use_reading_comprehention(self):
        text = self.extract_text()
        print(text)  # for testing
        self.parse_text(text)
        self.bilanz.show()


if __name__ == "__main__":
    ocr = Bilanz_OCR("Suchergebnis-Bundesanzeiger04.pdf", pdf_pages=(2,)) # THIS IS THE FILEPATH TO ADJUST
    ocr.computer_use_reading_comprehention()
