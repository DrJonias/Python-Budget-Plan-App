# Budget Planner

## About the Project

**Budget Planner** is a command-line application written in Python that helps users plan their personal finances. Users record their recurring expenses and, optionally, their income. The app then shows a clear monthly overview of where the money goes.

The project was developed as part of the *Programming Foundations* module in the BSc Business Information Technology programme at FHNW.

---

## Problem

Many young adults set up their own budget for the first time when they move out or start studying part-time alongside a job. They typically run into three problems:

1. **Costs are scattered.** Rent, health insurance, transport and fees are paid at different times and through different channels. Nobody has a single place where all fixed costs are listed together.
2. **Yearly costs are forgotten.** Bills like the Serafe fee or household insurance arrive once a year. Because they don't show up in the monthly bank statement, they are easily left out of the budget, and then they cause a surprise when they arrive.
3. **The key question remains unanswered.** Without an overview, it is hard to say whether an apartment is affordable or what workload percentage is needed to cover all costs.

Spreadsheets can solve this, but they require setting up formulas and structure first. Full finance apps are often too complex for a simple question and require linking bank accounts.

**Problem statement:** Students and young professionals planning their first independent budget lose track of scattered monthly and yearly fixed costs when moving out or working part-time, resulting in underestimated expenses, unexpected bills and uncertainty about whether they can afford their living situation.

**Project goals**
- **Effectiveness:** Users see all fixed costs in one place, with yearly costs included in the monthly view, so fewer costs are forgotten.
- **Efficiency:** Users can answer "Does my budget work with this income?" in a few minutes, without building a spreadsheet.

---

## Scenario

Lena is 21 and about to move into her first apartment in Basel. In September she starts a part-time degree and plans to work 60% alongside her studies. Before she signs the rental contract, she wants to know whether her budget will work.

1. Lena starts Budget Planner and adds her expected costs one after another: rent, utilities, health insurance, groceries and a public transport pass. She enters the Serafe fee and her household insurance as **yearly** items.
2. She opens the **overview** and sees all costs grouped by category, with yearly bills converted to monthly amounts. Housing makes up almost two thirds of her expenses.
3. She adds her income by entering her full-time salary and her **workload of 60%**. The app shows her remaining budget: it is negative, and a warning appears.
4. Lena changes her workload to 70%. Now the remaining budget is positive, with a small reserve.
5. She **exports the report** as a text file to discuss it with her parents before signing the contract.
6. She chooses **Save & exit**. A few weeks later she opens the app again, and her budget is loaded, so she can update the health insurance premium for the next year.

---

## User Roles

Budget Planner is a single-user application without login. We distinguish two roles:

| Role | Description | Interaction with the app |
| --- | --- | --- |
| **Budget Owner** (primary) | A person planning their own finances, typically a student or young professional moving out or working part-time. Has basic computer skills but no finance or spreadsheet expertise. | Uses the app directly: adds, edits and deletes items, sets income, views the overview and exports reports. |
| **Report Reader** (secondary) | A person the Budget Owner shares their budget with, for example parents, a partner or a financial advisor. | Does not use the app. Only reads the exported text report. |

---

## User Benefits

- **One place for all fixed costs:** Expenses are grouped by category, with a subtotal per category and a total.
- **No forgotten yearly bills:** Yearly costs are converted to monthly amounts, so they are part of the budget from the start.
- **Income is optional:** The app is useful with expenses alone. Once income is added, it shows the remaining budget and warns if it is negative.
- **Flexible income entry:** Income can be entered as a monthly salary, from a workload percentage or from an hourly wage.
- **Easy to share:** The overview can be exported as a text file and shared with people who don't use the app.
- **No setup needed:** No account, no bank connection, no spreadsheet formulas. Start the app and enter your costs.

---

## Project Requirements

