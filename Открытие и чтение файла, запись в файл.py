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
    number_ingredients = {}
    for meal in dishes:
        if meal in cook_book:
            for ingredients in cook_book[meal]:
                if ingredients['ingredient_name'] not in number_ingredients:
                    number_ingredients[ingredients['ingredient_name']] = {
                        'measure': ingredients['measure'],
                        'quantity': int(ingredients['quantity']) * person_count
                    }
                else:
                    number_ingredients[ingredients['ingredient_name']]['quantity'] = {
                        int(number_ingredients[ingredients['ingredient_name']]['quantity']) +
                        int(ingredients['quantity']) * person_count
                    }
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return number_ingredients 
    
    
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10))