from os import close

from lib.interface import cabeçalho, cores


def arqExist(nome=''):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True


def criaArq(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print(cores('ERRO: Não foi possivel criar arquivo', 'red'))
    else:
        print(cores(f'Arquivo {nome} criado com sucesso.','blue'))


def lerArq(nome):
    try:
        a = open(nome,'rt')
    except:
        print(cores('ERRO: falha ao ler arquivo','red'))
    else:
        cabeçalho(cores('Lista de cadastrados: ','green'))
        print(cores(f'{a.read():<30}', 'cyan'))


def cadastrar(arquivo,nome='Desconhecido',idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(cores('Houve um ERRO na abertura do arquivo', 'red'))
    else:
        try:
            a.write(f'{nome:<30}{idade:>3} anos.\n')
        except:
            print(cores('Houve um ERRO na gravação dos dados','red'))
        else:
            print(cores(f'{nome} cadastrado com sucesso!', 'green'))
            a.close()


def limpar(arquivo):
    a = open(arquivo, 'w')
    a.close()