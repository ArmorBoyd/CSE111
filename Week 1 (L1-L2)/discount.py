#To get the date and time I need to use the datetime library
import datetime

#Get the current day of the week and convert it into string using strftime()
today = datetime.datetime.now().strftime("%A")

#Get the user input
subtotal = float(input("Please enter the subtotal: "))

#Check if the subtotal is >= 50 and if the the day is either monday or tuesday. 

if subtotal >= 50 and (today == "Tuesday" or today == "Wednesday"):
    #calculate the discount amount
    discount = subtotal * .10
    print(f"Discount amount: {round(discount, 2)}")
else:
    discount = 0

#Calculate the sales tax amount
tax = subtotal * .06
# If the day is either monday or tueday, make sure to subtract the calculate the tax after deducting the discount from the subtotal
if today == "Tuesday" or today == "Wednesday":
    tax = (subtotal - discount) * .06
print(f"sales tax amount: {round(tax, 2)}")

#calculate and print the total amount
total = subtotal + tax - discount
print(f"Total: {round(total,2)}")

