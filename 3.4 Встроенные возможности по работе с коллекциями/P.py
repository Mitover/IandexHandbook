import itertools

suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

suit = input()
rank = input()

ranks.remove(rank)
coloda = itertools.product(ranks, suits.values())

layout = itertools.permutations(coloda, 3)
count = 0
for j in layout:
    if count == 10:
        break
    text = ", ".join([" ".join(i) for i in j])
    if suits[suit] not in text:
        continue
    count += 1
    print(text)
#####
from itertools import chain, permutations, product

suit = input().strip()
rank = input().strip()

suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

ranks.remove(rank)

deck = product(ranks, suits.values())

triplets = permutations(deck, 3)

triplets = [triplet for triplet in triplets if suits[suit] in chain.from_iterable(triplet)]
# triplets.sort()

sorted_combinations = sorted(triplets)
for combination in sorted_combinations:
    print(', '.join(f'{rank} {suit}' for rank, suit in combination))