#!/bin/python
"""
Goal of program: Develop dictionaries with course room numbers, course instructors, and course meeting times. To meet Module 6 Requirements, the program will require the user to provide a course number, and will subsequently show the corresponding course information.
"""
#Version 1.0.0


#Stores Room Numbers of Course
COURSE_ROOMS = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}


#Stores Instructors per Course
COURSE_INSTRUCTORS = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}


#Stores Times of Courses
COURSE_TIMES = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}


#MAIN
def main():

    #User Input
    user_course = input("Enter a course number: ").upper()

    #Course Lookup
    if user_course in COURSE_ROOMS:

        #Output
        print()
        print("COURSE INFO")
        print("=" * 80)
        print(f"{'Course Number':<20}{'Instructor':<20}{'Meeting Time':<20}{'Room Number':<20}")
        print("-" * 80)
        print(f"{user_course:<20}{COURSE_INSTRUCTORS[user_course]:<20}{COURSE_TIMES[user_course]:<20}{COURSE_ROOMS[user_course]:<20}")

    else:

        #Invalid Input
        print()
        print("COURSE NOT FOUND")
        print(f"{user_course} is not listed as a valid course number.")


#MAIN
if __name__ == "__main__":
    main()