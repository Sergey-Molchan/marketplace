


class Category:
    """Класс описывающий категории продуктов"""
    category_count = 0
    product_count = 0


    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        Category.category_count +=1
        Category.product_count +=len(product)
        