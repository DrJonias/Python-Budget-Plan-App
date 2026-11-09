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

#prints the overview
#Name is at least 15 character wide and left bound.
#Category is at least 12 characters wide and left bound.
#Value is at least 10 characters wiede and right bound.
#Interval is at least 8 character wide and right bound.
def showOverview(budget):
    line = "+" + "-" * 17 + "+" + "-" * 14 + "+" + "-" * 12 + "+" + "-" * 10 + "+"

    print(line)
    print(f"| {'Name':<15} | {'Category':<12} | {'Value':>10} | {'Interval':<8} |")
    print(line)

    for item in budget["items"]:
        print(f"| {item['name']:<15} | {item['category']:<12} | {item['value']:>10.2f} | {item['interval']:<8} |")

    print(line)

def exportAsPDF(budget):
    print(budget)