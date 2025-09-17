import json
import os

text = input("Enter name and grades: ")

students = []
for student in text.split(','):
    name, gpa = student.strip().split()
    gpa = float(gpa)
    students.append('name': name, 'grade': gpa)
print(students)

with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

