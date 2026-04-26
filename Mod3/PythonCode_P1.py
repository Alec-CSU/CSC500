#!/bin/python
"""
Program objective: Determine the total cost of a meal which includes tipping 18 percent and a sales tax of 7 percent.
"""
#Version 1.0.0

#Input of Meal Cost
food_cost = float(input("Enter cost of Meal:: "))

#Buisness Calculations
tax_amount = food_cost * 0.07
tip_amount = food_cost * 0.18
total_cost = food_cost + tax_amount + tip_amount

#Print Section
print("Food Cost: \t$", round(food_cost, 2))
print("Tax (7%): \t$", round(tax_amount, 2))
print("Tip (18%): \t$", round(tip_amount, 2))
print("Total Cost: \t$", round(total_cost, 2))