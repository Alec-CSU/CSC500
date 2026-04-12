#!/bin/python
"""
Goal of program: Create an object called 'ItemToPurchase' for Module 4 Cart assignment for CSC500 Module 4.
"""
#Version 1.0.0

#Class for Part 1.
class ItemToPurchase:

    #DEFAULT CONSTRUCTER = ItemToPurchase("none", 0.00, 0)
    #DEFAULT CONSTRUCTER: Forces inputs to be (str, float, int)
    def __init__(self,
                 item_name:str = "none",
                 item_price:float = 0.00,
                 item_quantity:int = 0):
        self.item_name = item_name
        self.item_price = round(item_price, 2)
        self.item_quantity = item_quantity

    #print_item_cost Method: ItemToPurchase.print_item_cost will print ItemToPurchase("Bottled Watter", 1.00, 1) as "Bottled Water 10 @ $1 = $10"
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${round(self.item_price * self.item_quantity, 2):.2f}")