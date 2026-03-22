#!/bin/python
"""
Goal of program: Satisfy the requirements of Part 1 and Part 2 of Critical Thinking Assignment for Module 1 of CSC500
"""
#Version 1.0.0

def grab_inputs():
    try:
        #Collect Inputs
        num1 = int(input("INPUT desired number for num1: "))
        num2 = int(input("INPUT desired number for num2: "))

        return(num1,num2)
    except:
        print("INPUTS was not accepted, try again.")
        main()

#Part 1
def part_func(num1, num2):
    try:
        print(f"PART1: Numbers provides for num1: {num1} and num2: {num2}.")
        res1 = num1+num2    #Store Results of Addition
        res2 = num1-num2    #Store Results of Subtraction
        return(res1,res2)
    except:
        print("INPUTS was not accepted, try again.")
        main()

#Main
def main():
    try:
        num1, num2 = grab_inputs()
        res1, res2 = part_func(num1,num2)
        print(f"Results of Addition:            {res1}")
        print(f"Results of Subtraction:         {res2}")
    except:
        pass
main()
