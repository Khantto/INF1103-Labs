
from product import Product


class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")

        if self.search_product(product.get_product_id()) is not None:
            raise ValueError("Product ID already exists.")

        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 60)

        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products:
                product.display_information()
        print("-" * 60)

    def get_products(self):
        """Return a copy of the product list."""
        return self.__products.copy()

    def get_product_count(self):
        return len(self.__products)
