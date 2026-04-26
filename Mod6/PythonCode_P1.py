#!/bin/python
"""
Goal of program: Create an object called 'ItemToPurchase' for Module 4 Cart assignment for CSC500 Module 4.
"""
#Version 1.1.0

#Class for Part 1.
class ItemToPurchase:

    #DEFAULT CONSTRUCTER = ItemToPurchase("none", 0.00, 0)
    #DEFAULT CONSTRUCTER: Forces inputs to be (str, float, int)
    def __init__(self,
                 item_name:str = "none",
                 item_description:str = "none",
                 item_price:float = 0.00,
                 item_quantity:int = 0):
        self.item_name = item_name
        self.item_description = item_description #Added as part 
        self.item_price = round(item_price, 2)
        self.item_quantity = item_quantity
        self.hash = hash((self.item_name.upper(), self.item_description.upper))

    #print_item_cost Method: ItemToPurchase.print_item_cost will print ItemToPurchase("Bottled Watter", 1.00, 1) as "Bottled Water 10 @ $1 = $10".
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${round(self.item_price * self.item_quantity, 2):.2f}")

    #print_item_decsription Method: ItemToPurchase.print_item_description will print ItemToPurchase("Bottled Watter", "Quench your Thirst" 1.00, 1) as "Bottled Water: Quench your Thirst". 
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

        

#Class for Part 4
class ShoppingCart:

    #DEFAULT CONSTRUCTER = ShoppingCart("none", "January 1, 2020", [])
    #DEFAULT CONSTRUCTER: Forces inputs to be (str, str, list):
    def __init__(self,
                 customer_name:str = "none",
                 current_date:str = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    #add_item Method: ShoppingCart.add_item will add item to cart_items.  
    def add_item(self, item:ItemToPurchase) -> None:
        for ind in range(len(self.cart_items)):
            if self.cart_items[ind].hash == item.hash and self.cart_items[ind].item_price == item.item_price:
                self.cart_items[ind] += item.item_quantity
                return
        self.cart_items.append(item)
                    
    
    #remove_item Method: ShoppingCart.remove_item will remove an item in cart_items, by the item_name of the item.
    def remove_item(self, item_name:str) -> None:
        count_items = len(self.cart_items)
        if count_items:
            for ind in range(count_items):
                if self.cart_items[ind].item_name.upper() == item_name.upper():
                    del self.cart_items[ind]
                    return
            print(f"Item not found in cart. Nothing removed.")
        else:
            print(f"No items in {self.customer_name}'s cart.")
    
    #modify_item Method: ShoppingCart.modify_item modifies existing items in cart_items, by the item_name.
    def modify_item(self, item:ItemToPurchase) -> None:
        count_items = len(self.cart_items)

        if count_items:
            for ind in range(len(self.cart_items)):
                if self.cart_items[ind].item_name.upper() == item.item_name.upper():
                    if item.item_price != 0.0:
                        self.cart_items[ind].item_price = item.item_price
                    if item.item_quantity != 0:
                        self.cart_items[ind].item_quantity = item.item_quantity
                    return
            print("Item not found in cart. Nothing modified.")
        else:
            print("Cart is empty.")

    #get_num_items_in_cart Method: ShoppingCart.get_num_items_in_cart returns the number of items in the cart total, using the python built-in sum function.
    def get_num_items_in_cart(self) -> int:
        return sum(item.item_quantity for item in self.cart_items)
    
    #get_cost_of_cart Method: ShoppingCart.get_cost_of_cart returns the total cost by summing the (item.item_quantity * item.item_price)
    def get_cost_of_cart(self) -> float:
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    #print_total Method: ShoppingCart.print_total provides a read out of all the current items, their cost, and the total cost of all the items.
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        
        total_items = self.get_num_items_in_cart()  # <-- FIX HERE
        print(f"Number of Items: {total_items}")

        if total_items <= 0:
            print("SHOPPING CART IS EMPTY")
            return

        for item in self.cart_items:
            item.print_item_cost()

        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    #print_descriptions Method: ShoppingCart.print_descriptions prodiveds a read out of all the current items and their descriptions.
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()

    