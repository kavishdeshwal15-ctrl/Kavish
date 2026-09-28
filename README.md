# Personal Expense Tracker

A simple command-line tool to record, view, and manage daily expenses. Built as a first-semester Python project.

**Note:** This is an in-memory application. Expenses tracked during the session will clear when the program is closed (file persistence involves concepts outside the current scope).

## Requirements
- Python 3.x
- A terminal or command prompt

To check your Python version, open a terminal and run:
`python --version` (or `python3 --version`)

## Setup and Run Instructions

1. Download or clone this repository so you have `expense_tracker.py` in a folder.
2. Open a terminal and navigate to that folder:
   ```bash
   cd path/to/your/folder
   ```
3. Run the program:
   ```bash
   python expense_tracker.py
   ```
   *(On macOS/Linux, you might need to use `python3 expense_tracker.py`)*

## Features Menu
1. **Add expense:** Enter the amount, category, and date. The program assigns a unique ID.
2. **View all:** Displays all added expenses along with a running total.
3. **View by category:** Shows available categories and lets you filter expenses accordingly.
4. **Summary:** Shows your total spent, a category-wise breakdown, and your single highest expense.
5. **Delete:** Enter an ID to remove an inputted expense.
6. **Quit:** Exits the application.

## Project Structure
```text
your-folder/
    ├── expense_tracker.py   <- The active Python script
    └── README.md            <- Instructions and details
```