# Se acertar:
# A opção B vira A e seleciona uma nova opção B
# Mostra a mensagem "Voce está certo", soma a quantidade de acertos e mostra
# Se errar:
# Mostra a mensagem "Voce errou", mostra a quantidade de acertos, encerra o jogo

from higher_lower_data import data
from higher_lower_art import logo, vs
import random
from replit import clear

def seleciona_a(opcao):
    opcao_a = opcao
    return opcao_a

def seleciona_b(opcao_a, opcao_b):
    opcao_b = opcao_b
    while opcao_a == opcao_b:
        opcao_b = random.choice(data)
    return opcao_b

def escolha():
    #escolha = str.lower(input("Quem tem mais seguidores? Digite 'A' ou 'B': "))
    escolha = input("Quem tem mais seguidores? Digite 'A' ou 'B': ").lower()
    return escolha

def verifica_maior(qtd_a, qtd_b):
    if qtd_a > qtd_b:
        return 'a'
    else:
        return 'b'    
    
def soma_acerto(acertos):
    return acertos + 1

def mostra_logo():
    print(logo)

acertos = 0
erro = False
opcao_a = seleciona_a(random.choice(data))
follow_a = int(opcao_a["follower_count"])
mostra_logo()
while not erro:
    print(f"Compare A: {opcao_a["name"]}, {opcao_a["description"]}, from {opcao_a["country"]}")
    print(vs)
    opcao_b = seleciona_b(opcao_a, random.choice(data))
    follow_b = int(opcao_b["follower_count"])
    print(f"Comparado com B: {opcao_b["name"]}, {opcao_b["description"]}, from {opcao_b["country"]}")        
    opcao = escolha()
    acertos = soma_acerto(acertos)
    maior = verifica_maior(follow_a, follow_b)
    if opcao == maior:
        clear()
        mostra_logo()
        print(f"Você está certo! Score atual: {acertos}")
        opcao_a = opcao_b
        follow_a = follow_b
    else:
        clear()
        mostra_logo()
        print(f"Você Errou! Score atual: {acertos}")
        erro = True
        
