import pytest
import products
import store

def test_non_stocked_product_show():
    product = products.NonStockedProduct("Windows License", price=125)
    assert product.show() == "Windows License, Price: 125, (Non-Stocked)"

def test_limited_product_show():
    product = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.show() == "Shipping, Price: 10, Quantity: 250, Maximum: 1"

def test_non_stocked_product_quantity():
    product = products.NonStockedProduct("Windows License", price=125)
    assert product.get_quantity() == 0

def test_limited_product_buy_within_limit():
    product = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    cost = product.buy(1)
    assert cost == 10
    assert product.get_quantity() == 249

def test_limited_product_buy_exceeds_limit():
    product = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(ValueError, match="Cannot buy more than 1 of Shipping."):
        product.buy(2)

def test_non_stocked_product_buy():
    product = products.NonStockedProduct("Windows License", price=125)
    cost = product.buy(2)
    assert cost == 250

def test_non_stocked_product_buy_zero():
    product = products.NonStockedProduct("Windows License", price=125)
    with pytest.raises(ValueError, match="Quantity must be greater than zero."):
        product.buy(0)

def test_non_stocked_product_buy_negative():
    product = products.NonStockedProduct("Windows License", price=125)
    with pytest.raises(ValueError, match="Quantity must be greater than zero."):
        product.buy(-1)