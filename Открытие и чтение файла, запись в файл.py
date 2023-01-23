#Задача №1
with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredient_count = int(f.readline())
        indigents = []
        for i in range(ingredient_count):
            emp = f.readline().strip()
            ingredient_name, quantity, measure = emp.split(' | ')
            indigents.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dish_name] = indigents
print(cook_book)