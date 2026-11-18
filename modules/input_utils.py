#the input_utils.py contains all the input validation.

#input for all text inputs.
def askText(message):
   userInput =input(message).strip()
   if userInput == "":
        return askText(message)
   else: 
       return userInput

#input for all numeric values.
def askValue(message):
    while True:
        try:
            input_value = input(message)
            value = float(input_value)
            return value
        except ValueError:
            print("Error: Please enter a valid number (e.g., 1200 or 12.50).")
     

#input for all Yes / No questions.
def askWM(message):
    while True:
        answer = input(message)
        
        if answer.strip().lower() == "w":
            return "w"
        elif answer.strip().lower() == "m":
            return "m"
        else:
            print("Invalid input. Please enter 'm' for monthly or 'w' for hourly wage.")
    

#input for all Month / Year question.
def askMonthYear():
    while True:
        interval = input("Interval [m]onthly / [y]early: ").strip().lower()
        if interval in ["m", "y"]:
            return interval
        else: print("Invalid input. Please enter 'm' for monthly or 'y' for yearly.")