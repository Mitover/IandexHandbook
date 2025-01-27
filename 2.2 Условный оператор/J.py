number = input()
n1 = int(number[0]) 
n2 = int(number[1])
n3 = int(number[2])
n23 = n2 + n3
n12 = n1 + n2
if n12 > n23:
    print(str(n12) + str(n23))
else:
    print(str(n23) + str(n12)) 
#####
number = int(input())
n1 = number // 100 
n2 = number // 10 % 10
n3 = number % 10
n23 = n2 + n3
n12 = n1 + n2
if n12 > n23:
    print(n12, n23, sep="")
else:
    print(n23, n12, sep="")
