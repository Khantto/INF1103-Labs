
import json
import os

from product import Product
from inventory import Inventory

FILE_NAME = "inventory.json"


def load_inventory():
    """Load product objects and transaction history from JSON."""
    inventory = Inventory()
    history = []

    if not os.path.exists(FILE_NAME):
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return inventory, history

    print("inventory.json found.")

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Support the original Lab 5 format: a list of products.
        if isinstance(data, list):
            data = {
                "products": data,
                "transaction_history": []
            }

        if not isinstance(data, dict):
            raise ValueError("Invalid inventory format.")

        products = data.get("products", [])
        history = data.get("transaction_history", [])

        if not isinstance(products, list):
            raise ValueError("Products must be a list.")

        if not isinstance(history, list):
            raise ValueError("Transaction history must be a list.")

        for item in products:
            if not isinstance(item, dict):
                raise ValueError("Invalid product entry.")

            product = Product(
                item["id"],
                item["name"],
                float(item["price"]),
                int(item["stock"])
            )

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
        print("Could not load inventory:", error)
        print("Starting with an empty inventory.")
        return Inventory(), []

    return inventory, history


def save_inventory(inventory, history):
    """Save product data and transaction history to JSON."""
    data = {
        "products": [
            product.to_dict()
            for product in inventory.get_products()
        ],
        "transaction_history": history
    }

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    except OSError as error:
        print("Error saving inventory:", error)


def add_product(inventory, history):
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("Product ID cannot be empty.")
        return

    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return

    name = input("Product Name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

    except ValueError:
        print("Invalid input. Enter a valid price and integer stock.")
        return

    product = Product(product_id, name, price, stock)

    try:
        inventory.add_product(product)
    except ValueError as error:
        print(error)
        return

    history.append({
        "action": "ADD",
        "product_id": product_id,
        "quantity_change": stock,
        "details": f"Added {name} with initial stock {stock}"
    })

    print("Product added successfully!")


def update_stock(inventory, history):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print("Name:", product.get_name())
    print("Current Stock:", product.get_stock())

    try:
        new_stock = int(input("New Stock Quantity: "))

        if new_stock < 0:
            print("Stock cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid integer.")
        return

    old_stock = product.get_stock()
    change = new_stock - old_stock

    product.update_stock(new_stock)

    history.append({
        "action": "UPDATE_STOCK",
        "product_id": product_id,
        "old_stock": old_stock,
        "new_stock": new_stock,
        "quantity_change": change
    })

    print("Stock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip().upper()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
    else:
        print("Product Found")
        print("-" * 40)
        product.display_information()
        print("-" * 40)


def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory, history = load_inventory()

    while True:
        show_menu()
        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()

        elif option == "2":
            add_product(inventory, history)

        elif option == "3":
            update_stock(inventory, history)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory, history)

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory, history)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please enter 1 to 6.")


if __name__ == "__main__":
    main()
