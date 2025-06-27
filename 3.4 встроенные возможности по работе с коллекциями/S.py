from itertools import product

code = "not A or B and C"#input()

varibles = sorted(list(set([i for i in code.split() if i.isupper()])))

print(" ".join(varibles) + " F") 

for value in product([False, True], repeat=len(varibles)):
    glob = {varibles[key] : value[key] for key in range(len(varibles))}
    print(" ".join([str(int(j)) for j in glob.values()]) + " " + str(int(eval(code, glob))))