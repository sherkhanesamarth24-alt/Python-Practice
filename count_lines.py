# Count Lines in a File

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))
