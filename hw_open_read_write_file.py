from pprint import pprint

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingr = file.readline().strip()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingredients.append(
                
                {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish_name] = ingredients
        file.readline()
pprint(cook_book, sort_dicts=False)


my_dishes = ['Омлет', 'Утка по-пекински', 'Фахитос']
dish_list = list(cook_book.keys())
def get_shop_list_by_dishes(my_dishes, person_count): 
    calculation_products_dict = {}
    for one_dish in my_dishes:
        for ingredient in cook_book[one_dish]:
            q = int(ingredient['quantity'])
            # print(cook_book[one_dish])
            # print(ingredient)
            # print(ingredient['ingredient_name'])
            if ingredient['ingredient_name'] in list(calculation_products_dict.keys()):
                q += int(ingredient['quantity'])
                # print(calculation_products_dict.keys())
                # ingredient['quantity'] += ingredient['quantity']
                calculation_products_dict[ingredient['ingredient_name']] = {'measure':ingredient['measure'], 'quantity':q * person_count}
            else:                
                calculation_products_dict[ingredient['ingredient_name']] = {'measure':ingredient['measure'], 'quantity':int(ingredient['quantity']) * person_count}


    return calculation_products_dict
   
pprint(get_shop_list_by_dishes(my_dishes, 1))

