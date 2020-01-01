# Tesseract OCR
import pytesseract
from PIL import Image
import sys
from pdf2image import convert_from_path
import os
import io

# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Matthew\AppData\Local\Tesseract-OCR\tesseract.exe'
for pdf in os.listdir('pdfs/'):
pdf_path = 'pdfs/A Production Implementation of an Associative Arran Processor -STARAN - Rudolph.pdf'
output_filename = "results.txt"
pages = convert_from_path(pdf_path)
pg_cntr = 1

sub_dir = str("images/" + pdf_path.split('/')[-1].replace('.pdf','')[0:20] + "/")
if not os.path.exists(sub_dir):
    os.makedirs(sub_dir)

for page in pages:
    if pg_cntr <= 20:
        filename = "pg_"+str(pg_cntr)+'_'+pdf_path.split('/')[-1].replace('.pdf','.jpg')
        page.save(sub_dir+filename)
        with io.open(output_filename, 'a+', encoding='utf8') as f:
            f.write(unicode("======================================================== PAGE " + str(pg_cntr) + " ========================================================\n"))
            f.write(unicode(pytesseract.image_to_string(sub_dir+filename)+"\n"))
            f.write(unicode("======================================================== ========================= ========================================================\n"))
        pg_cntr = pg_cntr + 1
