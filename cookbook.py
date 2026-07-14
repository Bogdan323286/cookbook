"""
Модуль для работы с кулинарной книгой.
Читает файл recipes.txt и предоставляет функции для работы с рецептами.
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
        # Удаляем пустые строки
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


def main():
    """Основная функция программы."""
    try:
        cook_book = parse_recipes('recipes.txt')
    except FileNotFoundError:
        print("Ошибка: файл recipes.txt не найден.")
        return

    print("Кулинарная книга загружена.\n")

    while True:
        print("1. Показать все рецепты")
        print("2. Найти рецепт по названию")
        print("3. Выйти")
        choice = input("Выберите действие (1-3): ").strip()

        if choice == '1':
            display_all_recipes(cook_book)
        elif choice == '2':
            dish = input("Введите название блюда: ").strip()
            display_recipe(dish, cook_book)
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод, попробуйте снова.\n")


if __name__ == '__main__':
    main()