
from modules import input_utils

def addIncome(budget):



    if budget["income"] is None:
        userSalary = input("Please enter your monthly salary:")
        return 


    else:
        return budget ["income"]
    

awnser = input ("Do you want to edit your existing Salary? y/n:")
#only accepts numeric value
if awnser.lower()== "y":
    newSalary = input_utils.askValue("Please enter your new monthly salary") 

workLoad = input("What's your workload percentage? (e.g 80)")
if workLoad == input_utils:
    print("Your Salary is",newSalary, "and your workload is",workLoad,"%. Do you want to continue with these values?")
    #continue with y/n, 

while  workLoad != input_utils:
    print("Error: Please enter a valid number (e.g., 1200 or 12.50).")
    break