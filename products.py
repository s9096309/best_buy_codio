class Product:
    """
    A class representing a product in the store.
    """
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError(f"Not enough {self.name} in stock.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return quantity * self.price

class NonStockedProduct(Product):
    """
    A product that is not stocked (e.g., a license).
    """
    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)  # Quantity always 0

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, (Non-Stocked)"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        return quantity * self.price

class LimitedProduct(Product):
    """
    A product with a maximum purchase quantity.
    """
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of {self.name}.")
        return super().buy(quantity)