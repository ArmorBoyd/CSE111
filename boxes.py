#Calls math module functions
import math

#Get user input
items = int(input("Enter the number of items: "))
items_box = int(input("Enter the number of items per box: "))
total_box = items / items_box 

total_box = math.ceil(total_box)

#Output
print(f"For {items} items, packing {items_box} in each box, you will need {total_box} boxes")
