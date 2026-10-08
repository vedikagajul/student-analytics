
import pandas as pd
import numpy as np

# Load student data
df = pd.read_csv("student.csv")

# Subjects used for calculating marks
subjects = ["Python", "Mathematics", "DBMS", "Statistics"]

# Calculate total and average marks
df["Total_Marks"] = np.sum(df[subjects], axis=1)
df["Average_Marks"] = np.mean(df[subjects], axis=1)


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


df["Grade"] = df["Average_Marks"].apply(calculate_grade)


# Function to check pass or fail
def check_result(average, attendance):
    if average >= 40 and attendance >= 75:
        return "Pass"
    else:
        return "Fail"


df["Result"] = df.apply(
    lambda row: check_result(row["Average_Marks"], row["Attendance"]),
    axis=1
)


# Main heading
print("\n========================================")
print("     STUDENT PERFORMANCE ANALYTICS")
print("========================================")

print("\nTotal Students:", len(df))


# Overall performance
print("\n----------------------------------------")
print("Overall Performance")
print("----------------------------------------")

class_average = np.mean(df["Average_Marks"])
highest_average = np.max(df["Average_Marks"])
lowest_average = np.min(df["Average_Marks"])

print("Class Average:", round(class_average, 2))
print("Highest Average:", round(highest_average, 2))
print("Lowest Average:", round(lowest_average, 2))


# Top student
top_student = df.loc[df["Average_Marks"].idxmax()]

print("\nTop Student:")
print(top_student[["Student_ID", "Name", "Average_Marks"]])


# Lowest student
lowest_student = df.loc[df["Average_Marks"].idxmin()]

print("\nLowest Student:")
print(lowest_student[["Student_ID", "Name", "Average_Marks"]])


# Pass and Fail statistics
print("\n----------------------------------------")
print("Pass/Fail Statistics")
print("----------------------------------------")

pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

total_students = len(df)

pass_percentage = (pass_count / total_students) * 100
fail_percentage = (fail_count / total_students) * 100

print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("Pass Percentage:", round(pass_percentage, 2), "%")
print("Fail Percentage:", round(fail_percentage, 2), "%")


# Subject-wise performance
print("\n----------------------------------------")
print("Subject-wise Performance")
print("----------------------------------------")

for subject in subjects:
    average = np.mean(df[subject])
    highest = np.max(df[subject])
    lowest = np.min(df[subject])

    print("\n", subject)
    print("Average:", round(average, 2))
    print("Highest:", highest)
    print("Lowest:", lowest)


# Top 5 performing students
top_performers = df.sort_values(
    by="Average_Marks",
    ascending=False
).head(5).reset_index(drop=True)

print("\n----------------------------------------")
print("Top 5 Performing Students")
print("----------------------------------------")

print(
    top_performers[
        ["Student_ID", "Name", "Average_Marks", "Grade"]
    ]
)
