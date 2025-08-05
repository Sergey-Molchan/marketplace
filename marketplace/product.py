from abc import ABC, abstractmethod


class ZeroQuantityError(ValueError):
    """Пользовательское исключение для товаров с нулевым количеством"""
    pass

class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = float(price)
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        print(f"Создан объект {self.__class__.__name__} с параметрами: {args}, {kwargs}")
        # Не вызываем super().__init__() здесь

    def __repr__(self):
        params = ', '.join([f"{k}={v!r}" for k, v in self.__dict__.items()
                            if not k.startswith('_')])
        return f"{self.__class__.__name__}({params})"


class Product(BaseProduct, LoggingMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")

        BaseProduct.__init__(self, name, description, price, quantity)
        LoggingMixin.__init__(self, name, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value

    def __str__(self):
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("Можно складывать только объекты одного класса")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_data):
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )


class Smartphone(Product):
    """Класс смартфона, наследующий Product."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс газонной травы, наследующий Product."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color