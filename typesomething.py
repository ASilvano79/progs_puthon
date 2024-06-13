#### Mostrar logo
#### Frases usadas:
#### Bem vindo ao Jogo de Descobrir um número
#### Eu estou pensando em um número entre 1 e 100
#### Grave o valor do número randomico escolhido 
#### Escolha um nível de dificuldade. Digite 'easy' ou 'hard'
#### Mostre a quantidade de tentativas disponiveis
#### Frase "Você tem X tentativas para acertar o número"
#### Pergunte: "Chute um número: "
#### Se acertou o numero randomico "Você é a propria Mãe Dinah. Acertou o número" entre outras frases
#### Se errou faça a comparação entre o numero chutado e o numero randomico e:
#### Se maior "Você chutou um número maior" e "Chute de novo" e mostre a quantidade de tentativas
#### Se menor "Você chutou um número menor" e "Chute de novo" e mostre a quantidade de tentativas
#### E pergunte novamente "Chute um número"


import random
from typesomething_logo import logo
from replit import clear

tentativas = 0
def game():    
    print(logo)
    print("Bem vindo ao Jogo de Descobrir um Número.\nEu estou pensando em um número entre 1 e 100.")
    random_number = random.randint(1,100)
    #print(f"Random Number: {random_number}")
    global tentativas
    nivel = input("Escolha um nível de dificuldade. Digite 'easy' ou 'hard': ")
    if nivel == "easy":
        tentativas = 10
    elif nivel == "hard":
        tentativas = 5
    else:
        tentativas = 0    
        
    def show_tentativas():
        global tentativas
        print(f"Você tem {tentativas} tentativas para acertar o número")
        
    def diminui_tentativas():
        global tentativas
        tentativas -= 1
        
    def chute():
        chute = int(input("Chute um número: "))
        return chute

    def analisa_result(chute):
        global tentativas
        if chute == random_number:
            print("Você é a propria Mãe Dinah. Acertou o número.")
            tentativas = 0
        elif chute > random_number:
            print("Você chutou um número MAIOR!")
            diminui_tentativas()
            if tentativas > 0:
                print("Chute de novo!")
            
        elif chute < random_number:
            print("Você chutou um número MENOR!")
            diminui_tentativas()
            if tentativas > 0:
                print("Chute de novo!")
        
    while tentativas > 0:    
        show_tentativas()
        opcao = chute()
        analisa_result(opcao)

game()

if tentativas == 0:
    jogar = input("O jogo acabou. Deseja jogar de novo? Digite 'sim' ou 'não'.\n")
    if jogar == "sim":
        clear()
        game()
    else:
        print("Tchau!!!")
