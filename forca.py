# Nicolas Cursino Magarifuchi e Renan Alves de Medeiros

from random import choice
import requests

request = requests.get('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt').text
palavras = request.splitlines()

forcas = ['''
        +------+
               |
               |
               |
               |
               |
    =============''',
    '''
        +------+
        |      |
               |
               |
               |
               |
    =============''', '''
        +------+
        |      |
        O      |
               |
               |
               |
    =============
    ''', '''
        +------+
        |      |
        O      |
        |      |
               |
               |
    =============
    ''', '''
        +------+
        |      |
        O      |
       /|      |
               |
               |
    =============
    ''', r'''
        +------+
        |      |
        O      |
       /|\     |
               |
               |
    =============
    ''', r'''
        +------+
        |      |
        O      |
       /|\     |
       /       |
               |
    =============
    ''', r'''
        +------+
        |      |
        O      |
       /|\     |
       / \     |
               |
    =============
    ''' ]

especiais = r'[@_!#$%^&*()<>?/\|}{~:ç]'
numeros = '0123456789'

def escolhe():
    return choice(palavras)

def desenha():
    print(forcas[len(erradas)])
    
def chute(letras):
    guess = input('\n\nChute uma letra: ')
    while guess in especiais or guess in numeros:
        guess = input('\nCaractere inválido. Chuta uma letra: ')
    while guess in certas+erradas:
        guess = input('\nVocê já chutou esta letra. Chute uma letra diferente: ')
    while len(guess) > 1:
        guess = input('\nChute apenas uma letra por vez: ')

    return guess.lower()

def ganhou():
    return False not in [c in certas for c in sorteada]
        
def jogar_novamente():
    if ganhou():
        resposta = input('\nVocê ganhou! Deseja jogar novamente? ([Y] Sim | [N] Não): ')
    if ganhou() == False:
        resposta = input('\nVocê perdeu... :( \n Deseja jogar novamente? ([Y] Sim | [N] Não): ')

    possiveis = 'yn'

    while resposta.lower() not in possiveis:
        resposta = input('\nCaractere inválido. Você deseja jogar novamente? ([Y] Sim | [N] Não): ')

    return 'y' in resposta.lower()
    
certas = erradas = ''
chances = 7
sorteada = escolhe()

while True:
    while chances:
        desenha()

        for c in sorteada:
            if c in certas:
                print (c, end = ' ')
            else:
                print ('_', end = ' ')

        guess = chute(certas+erradas)

        if guess in sorteada:
            certas += guess
            
        else:
            erradas += guess
            chances -= 1
        
        if ganhou():
            desenha()
            for i in sorteada:
                print (i, end = ' ')
            if jogar_novamente():
                certas = erradas = ''
                chances = 7
                sorteada = escolhe()
                continue
            if not jogar_novamente():
                break

    if not ganhou():
        print(forcas[7])
        for i in sorteada:
            print(i, end = ' ')
        if jogar_novamente():
            certas = erradas = ''
            chances = 7
            sorteada = escolhe()
            continue
        if not jogar_novamente():
            break
