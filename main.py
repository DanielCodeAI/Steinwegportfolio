import os
import sys
os.chdir(sys.path[0])

from Bilanzklassen import *
from PDF_Read import *
from kennzahlen import *

balken = "=" * 100

pdf_0 = Bilanz_PDF("pdfs/Gastro01.pdf", pdf_pages=(0,))
pdf_0.computer_use_reading_comprehention()

pdf_1 = Bilanz_PDF("pdfs/Gastro02.pdf", pdf_pages=(1,))
pdf_1.computer_use_reading_comprehention()

strk_blnz_0 = Bilanzklassen.Strukturbilanz(pdf_0.bilanz)
print("\n\nStrukturbilanz für Gastro 1")
strk_blnz_0.show()
print("\n", balken, "\n\nKennzahlen für Gastro 1\n")
alle_kennzahlen_auf_einmal(strk_blnz_0)

print("\n", balken, "\n\n")

strk_blnz_1 = Bilanzklassen.Strukturbilanz(pdf_1.bilanz)
print("Strukturbilanz für Gastro 2")
strk_blnz_1.show()
print("\n", balken, "\n\nKennzahlen für Gastro 2\n")
alle_kennzahlen_auf_einmal(strk_blnz_1)

input() # Damit es bei dateiaufruf das terminal nicht sofort schließt
