def month(number, language):
    months = {"en": ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
              "ru": ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']}
    return months[language][number - 1]


result = month(7, "ru")
print(result)
result = month(1, "en")
print(result)
