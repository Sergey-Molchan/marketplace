from marketplace.category import Category
from marketplace.product import Product

def test_category_init():
    product = Product("Test", "Desc", 100.0, 5)
    category = Category("Test Category", "Desc", [product])
    assert category.name == "Test Category"
    assert category.description == "Desc"
    assert len(category.products) == 1
    assert isinstance(category.products[0], Product)