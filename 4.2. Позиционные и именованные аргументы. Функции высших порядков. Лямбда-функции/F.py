RECIPES = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1},
}
in_stock = {"coffee": 1, "milk": 2, "cream": 3}
in_stock = {"coffee": 4, "milk": 4, "cream": 0}
###
in_stock = {}
def order(*drinks):
    global in_stock

    temp = in_stock
    for drink in drinks:
        for ingredient in RECIPES[drink]:
            if RECIPES[drink][ingredient] > in_stock[ingredient]:
                break
        else:
            for ingredient in RECIPES[drink]:
                in_stock[ingredient] -= RECIPES[drink][ingredient]
            return drink

    if in_stock == temp:
        return "К сожалению, не можем предложить Вам напиток"
###
in_stock = {}
def order(*drinks):
    global in_stock

    temp = in_stock
    for drink in drinks:
        for ingredient in RECIPES[drink]:
            if in_stock[ingredient] >= RECIPES[drink][ingredient]  :
                break
        else:
            for ingredient in RECIPES[drink]:
                in_stock[ingredient] -= RECIPES[drink][ingredient]
            return drink

    if in_stock == temp:
        return "К сожалению, не можем предложить Вам напиток"
# def order(*name_drink):
#     global in_stock
#     flag = True
#     for name in name_drink:
#         match name:
#             case "Эспрессо":
#                 if in_stock["coffee"] >= 1:
#                     in_stock["coffee"] -= 1
#                     return name
#             case "Капучин":
#                 if in_stock["coffee"] >= 1 and in_stock["milk"] >= 3:
#                     in_stock["coffee"] -= 1
#                     in_stock["milk"] -= 3
#                     return name
#             case "Макиато":
#                 if in_stock["coffee"] >= 2 and in_stock["milk"] >= 1:
#                     in_stock["coffee"] -= 2
#                     in_stock["milk"] -= 1
#                     return name
#             case "Кофе по-венски":
#                 if in_stock["coffee"] >= 1 and in_stock["cream"] >= 2:
#                     in_stock["coffee"] -= 1
#                     in_stock["cream"] -= 2
#                     return name
#             case "Латте Макиато":
#                 if in_stock["coffee"] >= 1 and in_stock["milk"] >= 2 and in_stock["cream"] >= 1:
#                     in_stock["coffee"] -= 1
#                     in_stock["cream"] -= 1
#                     in_stock["milk"] -= 2
#                     return name
#             case "Кон Панна":
#                 if in_stock["coffee"] >= 1 and in_stock["cream"] >= 1:
#                     in_stock["coffee"] -= 1
#                     in_stock["cream"] -= 1
#                     return name

#     if flag:
#         return "К сожалению, не можем предложить Вам напиток"
### 
def is_enough_ingredients(drink):
    global RECIPES, in_stock
    return all(RECIPES[drink][ingredient] <= in_stock[ingredient] for ingredient in RECIPES[drink])
def order(*drinks):
    global RECIPES, in_stock
    for drink in drinks:
        if is_enough_ingredients(drink):
            for ingredient, amount in RECIPES[drink].items():
                in_stock[ingredient] -= amount
            return drink
    return 'К сожалению, не можем предложить Вам напиток'
###




# print(order("Капучино", "Макиато", "Эспрессо"))
# print(order("Капучино", "Макиато", "Эспрессо"))
# print(order("Капучино", "Макиато", "Эспрессо"))

