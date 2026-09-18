def get_valid_input():
    while True:
        stock_value = input("Enter the stock quatity or 'quit' to finish: ")
        if stock_value.lower() == "quit":
            return "quit"
        elif not stock_value.isdigit():
            print("Error: Please enter a valid integer.")
            return None

        stock_value = int(stock_value)

        if stock_value < 0:
            print("Error: Negative numbers are not allowed.")
            return None

        return stock_value

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("\nInventory Report")
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


inventory=0
failed_entries=0
total_deliveries=0

while True:
    stock_value =get_valid_input()

    if stock_value == "quit":
        break
    if stock_value is None:
        failed_entries +=1
        continue

    inventory =process_delivery(inventory,stock_value)

    tax =calculate_tax(stock_value)
    print("Tax for this delivery:", tax)
    print("Stock added.")
    print("Current Inventory:", inventory)

    total_deliveries+=1

    if inventory>500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break

generate_report(inventory,failed_entries)
print("Total Deliveries Processed:", total_deliveries)










    


