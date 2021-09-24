from pprint import pprint

cook_book = dict()


def format_recipe_list(file_name):
    with open(file_name) as file:
        for line in file:
            recipe_name = line.strip()
            ingredient_count = int(file.readline())

            recipes_list = []
            for item in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                recipes_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip('\n')}
                )
            cook_book[recipe_name] = recipes_list

            file.readline()
    return cook_book


format_recipe_list('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for item in cook_book[dish]:
            items_list = dict([(item['ingredient_name'],
                                {'measure': item['measure'], 'quantity': int(item['quantity'] * person_count)})])
            if shop_list.get(item['ingredient_name']):
                add_item = (int(shop_list[item['ingredient_name']]['quantity']) +
                            int(items_list[item['ingredient_name']]['quantity']))
                shop_list[item['ingredient_name']]['quantity'] = add_item
            else:
                shop_list.update(items_list)

    return shop_list


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
