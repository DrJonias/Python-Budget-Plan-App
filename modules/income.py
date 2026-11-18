
from modules import input_utils

#ask if hourly wage or fixed income
def addIncome(budget):
    answer = input_utils.askWM("is your income hourly (w) or monthly (m) calculated ")
      
    if answer.lower() == "w":
        addWage(budget)
      
    elif answer.lower() == "m":
        addMontly(budget)
    else:
        print("something went wrong, nothing happend")
      
#code for weekly wage
    
def addWage(budget):
    if budget["income"] is None:

        userSalary = input_utils.askValue("Please enter your hourly wage: ")
        budget["income"] = userSalary
        

    else:   
        userSalary = budget["income"]

#demand hours per week
    while True:
        workLoad = float(input("How many hours do you work per week? (For example: 50 )"))
                
        if workLoad < 0 or workLoad > 168:
            print("Error: Please enter a number between 0 and 168.")
                
        elif workLoad ==str:
            print("Error: Please enter a number between 0 and 168.")
        
                
        elif workLoad > 0 or workLoad <= 168:
            break
            
    budget["income"] = userSalary






#Check if salary exist / demand new
#ADDINCOME restrcit input
def addMontly(budget):

    if budget["income"] is None:
            userSalary = input_utils.askValue("Please enter your monthly salary: ")
            budget["income"] = userSalary
            
    else:   
        userSalary= budget["income"]

#Salary edit

    newSalary = budget["income"]
    while True:
        awnser = input ("Do you want to edit your existing Salary? y/n:")
        if awnser.lower() == "y":

            newSalary = input_utils.askValue("Please enter your new full-time salary:")
            break

        
        elif awnser.lower() == "n":
            break

        else :
            print("Error: Please enter y or n") 
#Workload Input 
    while True: 
    #WORKLOAD Restrict str (error, couldnt convert to float)
        workLoad = float(input("What's your workload percentage? (For example: 80)"))
        
        if workLoad < 0 or workLoad > 100:
            print("Error: Please enter a number between 0 and 100.")
        
        elif workLoad ==str:
            print("Error: Please enter a number between 0 and 100.")

        
        elif workLoad > 0 or workLoad <100:
            break
    
    budget["income"] = newSalary
    return budget, newSalary, workLoad
    
    
    #Calculation salary to workload to get 100% Salary
def CalcWorkload(workLoad,newSalary):

    workdLoad100 = workLoad / 100
    salary100 = newSalary / workdLoad100
        
    print("Your full-time salary (100%) is",salary100,)

    

    