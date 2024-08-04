string = 'Российская Федерация'
print(''.join(word[0].upper() for word in string.split()))
###
print(''.join([i for i in string.title() if i.isupper()]))
