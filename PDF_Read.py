import pypdf
import re  # Kakyoin can't comprehent stopped time - if you dont get it, dont sweat it
import Bilanzklassen # don't forget the class file :3

# this was fun, so I did it myself, no cheating this time (stack overflow is fair game) :O
class Bilanz_PDF:
    def __init__(self, pdf_path:str, pdf_pages:tuple=None):
        self.pdf_path = pdf_path

        if pdf_pages == None:
            self.pdf_pages = self.find_relevant_pages()
        else:
            self.pdf_pages = pdf_pages

        self.bilanz = Bilanzklassen.Bilanz()
    
    def find_relevant_pages(self):
        reader = pypdf.PdfReader(self.pdf_path)

        pages = []

        for page_num in range(reader.get_num_pages()):
            if "bilanz" in reader.pages[page_num].extract_text().lower():
                pages.append(page_num)

        return tuple(pages)
    
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
        
    def parse_text(self, text, verbose=True):
        bilanz_header = r"anlagevermögen|umlaufvermögen|c. rechnungsabgrenzungsposten|aktive latente steuern|unterschiedsbetrag|fehlbetrag|a. eigenkapital|rückstellungen|verbindlichkeiten|d. rechnungsabgrenzungsposten|passive latente steuern"
        activa_headers = ["anlagevermögen", "umlaufvermögen", "c. rechnungsabgrenzungsposten", "aktive latente steuern", "unterschiedsbetrag", "fehlbetrag"]

        # Find last category title, to ensure we stop scanning at the correct location later
        final_category = ""
        for line in text.split("\n"):
            scan_category = re.findall(bilanz_header, line.lower())
            if scan_category:
                final_category = scan_category[0]


        active_category= ''
        for line in text.split("\n"):
            scan_category = re.findall(bilanz_header, line.lower())
            if scan_category:
                active_category = scan_category[0]
            
                skip_line = False
                # Hiermit ignorieren wir Summenzeilen, welche keinen MEHRWERT haben
                if (not any(char.isalpha() for char in line)) or ("EUR" in line) or ("Euro" in line) or ("€" in line):
                    skip_line = True

                scan_money = re.findall(r"(\s+\d*[.,]*\d*[.,]*\d*[.,]*\d*[.,]*\d*[.,]*\d*[.,]*\d+[,]\d+)", line)

                if scan_money and "  " in scan_money[0]:
                    skip_line = True

                if verbose:
                    print(f"In line: {line}")
                    print(f"We have category: {active_category}")
                    print(f"Money found: {scan_money}")
                    print(f"Line skipped: {skip_line}")
                    print("" * 80)

                if skip_line:
                    if active_category == final_category: # Diese Abfrage checkt ob das das Ende der Bilanz ist
                        break
                    continue

                if scan_money:
                    if active_category in activa_headers: # Aktiva go in the Aktiva UwU
                        self.bilanz.aktiva[active_category] += self.get_clean_number(scan_money[0])
                    else:
                        self.bilanz.passiva[active_category] += self.get_clean_number(scan_money[0])
                    continue
             
    def computer_use_reading_comprehention(self, verbose=False):
        text = self.extract_text()
        if verbose:
            print(text)  # for testing
        self.parse_text(text, verbose=verbose)
        if verbose:
            self.bilanz.show()


if __name__ == "__main__":
    pdf_0 = Bilanz_PDF("pdfs/Gastro01.pdf", pdf_pages=(0,)) # THIS IS THE FILEPATH TO ADJUST
    pdf_0.computer_use_reading_comprehention()

    pdf_1 = Bilanz_PDF("pdfs/Gastro02.pdf", pdf_pages=(1,))
    pdf_1.computer_use_reading_comprehention()

    strk_blnz_0 = Bilanzklassen.Strukturbilanz(pdf_0.bilanz)
    strk_blnz_0.show()

    strk_blnz_1 = Bilanzklassen.Strukturbilanz(pdf_1.bilanz)
    strk_blnz_1.show()
