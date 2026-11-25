# Expense Tracker

## Project Description
Expense Tracker is a simple Python-based application that helps users record and manage their daily expenses. It stores expense details such as date, category, and amount, and calculates total spending for each category.

## Features
- Add daily expenses.
- Store expenses using Python dictionaries.
- Validate expense dates.
- Validate expense amounts.
- Calculate total spending by category.
- Save expense records into a CSV file.
- Open the CSV file using Excel or other spreadsheet applications.

## Technologies Used
- Python 3
- CSV Module
- Datetime Module

## Project Structure

```text
Expense_Tracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

## How to Run the Project

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python expense_tracker.py
```

## Menu Options

1. Add Expense
2. Show Category Totals
3. Save Expenses
4. Exit

## Sample Input

| Date | Category | Amount |
|---|---|---:|
| 2026-11-23 | Food | 100 |
| 2026-11-23 | Travel | 50 |
| 2026-11-23 | Food | 200 |

## Sample Output

```text
Food : 300.0
Travel : 50.0
```

## Output File
The application generates an `expenses.csv` file containing all recorded expenses.

## Conclusion
This project helps users understand basic Python programming concepts such as functions, dictionaries, loops, conditional statements, file handling, CSV operations, and input validation.

## Author
Kishore Kumar R

**Project:** Expense Tracker  
**Language:** Python
