from modules import input_utils

def addItem(budget):
   
    name = input_utils.askText("what is the item called? ")
    category = input_utils.askText("what category do you want to add to? ")
    value = input_utils.askValue("what is the value of the item? ")

    while True:
        interval = input_utils.askMonthYear("Interval [m]onthly / [y]early: ").strip().lower()
        if interval in ["m", "y"]:
            break

    item = {"name": name, "category": category, "value": value, "interval": interval}
    budget["items"].append(item)
    print(f"Item '{name}' added successfully.")

def editItem(budget):
    if not budget["items"]:
        print("No items to edit.")
        return

    #list items with their index
    print("\n--- Current Items ---")
    for index, item in enumerate(budget["items"], start=1):
        print(f"{index}) {item['name']} - {item['category']} - {item['value']} - {item['interval']}")

    try:
        item_index = int(input("Enter the index of the item you want to edit: ")) - 1
        
        if 0 <= item_index < len(budget["items"]):
            current_item = budget["items"][item_index]
            print(f"Editing: {current_item['name']} (Press Enter to keep the current value)")
           
        else:
            print("Invalid item number.")
            return