
from modules import input_utils

def addIncome(budget):



    if budget["income"] is None:
        userSalary = input("Please enter your monthly salary:")
        return 


    else:
        return budget ["income"]
    
while True:
    awnser = input ("Do you want to edit your existing Salary? y/n:")
    if awnser.lower() == "y":

         newSalary = input_utils.askValue("Please enter your new full-time salary:")
         break
    
    elif awnser.lower() == "n":
         break

    else :print("Error: Please enter y or n")


#Workload

while True: 
    workLoad = float(input("What's your workload percentage? (For example: 80)"))
    
    if workLoad < 0 or workLoad > 100:
        print("Error: Please enter a number between 0 and 100.")
    
    elif workLoad > 0 or workLoad <100
    
    #Calculation salary to workload to get 100% Salary
    