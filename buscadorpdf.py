import os
from PyPDF2 import PdfReader, PdfWriter

# Get path
pdf_path = os.path.join(r"/Users/gabriel/Desktop/Projeto")

# test
# print(os.path.exists(caminho))


reader = PdfReader(pdf_path)

procurado1 = 'Gabriel Lombardi'
procurado2 = 'concurso'

# reader and writer perform operations
reader = PdfReader(pdf_path)
writer = PdfWriter()

for page in reader.pages:
    # Extract text from page
    text = page.extract_text().lower()
    
    # Find all occurances of key word
    if text.find(procurado1) or text.find(procurado2) > -1:
        writer.add_page(page)
    
# Write all pages to new pdf, saves in working dir
writer.write('results.pdf')
