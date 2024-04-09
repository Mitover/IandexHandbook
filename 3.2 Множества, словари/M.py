N = int(input()) #кол. блюд
dishesSet = set()
for _ in range(N):
    dish = input()
    dishesSet.add(dish)

M = int(input()) #
for _ in range(M):
    countDishInDay = int(input())
    for _ in range(countDishInDay):
        dishInDay = input()
        if dishInDay in dishesSet:
            dishesSet.remove(dishInDay)
dishesSet = sorted(dishesSet)
if len(dishesSet) == 0:
    print("Готовить нечего")
else:
    for i in dishesSet:
        print(i)