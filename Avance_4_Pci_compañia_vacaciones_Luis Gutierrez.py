"""

This proyect aims to adress an issue regarding the system of human resources of a company.

Context:
The system does not take away nor adds the appropiate days of vacation from the employees.
According to the CEO, every employee has the right to two days of vacation per month and
three days of sick leave(not fixed, which could change depending on the medical diagnosis).

"""

# Menu
""""
Option 1 --> vacations section
    Number of vacations days left
    Take days off
        Subtracts the number of days selected by employee
        if the number selected is greater than the number of vacation days left
            choose less days
        else
            subtract the number of days slected from the total number of vacation days
            
Option 2 --> Sick Leave
    Number of sick leave days available
    Take sick leave days off
    Select the type if ilness
        options
            1) Cold
            2) Doctor appointment
            3) Covid
            4) Gastroenteritis
            5) Influenza
            6) Other
    Depending on the option chosen the system will calculate the number of sick leave days
    
Option 3 --> Comulative days
    Section which will store the number of days available for both sick leave and vacation days,
    So user can check how many days has more easily
    
Option 4 --> Exit
    
"""

# Variables 
#vacations_days = 2
#sick_leave_days = 3
cumulative_days = 0 

# //// Comulative days tab pending ////

def menu():
    print("")
    print("Welcome to the Menu")
   
    print("")

    print("For Vacations Section enter 1")
    print("For Sick Leave Section enter 2")
    
    print("")

    option_choice = int(input("Which Section do you want to enter? "))
    
    if option_choice == 1:
        vacation_days_calc()
    elif option_choice == 2:
        sick_leave_days() 
         
                     
def return_to_menu():
    print("")
    print("Enter 1 if you want to return to the main menu")
    print("Enter 0 if you do not want to return to the main menu")
    print("")
    return_menu = int(input("Do you want to go back to the main menu? "))
                      
    if return_menu == 1:
        menu()
    else:
        print("You are exiting...")

# This function aims to calculate the number of vacation days left when the user enters any amount
# It should check if the entered amount has is less than or equal to the available amount of days
def vacation_days_calc():
   
    vacations_days = 2
    # Ask the user(employee) how many days wants to take off
    desired_vacations_days = int(input("Enter the number of vacation day(s) you want to take: "))

    #If statement that will check if the user has enough days available and update the variable "vacation_days"
    if desired_vacations_days > vacations_days:
        print("")
        print("You don't have enough vacation days to take.")
    elif desired_vacations_days < 0:
        print("The vacation days cannot be lower than zero.")
    else:
        vacations_days = vacations_days - desired_vacations_days                                       
        print(" ") #Space in console(terminal) between the input and the outcome
        print( "Vacation day(s) left:")
        print(int(vacations_days))
        print("Day(s) witdrawn succesfully")
        
    return desired_vacations_days

#vacation_days_calc()

print(" ") #Space in console(terminal) between vacation days and sick leave days

# This function aims to calculate the number of vacation days left when the user enters any amount
# It should check if the entered amount has is less than or equal to the available amount of days
def sick_leave_days():
    
    sick_leave_days = 3
    # Ask the user(employee) how many days wants to take off
    desired_sick_leave_days = int(input("Enter the number of sick_leave_day(s) you want to take: "))

    #If statement that will check if the user has enough sick leave days available and update the variable "sick_leave_days"
    if desired_sick_leave_days > sick_leave_days:
        print("")
        print("You don't have enough sick leave days to take.")
    elif desired_sick_leave_days <= sick_leave_days:
        sick_leave_days = sick_leave_days - desired_sick_leave_days
        print(" ") #Space in console(terminal) between the input and the outcome
        print( "Sick leave day(s) left:")
        print(int(sick_leave_days))
        print("Day(s) witdrawn succesfully")

    return desired_sick_leave_days

#sick_leave_days()

menu()
return_to_menu()
print("End of the program")

# Disclaimer sick leave tab is under construction, for now it only calculates similarly to vacation days
"""
Note:
Fix
After some time of running over and over, if you enter more than the days available it ends the program.
It should ask again to return to the menu.
"""