| Requirement | How Budget Planner meets it | Where |
| --- | --- | --- |
| **Console interaction** | The app runs in the terminal with a numbered main menu. All data is entered with `input()`; all results are shown with `print()`. | All stories, S2 |
| **Input validation** | Every input is checked for type, range and format (e.g. positive amounts, workload 1–100, weekly hours 1–168, `m`/`y` interval, valid item numbers, `y`/`n` confirmations). Invalid input shows an error message and asks again; the program never crashes because of user input. | US1–US5, US9, S2 |
| **File processing** | The budget is **read** from and **written** to `budget.json`, including handling of missing and corrupted files. The overview is **written** to a dated `.txt` report. | US8, S1 |

---

## Calculations and Rounding

### Rules

| Calculation | Formula |
| --- | --- |
| Monthly amount of a yearly item | yearly amount ÷ 12 |
| Yearly amount of a Montly item | Monthly amount * 12 |
| Category subtotal | sum of the monthly amounts of all items in the category |
| Total expenses | sum of the monthly amounts of all items |
| Monthly salary from workload (US5) | full-time salary × workload ÷ 100 |
| Monthly salary from hourly wage (US9) | hourly wage × weekly hours × 4.33 (named constant `WEEKS_PER_MONTH`) |
| Remaining budget | monthly income − total expenses |
| Expenses as % of income | total expenses ÷ monthly income × 100 |

### Rounding and display

- All calculations use **unrounded values**. Rounding happens **only when displaying** values.
- Yearly items are stored with their yearly amount as entered and converted to a monthly amount only for calculations and display.
- **Amounts** are displayed in CHF with 2 decimals and an apostrophe as thousands separator, e.g. `2'507.92`.
- **Percentages** are displayed with 1 decimal, e.g. `89.6 %`.

### Reference example

All calculation examples in the acceptance criteria use this budget:

| Category / Item | Monthly | Yearly |
| --- | ---: | ---: |
| **Housing** | **1'600.00** | **19'200.00** |
| Rent | 1'450.00 | 17'400.00 |
| Utilities | 150.00 | 1'800.00 |
| **Food** | **400.00** | **4'800.00** |
| Groceries | 400.00 | 4'800.00 |
| **Insurance** | **400.00** | **4'800.00** |
| Health insurance | 380.00 | 4'560.00 |
| Household insurance | 20.00 | 240.00 |
| **Transport** | **80.00** | **960.00** |
| Public transport pass | 80.00 | 960.00 |
| **Fees** | **27.92** | **335.00** |
| Serafe | 27.92 | 335.00 |
| **Total** | **2'507.92** | **30'095.00** |

Note: Serafe is 335.00 ÷ 12 = 27.9166… per month. Totals are calculated from unrounded values and only rounded for display. The monthly total is therefore 30'095.00 ÷ 12 = 2'507.9166… → 2'507.92, not 2'507.92 × 12 = 30'095.04 for the yearly total.

---

## User Stories

The **agreed stories US1–US9** are the scope we commit to. Each team member is responsible for three of them (see Team Split). The **optional extensions US10–US11** are only implemented if time allows or as a replacement for an agreed story, which we would communicate to the lecturers first. **Supporting functionality** (saving, loading and menu navigation) is shared by the whole team and does not count towards the three stories per student.

### US1 – Add items
As a Budget Owner, I want to add budget items with name, amount, category and interval, one after another, so that I can record my expenses quickly.

