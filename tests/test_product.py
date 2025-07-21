import pytest
from marketplace.product import Product
from marketplace.product import LawnGrass
from marketplace.product import Smartphone
from marketplace.category import Category

def test_product_init():
    product = Product("Test", "Desc", 100.0, 5)
    assert product.name == "Test"
    assert product.description == "Desc"
    assert product.price == 100.0
    assert product.quantity == 5


def test_price_setter():
    product = Product("Test", "Desc", 100.0, 5)

    # Корректное значение
    product.price = 150.0
    assert product.price == 150.0

    # Отрицательная цена
    with pytest.raises(ValueError, match="Цена должна быть положительной"):
        product.price = -50.0

    # Нулевая цена
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
    assert p1 + p2 == 100*2 + 200*3

    with pytest.raises(TypeError):
        p1 + "not a product"

# test_product.py (дополнение)
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
    assert p1 + p2 == 100*2 + 200*3

def test_add_different_class_products():
    p1 = Smartphone("Phone", "Desc", 100, 2, 90, "M1", 128, "Black")
    p2 = LawnGrass("Grass", "Desc", 50, 10, "RU", "1w", "Green")
    with pytest.raises(TypeError):
        p1 + p2

def test_add_non_product_to_category():
    category = Category("Test", "Desc", [])
    with pytest.raises(TypeError):
        category.add_product("not a product")