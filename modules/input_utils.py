#the input_utils.py contains all the input validation.

#input for all text inputs.
def askText():
    print("text")

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
def askYesNo():
    print("yes / No")

#input for all Month / Year question.
def askMonthYear():
    print("M/Y")