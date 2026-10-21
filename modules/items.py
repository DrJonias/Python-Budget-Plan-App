def addItem(budget):
   
    name = input("what is the item called? ")
    category = input("what category do you want to add to? ")
    value = input("what value does the item have? ")
    
    while True:
        interval = input("Interval [m]onthly / [y]early: ").strip().lower()
        if interval in ["m", "y"]:
            break


    item = {"name": name, "category": category, "value": value, "interval": interval}
    budget["items"].append(item)


