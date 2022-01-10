from pprint import pprint
cook_book = dict()

def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file: # читаем файл построчно
            dish_name = line.strip() # первая строка - ключ
            counter = int(file.readline())
            temp_list = []
            for item in range(counter): # чтение строки с ингридиентами
                ingridient, quantity, measure = file.readline().split('|')
                temp_list.append({'ingridient_name': ingridient, 'quantity': quantity, 'measure': measure})
            cook_book[dish_name] = temp_list
            file.readline()
    return cook_book

read_data('recipes.txt')
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    cooking_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                if ingridient['ingridient_name'] not in cooking_list:
                    val = {'quantity': int(ingridient['quantity'])*person_count, 'measure': ingridient['measure']}
                    cooking_list[ingridient['ingridient_name']] = val
                else:
                    cooking_list[ingridient['ingridient_name']]['quantity'] += int(ingridient['quantity'])*person_count
    return cooking_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))