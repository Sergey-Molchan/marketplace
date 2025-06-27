import json


class JsonFile:
    """Простой класс для работы с JSON файлом"""

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        """Загрузка данных из JSON файла"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Ошибка: {e}")
            return []


# Использование
if __name__ == "__main__":
    # 1. Загружаем данные
    data = JsonFile("/Users/sergejmolcan/marketplace/data/products.json").data

    # 2. Выводим все категории
    print("Все категории:")
    for category in data:
        print(f"- {category['name']}")

    # 3. Выводим все товары
    print("\nВсе товары:")
    for category in data:
        print(f"\n{category['name']}:")
        for product in category['products']:
            print(f"  {product['name']} - {product['price']} руб. (Остаток: {product['quantity']})")