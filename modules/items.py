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

            name = input(f"New name [{current_item['name']}]: ") or current_item['name']
            category = input(f"New category [{current_item['category']}]: ") or current_item['category']
            
            val_input = input(f"New value [{current_item['value']}]: ")
            value = float(val_input) if val_input else current_item['value']

            while True:
                interval_input = input(f"New interval [m/y] [{current_item['interval']}]: ").strip().lower()
                if not interval_input:
                    interval = current_item['interval']
                    break
                elif interval_input in ["m", "y"]:
                    interval = interval_input
                    break
                print("Invalid input. Please enter 'm' or 'y'.")

            # Update the item
            budget["items"][item_index] = {
                "name": name,
                "category": category,
                "value": value,
                "interval": interval
            }
            print("Item updated successfully!")
        else:
            print("Error: Invalid item index.")
            
    except ValueError:
        print("Error: Please enter a valid number.")
        