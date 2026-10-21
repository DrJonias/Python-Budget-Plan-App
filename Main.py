from modules import items, income, input_utils

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
        7) save & quit
        """)


    match(option):
        case "1":
            createOverview()
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
            print(7)
        case _:
            main("""
            Error - Invalid input
            What do you want to do?
            """)
               

main("What do you want to do?")