**Acceptance criteria**
1. **Given** the main menu, **when** I choose "Add items" and enter `Rent`, `1450`, `Housing` and `m`, **then** the item is saved as Rent, 1450.00, Housing, monthly, and the message "Rent added." is shown.
2. **Given** the name prompt, **when** I enter nothing or only spaces, **then** "Name must not be empty." is shown and I am asked again.
3. **Given** the amount prompt, **when** I enter `abc`, `0` or `-50`, **then** "Please enter a positive number." is shown and I am asked again.
4. **Given** the amount prompt, **when** I enter `1450,50`, **then** "Please use a dot as decimal separator (e.g. 1450.50)." is shown and I am asked again.
5. **Given** the category prompt, **when** I press Enter without input, **then** the category is set to "Miscellaneous".
6. **Given** the category prompt, **when** I enter ` housing `, **then** the category is saved as "Housing" (trimmed, first letter capitalised), so it is grouped together with existing "Housing" items.
7. **Given** the interval prompt, **when** I enter `M` or ` y `, **then** the input is accepted (case-insensitive, spaces ignored); **when** I enter `monthly` or `x`, **then** "Please enter m or y." is shown and I am asked again.
8. **Given** an item was just added, **when** I answer `y` to "Add another item? (y/n)", **then** I can enter the next item; **when** I answer `n`, **then** I return to the main menu and see how many items were added (e.g. "2 items added."); **when** I enter anything else, **then** I am asked again.

### US2 – List and edit items
As a Budget Owner, I want to see all items as a numbered list and change an existing one, so that I keep an overview and can correct mistakes.

**Acceptance criteria**
1. **Given** a budget with 3 items, **when** I choose "Edit item", **then** all items are listed as 1–3 with name, amount in CHF, category and interval.
2. **Given** a budget without items, **when** I choose "Edit item", **then** "No items recorded yet." is shown and I return to the main menu.
3. **Given** a budget with 3 items, **when** I enter `0`, `4` or `abc` as item number, **then** "Please enter a number between 1 and 3." is shown and I am asked again.
4. **Given** the item number prompt, **when** I press Enter without input, **then** editing is cancelled and nothing is changed.
5. **Given** item 1 is Rent, CHF 1'450.00, **when** I press Enter for all fields except the amount and enter `1500`, **then** only the amount changes to CHF 1'500.00.
6. **Given** I am editing an item, **when** I enter an invalid value, **then** the same validation rules as in US1 apply.

### US3 – Delete an item
As a Budget Owner, I want to delete an item, so that my budget stays up to date.

**Acceptance criteria**
1. **Given** a budget with 3 items, **when** I select item 2 (Utilities) and confirm with `y`, **then** the item is deleted, "Utilities deleted." is shown and the remaining items are numbered 1–2.
2. **Given** I selected an item to delete, **when** I answer `n` to the confirmation, **then** nothing is deleted and "Deletion cancelled." is shown.
3. **Given** the confirmation prompt, **when** I enter anything other than `y` or `n`, **then** I am asked again.
4. **Given** a budget without items, **when** I choose "Delete item", **then** "No items to delete." is shown, no number is requested, and I return to the main menu.
5. **Given** a budget with 3 items, **when** I enter `0`, `4` or `abc`, **then** "Please enter a number between 1 and 3." is shown and I am asked again; **when** I press Enter without input, **then** I return to the main menu without deleting anything.

### US4 – Enter income as monthly salary
As a Budget Owner, I want to optionally enter my net monthly salary, so that I can see how much money I have left.

**Acceptance criteria**
1. **Given** no income is recorded, **when** I choose "Set income" → "Monthly salary" and enter `3500`, **then** the income is saved as 3500.00 and shown in the main menu header.
2. **Given** the salary prompt, **when** I enter `abc`, `0` or `-100`, **then** "Please enter a positive number." is shown and I am asked again.
3. **Given** an income is recorded, **when** I enter a new income in any mode (US4, US5 or US9), **then** the new value replaces the old one (it is not added to it).
4. **Given** an income is recorded, **when** I choose "Remove income" and confirm with `y`, **then** no income is recorded anymore and the overview no longer shows a remaining budget; **when** I answer `n`, **then** the income stays unchanged.

### US5 – Calculate income from workload percentage
As a Budget Owner working part-time, I want to enter my full-time (100%) salary and my workload percentage, so that I can compare different workloads.

