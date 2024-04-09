rle = [('a', 2), ('b', 3), ('c', 1)]
w = ''.join(char * count for char, count in rle)
print(w)