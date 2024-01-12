number = int(input())
n1 = int(str(number)[0]) #number // 100 
n2 = int(str(number)[1])  #number // 10 % 10
n3 = int(str(number)[2])  #number % 10
n23 = n2 + n3
n12 = n1 + n2
if n12 > n23:
    print(str(n12) + str(n23))#print(n12, n23, sep="")
else:
    print(str(n23) + str(n12)) #, sep="")
