import os
from PyPDF2 import PdfReader

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




caminho = os.path.join(r"C:\Users\gabri\OneDrive\Desktop\Projetos\venv\Diarios")
# print(os.path.exists(caminho))


reader = PdfReader(r"C:\Users\gabri\OneDrive\Desktop\Projetos\venv\Diarios\2023_01_27_1674851749.pdf")
num_paginas = len(reader.pages)
listinha=[]

procurado1 = 'Gabriel Lombardi'
procurado2 = 'concurso'

for pagina in range(num_paginas):
    pagina_atual = reader.pages[pagina]
    texto_atual = pagina_atual.extract_text()
    if procurado1 in texto_atual:
        listinha.append(pagina)
        listinha.append(isolar_paragrafo(texto_atual , procurado1))

for coisas in listinha:
    coisas = str(coisas).replace(r"\n","\n")
    print (coisas)

# caminho_arquivo = 'textodopdf.txt'
# with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
#     for coisas in listinha:
#         arquivo.write('\n')
#         arquivo.write(str(coisas))
