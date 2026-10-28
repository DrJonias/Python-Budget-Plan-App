def calculateRemainingBudget(budget: dict):

    if budget["income"] != None:
        totalExenses = 0
        for item in budget["items"]:
            totalExenses = totalExenses + int(item["value"])
        print(item["value"])    

        rest = budget["income"] - totalExenses
        print(rest)
    else: 
        print("no income given")


def showOverview(budget):
    print(f"{'Name':<15} {'Category':<12} {'Value':>10} {'Interval':<8}")
    print("-" * 48)

    for item in budget["items"]:
        print(f"{item['name']:<15} {item['category']:<12} {item['value']:>10.2f} {item['interval']:<8}")

def exportAsPDF(budget):
    print(budget)