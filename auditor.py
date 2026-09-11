inventory = 0
failed_entries = 0
while True:
    stock_value = input("Enter the stock quatity or 'quit' to finish: ")
    if stock_value.lower() == "quit":
        break
    elif not stock_value.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

    stock_value = int(stock_value)

    if stock_value < 0:
        print("Error: Negative numbers are not allowed.")
        failed_entries += 1
        continue

    inventory += stock_value
    print("Stock added. \nCurrent inventory:", inventory)

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break

print("\nInventory Report")
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)



