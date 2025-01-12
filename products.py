class Product:
    """
    A class representing a product in the store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available quantity of the product in stock.
        active (bool): The status of the product (active or inactive).
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new product with the given name, price, and quantity.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product available in stock.

        Raises:
            ValueError: If the name is empty, price is less than 0, or quantity is less than 0.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product in stock.

        Returns:
            int: The current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Set the quantity of the product in stock.

        If the quantity reaches zero, the product will be deactivated.

        Args:
            quantity (int): The new quantity of the product.

        Raises:
            ValueError: If the quantity is less than 0.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Check if the product is active (in stock).

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activate the product (make it available for sale again).
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product (make it unavailable for sale).
        """
        self.active = False

    def show(self) -> str:
        """
        Get a string representation of the product, including its name, price, and quantity.

        Returns:
            str: A string representation of the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Purchase a given quantity of the product.

        If the quantity is greater than the available stock, an error is raised.

        Args:
            quantity (int): The number of units to buy.

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If the quantity is less than or equal to zero, or if there is not enough stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError(f"Not enough {self.name} in stock.")

        self.quantity -= quantity  # Deduct the quantity

        # Ensure the product only deactivates when quantity reaches exactly zero.
        if self.quantity == 0:
            self.deactivate()  # Only deactivate when quantity reaches zero

        return quantity * self.price  # Return total cost
