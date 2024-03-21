text = 'Мама мыла раму!'
symbols = {letter: text.lower().count(letter) for letter in set(text.lower()) if letter.isalpha()}
print(symbols)