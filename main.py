from Bilanzklassen import *
from PDF_Read import *
from kennzahlen import *

pdf_0 = Bilanz_PDF("pdfs/Gastro01.pdf", pdf_pages=(0,))
pdf_0.computer_use_reading_comprehention()

pdf_1 = Bilanz_PDF("pdfs/Gastro02.pdf", pdf_pages=(1,))
pdf_1.computer_use_reading_comprehention()

strk_blnz_0 = Bilanzklassen.Strukturbilanz(pdf_0.bilanz)
strk_blnz_0.show()
print(alle_kennzahlen_auf_einmal(strk_blnz_0))

strk_blnz_1 = Bilanzklassen.Strukturbilanz(pdf_1.bilanz)
strk_blnz_1.show()
print(alle_kennzahlen_auf_einmal(strk_blnz_1))
