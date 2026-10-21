from modules import items, income, input_utils, storage

#budget stores alle items and the income
#items is a list of dictionaries.
#example of an item: {"name": "Rent", "category": "Housing", "value": 1200, "interval": "m"}
budget = {
    "items": [],
    "income": None,
}

#The Main function
def main(message):
    option = input(f"""
        Welcome to the Budget Plan
        
        {message}

        1) Overview
        2) add position
        3) edit position
        4) delete position
        5) add or edit income
        6) export as pdf
        7) save
        8) exit
        """)

    match(option):
        case "1":
            print(1)
        case "2":
            items.addItem(budget)
            print(budget)
            main("""
            Position added
            What do you want to do?
            """)
        case "3":
            print(3)
        case "4":
            print(4)
        case "5":
            print(5)
        case "6":
            print(6)
        case "7":
            storage.saveBudgetToJson(budget)
            main("""
                Budget saved
                What do you want to do?
                """)
        case "8":   
            print("closing")
        case _:
            main("""
            Error - Invalid input
            What do you want to do?
            """)

#start of script
# budget gets loaded from file
# !!! TODO !!! check if file exists and is correct. Else some errors can happen     
budget = storage.loadBudgetFromJson()

#Start the main menu circle
main("What do you want to do?")

