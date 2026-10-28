#the input_utils.py contains all the input validation.

#input for all text inputs.
def askText(message):
   userInput =input(message).strip()
   if userInput == "":
        return askText(message)
   else: 
       return userInput

#input for all numeric values.
def askValue():
    print("value")

#input for all Yes / No questions.
def askYesNo():
    print("yes / No")

#input for all Month / Year question.
def askMonthYear():
    print("M/Y")