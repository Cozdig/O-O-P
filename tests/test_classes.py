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

def test_product_price_getter_setter():
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.price == 100.0

    product.price = 150.0
    assert product.price == 150.0

def test_new_product():
    params = {
        'name': "Test Product",
        'description': "Description",
        'price': 100.0,
        'quantity': 10
    }
    product = Product.new_product(params)

    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10

def test_add_product(products):
    category = Category("Смартфоны", "Описание категории", products)
    initial_product_count = len(category.products)

    new_product = Product("Google Pixel 7", "128GB, Черный", 150000.0, 10)
    category.add_product(new_product)

    assert len(category.products) == initial_product_count + 1
    assert Category.product_count == initial_product_count + 1
    assert new_product in category.products

def test_products_property(products):
    category = Category("Смартфоны", "Описание категории", products)
    assert category.products == products

def test_get_products(products):
    category = Category("Смартфоны", "Описание категории", products)
    products_list = category.get_products()

    assert len(products_list) == 3
    assert products_list[0] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert products_list[1] == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert products_list[2] == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."