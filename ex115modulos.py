from lib.interface import *
from time import sleep
while True:
    resp = menu(['inscrever', 'pesquisar', 'deletar', 'sair'])
    if resp == 1:
        print('\033[35mOpção 1: \033[m')
    elif resp ==2:
        print('Opção 2: ')
    elif resp ==3:
        print('Opção 3: ')
    elif resp == 4:
        print('\033[1;36;107mAté logo',end='')
        sleep(0.5)
        print(' volte sempre!\033[m')
        break
    else: print(cores(" ERRO: digite uma opção válida de acordo com o menu ",fundo='yellow',cor='red'))

print(cores(cores('mensagem', 'red'),'white', 'green'),end='')