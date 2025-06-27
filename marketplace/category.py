class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products  # Эта строка ОБЯЗАТЕЛЬНА
        Category.category_count += 1
        Category.product_count += len(products)
