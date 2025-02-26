import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

best_buy = store.Store(product_list)

# Example usage (you can expand this):
for product in best_buy.get_all_products():
    print(product.show())

try:
    best_buy.order([(product_list[4], 2)]) #test limited product exception.
except Exception as e:
    print(e)