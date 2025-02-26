from abc import ABC, abstractmethod

class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """Applies the promotion and returns the discounted price."""
        pass

class PercentageDiscount(Promotion):
    """Applies a percentage discount to the product price."""

    def __init__(self, name: str, discount_percentage: float):
        super().__init__(name)
        self.discount_percentage = discount_percentage / 100.0

    def apply_promotion(self, product, quantity: int) -> float:
        return product.price * quantity * (1 - self.discount_percentage)

class SecondHalfPrice(Promotion):
    """Applies a 'second item at half price' promotion."""

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        full_price_items = quantity // 2
        half_price_items = quantity % 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)

class BuyXGetYFree(Promotion):
    """Applies a 'buy X get Y free' promotion."""

    def __init__(self, name: str, x: int, y: int):
        super().__init__(name)
        self.x = x
        self.y = y

    def apply_promotion(self, product, quantity: int) -> float:
        free_items = (quantity // (self.x + self.y)) * self.y
        paid_items = quantity - free_items
        return paid_items * product.price

class Product:
    """A class representing a product in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Add promotion attribute

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
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError(f"Not enough {self.name} in stock.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return quantity * self.price

    def set_promotion(self, promotion: Promotion):
        self.promotion = promotion

    def get_promotion(self) -> Promotion:
        return self.promotion

class NonStockedProduct(Product):
    """A product that is not stocked (e.g., a license)."""
    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)  # Quantity always 0

    def show(self) -> str:
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, (Non-Stocked){promotion_info}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return quantity * self.price

class LimitedProduct(Product):
    """A product with a maximum purchase quantity.
    """
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}{promotion_info}"

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of {self.name}.")
        return super().buy(quantity)