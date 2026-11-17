import os
import pandas as pd
import matplotlib.pyplot as plt


def get_category(rating):
    if rating >= 4.5:
        return "Outstanding"
    elif rating >= 3.5:
        return "Good"
    elif rating >= 2.5:
        return "Average"
    else:
        return "Needs Improvement"


def load_employees():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "employees.csv")

    try:
        employees = pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: employees.csv was not found.")
        return pd.DataFrame()

    required_columns = ["Name", "Department", "Rating", "Projects"]

    for column in required_columns:
        if column not in employees.columns:
            print("Error: CSV file must contain Name, Department, Rating and Projects columns.")
            return pd.DataFrame()

    employees["Rating"] = pd.to_numeric(employees["Rating"], errors="coerce")
    employees["Projects"] = pd.to_numeric(employees["Projects"], errors="coerce")

    valid_rows = employees[
        employees["Name"].notna()
        & employees["Department"].notna()
        & employees["Rating"].between(1, 5)
        & employees["Projects"].notna()
        & (employees["Projects"] >= 0)
    ].copy()

    invalid_rows = employees[
        employees["Name"].isna()
        | employees["Department"].isna()
        | ~employees["Rating"].between(1, 5)
        | employees["Projects"].isna()
        | (employees["Projects"] < 0)
    ]

    for _, row in invalid_rows.iterrows():
        name = row["Name"] if pd.notna(row["Name"]) else "Unknown"
        rating = row["Rating"]

        if pd.notna(rating) and not 1 <= rating <= 5:
            print("Invalid rating {} for {}. Rating must be between 1 and 5. Row skipped.".format(rating, name))
        else:
            print("Invalid data for {}. Row skipped.".format(name))

    if valid_rows.empty:
        print("No valid employee records found.")
        return pd.DataFrame()

    valid_rows["Category"] = valid_rows["Rating"].apply(get_category)
    return valid_rows


def show_department_average(employees):
    averages = employees.groupby("Department")["Rating"].mean().sort_index()

    print("\nDepartment-wise Average Rating")
    for department, average in averages.items():
        print("{}: {:.2f}".format(department, average))

    averages.plot(kind="bar", title="Average Rating by Department", ylabel="Average Rating")
    plt.xlabel("Department")
    plt.tight_layout()
    plt.show()


def show_top_performer(employees):
    top_index = employees["Rating"].idxmax()
    top_employee = employees.loc[top_index]

    print("\nTop performer: {} ({}) | Rating: {:.1f} | Category: {}".format(
        top_employee["Name"],
        top_employee["Department"],
        top_employee["Rating"],
        top_employee["Category"]
    ))


def show_categories(employees):
    category_order = ["Outstanding", "Good", "Average", "Needs Improvement"]

    print("\nEmployee Performance Categories")
    for category in category_order:
        names = employees.loc[employees["Category"] == category, "Name"].tolist()
        if names:
            print("{}: {} ({})".format(category, len(names), ", ".join(names)))

    category_counts = employees["Category"].value_counts().reindex(category_order, fill_value=0)
    category_counts = category_counts[category_counts > 0]

    category_counts.plot(kind="pie", autopct="%1.1f%%", title="Employee Performance Categories")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


def show_projects_by_department(employees):
    project_totals = employees.groupby("Department")["Projects"].sum().sort_index()

    print("\nTotal Projects by Department")
    for department, total in project_totals.items():
        print("{}: {}".format(department, int(total)))

    project_totals.plot(kind="bar", title="Projects per Department", ylabel="Total Projects")
    plt.xlabel("Department")
    plt.tight_layout()
    plt.show()


def main():
    employees = load_employees()

    if employees.empty:
        return

    while True:
        print("\n===== Employee Performance Dashboard =====")
        print("1. Department-wise average rating")
        print("2. Top performer")
        print("3. Employee performance categories")
        print("4. Total projects per department")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_department_average(employees)
        elif choice == "2":
            show_top_performer(employees)
        elif choice == "3":
            show_categories(employees)
        elif choice == "4":
            show_projects_by_department(employees)
        elif choice == "5":
            print("Exiting Employee Performance Dashboard.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
