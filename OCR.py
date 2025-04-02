import cv2  # process those images
import pytesseract  # no dyslexia anymore (except it still has dyslexia)
import re  # Kakyoin can't comprehent stopped time - if you dont get it, dont sweat it
import Bilanzklassen # don't forget the class file :3

# this was fun, so I did it myself, no cheating this time (stack overflow is fair game) :O
class Bilanz_OCR:
    def __init__(self, image_path):
        self.image_path = image_path
        self.bilanz = Bilanzklassen.Bilanz()
    
    def preprocess_image(self):
        image = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)  # greyscale cause less information flooding
        _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # >150=white, <=150=black, true binary makes OCR smoother, thresh
        cv2.imwrite("processed_image.png", thresh)  # for testing
        return thresh
    
    def extract_text(self):
        processed_img = self.preprocess_image()

        custom_config = "--oem 3 --psm 6"  # LSTM OCR Engine mit semi-automatischem Layout-Parsing (schlechter
        text = pytesseract.image_to_string(processed_img, lang="deu",config=custom_config)  # <- dark magic
        return text
    
    def get_clean_number(self, x: str)->float:
        xclean = x.replace(".", "")
        xclean = xclean.replace(",", "")
        x_floatable = xclean[:-2] + "." + xclean[-2:]
        return float(x_floatable)
        
    def parse_text(self, text):
        active_category= ''
        for line in text.split("\n"):
            scan_category = re.findall(r"Anlagevermögen|Umlaufvermögen|Eigenkapital|Rückstellungen|Verbindlichkeiten|Rechnungsabgrenzungsposten", line)
            if scan_category:
                active_category = scan_category[0]
                continue

            scan_money = re.findall(r"\s+(\d*[.,]*\d*[.,]*\d*[.,]*\d*[.,]*\d*[.,]*\d*[.,]*\d+[,]\d+)", line)
            print(scan_money)
            if scan_money:
                if active_category in ["Anlagevermögen", "Umlaufvermögen"]: # Aktiva go in the Aktiva UwU
                    self.bilanz.aktiva[active_category] += self.get_clean_number(scan_money[0])
                else:
                    self.bilanz.passiva[active_category] += self.get_clean_number(scan_money[0])
                continue
             
    def computer_use_reading_comprehention(self):
        text = self.extract_text()
        print(text)  # for testing
        self.parse_text(text)
        print(self.bilanz.aktiva)
        print(self.bilanz.passiva)


if __name__ == "__main__":
    ocr = Bilanz_OCR("Eschborn_sharp.png") # THIS IS THE FILEPATH TO ADJUST
    ocr.computer_use_reading_comprehention()
