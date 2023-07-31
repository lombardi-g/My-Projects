import os
from PyPDF2 import PdfReader, PdfWriter

def isolar_paragrafo(texto,alvo):
    palavra_procurada = alvo
    paragrafos_isolados = []

    paragraphs = texto.split("\n")  # Split by newline, replace "\n" with appropriate delimiter

    for paragrafo in paragraphs:
        if palavra_procurada in paragrafo:
            paragrafo_tratado = paragrafo.strip()  # Trim leading/trailing whitespaces
            paragrafos_isolados.append(paragrafo_tratado)

    return paragrafos_isolados
    # trimmed_paragraphs now contains all trimmed paragraphs that contain the word "concurso"

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