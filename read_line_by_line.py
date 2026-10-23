# Read File Line by Line

with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.rstrip()}")
