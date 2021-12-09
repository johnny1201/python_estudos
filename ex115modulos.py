from lib.interface import *
from lib.arquivo import *
from time import sleep
cadastrados = 'cadastro.txt'
if arqExist(cadastrados):
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')
    criaArq(cadastrados)
while True:
    resp = menu(['Exibir Cadastrados', 'Cadastrar Novo Usuário', 'Deletar Usuário', 'sair'])
    if resp == 1:
        cabeçalho(cores('Exibir Cadastrados', 'blue'))
        lerArq(cadastrados)        
    elif resp ==2:
        cabeçalho(cores('Cadastrar Novo Usuário', 'blue'))
        nome = str(input('Nome: '))
        idade = lerInt('Idade: ')
        cadastrar(cadastrados,nome,idade)
    elif resp ==3:
        cabeçalho(cores('Deletar Usuário', 'blue'))
        limpar(cadastrados)
        print(cores('Dados deletados com sucesso!', 'cyan'))
    elif resp == 4:
        cabeçalho(cores('sair', 'blue'))
        sleep(0.5)
        print(cores('Sistema encerrado, volte sempre!', 'blue'))
        break
    else: print(cores(" ERRO: digite uma opção válida de acordo com o menu ",fundo='yellow',cor='red'))