**Acceptance criteria**
1. **Given** "Set income" → "Workload", **when** I enter a full-time salary of `4000` and a workload of `60`, **then** "Monthly salary: CHF 2'400.00" is shown and saved as income.
2. **Given** an income based on 60% workload, **when** I change the workload to `70`, **then** the income is recalculated to CHF 2'800.00.
3. **Given** the workload prompt, **when** I enter `1` or `100`, **then** the value is accepted (boundaries).
4. **Given** the workload prompt, **when** I enter `0`, `101`, `60.5` or `abc`, **then** "Please enter a whole number between 1 and 100." is shown and I am asked again.
5. **Given** the full-time salary prompt, **when** I enter an invalid value, **then** the same validation as in US4 applies.

### US6 – Budget overview by category
As a Budget Owner, I want to see my monthly expenses grouped by category, so that I know where my money goes.

**Acceptance criteria**
1. **Given** the reference budget, **when** I choose "Show overview", **then** the following overview is shown (amounts in CHF per month and year):

| Category / Item | Monthly | Yearly |
| --- | ---: | ---: |
| **Housing** | **1'600.00** | **19'200.00** |
| Rent | 1'450.00 | 17'400.00 |
| Utilities | 150.00 | 1'800.00 |
| **Food** | **400.00** | **4'800.00** |
| Groceries | 400.00 | 4'800.00 |
| **Insurance** | **400.00** | **4'800.00** |
| Health insurance | 380.00 | 4'560.00 |
| Household insurance | 20.00 | 240.00 |
| **Transport** | **80.00** | **960.00** |
| Public transport pass | 80.00 | 960.00 |
| **Fees** | **27.92** | **335.00** |
| Serafe | 27.92 | 335.00 |
| **Total** | **2'507.92** | **30'095.00** |

2. **Given** several categories, **then** they are sorted by subtotal, highest first; categories with the same subtotal (Food and Insurance, 400.00 each) are sorted alphabetically.
3. **Given** several items in one category, **then** they are also listed highest first and if same alphabetically.
4. **Given** a budget without items, **when** I choose "Show overview", **then** "No expenses recorded yet. Add items first." is shown instead of the overview, and no total is calculated.

### US7 – Calculate remaining budget
As a Budget Owner with recorded income, I want to see how much I have left after all expenses, so that I know whether my budget works.

**Acceptance criteria**
1. **Given** the reference budget and an income of CHF 2'800.00, **when** I open the overview, **then** below the total it shows a remaining budget of CHF 292.08 and expenses of 89.6 % of income.
2. **Given** the reference budget and an income of CHF 2'400.00, **then** the remaining budget is CHF −107.92 and the warning "Warning: your expenses exceed your income by CHF 107.92." is shown.
3. **Given** expenses exactly equal to the income, **then** the remaining budget is CHF 0.00 and the note "No reserve left." is shown instead of a warning.
4. **Given** an income of CHF 2'800.00 and no items, **then** No overview can be shown because of US6 AC4.
5. **Given** no income is recorded, **then** no remaining budget is calculated and "No income recorded. Set an income to see your remaining budget." is shown.

### US8 – Export report
As a Budget Owner, I want to save my overview as a text file, so that I can share it with a Report Reader.

**Acceptance criteria**
1. **Given** the reference budget on 14 October 2026, **when** I choose "Export report", **then** the file `budget_report_2026-10-14.txt` is created in the program folder and "Report saved as budget_report_2026-10-14.txt" is shown.
2. **Given** an exported report, **then** its content is identical to the overview from US6, plus the remaining budget from US7 if an income is recorded.
3. **Given** a report for today already exists, **when** I export again, **then** the file is overwritten and the message says so.
4. **Given** a budget without items, **when** I choose "Export report", **then** "Nothing to export. Add items first." is shown and no file is created.
5. **Given** the file cannot be written (e.g. missing permissions), **then** an error message is shown and the program continues running.

### US9 – Calculate income from hourly wage
As a Budget Owner paid by the hour, I want to enter my hourly wage and weekly hours, so that the program calculates my monthly salary.

