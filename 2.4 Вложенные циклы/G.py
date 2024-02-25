# count = int(input())
# base_delay = 3
# for number in range(1, count + 1):
#     for delay in range(base_delay, 0, -1):
#         print(f'До старта {delay} секунд(ы)')
#     print(f'Старт {number}!!!')
#     base_delay += 1


count = int(input())
base_delay = 3
for number in range(1, count + 1):
    for delay in range(base_delay):
        print(f'До старта {base_delay - delay} секунд(ы)')
    print(f'Старт {number}!!!')
    base_delay += 1