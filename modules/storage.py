import json

def saveBudgetToJson(budget):
    with open("budget.json", "w", encoding="utf-8") as file:
        json.dump(budget, file, indent=2, ensure_ascii=False)

def loadBudgetFromJson():
    with open("budget.json", "r", encoding="utf-8") as file:
        budget = json.load(file)
    return budget