**Acceptance criteria**
1. **Given** "Set income" → "Hourly wage", **when** I enter an hourly wage of `32.50` and `20` weekly hours, **then** "Monthly salary: CHF 2'814.50" is shown and saved as income.
2. **Given** the weekly hours prompt, **when** I enter `1`, `168` or `8.5`, **then** the value is accepted.
3. **Given** the weekly hours prompt, **when** I enter `0`, `169` or `abc`, **then** "Please enter a number between 1 and 168." is shown and I am asked again.
4. **Given** the hourly wage prompt, **when** I enter `abc`, `0`, `-5` or `32,50`, **then** the same validation as for amounts in US1 applies.
5. **Given** an income based on workload (US5), **when** I enter an hourly-wage income, **then** it replaces the previous income.

---

## Optional Extensions

Not part of the agreed scope. Only implemented if time allows or as an agreed replacement for a story.

### US10 – Add items from templates
As a Budget Owner, I want to pick typical items such as rent, health insurance or Serafe from a template list, so that I don't have to type them myself.

**Acceptance criteria**
1. **Given** a `templates.csv` with 5 templates, **when** I choose "Add from template", **then** the templates are listed as 1–5 and I can adjust the amount before adding.
2. **Given** `templates.csv` is missing or empty, **then** "No templates available." is shown and I return to the main menu.

### US11 – Compare workload scenarios
As a Budget Owner working part-time, I want to compare my budget at two different workloads, so that I see the minimum workload I need.

**Acceptance criteria**
1. **Given** the reference budget and a full-time salary of CHF 4'000.00, **when** I compare 60 % and 70 %, **then** remaining budgets of CHF −107.92 and CHF 292.08 are shown side by side.
2. **Given** the workload prompts, **then** the same validation as in US5 applies.

---

## Supporting Functionality (whole team)

Shared by all team members. Not counted as user stories.

### S1 – Save and load budget
The budget (items and income) is loaded from `budget.json` at start and written to it on "Save & exit".

**Acceptance criteria**
1. **Given** a valid `budget.json` with 7 items and an income, **when** I start the app, **then** all items and the income are loaded and "7 items loaded." is shown.
2. **Given** no `budget.json` exists, **when** I start the app, **then** it starts with an empty budget and shows "No saved budget found. Starting with an empty budget."
3. **Given** a corrupted `budget.json` (invalid JSON, a missing field, or an amount that is not a number), **when** I start the app, **then** it does not crash, shows "The budget file is damaged and could not be loaded. Starting with an empty budget." and leaves the file unchanged.
4. **Given** a corrupted file was detected at start, **when** I choose "Save & exit", **then** I am asked "Overwrite the damaged budget file? (y/n)"; with `y` the current budget is saved, with `n` the app exits without saving.
5. **Given** a budget with items and income, **when** I choose "Save & exit" and start the app again, **then** all items and the income are exactly the same as before.

### S2 – Main menu
The app is controlled through a numbered main menu that shows the number of items and the current income.

**Acceptance criteria**
1. **Given** the main menu, **when** I enter a valid option number, **then** the corresponding function starts and I return to the menu afterwards.
2. **Given** the main menu, **when** I enter `9`, `abc` or nothing, **then** "Please choose a valid option." is shown and the menu is displayed again.
3. **Given** the main menu, **when** I choose `0`, **then** the budget is saved (see S1) and the app exits.

---

## Team Split

| Student | User stories | Module |
| --- | --- | --- |
| Gaëtan Saucy | US1 – Add items, US2 – List and edit items, US3 – Delete an item | `items.py` |
| Melvin Orji | US4 – Monthly salary, US5 – Workload percentage, US9 – Hourly wage | `income.py` |
| Jonas Bachmann | US6 – Overview by category, US7 – Remaining budget, US8 – Export report | `report.py` |
| Whole team | S1 – Save and load, S2 – Main menu, shared validation helpers | `storage.py`, `main.py`, `input_utils.py` |

The main menu and the validation helpers are needed by everyone and are built first.