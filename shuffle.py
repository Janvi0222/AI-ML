import random
suits = ['Hearts', 'Diamonds' , 'Clubs', 'Spades']
ranks=['2', '3','4','5','6','7','8','9','10','J','Q','K','A']

deck = []

for suit in suits:
  for rank in ranks:
    deck.append(rank+ ' of ' +suit)

print("Original Deck:")
print(deck)

random.shuffle(deck)

print("\nShuffled Deck:")
for card in deck:
  print(card)
