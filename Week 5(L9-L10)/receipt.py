import csv
import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first row (column headers)
        for row in reader:
            
            product_number = row[key_column_index]
            product_name = row[key_column_index + 1]
            retail_price = row[key_column_index + 2]
            products_dict[product_number] = [product_number, product_name, float(retail_price)]
    return products_dict

def apply_discount(price, discount_percentage):
    discounted_price = price - (price * discount_percentage)
    return discounted_price

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)  # Assuming product number is in the first column

        # Print the store name
        print("Inkom Emporium")
        print()

        today = datetime.datetime.now().weekday()
        is_discount_day = today == 1 or today == 2

        # Read the ordered items
        ordered_items = []
        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first row (column headings)
            for row in reader:
                product_number, quantity = row
                product = products_dict.get(product_number)
                if product is None:
                    raise KeyError(f"Product number {product_number} not found in the products dictionary.")
                product_name = product[1]
                product_price = product[2]
                ordered_items.append((product_name, int(quantity), product_price))
                if is_discount_day:
                        product_price = apply_discount(product_price, 0.1)  # 10% discount
                        ordered_items.append((product_name, int(quantity), product_price))

        # Print the list of ordered items
        print("Requested Items")
        print()
        subtotal = 0
        total_quantity = 0
        for item in ordered_items:
            product_name, quantity, price = item
            subtotal += quantity * price
            total_quantity += quantity
            print(f"{product_name}: {quantity} @ {price}")

        # Print the number of ordered items
        print()
        print(f"Number of items: {total_quantity}")

        # Print the subtotal due
        print(f"Subtotal: ${subtotal:.2f}")

        # Compute and print the sales tax amount
        sales_tax_rate = 0.06  # 6%
        sales_tax_amount = subtotal * sales_tax_rate
        print(f"Sales Tax: ${sales_tax_amount:.2f}")

        # Compute and print the total amount due
        total_amount = subtotal + sales_tax_amount
        print(f"Total: ${total_amount:.2f}")

        # Print a thank you message
        print()
        print("Thank you for shopping at Inkom Emporium!")

        # Get the current date and time
        current_datetime = datetime.datetime.now()
        print(f"Date and Time: {current_datetime}")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied while accessing the file.")
    except KeyError as e:
        print(f"Error: Key not found in dictionary - {str(e)}")

if __name__ == '__main__':
    main()







