class ZeroQuantityError(Exception):
    pass

class Product:
    def __init__(self, name, price, quantity):
        if quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.price = price
        self.quantity = quantity

def add_product_to_category(category, product):
    try:
        if product.quantity == 0:
            raise ZeroQuantityError
        category.products.append(product)
        print("Товар успешно добавлен")
    except ZeroQuantityError:
        print("Ошибка: Товар с нулевым количеством не может быть добавлен")
    finally:
        print("Обработка добавления товара завершена")