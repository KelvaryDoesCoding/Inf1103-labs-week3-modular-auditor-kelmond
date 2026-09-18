#Variables
stock_quantity = 0 # Initialize stock to zero
failed_entries = 0 # Counter for failed entries

# Retrieve and validate input
def get_valid_input():
    failed_attempts = 0
    while True:
        stock_input = input("Please enter stock quantity: ") 
        if stock_input.lower() == "quit":
            return "quit", failed_attempts
        
      # Integer check
        try:
        # Convert stock_input to integer after "Quit" string has been checked
            stock_input = int(stock_input)
        except ValueError:
             print("\nError: Please enter a valid integer!")
             failed_attempts += 1    
             continue  
    
            # Negative value check
        if stock_input < 0:
            print("\nError: Please enter a positive integer!")
            # stock_quantity -= stock_input
            failed_attempts += 1
            continue

        return stock_input, failed_attempts
    
# Process delivery
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

# Calculate tax on this delivery
def calculate_tax(amount):
    tax = amount * 0.10
    return tax

# Final report summary
def generate_reports(total_units, failed_attempts):
    print("\n===== Final Report Summary =====")
    print(f"Total units processed: {total_units}")
    print(f"Total failed entries: {failed_attempts}")

# Stock Validation
while stock_quantity < 500:
    stock_input, new_failures = get_valid_input()

    failed_entries += new_failures

    # User exits program check
    if stock_input == "quit":
        break

    new_total = process_delivery(stock_quantity, stock_input)

    # Overstock check
    if new_total > 500:
        print("Alert: Inventory has exceeded 500 units!")
        break
    
    # Calculate tax on current delivery
    tax = calculate_tax(stock_input)

    # Update stock quantity
    stock_quantity = new_total

    print("\n===== Current Delivery Summary =====")

    # Plural form or Singular form validation
    if stock_input <= 1:
        print(f"Total delivery amount: {stock_input} unit")
    else:
        print(f"Total delivery amount: {stock_input} units")

    # Tax output for the current delivery
    print(f"Tax (10%) for this delivery: {tax:.2f}")

    # Plural form or Singular form validation
    if stock_quantity <= 1:
        print(f"Total inventory is {stock_quantity} unit")
    else:   
        print(f"Total inventory is {stock_quantity} units")

generate_reports(stock_quantity, failed_entries)