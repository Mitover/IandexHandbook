stroka1 = input()
stroka2 = input()
stroka3 = input()

minStroka = ""

if "зайка" in stroka1:
    minStroka = stroka1
if "зайка" in stroka2:
    if minStroka > stroka2 or not minStroka:
        minStroka = stroka2
if "зайка" in stroka3:
    if minStroka > stroka3 or not minStroka:
        minStroka = stroka3
        
print(minStroka, len(minStroka))