def cores(msg='',cor='white',fundo='none'): 
    """Função que recebe uma mensagem e de acordo com outros 2 parâmetros, atribui cores para a fonte da mensagem e para o fundo. Caso não seja informada a cor da fonte, o padrão é atribuir branco. Caso não seja informada a cor de fundo, o padrão é não aplicar cor de fundo.
    msg: mensagem que o usuário pretende atribuir cores.
    cor: parâmetro que informa a cor que se pretende aplicar à mensagem, deve ser o nome da cor em inglês, as cores podem ser: black, red, green, yellow, blue, purple ou cyan.
    fundo: parâmetro que informa a cor que se pretende aplicar ao fundo da mensagem, as cores devem ser informadas em inglês e podem ser: black, red, green, yellow, blue, purple ou cyan.
    return: retorna a mensagem com as transformações que foram informadas. 
    """
    fundos = {'black':'\033[1;40m',
              'red':'\033[1;41m', 
              'green':'\033[1;42m',
              'yellow':'\033[1;43m',
              'blue':'\033[1;44m',
              'purple':'\033[1;45m',
              'cyan':'\033[1;46m'}  
    fontes = {'black':'\033[30m',
              'red':'\033[31m',
              'green':'\033[32m',
              'yellow':'\033[33m',
              'blue':'\033[34m',
              'purple':'\033[35m',
              'cyan':'\033[36m'}
    try:
        if cor != 'white':       
            msgcor = fontes[cor] + msg + '\033[m'
            if fundo != 'none':
                msgfundo = fundos[fundo] + msgcor + '\033[m'
        else: msgfundo = fundos[fundo] + msg + '\033[m'
        
    except (ValueError, TypeError):
            print('\033[31mErro: entrada inválida, utilize o nome da cor entre '' e em inglês, confira a lista das 7 cores disponíveis.\033[m')
    else: 
        if fundo == 'none':
            return msgcor
        else:
            return msgfundo


def lerInt (msg):
    """Função que recebe um texto para personalização do input e verifica se a entrada é um inteiro ou não
    entrada: msg -> mensagem personalizada para o input
    return: retorna o numero convertido para inteiro ou 0 caso seja interrompido
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(cores('Erro: entrada inválida, por favor digite um número inteiro válido.','red'))
        except (KeyboardInterrupt):
            print(cores('ERRO: usuário não informou o número.','red'))
            return 0
        else:
            return n


def linha (tamanho=42):
    """Função para criar uma linha com o tamanho especificado na entrada
    entrada: tamanho-> define o tamanho da linha a ser construida, por default é 42
    return: retorna a linha construida
    """
    return '-' * tamanho


def cabeçalho (txt):
    '''Função para formatar um cabeçalho ou titulo entre linhas superiores e inferiores
    entrada: txt-> texto que deve ser colodado em destaque entre linhas
    return: txt formatado entre uma linha superior e uma linha inferior
    '''
    print(linha())
    print(txt)
    print(linha())


def menu(lista):
    '''Função que recebe uma lista de opções e formata para uma tabela de menu
    entrada: lista-> lista com as opções a serem colocadas no menu
    return: menu formatado com as opções fornecidas em lista
    '''
    cabeçalho('\033[35mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = lerInt('\033[33mSua Opção: \033[m')
    return opc  