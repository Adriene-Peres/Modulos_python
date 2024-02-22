# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code

'''
exemplo de como passar argumetos:
PS C:\\Users\\Adriene\\Documents\\CursoPython\\Aulas\\Modulos_python> cls ; python -u "c:\\Users\\Adriene\\Documents\\CursoPython\\Aulas\\Modulos_python\\tempCodeRunnerFile.python" 
"oi" "coca" "bola"
'''

import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumetos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça algo com {argumentos[1]}')
        print(f'Faça algo com {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')
