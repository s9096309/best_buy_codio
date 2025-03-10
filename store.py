from typing import List
from products import Product, PercentageDiscount, BuyXGetYFree, NonStockedProduct

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
        consolidated_order = {}  # Dictionary to consolidate quantities
        for product, quantity in shopping_list:
            if product in consolidated_order:
                consolidated_order[product] += quantity
            else:
                consolidated_order[product] = quantity

        for product, quantity in consolidated_order.items():
            if not product.is_active():
                raise Exception(f"Product {product.name} is inactive and cannot be ordered.")
            if not isinstance(product, NonStockedProduct) and product.get_quantity() < quantity:
                raise Exception(
                    f"Not enough quantity of {product.name} available. "
                    f"Requested: {quantity}, Available: {product.get_quantity()}")
            cost = product.buy(quantity)
            total_cost += cost
            if product.promotion:
                original_cost = product.price * quantity
                if isinstance(product.promotion, BuyXGetYFree):
                    total_sets = quantity // (product.promotion.x + product.promotion.y)
                    free_items = total_sets * product.promotion.y
                    remaining_items = quantity % (product.promotion.x + product.promotion.y)
                    if remaining_items >= product.promotion.x:
                        free_items += min(remaining_items // product.promotion.x, product.promotion.y)
                    discount = free_items * product.price
                else:
                    discount = original_cost - cost

                if isinstance(product.promotion, PercentageDiscount):
                    discount_percentage = product.promotion.discount_percentage * 100
                    order_details.append(
                        f"Bought {quantity} {product.name} for ${cost:.2f} (saved ${discount:.2f} with promotion \"{product.promotion.name} ({discount_percentage:.0f}%)\")")
                elif isinstance(product.promotion, BuyXGetYFree):
                    total_sets = quantity // (product.promotion.x + product.promotion.y)
                    free_items = total_sets * product.promotion.y
                    remaining_items = quantity % (product.promotion.x + product.promotion.y)
                    if remaining_items >= product.promotion.x:
                        free_items += min(remaining_items // product.promotion.x, product.promotion.y)
                    order_details.append(
                        f"Bought {quantity} {product.name}, got {free_items} for free. Saved ${discount:.2f} with promotion \"{product.promotion.name} (Buy {product.promotion.x} Get {product.promotion.y} Free)\"")

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