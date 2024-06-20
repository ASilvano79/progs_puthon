from random import randint
from typesomething_logo import logo
from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

tentativas = 0

def seta_dificuldade():
    nivel = input("Escolha um nível de dificuldade. Digite 'easy' ou 'hard': ")
    if nivel == "easy":
        return EASY_LEVEL_TURNS
    elif nivel == "hard":
        return HARD_LEVEL_TURNS
    else:
        return 0    
    
def show_tentativas(tentativas):
    print(f"Você tem {tentativas} tentativas para acertar o número")
    
def chute():
    chute = int(input("Chute um número: "))
    return chute

def analisa_result(random_number,chute,chutes):
    if chute > random_number:
        print("Você chutou um número MAIOR!")
        return chutes - 1
    elif chute < random_number:
        print("Você chutou um número MENOR!")
        return chutes - 1
    else:
        print(f"Você é a propria Mãe Dinah. Acertou o número: {chute}")
        return 0

def game():    
    
    print(logo)
    print("Bem vindo ao Jogo de Descobrir um Número.\nEu estou pensando em um número entre 1 e 100.")
    random_number = randint(1,100)
    #print(f"Random Number: {random_number}")
    tentativas = seta_dificuldade()
    opcao = 0
    
    while random_number != opcao:    
        show_tentativas(tentativas)
        opcao = chute()
        tentativas = analisa_result(random_number,opcao,tentativas)
        if tentativas == 0:
            jogar = input("O jogo acabou. Deseja jogar de novo? Digite 'sim' ou 'não'.\n")
            if jogar == "sim":
                clear()
                game()
            else:
                print("Tchau!!!")
                return
game()


