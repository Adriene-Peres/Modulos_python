# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostar "Olá mundo" na tela',
    # type=str, # tipo argumento
    metavar='STRING',
    # default='Olá mundo', # valor padrão
    required=False,
    # recebe o argumento mais de uma vez: (...) -b 'a' -b 'b' -b 'c'
    # o tipo deve ser list (não usar o type nem o defaut se não for lista)
    action='append'
    # nargs='+' # recebe mais de um valor: (...) -b 'a' 'b' 'c'
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostar logs',
    action='store_true'  # apenas checa se o argumento foi passado: PS C:\Users\Adriene\Documents\CursoPython\Aulas\Modulos_python> python .\25_argparse_para_argumentos_mais_complexos.py -b 'a' -b 'b' -v
)

args = parser.parse_args()

# utilizar no terminal para mandar -b: python .\25_argparse_para_argumentos_mais_complexos.py -b 123
if args.basic is None:
    print('Você não passou o valor de basic.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

print(args.verbose)
