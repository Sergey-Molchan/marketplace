class Category:
    category_count = 0
    product_count = 0

  
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        """Геттер для отображения товаров"""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    def add_product(self, product):
        """Метод для добавления товара"""
        self.__products.append(product)
        Category.product_count += 1

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

