#!/bin/python
"""
Program objective: Record rainfall data in nested loops over a given number of years and compute the total rainfall, total number of months and the average number of rainfall per month.
"""
#Version 1.0.0

#Num of Years
number_of_years = int(input("Enter the # of years:\t"))

#Rainfall Holding Vars
total_rainfall = 0.0
total_months = 0

#Outer Loop (Years)
for current_year in range(0, number_of_years):

    #Inner Loop (Months)
    for current_month in range(0, 12):
        monthly_rainfall = float(input(f"\tEnter rainfall for the Year {current_year + 1}, Month {current_month+1} in inches:\t"))
        total_rainfall = total_rainfall + monthly_rainfall
        total_months = total_months + 1

#Rainfall Calc
average_rainfall = total_rainfall / total_months

#Print Points Awarded
print("Num of Months:   ", total_months)
print("Total Rainfall:  ", round(total_rainfall, 2), "inches")
print("Average Rainfall:", round(average_rainfall, 2), "inches")