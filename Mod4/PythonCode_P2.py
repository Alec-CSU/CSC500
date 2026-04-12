#!/bin/python
"""
Goal of program: Use Part 1 object from Module 4 Cart assignment for CSC500 Module 4 Part 2.
"""
#Version 1.0.0

from PythonCode_P1 import ItemToPurchase as ITP

#Function for grabing user input for MAIN.
def grab_item_input(item_number:int):
    item_name, item_price, item_quantity = None, None, None
    try:
        print(f"Item {item_number}")
        item_name = input("\tEnter the item name:\n\t\t")
        item_price = float(input("\tEnter the item price:\n\t\t"))
        item_quantity = int(input("\tEnter the item quantity:\n\t\t"))
        return ITP(item_name, item_price, item_quantity)
    except:
        print(f"\n\t\tThe input you inputed: {item_name, item_price, item_quantity} was invalid, please try again. \n")
        return grab_item_input(item_number)

#MAIN program for Part 2.
def main():
    #Grabs 2 items
    items = list()
    for item_number in range(1,5): #Change the number to change how many items to collect
        item = grab_item_input(item_number)
        items.append(item)
    

    total_cost = float()
    for item in items:
        total_cost = round(item.item_price * item.item_quantity, 2) + total_cost

    print("TOTAL COST")
    for item in items:
        item.print_item_cost()
    print(f"\nTotal: ${total_cost:.2f}")

main()