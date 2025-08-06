import json
import os
from tempfile import NamedTemporaryFile
from marketplace.reader_json import JsonFile


TEST_DATA = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны...",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            }
        ]
    }
]


def test_json_file_loading(capsys):
    """Тест корректной загрузки JSON файла"""
    with NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
        json.dump(TEST_DATA, tmp, ensure_ascii=False)
        tmp_path = tmp.name

    try:
        json_file = JsonFile(tmp_path)
        assert json_file.data == TEST_DATA
        captured = capsys.readouterr()
        assert captured.out == ""  # Нет сообщений об ошибке
    finally:
        os.unlink(tmp_path)


def test_json_file_not_found(capsys):
    """Тест обработки отсутствующего файла"""
    json_file = JsonFile("nonexistent_file.json")
    assert json_file.data == []
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out


def test_json_file_invalid_format(capsys):
    """Тест обработки невалидного JSON"""
    with NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
        tmp.write("invalid json")
        tmp_path = tmp.name

    try:
        json_file = JsonFile(tmp_path)
        assert json_file.data == []
        captured = capsys.readouterr()
        assert "Ошибка" in captured.out
    finally:
        os.unlink(tmp_path)


def test_json_file_empty_data(capsys):
    """Тест обработки пустого файла"""
    with NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
        tmp.write("[]")
        tmp_path = tmp.name

    try:
        json_file = JsonFile(tmp_path)
        assert json_file.data == []
        captured = capsys.readouterr()
        assert captured.out == ""  # Нет сообщений об ошибке
    finally:
        os.unlink(tmp_path)
