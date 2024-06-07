from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bids = {}
bid_finished = False

def find_highest_bidder(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = float(bid_record[bidder])
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  

while not bid_finished:
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bid_finished = True
        find_highest_bidder(bids)    
    elif should_continue == "yes":
        clear()
    
