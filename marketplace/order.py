from abc import ABC, abstractmethod

class BaseEntity(ABC):
    """Абстрактный класс для сущностей с именем."""
    @abstractmethod
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass

class Order(BaseEntity):
    """Класс заказа."""
    def __init__(self, product, quantity):
        super().__init__(f"Заказ {product.name}")
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} шт. по {self.product.price} руб. Итого: {self.total_cost} руб."