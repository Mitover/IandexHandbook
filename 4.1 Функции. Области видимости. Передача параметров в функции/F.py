history = []


def modern_print(string):
    if string not in history:
        print(string)
        history.append(string)
#####
history = set()


def modern_print(string):
    if string not in history:
        print(string)
        history.add(string)