def menu_book():
    with open('cookbook.txt') as menu_cook:
        menu_cookbook = {}
        while True:
            dish_name = menu_cook.readline().lower().strip()
            if dish_name:
                menu_cookbook[dish_name] = []
                count_of_ingridients = int(menu_cook.readline())
                for i in range(count_of_ingridients):
                    ingridient = {}
                    part = menu_cook.readline().split(' | ')
                    ingridient['название_ингредиента'] = part[0]
                    ingridient['количество'] = int(part[1])
                    ingridient['ед_измерения'] = part[2]
                    menu_cookbook[dish_name].append(ingridient)
            else:
                break
        return menu_cookbook


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in menu_cookbook[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
