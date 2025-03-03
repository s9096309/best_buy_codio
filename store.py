from typing import List
from products import Product, PercentageDiscount, BuyXGetYFree

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
        order_details = []
        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(f"Product {product.name} is inactive and cannot be ordered.")
            if product.get_quantity() < quantity:
                raise Exception(
                    f"Not enough quantity of {product.name} available. "
                    f"Requested: {quantity}, Available: {product.get_quantity()}")
            cost = product.buy(quantity)
            total_cost += cost
            if product.promotion:
                original_cost = product.price * quantity
                discount = original_cost - cost
                if isinstance(product.promotion, PercentageDiscount):
                    discount_percentage = product.promotion.discount_percentage * 100
                    order_details.append(
                        f"Bought {quantity} {product.name} for ${cost:.2f} (saved ${discount:.2f} with promotion \"{product.promotion.name} ({discount_percentage:.0f}%)\")")
                elif isinstance(product.promotion, BuyXGetYFree):
                    # Correct discount calculation for BuyXGetYFree
                    total_sets = quantity // (product.promotion.x + product.promotion.y)
                    remaining_items = quantity % (product.promotion.x + product.promotion.y)
                    free_items = total_sets * product.promotion.y
                    # Check if there are remaining items that qualify for free items.
                    if remaining_items >= product.promotion.x:
                        free_items += min(remaining_items // product.promotion.x, product.promotion.y)
                    discount = free_items * product.price
                    order_details.append(
                        f"Bought {quantity} {product.name} for ${cost:.2f} (saved ${discount:.2f} with promotion \"{product.promotion.name}\")")

                else:
                    order_details.append(
                        f"Bought {quantity} {product.name} for ${cost:.2f} (saved ${discount:.2f} with promotion \"{product.promotion.name}\")")
            else:
                order_details.append(f"Bought {quantity} {product.name} for ${cost:.2f}")

        print("Order placed successfully!")
        for detail in order_details:
            print(detail)
        print(f"Total cost: $ {total_cost:.2f}")
        return total_cost