# Search Word in File

word = input("Enter word to search: ")

with open("student.txt", "r") as file:
    content = file.read()

if word.lower() in content.lower():
    print("Word found!")
else:
    print("Word not found!")
