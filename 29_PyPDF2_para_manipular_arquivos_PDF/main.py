# PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

# 29_PyPDF2_para_manipular_arquivos_PDF

from pathlib import Path
from PyPDF2 import PdfReader, PdfFileWriter, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = Path(__file__).parent / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20240209.pdf'

PASTA_NOVA.mkdir(exist_ok=True)


reader = PdfReader(RELATORIO_BACEN)
# print(len(reader.pages))

# for pages in reader.pages:
#     ...

page0 = reader.pages[0]
imagem0 = page0.images[0]

# print(page0.extract_text())
# print(len(page0.images))
# print(page0.images[0])

# salvar uma imagem do PDF
with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)

# escrever em PDF
# writer = PdfWriter()
# writer.add_page(page0)

# with open(PASTA_NOVA / 'page0.pdf', 'wb') as arquivo:
#     writer.write(arquivo)  # type: ignore

# escreve as paginas do pdf em um so (copia do pdf) - mais facil fazer cópia
# with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as arquivo:
#     for page in reader.pages:
#         writer.add_page(page)

#     writer.write(arquivo)  # type: ignore

# escreve as paginas do pdf em pdf's diferentes
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page_{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore


files = [
    PASTA_NOVA / f'page_1.pdf',
    PASTA_NOVA / f'page_0.pdf'

]
merger = PdfMerger()

for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / f'MERGED.pdf')  # iverteu as paginas
merger.close()
