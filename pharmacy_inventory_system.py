
# Task 2: Smart Pharmacy Inventory & Sales Management System

# Step 1: Display program title
print("==============================================")
print("   SMART PHARMACY INVENTORY & SALES SYSTEM")
print("==============================================")

# Step 2: Ask how many medicines need to be processed
total_medicines = int(input("How many different medicines do you want to process? "))

# Step 3: Initialize counters and accumulator
total_revenue = 0
restock_count = 0
processed_count = 0

# Step 4: Use a for loop to process each medicine
for i in range(1, total_medicines + 1):

    print("\n----------------------------------------------")
    print("Processing Medicine Number:", i)
    print("----------------------------------------------")

    # Step 5: Collect medicine information
    medicine_name = input("Enter Medicine Name: ")

    available_stock = int(input("Enter Available Stock: "))

    price = float(input("Enter Price Per Unit (Rs.): "))

    quantity_sold = int(input("Enter Quantity Sold: "))

    # Step 6: Validate medicine information
    if available_stock < 0 or price < 0 or quantity_sold < 0:

        print("\nInvalid Input! Negative values are not allowed.")

    else:

        # Count successfully processed medicine records
        processed_count = processed_count + 1

        # Step 7: Check whether requested quantity is available
        if quantity_sold <= available_stock:

            # Step 8: Calculate total sales amount
            sales_amount = quantity_sold * price

            # Step 9: Calculate remaining stock
            remaining_stock = available_stock - quantity_sold

            # Step 10: Add sales amount to total pharmacy revenue
            total_revenue = total_revenue + sales_amount

            # Step 11: Display medicine sales details
            print("\nMedicine Sales Details")
            print("Medicine Name:", medicine_name)
            print("Available Stock:", available_stock)
            print("Quantity Sold:", quantity_sold)
            print("Price Per Unit: Rs.", price)
            print("Total Sales Amount: Rs.", sales_amount)
            print("Remaining Stock:", remaining_stock)

            # Step 12: Check whether stock is low
            if remaining_stock < 10:

                print("WARNING: Low Stock! Restocking Required.")

                # Increase restocking counter
                restock_count = restock_count + 1

            else:
                print("Stock Status: Sufficient Stock")

        else:

            # Display message if stock is insufficient
            print("\nInsufficient Stock!")
            print("Medicine Name:", medicine_name)
            print("Available Stock:", available_stock)
            print("Requested Quantity:", quantity_sold)
            print("Sale could not be completed.")

# Step 13: Display final pharmacy report
print("\n==============================================")
print("          FINAL PHARMACY SALES REPORT")
print("==============================================")

print("Total Medicines Entered:", total_medicines)
print("Successfully Processed Medicines:", processed_count)
print("Total Pharmacy Revenue: Rs.", total_revenue)
print("Medicines Requiring Restocking:", restock_count)

print("----------------------------------------------")
print("        PHARMACY REPORT COMPLETED")
print("==============================================")
