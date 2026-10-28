import json
import os

#saving the given dict into a json file in the projekt directory.
def saveBudgetToJson(budget):
    with open("budget.json", "w", encoding="utf-8") as file:
        json.dump(budget, file, indent=2, ensure_ascii=False)

#writiing the items and income from the json file to the given dict.
def loadBudgetFromJson(budget):
    try:
        with open("budget.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        #adding the data to the dict.
        budget["items"] = data["items"]
        budget["income"] = data["income"]

    #if the file does not exist. create the file and write the empty budget template in it.
    except FileNotFoundError:
        saveBudgetToJson(budget)
    #for every other error print "invalid json file".
    except Exception:

        #rename the invalid budget json.
        os.replace("budget.json", "invalid_budget.json")

        #create a new file with the empty budget template.
        saveBudgetToJson(budget)
