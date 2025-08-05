from marketplace.product import Product
from marketplace.zerro_error import ZeroQuantityError

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        return "\n".join(str(p) for p in self.__products)



    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        return iter(self.__products)

    def average_price(self) -> float:
        """Подсчитывает средний ценник всех товаров категории"""
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    def add_product(self, product: Product) -> bool:
        """Добавляет товар в категорию с обработкой исключений"""
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты Product")

            if product.quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")

            self.__products.append(product)
            Category.product_count += 1
            print("✓ Товар успешно добавлен")
            return True

        except (TypeError, ZeroQuantityError) as e:
            print(f"✗ Ошибка: {e}")
            return False

        finally:
            print("Обработка добавления завершена")

    def middle_price(self) -> float:
        """Подсчет средней цены (для совместимости с main.py)"""
        try:
            return round(sum(p.price for p in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0.0
