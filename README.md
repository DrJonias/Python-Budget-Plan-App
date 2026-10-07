# Budget Plan

## Description
For the Programming Foundations (BIT) module we need to write a Python terminal app.
We decided to create a budget planner: users record any number of budget items, optionally their income, and get a monthly overview. Data is stored in `budget.json`; reports are exported as `.txt`.

---

## User Stories

### US1 – Add items
As a user, I want to add budget items with name, amount, category and interval, one after another, so that I can record my expenses quickly.

**Acceptance criteria**
- Name must not be empty
- Amount must be a positive number; on invalid input the user is asked again
- Category is free text; empty input defaults to "Miscellaneous"
- Interval is `m` (monthly) or `y` (yearly); any other input is rejected
- After each item the program asks "Add another item? (y/n)"; there are no predefined items

### US2 – List and edit items
As a user, I want to see all items as a numbered list and change an existing one, so that I keep an overview and can correct mistakes.

**Acceptance criteria**
- Each line shows number, name, amount in CHF, category and interval
- If the list is empty, a message is shown instead of empty output
- Selection by number; invalid numbers are rejected
- Pressing Enter without input keeps the current value; new values are validated as in US1

### US3 – Delete an item
As a user, I want to delete an item, so that my budget stays up to date.

**Acceptance criteria**
- Selection by number; invalid numbers are rejected
- A confirmation (y/n) is required before deleting

### US4 – Enter income as monthly salary
As a user, I want to optionally enter my net monthly salary, so that I can see how much money I have left.

**Acceptance criteria**
- Accessible via the menu option "Set income"
- Amount must be a positive number
- Recorded income can be removed again

### US5 – Calculate income from workload percentage
As a part-time student, I want to enter my full-time (100%) salary and my workload percentage, so that I can compare different workloads.

**Acceptance criteria**
- Workload must be a whole number between 1 and 100
- Monthly salary = 100% salary × workload / 100
- The calculated monthly salary is shown for confirmation

### US6 – Monthly overview by category
As a user, I want to see my expenses per month and per category, so that I know where my money goes.

**Acceptance criteria**
- Yearly items are divided by 12 and counted as a monthly amount
- For each category, the sum and its share of total expenses in % are shown
- The monthly total of all expenses is shown at the end

### US7 – Calculate remaining budget
As a user with recorded income, I want to see how much I have left after all expenses, so that I know whether my budget works.

**Acceptance criteria**
- Only shown if income is recorded; otherwise a short message appears
- Remaining budget = monthly income − monthly expenses
- Expenses are also shown as % of income
- A clear warning appears if the remaining budget is negative

### US8 – Export report
As a user, I want to save my overview as a text file, so that I can print or share it.

**Acceptance criteria**
- File name contains the current date, e.g. `budget_report_2026-10-07.txt`
- Content matches US6, plus US7 if income is recorded
- The file name is shown after the export

### US9 – Save and load budget
As a user, I want my budget to be saved on exit and loaded on start, so that I don't have to enter everything again.

**Acceptance criteria**
- All items and the income are stored in `budget.json`
- If the file is missing, the program starts with an empty budget
- If the file is corrupted, a message appears and the program does not crash

---

## Optional Extensions
If time allows or as a replacement for a story.

### US10 – Calculate income from hourly wage
As a user paid by the hour, I want to enter my hourly wage and weekly hours, so that the program calculates my monthly salary.

**Acceptance criteria**
- Both values must be positive numbers; weekly hours at most 60
- Conversion: hourly wage × weekly hours × 4.33
- The calculated monthly salary is shown for confirmation

### US11 – Add items from templates
As a user, I want to pick typical items such as rent, health insurance or Serafe from a template list, so that I don't have to type them myself.

**Acceptance criteria**
- Templates are read from `templates.csv`
- The amount can be adjusted before adding
- If the file is missing, a message appears

### US12 – Compare workload scenarios
As a part-time student, I want to compare my budget at two different workloads, so that I see the minimum workload I need.

**Acceptance criteria**
- Enter two workload percentages; the remaining budget for both is shown side by side
- Validation as in US5

---

## Team Split

| Person | User stories | Modules |
| --- | --- | --- |
| A | US1, US2, US3 | `items.py`, `input_utils.py` |
| B | US4, US5, US9 | `income.py`, `storage.py` |
| C | US6, US7, US8 | `report.py` |

The main menu (`main.py`) and the validation helpers in `input_utils.py` are needed by everyone and are built first.