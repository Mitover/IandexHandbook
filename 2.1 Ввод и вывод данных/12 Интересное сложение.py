a = int(input())
b = int(input())
n1 = ((a // 100 + b // 100) % 10)
n2 = (a // 10 % 10 + b // 10 % 10) % 10
n3 = (a % 10 + b % 10) % 10
print(n1 * 100 + n2 * 10 + n3)