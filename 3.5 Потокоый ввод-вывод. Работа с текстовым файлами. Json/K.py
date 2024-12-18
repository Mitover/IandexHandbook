import json
with open(input(), encoding='UTF-8') as f:
    spisok = [int(i) for i in f.read().split()]
    length = len(spisok)
    posit = 0
    for _ in spisok:
        if _ > 0:
            posit += 1
    minim = min(spisok)
    maxim = max(spisok)
    summ = sum(spisok)
    sa = summ / length
data = {
    "count": length,
    "positive_count": posit,
    "min": minim,
    "max": maxim,
    "sum": summ,
    "average": round(sa, 2),
}
with open(input(), "w", encoding="UTF-8") as file_out:
    json.dump(data, file_out, ensure_ascii=False, indent=2)
###
import json
file_in = input().strip()
file_out = input().strip()
with open(file_in, encoding="UTF-8") as file:
    numbers = [int(number) for number in file.read().split()]
data = {
    "count": len(numbers),
    "positive_count": len([number for number in numbers if number > 0]),
    "min": min(numbers),
    "max": max(numbers),
    "sum": sum(numbers),
    "average": round(sum(numbers) / len(numbers), 2),
}
with open(file_out, "w", encoding="UTF-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)