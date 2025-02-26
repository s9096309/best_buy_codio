from store import Store
from products import Product, NonStockedProduct, LimitedProduct


def main():
    """
    Main function to initialize the store and display the menu-driven interface.
    """
    # Initialize the store with products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Open the store
    store = Store(product_list)

    # Start the menu-driven interface
    while True:
        print("""
Store Menu:
-----------

1. List all products in store
2. Show total amount in store
3. Place an order
4. Quit
""")
        try:
            ask_user = int(input("Please choose a number: "))

            if ask_user == 1:
                # List all products in store
                print("Products in store:")
                for product in store.get_all_products():
                    print(product.show())  # Show product details

            elif ask_user == 2:
                # Show total amount in store (total quantity)
                print(f"Total quantity in store: {store.get_total_quantity()}")

            elif ask_user == 3:
                # Make an order
                print("Making an order...")
                order_items = []

                # Display available products
                available_products = store.get_all_products()
                for index, product in enumerate(available_products, start=1):
                    print(f"{index}. {product.show()}")  # Display each product

                # Ask user to select products and quantities
                while True:
                    try:
                        product_num = int(
                            input(f"Choose a product number (1 to {len(available_products)}), or 0 to finish: ")
                        )
                        if product_num == 0:
                            break  # End the order
                        if 1 <= product_num <= len(available_products):
                            quantity = int(
                                input(f"How many of {available_products[product_num - 1].name} would you like to order? ")
                            )
                            product = available_products[product_num - 1]

                            # Check if the requested quantity exceeds available stock
                            if quantity > product.get_quantity():
                                print(
                                    f"Not enough {product.name} in stock. Only {product.get_quantity()} available."
                                )
                            else:
                                order_items.append((product, quantity))
                        else:
                            print("Invalid product number, try again.")
                    except ValueError:
                        print("Please enter a valid number.")

                if order_items:
                    # Process the order and display the total cost
                    try:
                        order_cost = store.order(order_items)
                        print(f"Order placed successfully! Total cost: $ {order_cost}")
                    except ValueError as e:
                        print(f"Error processing order: {e}")
                    except Exception as e:
                        print(f"Error processing order: {e}")
                else:
                    print("No items were selected for the order.")

            elif ask_user == 4:
                # Quit the program
                print("Thanks for your visit at Best Buy!")
                break

            else:
                print("Invalid choice. Please select a number between 1 and 4.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()