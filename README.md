# Python Conditions and Loops Assessment

This project is an assignment submission covering basic logic building in Python using control structures, conditional branching, and iteration loops.

---

## Files in this Repository

### 1. `pharmacy_inventory_system.py`
This script manages stock tracking and order pricing for a basic pharmacy store logic.

* **What it does:**
  * Takes user inputs for medicine name, requested quantity, and base price per unit.
  * Checks stock levels to ensure the requested quantity is available before processing.
  * Calculates the total cost based on purchase quantity.
  * Applies volume discounts using `if-elif-else` conditions (e.g., bulk purchase discounts).
  * Warns the user when stock is running low so restock can be requested.

* **Python concepts used:**
  * `if / elif / else` for checking stock thresholds and price tiers.
  * Relational operators (`>=`, `<`, `==`) for condition checks.
  * Basic data types (`int`, `float`, `str`) and input conversion.

---

### 2. `student_scholarship_system.py.py`
This script determines student scholarship eligibility based on academic performance and attendance.

* **What it does:**
  * Takes inputs for student details including GPA, attendance percentage, and household income level.
  * Processes student records to evaluate eligibility criteria for different scholarship categories (Full, Partial, or None).
  * Uses loops to process multiple student records in a single run.
  * Outputs clear pass/fail status along with reasons if criteria are not met.

* **Python concepts used:**
  * Logical operators (`and`, `or`, `not`) to combine GPA and attendance rules.
  * `while` or `for` loops to handle continuous user prompts and iterative evaluation.
  * Input validation to make sure GPA and attendance values fall within expected numeric ranges.

---

## Requirements & Setup

* **Python Version:** Python 3.x required.
* **External Libraries:** None (standard Python library only).

---

## Execution Guide

Open a terminal inside the project directory and run whichever module you want to test:

```bash
# Run Pharmacy Inventory System
python pharmacy_inventory_system.py

# Run Student Scholarship Evaluation System
python student_scholarship_system.py.py
```

---

## Learning Objectives Addressed

1. Writing clear nested conditional blocks without redundant logical branches.
2. Managing loop control flow (`break`/`continue` or standard termination conditions).
3. Formatting terminal outputs cleanly for user interaction.