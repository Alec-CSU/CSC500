#!/bin/python
"""
Goal of program: Add menu for Module 6 'The ShoppingCart assignment'.
"""
#Version 1.0.0

import os
import time
from PythonCode_P1 import ItemToPurchase
from PythonCode_P1 import ShoppingCart


#clear_screen Method: Waits 2 seconds, then clears terminal.
def clear_screen():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

#print_menu Method: Handles all user interaction with ShoppingCart through a looping menu system until user quits.
def print_menu(cart: ShoppingCart):

    inp = ""

    while inp != "q":

        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        inp = input("Choose an option:\n").lower()

        #a Option: Collects item information, then adds to cart.
        if inp == "a":
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))

            cart.add_item(ItemToPurchase(item_name, item_description, item_price, item_quantity))
            clear_screen()

        #r Option: Removes item.
        elif inp == "r":
            print("\nREMOVE ITEM FROM CART")
            cart.remove_item(input("Enter name of item to remove:\n"))
            clear_screen()

        #c Option: Changes item quantity.
        elif inp == "c":
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            item_quantity = int(input("Enter the new quantity:\n"))

            cart.modify_item(ItemToPurchase(item_name=item_name, item_quantity=item_quantity))
            clear_screen()

        #i Option: Outputs item descriptions.
        elif inp == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            clear_screen()

        #o Option: Outputs full shopping cart.
        elif inp == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
            clear_screen()

        #q Option: Quits program.
        elif inp == "q":
            clear_screen()
            return

        #Invalid Option: Prompts again.
        else:
            print("Invalid option. Please choose a valid option.")
            clear_screen()


#MAIN: Initializes ShoppingCart object and ties user input and starts function print_menu.
def main():

    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)


main()