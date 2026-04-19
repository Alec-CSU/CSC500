#!/bin/python
"""
Program objective: Identify the number of points given by the CSU Global Bookstore book club within a month according to the amount of books bought.
"""
#Version 1.0.0

#Books Purchased
books_purchased = int(input("Enter the # of books purchased this month: "))

#Points Map
points_map = {
    0: 0,
    2: 5,
    4: 15,
    6: 30
}

#Points Awarded
points_awarded = 0
for key in points_map:
    if books_purchased >= key and points_awarded <= points_map[key]:
        points_awarded = points_map[key]

#Print Points Awarded
print("\tBooks Purchased: ", books_purchased)
print("\tPoints Awarded:  ", points_awarded)