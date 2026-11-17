# Employee Performance Dashboard

**PS No.:** 66  
**Author:** Kanak Dixit
**ERP:** RU-26-00960

## About the Project

The Employee Performance Dashboard is a console-based Python application that analyses employee performance data stored in a CSV file.

It displays department-wise average ratings, identifies the top performer, groups employees by performance category, and calculates the total projects completed by each department. It also generates charts to make the results easier to understand.

## Features

- Reads employee records from `employees.csv` using Pandas.
- Checks employee ratings and skips invalid records with a message.
- Calculates department-wise average ratings.
- Finds the top-performing employee.
- Assigns a performance category to every valid employee.
- Counts employees in each performance category.
- Calculates the total projects for each department.
- Displays Matplotlib bar charts and a pie chart.

## Technologies Used

- Python 3
- Pandas
- Matplotlib

## Project Structure

```text
Employee-Performance-Dashboard/
│
├── main.py
├── employees.csv
├── requirements.txt
└── README.md
```

## Performance Categories

| Rating | Category |
|---|---|
| 4.5 or above | Outstanding |
| 3.5 to below 4.5 | Good |
| 2.5 to below 3.5 | Average |
| Below 2.5 | Needs Improvement |

## Installation

1. Install Python 3.
2. Open a terminal in the project folder.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command from the project folder:

```bash
python main.py
```

The dashboard will display a menu in the console. Enter the menu number to select an operation.

## CSV Format

The `employees.csv` file must contain these columns:

```csv
Name,Department,Rating,Projects
Amit,IT,4.5,8
Riya,IT,3.5,6
Neha,HR,4.0,5
Karan,HR,2.0,3
Sita,Sales,3.0,4
```

- `Name`: Employee name
- `Department`: Employee department
- `Rating`: Performance rating from 1 to 5
- `Projects`: Number of projects completed

Invalid ratings and incomplete or invalid records are skipped with a message.

## Menu Options

| Option | Operation |
|---|---|
| 1 | Department-wise average rating and bar chart |
| 2 | Display the top performer |
| 3 | Performance category counts and pie chart |
| 4 | Total projects per department and bar chart |
| 5 | Exit the program |

## Charts

The project uses Matplotlib to display:

1. **Average Rating by Department** – a bar chart showing the average employee rating in each department.
2. **Employee Performance Categories** – a pie chart showing the distribution of employees across performance categories.
3. **Projects per Department** – a bar chart showing the total projects completed by each department.

## Requirements

Only Pandas and Matplotlib are used as external Python libraries. Other modules are part of Python's standard library.
