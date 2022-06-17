# cards

deck = []
cards = ["heart", "diamond", "spade", "club"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for card in cards:
    for value in values:
        deck.append(f'{value} of {card}')


for card in deck:
    print(card)