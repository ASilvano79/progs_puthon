import random
from replit import clear
from black_logo import logo

def deal_card():
  """Retorna carta randomica do deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Pega uma lista de cartas e retorna o score calculado a partir das cartas"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "Você ultrapassou 21. Você PERDEU 😤"

  if user_score == computer_score:
    return "EMPATE 🙃"
  elif computer_score == 0:
    return "PERDEU, adversário fez Blackjack 😱"
  elif user_score == 0:
    return "Você VENCEU com um Blackjack 😎"
  elif user_score > 21:
    return "Você ultrapassou 21. Você PERDEU 😭"
  elif computer_score > 21:
    return "Adversário ultrapassou 21. Você GANHOU 😁"
  elif user_score > computer_score:
    return "Você GANHOU 😃"
  else:
    return "Você PERDEU 😤"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Suas cartas: {user_cards}, current score: {user_score}")
    print(f"   Primeira carta do computador: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Digite 'y' para uma nova carta, digite 'n' para passar: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Sua mão final: {user_cards}, score final: {user_score}")
  print(f"   Mão final do computador: {computer_cards}, score final: {computer_score}")
  print(compare(user_score, computer_score))

while input("Você quer jogar Blackjack? Digite 'y' ou 'n': ") == "y":
  clear()
  play_game()
