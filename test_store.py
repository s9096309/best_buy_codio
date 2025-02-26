import pytest
from store import Store
from products import Product, NonStockedProduct, LimitedProduct

def test_add_product():
    store = Store([])  # Initialize an empty store
    product = Product("Test Product", 100, 5)
    store.add_product(product)
    assert product in store.products

def test_remove_product():
    product = Product("Test Product", 100, 5)
    store = Store([product])
    store.remove_product(product)
    assert product not in store.products

def test_get_total_quantity():
    products = [
        Product("Product 1", 10, 5),
        Product("Product 2", 20, 10),
        NonStockedProduct("License", 50)
    ]
    store = Store(products)
    assert store.get_total_quantity() == 15

def test_get_all_products():
    products = [
        Product("Product 1", 10, 5),
        Product("Product 2", 20, 0),  # Inactive product
        NonStockedProduct("License", 50)
    ]
    store = Store(products)
    active_products = store.get_all_products()
    assert len(active_products) == 3
    assert set(active_products) == {products[0], products[2]}
    assert products[1] not in active_products

def test_order_valid():
    products = [
        Product("Product 1", 10, 5),
        Product("Product 2", 20, 10)
    ]
    store = Store(products)
    shopping_list = [(products[0], 2), (products[1], 3)]
    total_cost = store.order(shopping_list)
    assert total_cost == 80
    assert products[0].get_quantity() == 3
    assert products[1].get_quantity() == 7

def test_order_insufficient_stock():
    products = [Product("Product 1", 10, 2)]
    store = Store(products)
    shopping_list = [(products[0], 3)]
    with pytest.raises(Exception, match="Not enough quantity of Product 1 available."):
        store.order(shopping_list)

def test_order_inactive_product():
    products = [Product("Product 1", 10, 0)]
    store = Store(products)
    shopping_list = [(products[0], 1)]
    with pytest.raises(Exception, match="Product Product 1 is inactive and cannot be ordered."):
        store.order(shopping_list)