# Student Performance Analytics System

## Project Overview

The Student Performance Analytics System is a Python-based project developed to analyze student academic performance using **Pandas and NumPy**.

The system reads student information from a CSV file, calculates total and average marks, assigns grades, checks pass/fail status based on marks and attendance, and provides different performance statistics.

It also performs subject-wise analysis and identifies the top-performing students.

## Objective

The main objective of this project is to build a simple student performance analysis system using Python concepts such as:

* Functions
* Loops
* Conditional statements
* Pandas
* NumPy
* Data analysis

The project helps convert raw student data into useful academic performance information.

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **CSV dataset**
* **VS Code** for development

## Dataset Description

The project uses a CSV file named `student.csv`.

The dataset contains **30 student records**.

### Important Columns

| Column      | Description                   |
| ----------- | ----------------------------- |
| Student_ID  | Unique ID of each student     |
| Name        | Student name                  |
| Department  | Student department            |
| Python      | Python marks                  |
| Mathematics | Mathematics marks             |
| DBMS        | DBMS marks                    |
| Statistics  | Statistics marks              |
| Attendance  | Student attendance percentage |

## Main Features

### 1. Total Marks

The system calculates the total marks obtained by each student across all four subjects.

### 2. Average Marks

The average marks of each student are calculated using the subject marks.

### 3. Grade Calculation

Grades are assigned according to the following rules:

| Average Marks | Grade |
| ------------: | :---: |
|  90 and above |   A+  |
|      80–89.99 |   A   |
|      70–79.99 |   B   |
|      60–69.99 |   C   |
|      50–59.99 |   D   |
|      Below 50 |   F   |

### 4. Pass/Fail Analysis

A student is considered **Pass** when:

* Average marks are at least 40
* Attendance is at least 75%

Otherwise, the student is marked as **Fail**.

### 5. Overall Performance Analysis

The system calculates:

* Class average
* Highest average
* Lowest average
* Top-performing student
* Lowest-performing student

### 6. Subject-wise Analysis

The system analyzes each subject and finds:

* Average marks
* Highest marks
* Lowest marks

The subjects analyzed are:

* Python
* Mathematics
* DBMS
* Statistics

### 7. Top 5 Performing Students

Students are sorted according to their average marks, and the top five performers are displayed.

## Project Structure


student-performance-analytics/
│
├── main.py
├── student.csv
└── README.md


## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install Required Libraries

Open the terminal and run:

```bash
pip install pandas numpy
```

### 3. Run the Project

Keep `main.py` and `student.csv` in the same folder.

Then run:

```bash
python main.py
```

The program will display the student performance analysis in the terminal.

## Sample Results

The current dataset contains 30 students.

Some of the results obtained are:

* **Class Average:** 77.06
* **Highest Average:** 94.00
* **Lowest Average:** 50.00
* **Pass Count:** 26
* **Fail Count:** 4
* **Pass Percentage:** 86.67%
* **Fail Percentage:** 13.33%

### Top Performer

**Aryan (STU023)** achieved the highest average of **94.00** and received an **A+ grade**.

### Best Subject by Class Average

**DBMS** had the highest class average at **77.30**.

## Learning Outcomes

Through this project, I practiced:

* Reading CSV data using Pandas
* Working with DataFrames
* Performing numerical calculations using NumPy
* Creating and using functions
* Using loops for repeated analysis
* Applying conditional statements
* Sorting and analyzing student data
* Generating meaningful results from raw data

## Conclusion

The Student Performance Analytics System successfully analyzes student academic data and provides useful information about individual and overall performance.

The project demonstrates the practical use of Python, Pandas, and NumPy for basic data analysis while applying fundamental programming concepts such as functions, loops, and conditions.





