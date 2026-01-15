import json

file = open("students.json", "r", encoding="utf-8")
students = json.load(file)
file.close()

for s in students:
    grades = s["grades"]
    if len(grades) > 0:
        s["average"] = sum(grades) / len(grades)
    else:
        s["average"] = 0

file = open("students_with_avg.json", "w", encoding="utf-8")
json.dump(students, file, indent=4)
file.close()
