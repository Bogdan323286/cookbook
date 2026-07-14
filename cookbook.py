"""
Модуль для работы с кулинарной книгой.
Читает файл recipes.txt, предоставляет функции для просмотра рецептов
и составления списка покупок.
"""


def parse_recipes(file_path: str) -> dict:
    """
    Читает файл с рецептами и возвращает словарь вида:
    {
        'Название блюда': [
            {'ingredient_name': '...', 'quantity': ..., 'measure': '...'},
            ...
        ],
        ...
    }
    """
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        dish_name = lines[i]
        i += 1
        ingredient_count = int(lines[i])
        i += 1

        ingredients = []
        for _ in range(ingredient_count):
            parts = lines[i].split(' | ')
            ingredient = {
                'ingredient_name': parts[0],
                'quantity': int(parts[1]),
                'measure': parts[2]
            }
            ingredients.append(ingredient)
            i += 1

        cook_book[dish_name] = ingredients

    return cook_book


def display_recipe(recipe_name: str, cook_book: dict) -> None:
    """Выводит ингредиенты для указанного блюда."""
    if recipe_name not in cook_book:
        print(f"Рецепт '{recipe_name}' не найден.")
        return
    print(f"\nРецепт: {recipe_name}")
    for ing in cook_book[recipe_name]:
        print(f"  {ing['ingredient_name']}: {ing['quantity']} {ing['measure']}")


def display_all_recipes(cook_book: dict) -> None:
    """Выводит все рецепты."""
    for dish_name, ingredients in cook_book.items():
        print(f"\nРецепт: {dish_name}")
        for ing in ingredients:
            print(f"  {ing['ingredient_name']}: {ing['quantity']} {ing['measure']}")
    print()


def get_shop_list_by_dishes(dishes: list, person_count: int, cook_book: dict) -> dict:
    """
    Возвращает словарь с общим количеством ингредиентов
    для приготовления указанных блюд на заданное число персон.

    Формат возврата:
    {
        'ингредиент': {'measure': 'ед.', 'quantity': число},
        ...
    }
    """
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f"Предупреждение: блюдо '{dish}' не найдено в кулинарной книге.")
            continue
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count

            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list


def main() -> None:
    """Основная функция программы."""
    try:
        cook_book = parse_recipes('recipes.txt')
        print("Кулинарная книга загружена.\n")
    except FileNotFoundError:
        print("Ошибка: файл recipes.txt не найден.")
        return

    while True:
        print("Меню:")
        print("1. Показать все рецепты")
        print("2. Найти рецепт по названию")
        print("3. Составить список покупок для блюд")
        print("4. Выйти")
        choice = input("Выберите действие (1-4): ").strip()

        if choice == '1':
            display_all_recipes(cook_book)
        elif choice == '2':
            dish = input("Введите название блюда: ").strip()
            display_recipe(dish, cook_book)
        elif choice == '3':
            dishes_input = input("Введите названия блюд через запятую: ").strip()
            dishes = [d.strip() for d in dishes_input.split(',') if d.strip()]
            if not dishes:
                print("Вы не ввели ни одного блюда.\n")
                continue
            try:
                person_count = int(input("На сколько персон готовим? ").strip())
            except ValueError:
                print("Ошибка: введите целое число.\n")
                continue

            shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
            if shop_list:
                print("\nСписок покупок:")
                for ingredient, data in shop_list.items():
                    print(f"  {ingredient}: {data['quantity']} {data['measure']}")
                print()
            else:
                print("Ничего не добавлено (возможно, блюда не найдены).\n")
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод, попробуйте снова.\n")


if __name__ == '__main__':
    main()