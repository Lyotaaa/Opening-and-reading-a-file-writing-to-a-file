from Task1 import cook_book

def get_shop_list_by_dishes(dishes, person_count):
    book = cook_book()
    number_ingredients = {}
    for meal in dishes:
        meal = meal.capitalize()
        if meal in book:
            for ingredients in book[meal]:
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

if __name__ == '__main__':
    print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10))