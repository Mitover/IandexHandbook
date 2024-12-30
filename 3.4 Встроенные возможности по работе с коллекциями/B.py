A = input().replace(",", "").split()
B = input().replace(",", "").split()
C = list(zip(A, B))
for i in C:
    print(f'{i[0]} - {i[1]}')
#####
left = input().split(', ')
right = input().split(', ')
print('\n'.join([f'{child_left} - {child_right}' for [child_left, child_right] in list(zip(left, right))]))
#####
left = input().split(', ')
right = input().split(', ')
for kids in zip(left, right):
    print(f'{kids[0]} - {kids[1]}')