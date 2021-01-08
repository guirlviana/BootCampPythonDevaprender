def line():
    print('-' * 30)

def showProgramName():
    print('Bem-Vindo ao Gerador de Dados p/ Testes - Para encerrar o programa, basta digitar "parar"')

def menuOptions():
    print(
'''Escolha uma ou mais opções abaixo a serem geradas aleatóriamente (separe por virgulas exemplo: 1,2,4)
[1] - Nome
[2] - E-mail
[3] - Telefone
[4] - Cidade
[5] - Estado''')


def getNames():
    return ['Goku', 'Piccolo', 'Kuririn', 'Vegeta', 'Bulma']

def getEmails():
    return ['chichi43@gmail.com', 'kamedbz@hotmail.com', 'reifreeza@yahoo.com', 'trunksdofuturo@gmail.com', 'yamchagod@hotmail.com'] 

def getCity():
    return ['cidade do sul', 'cidade do norte', 'cidade do leste', 'cidade do oeste', 'cidade do nordeste']

def getState():
    return ['estado a', 'estado b', 'estado c', 'estado d', 'estado e']

def getPhone():
    return ['(89) 34749-5394', '(71) 67693-2130', '(39) 55143-7610', '(46) 65385-8531', '(82) 39830-8157']
