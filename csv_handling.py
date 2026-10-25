# CSV File Handling

import csv

students = [
    ["Name", "Age", "Course"],
    ["Samarth", 21, "AIML"],
    ["Rahul", 20, "CSE"],
    ["Amit", 22, "Data Science"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
