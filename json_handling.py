# JSON File Handling

import json

student = {
    "name": "Samarth",
    "course": "AIML",
    "skills": ["Python", "Machine Learning"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    data = json.load(file)

print("Student Name:", data["name"])
print("Course:", data["course"])
print("Skills:", data["skills"])
