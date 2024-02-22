# Usamos a pathlib para trabalhar com caminhos, pastas e arquivos
# de forma que um código funcione em Windows, Linux e Mac.

from pathlib import Path
# from shutil import rmtree


CAMINHO_PROJETO = Path()
# print(CAMINHO_PROJETO.absolute())

CAMINHO_ARQUIVO = Path(__file__)

# print(CAMINHO_ARQUIVO)
# print(CAMINHO_ARQUIVO.parent)
# print(CAMINHO_ARQUIVO.parent.parent)
# ----------------------------------------------------------
ideias = CAMINHO_ARQUIVO.parent / 'aula_pathlib'
# print(ideias / 'arquivo.txt')

# print(Path.home())
# print(Path.home() / 'Desktop' / 'arquivo.txt')

# arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo = Path(__file__).parent / 'arquivo.txt'
# -------------------------------------------------------------
# caminho_arquivo.touch()  # criar/salvar arquivo
# # escreve no arquivo (se tiver algo, sobrescreve)
# caminho_arquivo.write_text('Olá Mundo!')
# print(caminho_arquivo.read_text())
# caminho_arquivo.unlink()  # apaga o arquivo
# ----------------------------------------------------------------
# caminho_arquivo.touch()
# caminho_arquivo.write_text('')
# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha\n')
#     file.write('Outra linha\n')

# print(caminho_arquivo.read_text())
# -------------------------------------------------------------------
caminho_arquivo.touch()
caminho_arquivo.write_text('Olá mundo', encoding='utf8')
caminho_arquivo.unlink()

caminho_pasta = Path(__file__).parent / '15_aula_python_path'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Olá mundo', encoding='utf8')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Olá mundo', encoding='utf8')

# caminho_pasta.rmdir() # apagar pasta caso não tenha nenhum diretorio dentro


files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Ola mundo\n')
        text_file.write(f'file_{i}.txt')

# usando recursão para apagar arquivos
# rmtree(caminho_pasta)


def rmtree_(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree_(file, False)
            file.rmdir()
        else:
            print('  FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree_(caminho_pasta)
