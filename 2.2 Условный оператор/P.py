p = int(input())
v = int(input())
t = int(input())

first_str = ""
second_str = ""
third_str = ""

if p > v and p > t:
    if v > t:
        first_str = "Петя"
        second_str = "Вася"
        third_str = "Толя"
    else:
        first_str = "Петя"
        second_str = "Толя"
        third_str = "Вася"
elif v > p and v > t:
    if p > t:    
        first_str = "Вася"
        second_str = "Петя"
        third_str = "Толя"
    else:
        first_str = "Вася"
        second_str = "Толя" 
        third_str = "Петя"
elif t > p and t > v:
    if p > v:
        first_str = "Толя"
        second_str = "Петя" 
        third_str = "Вася"
    else:
        first_str = "Толя"
        second_str = "Вася"
        third_str = "Петя" 


print(f"{first_str: ^24}")
print(f"{'  ' + second_str: <24}")
print(f"{third_str: >22}")
print(f"{' II': ^8}{'I': ^8}{'III': ^8}")

