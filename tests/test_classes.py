import pytest

from src.classes import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


def test_product_initialization(products):
    product = products[0]
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization(products):
    category = Category("Смартфоны", "Описание категории", products)
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_product_count(products):
    Category("Смартфоны", "Описание категории", products)
    assert Category.product_count == 3

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    Category("Телевизоры", "Описание категории", [product4])
    assert Category.product_count == 4


def test_category_count(products):
    Category("Смартфоны", "Описание категории", products)
    assert Category.category_count == 1

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    Category("Телевизоры", "Описание категории", [product4])
    assert Category.category_count == 2
