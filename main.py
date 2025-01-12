from store import Store
from products import Product

def main():
    # Initialize the store with products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Open the store
    store = Store(product_list)


from store import Store
from products import Product


def main():
    # Initialize the store with products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Open the store
    store = Store(product_list)

    while True:
        print("""
Store Menu:
-----------

1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")
        try:
            ask_user = int(input("Please choose a number:"))

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
                for index, product in enumerate(store.get_all_products(), start=1):
                    print(f"{index}. {product.show()}")  # Display each product

                # Ask user to select products and quantities
                while True:
                    product_num = int(
                        input(f"Choose a product number (1 to {len(store.get_all_products())}), or 0 to finish: "))
                    if product_num == 0:
                        break  # End the order
                    if 1 <= product_num <= len(store.get_all_products()):
                        quantity = int(input(
                            f"How many of {store.get_all_products()[product_num - 1].name} would you like to order? "))
                        order_items.append((store.get_all_products()[product_num - 1], quantity))
                    else:
                        print("Invalid product number, try again.")

                if order_items:
                    # Process the order and display the total cost
                    order_cost = store.order(order_items)
                    print(f"Order placed successfully! Total cost: $ {order_cost}")
                else:
                    print("No items were selected for the order.")

            elif ask_user == 4:
                # Quit the program
                print("Thanks for your visit at Best Buy!")
                break

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
