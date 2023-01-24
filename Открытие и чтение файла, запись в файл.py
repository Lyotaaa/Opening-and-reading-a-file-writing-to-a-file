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
# print(cook_book)

#Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    number_indigents = {}
    for meal in dishes:
        if meal in cook_book:
            for ingredients in cook_book[meal]:
                #Свой вариант
                ingredients['quantity'] = int(ingredients["quantity"]) * person_count
                ingredients = {
                    'measure': ingredients['measure'],
                    'quantity': ingredients['quantity'],
                    'ingredient_name': ingredients['ingredient_name']
                }
                number_indigents[ingredients['ingredient_name']] = ingredients
                retrievable_value = ingredients.pop('ingredient_name')
                #Подсказал эксперт(аспират)
                # number_indigents[indigents['ingredient_name']] = {
                #     'measure': indigents['measure'],
                #     'quantity': int(indigents['quantity']) * person_count
                # }
    return print(number_indigents)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10)