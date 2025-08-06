from marketplace.zerro_error import ZeroQuantityError
import pytest
from marketplace.product import Product, ZeroQuantityError


def test_zero_quantity_error():
    """Тест создания продукта с нулевым количеством."""
    with pytest.raises(ZeroQuantityError) as exc_info:
        Product("Test", "Desc", 100, 0)

    # Проверяем текст сообщения об ошибке
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_zero_quantity_error_creation():
    """Тест создания исключения с сообщением."""
    error = ZeroQuantityError("Тестовое сообщение")
    assert str(error) == "Тестовое сообщение"

def test_zero_quantity_error_inheritance():
    """Тест иерархии наследования."""
    assert issubclass(ZeroQuantityError, ValueError)