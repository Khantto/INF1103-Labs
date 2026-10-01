
def load_inventory(filename="inventory.txt"):
    orders = []

    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) == 3:
                    order_id = int(parts[0])
                    product_name = parts[1]
                    quantity = int(parts[2])
                    orders.append((order_id, product_name, quantity))

    except FileNotFoundError:
        # If file doesn't exist, start with empty inventory
        pass

    return orders


def save_inventory(orders, filename="inventory.txt"):
    with open(filename, "w") as file:
        for order_id, product_name, quantity in orders:
            file.write(f"{order_id},{product_name},{quantity}\n")


def add_order(orders):
    product_name = input("\nEnter Product Name or 'quit': ")

    # Check for quit BEFORE asking for quantity
    if product_name.lower() == "quit":
        return "quit"

    quantity_input = input("Enter Quantity: ")

    # Validate that quantity is a non-negative integer
    if not quantity_input.isdigit():
        print("Error: Please enter a valid non-negative integer.")
        return None

    quantity = int(quantity_input)

    new_id = (max([order[0] for order in orders]) + 1) if orders else 1

    new_order = (new_id, product_name, quantity)
    orders.append(new_order)

    print("\nNew Order Added:")
    print(f"{new_id}, {product_name}, {quantity}")

    return orders


def display_orders(orders):
    print("\nCurrent Orders:")

    if not orders:
        print("(No orders yet)")
    else:
        for order_id, product_name, quantity in orders:
            print(f"{order_id}, {product_name}, {quantity}")


def main():
    orders = load_inventory()
    display_orders(orders)

    while True:
        result = add_order(orders)

        if result == "quit":
            break

    save_inventory(orders)
    print("\nOrders successfully saved to inventory.txt")

    display_orders(orders)


if __name__ == "__main__":
    main()