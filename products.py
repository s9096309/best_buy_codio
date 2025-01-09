class Product:
    def __init__(self, name=str, price=float, quantity=int):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input! Name cannot be empty, and price and quantity must be non-negative.")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if self.quantity <= 0:
            raise ValueError("Quantity is zero.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
            return self.active
    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(0))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()

mac.set_quantity(100000)
mac.show()