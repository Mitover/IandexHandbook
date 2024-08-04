text = 'Мама мыла раму!'.lower()
symbols = {letter: text.count(letter) for letter in set(text) if letter.isalpha()}
print(symbols)

number = {i : i**2 for i in range(10)}