#Задача №1
def cook_book():
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
        return cook_book
# print(cook_book())

#Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    book = cook_book()
    number_ingredients = {}
    for meal in dishes:
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
# print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10))

# Задача №3
def textual_systematisation(number_files, recording_file):
    joint_file = {}
    for i in range(1, number_files + 1):
        name = f'{i}.txt'
        with open(name, 'r', encoding='utf-8') as f:
            joint_file[name] = [x for x in f.read().splitlines() if x]
    with open(recording_file, 'w', encoding='utf-8') as file:
        for file_number, value in sorted(joint_file.items(), key=lambda x: len(x[1])):
            file.write(file_number + '\n')
            file.write(str(len(value)) + '\n')
            file.write('\n'.join(value))
            file.write('\n')
    return

textual_systematisation(3, '4.txt')