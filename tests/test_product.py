import pytest
from marketplace.product import Product, Smartphone, LawnGrass, BaseProduct, LoggingMixin, ZeroQuantityError
from marketplace.category import Category

def test_product_zero_quantity():
    with pytest.raises(ZeroQuantityError):
        Product("Тест", "Описание", 100, 0)

def test_category_average_price():
    # Тест с товарами
    category = Category("Тест", "Описание", [
        Product("Товар1", "Описание1", 100, 1),
        Product("Товар2", "Описание2", 200, 1)
    ])
    assert category.average_price() == 150.0

    # Тест пустой категории
    empty_category = Category("Пустая", "Описание", [])
    assert empty_category.average_price() == 0.0

def test_add_product():
    category = Category("Тест", "Описание", [])
    product = Product("Товар", "Описание", 100, 1)

    # Тест успешного добавления
    assert category.add_product(product) is True

    # Тест с нулевым количеством
    with pytest.raises(ZeroQuantityError):
        Product("Нулевой", "Описание", 100, 0)

def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100.0, 5)

def test_product_inherits_from_base_product():
    assert issubclass(Product, BaseProduct)

def test_logging_mixin(capsys):
    class TestClass(LoggingMixin):
        def __init__(self, x, y):
            super().__init__(x, y)

    TestClass(1, 2)
    captured = capsys.readouterr()
    assert "Создан объект TestClass с параметрами: (1, 2)" in captured.out

def test_product_init():
    product = Product("Test", "Desc", 100.0, 5)
    assert product.name == "Test"
    assert product.description == "Desc"
    assert product.price == 100.0
    assert product.quantity == 5

def test_price_setter():
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0

    with pytest.raises(ValueError, match="Цена должна быть положительной"):
        product.price = -50.0

    with pytest.raises(ValueError):
        product.price = 0

def test_new_product():
    data = {
        "name": "New",
        "description": "New Desc",
        "price": 200.0,
        "quantity": 10
    }
    product = Product.new_product(data)
    assert product.name == "New"
    assert product.price == 200.0

def test_product_str():
    product = Product("Test", "Desc", 100.0, 5)
    assert str(product) == "Test, 100 руб. Остаток: 5 шт."

def test_product_add():
    p1 = Product("P1", "Desc", 100.0, 2)
    p2 = Product("P2", "Desc", 200.0, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3

    with pytest.raises(TypeError):
        p1 + "not a product"

def test_smartphone_init():
    phone = Smartphone("iPhone", "Cool phone", 1000.0, 10, 95.5, "13 Pro", 256, "Black")
    assert phone.name == "iPhone"
    assert phone.memory == 256
    assert phone.color == "Black"

def test_lawn_grass_init():
    grass = LawnGrass("Grass", "Green grass", 50.0, 100, "Russia", "2 weeks", "Green")
    assert grass.country == "Russia"
    assert grass.germination_period == "2 weeks"

def test_add_same_class_products():
    p1 = Smartphone("Phone1", "Desc", 100, 2, 90, "M1", 128, "Black")
    p2 = Smartphone("Phone2", "Desc", 200, 3, 95, "M2", 256, "White")
    assert p1 + p2 == 100 * 2 + 200 * 3

def test_add_different_class_products():
    p1 = Smartphone("Phone", "Desc", 100, 2, 90, "M1", 128, "Black")
    p2 = LawnGrass("Grass", "Desc", 50, 10, "RU", "1w", "Green")
    with pytest.raises(TypeError):
        p1 + p2

def test_add_non_product_to_category():
    category = Category("Test", "Desc", [])
    result = category.add_product("not a product")
    assert result is False

def test_product_zero_quantity_message():
    with pytest.raises(ZeroQuantityError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Тест", "Описание", 100, 0)

def test_add_product_output(capsys):
    category = Category("Тест", "Описание", [])
    product = Product("Товар", "Описание", 100, 1)
    category.add_product(product)
    captured = capsys.readouterr()
    assert "Товар успешно добавлен" in captured.out
    assert "Обработка добавления завершена" in captured.out


def test_product_price_validation():
    product = Product("Test", "Desc", 100, 5)
    with pytest.raises(ValueError):
        product.price = -50