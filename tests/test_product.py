import pytest
from marketplace.product import Product

def test_product_init():
    product = Product("Test", "Desc", 100.0, 5)
    assert product.name == "Test"
    assert product.description == "Desc"
    assert product.price == 100.0
    assert product.quantity == 5
    