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

    # Display total quantity of all products
    print(f"Total quantity in store: {store.get_total_quantity()}")

    # Place an initial test order
    try:
        initial_order_cost = store.order([
            (store.get_all_products()[0], 1),  # Order 1 MacBook Air M2
            (store.get_all_products()[1], 2),  # Order 2 Bose QuietComfort Earbuds
        ])
        print(f"Initial order placed successfully! Total cost: {initial_order_cost}")
    except Exception as e:
        print(f"Error placing initial order: {e}")

    # Get active products
    active_products = store.get_all_products()

    # Display active products
    print("\nAvailable Products:")
    for product in active_products:
        print(product.show())

    # Place another order
    try:
        order_cost = store.order([
            (active_products[0], 1),  # "MacBook Air M2" x 1
            (active_products[1], 2),  # "Bose QuietComfort Earbuds" x 2
        ])
        print(f"\nOrder placed successfully! Total cost: {order_cost}")
    except Exception as e:
        print(f"\nError placing order: {e}")

    # Print updated product quantities
    print("\nUpdated Products:")
    for product in store.get_all_products():
        print(product.show())

if __name__ == "__main__":
    main()
