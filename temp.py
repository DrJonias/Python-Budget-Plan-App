case "5":
        
            
    answer = input("Hourly wage or fixed salary? h/f: ")

    if answer.lower() == "h":
        budget, userSalary, workLoad = income.addWage(budget)

    elif answer.lower() == "f":
        budget, userSalary, workLoad = income.addIncome(budget)
    
    else:
        print("Please enter h or f.")

            
            #Load existing budget
        budget = storage.loadBudgetFromJson(budget)

            #Add or edit income
        budget, newSalary, workLoad = income.addIncome(budget)

            #Calculate workload
        income.CalcWorkload(workLoad, newSalary)

            #Save updated budget
        storage.saveBudgetToJson(budget)
            