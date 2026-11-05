
# Python Conditions & Loops Assessment

## Project Introduction

This project contains two beginner-level Python applications
developed as part of the Python Conditions and Loops Assessment.

The project demonstrates the use of conditional statements,
loop structures, input validation, counters, and accumulators.

## Task 1: Student Scholarship Eligibility System

This program evaluates students' eligibility for university
scholarships based on three conditions:

- Academic marks must be at least 80%.
- Attendance must be at least 85%.
- Monthly family income must be Rs. 50,000 or less.

### Scholarship Categories

- 90% or above marks: Full Scholarship.
- 80% to 89% marks: Partial Scholarship.
- Students who do not meet the eligibility conditions
  receive an ineligibility report with reasons.

### Python Concepts Used

- if, elif, and else statements
- Comparison operators
- Logical operators
- User input
- Type conversion
- Input validation
- Formatted output

## Task 2: Smart Pharmacy Inventory & Sales Management System

This program manages medicine inventory and calculates
daily pharmacy sales revenue.

The application:

- Processes multiple medicines using a for loop.
- Collects medicine names, stock, prices, and quantities sold.
- Checks medicine stock availability.
- Calculates sales amounts.
- Updates remaining stock.
- Displays low-stock warnings.
- Calculates total pharmacy revenue.
- Counts medicines requiring restocking.

### Python Concepts Used

- for loop
- range()
- Conditional statements
- Counters
- Accumulators
- Arithmetic operators
- User input
- Type conversion

## Project Structure

python-conditions-loops-assessment/
|
|-- student_scholarship_system.py
|-- pharmacy_inventory_system.py
|-- README.md

## Requirements

- Python 3 installed
- Visual Studio Code or any Python-supported editor

## How to Run the Programs

### Run Task 1

Open the terminal and execute:

```bash
python student_scholarship_system.py
```

### Run Task 2

Open the terminal and execute:

```bash
python pharmacy_inventory_system.py
```

## Sample Input and Output

### Task 1: Scholarship System

Sample Input:

```text
Student Name: Ali
Academic Marks: 95
Attendance: 90
Monthly Family Income: 40000
```

Sample Output:

```text
Eligibility Status: Eligible
Scholarship Award: Full Scholarship
```

### Task 2: Pharmacy System

Sample Input:

```text
Number of Medicines: 1
Medicine Name: Panadol
Available Stock: 50
Price Per Unit: 20
Quantity Sold: 45
```

Sample Output:

```text
Total Sales Amount: Rs. 900
Remaining Stock: 5
WARNING: Low Stock!
Total Pharmacy Revenue: Rs. 900
Medicines Requiring Restocking: 1
```

## Conclusion

This project demonstrates practical applications of
Python conditional statements and loop structures.

Both applications help develop fundamental programming
skills through simple real-world scenarios.
