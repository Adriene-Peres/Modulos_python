# os + shutil - Copiando arquivos com Python
# Mover/Renomear -> shutil.move ou os.rename
# Copiar -> shutil.copy
# Apagar arquivos-> os.unlink
# Copiar diretório recursivamente -> shutill.copytree
# Apagar diretório recursivamente -> shutil.rmtree

# 1 - copiar arquivos de uma pasta para outra
import os
import shutil

HOME = os.path.expanduser('~')  # pega o caminho de user "C:\Users\Adriene\"
DESKTOP = os.path.join(HOME, 'Desktop')
# escolher uma pasta do desktop
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Hackers do Bem')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

# os.makedirs(NOVA_PASTA, exist_ok=True) # cria a pasta no desktop (ou caminho q escolher)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file_ in files:
#         caminho_arquivo = os.path.join(root, file_)
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file_
#         )
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)

# --------------------------------------------------------------------------
# 2 - apagando e copiando pastas com python

shutil.rmtree(NOVA_PASTA, ignore_errors=True)  # apaga a pasta
# fuciona para copiar caso a pasta nao exista
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')  # renomear pasta
