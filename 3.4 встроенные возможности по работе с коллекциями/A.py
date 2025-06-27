text = input().split()
for i in range(len(text)):
    print(f"{i + 1}. {text[i]}")
#####
for index, word in enumerate(input().split(), start=1):
    print(f'{index}. {word}')  
##### 
print('\n'.join([f'{index}. {value}' for index, value in enumerate(input().split(), 1)]))