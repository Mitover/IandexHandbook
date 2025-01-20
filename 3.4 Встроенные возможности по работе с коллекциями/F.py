from itertools import product
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(input())
for card, suit in product(cards, suits):
    print(card, suit)
#####
from itertools import product
ban = input()
suits = ['пик', 'треф', 'бубен', 'червей']
cards = [str(cards) for cards in range(2, 11)] + ['валет', 'дама', 'король', 'туз'] 
suits.remove(ban)
print('\n'.join([f'{card} {suit}' for card, suit in list(product(cards, suits))]))
