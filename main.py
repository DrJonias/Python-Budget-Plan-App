from modules import items, income, input_utils, storage

#budget stores all items and the income
#items is a list of dictionaries.
#example of an item: {"name": "Rent", "category": "Housing", "value": 1200, "interval": "m"}
budget = {
    "items": [],
    "income": None,
}

#The main menu cylce
def main(message):
    option = input(f"""
        Welcome to the Budget Plan
        
        {message}

        1) Overview
        2) add item
        3) edit item
        4) delete item
        5) add or edit income
        6) export as pdf
        7) save
        8) exit
        """)

    match(option):

        #show overview
        case "1":
            print(1)
            
        #add item
        case "2":
            items.addItem(budget)

            #restart the main menu cycle
            main("""
            Position added
            What do you want to do?
            """)

        #edit item 
        case "3":
            print(3)

        #delete item
        case "4":
            print(4)

        #add or edit income
        case "5":
            print(5)

        #export as pdf
        case "6":
            print(6)

        #save
        case "7":
            storage.saveBudgetToJson(budget)
            main("""
                Budget saved
                What do you want to do?
                """)

        #exit
        case "8":   
            print("closing")

        #every other input
        case _:
            #restart main menu cycle
            main("""
            Error - Invalid input
            What do you want to do?
            """)

#start of script
# budget gets loaded from file
storage.loadBudgetFromJson(budget)

#Start the main menu circle
main("What do you want to do?")

