import pytest
from store import Store
from products import Product

def test_product_creation():
    product = Product("Laptop", price=1000, quantity=5)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 5
    assert product.is_active() is True

def test_product_methods():
    product = Product("Laptop", price=1000, quantity=5)