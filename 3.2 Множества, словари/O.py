numbers = input().split()
total = []
result = dict()
for item in numbers:
    units = zeros = 0
    number = int(item)
    while number > 0:
        if number % 2:
            units += 1
        else:
            zeros += 1
        number = number // 2
    result['digits'] = zeros + units
    result['units'] = units
    result['zeros'] = zeros
    total.append(result.copy())
print(total)
###
numbers = input().split()
total = []
listBin = []
for number in numbers:
    listBin.append(bin(int(number))[2:])
for bn in listBin:
    res = {}
    res['digits'] = len(bn)
    res['units'] = bn.count("1")
    res['zeros'] = bn.count("0")
    total.append(res.copy())
print(total)