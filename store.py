from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        """Initializes the store with a list of products."""
        self.products = products

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list) -> float:
        """
        Processes a shopping list of (product, quantity) tuples.
        Reduces product quantities and returns the total cost.
        """
        total_cost = 0
        for product, quantity in shopping_list:
            # Check if the product is active
            if not product.is_active():
                raise Exception(f"Product {product.name} is inactive and cannot be ordered.")

            # Check if the requested quantity is available
            if product.get_quantity() < quantity:
                raise Exception(
                    f"Not enough quantity of {product.name} available. "
                    f"Requested: {quantity}, Available: {product.get_quantity()}")

            # Reduce the quantity and calculate the cost
            total_cost += product.buy(quantity)
        return total_cost
