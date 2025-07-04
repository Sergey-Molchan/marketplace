class Product:
    """Класс для отображения продукции"""
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = float(price)  # Приватный атрибут
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        """Класс-метод для создания продукта из словаря"""
        return cls(
            name=product_dict['name'],
            description=product_dict['description'],
            price=product_dict['price'],
            quantity=product_dict['quantity']
        )

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой"""
        value = float(value)
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value