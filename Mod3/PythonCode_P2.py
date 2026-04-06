#!/bin/python
"""
Program objective: Find out the time an alarm stops with a 24-hour clock, time and number of hours to wait.
"""
#Version 1.0.0

#Input of Current and Wait Time
current_time = int(input("Enter current time in Hours:: \t\t"))
wait_time = int(input("Enter time till the alarm goes off:: \t"))

#Alarm Calculations
alarm_time = (current_time + wait_time) % 24

#Print Section
print("Current Time: \t", f"{current_time:02d}:00")
print("Wait Time: \t", wait_time, "hours")
print("Alarm Time: \t", f"{alarm_time:02d}:00")