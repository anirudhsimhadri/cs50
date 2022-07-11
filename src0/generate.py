import random

def main():
    cards = ["jack", "queen", "kind"]
    random.shuffle(cards)
    for card in cards:
        print(card)

main()