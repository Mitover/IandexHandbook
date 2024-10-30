with open(input(), encoding='UTF-8') as file_in:
    items_1 = set([item for item in file_in.read().split()])
with open(input(), encoding='UTF-8') as file_in:
    items_2 = set([item for item in file_in.read().split()])
with open(input(), 'w', encoding='UTF-8') as file_name:
    print('\n'.join(sorted(items_1 ^ items_2)), file=file_name)
###
file_1 = input()
file_2 = input()
file_out = input()
with open(file_1, encoding='UTF-8') as file_in:
    items_1 = set([item for item in file_in.read().split()])
with open(file_2, encoding='UTF-8') as file_in:
    items_2 = set([item for item in file_in.read().split()])
unique = items_1 ^ items_2
with open(file_out, 'w', encoding='UTF-8') as file_name:
    print('\n'.join(sorted(unique)), file=file_name)


file_1 = input()
file_2 = input()
file_out = input()