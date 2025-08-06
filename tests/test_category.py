from marketplace.category import Category
from marketplace.product import Product


def test_category_init():
    product = Product("Test", "Desc", 100.0, 5)
    category = Category("Test Category", "Description", [product])
    assert category.name == "Test Category"
    assert category.description == "Description"
    assert "Test, 100 руб. Остаток: 5 шт." in category.products


def test_add_product():
    initial_count = Category.product_count
    category = Category("Test", "Desc", [])
    product = Product("New", "Desc", 50.0, 2)

    category.add_product(product)
    assert Category.product_count == initial_count + 1
    assert "New, 50 руб. Остаток: 2 шт." in category.products


def test_products_property():
    p1 = Product("P1", "Desc", 10.0, 1)
    p2 = Product("P2", "Desc", 20.0, 2)
    category = Category("Test", "Desc", [p1, p2])

    products_str = category.products
    assert "P1, 10 руб. Остаток: 1 шт." in products_str
    assert "P2, 20 руб. Остаток: 2 шт." in products_str


def test_counters():
    initial_cat = Category.category_count
    initial_prod = Category.product_count

    p1 = Product("P1", "Desc", 10.0, 1)
    p2 = Product("P2", "Desc", 20.0, 2)
    category = Category("Test", "Desc", [p1, p2])

    assert Category.category_count == initial_cat + 1
    assert Category.product_count == initial_prod + 2


def test_category_str():
    p1 = Product("P1", "Desc", 10.0, 1)
    p2 = Product("P2", "Desc", 20.0, 2)
    category = Category("Test", "Desc", [p1, p2])
    assert str(category) == "Test, количество продуктов: 3 шт."


def test_category_iterator():
    p1 = Product("P1", "Desc", 10.0, 1)
    p2 = Product("P2", "Desc", 20.0, 2)
    category = Category("Test", "Desc", [p1, p2])

    products = list(category)
    assert len(products) == 2
    assert products[0] == p1
    assert products[1] == p2


def test_add_product_invalid_type():
    category = Category("Test", "Desc", [])
    result = category.add_product("not a product")  # Должно вызвать TypeError
    assert result is False