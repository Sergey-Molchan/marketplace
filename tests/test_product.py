import pytest
from marketplace.product import Product


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