import pytest
from products import Product

# Test 1: Test that creating a normal product works
def test_create_normal_product():
    product = Product("Laptop", price=1000, quantity=10)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 10
    assert product.is_active() is True

# Test 2: Test that creating a product with invalid details (empty name, negative price, negative quantity) invokes an exception
def test_create_product_with_invalid_details():
    with pytest.raises(ValueError, match="Invalid product details"):
        Product("", price=1450, quantity=100)  # Empty name
    with pytest.raises(ValueError, match="Invalid product details"):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price
    with pytest.raises(ValueError, match="Invalid product details"):
        Product("MacBook Air M2", price=1450, quantity=-1) # Negative quantity

# Test 3: Test that when a product reaches 0 quantity, it becomes inactive
def test_product_inactive_when_quantity_zero():
    product = Product("Phone", price=500, quantity=1)
    product.buy(1)  # Reduce quantity to 0
    assert product.get_quantity() == 0
    assert product.is_active() is False

# Test 4: Test that product purchase modifies the quantity and returns the right output
def test_product_purchase_modifies_quantity_and_returns_cost():
    product = Product("Tablet", price=300, quantity=5)
    total_cost = product.buy(2)  # Buy 2 units
    assert total_cost == 600  # 2 * 300
    assert product.get_quantity() == 3  # Quantity reduced to 3
    assert product.is_active() is True  # Product is still active

# Test 5: Test that buying a larger quantity than exists invokes an exception
def test_buying_larger_quantity_than_exists_raises_exception():
    product = Product("Headphones", price=200, quantity=2)
    with pytest.raises(ValueError, match="Not enough Headphones in stock."):
        product.buy(3)  # Attempt to buy more than available quantity

# Test 6: Test that buying with a non-positive quantity raises an exception
def test_buying_non_positive_quantity_raises_exception():
    product = Product("Speaker", price=150, quantity=5)
    with pytest.raises(ValueError, match="Quantity must be greater than zero."):
        product.buy(0)  # Attempt to buy 0 units
    with pytest.raises(ValueError, match="Quantity must be greater than zero."):
        product.buy(-1)  # Attempt to buy a negative quantity