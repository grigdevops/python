student_scores = {
    "Henry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}
print(student_scores)

student_grades = {}

for student in student_scores:
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    elif 71 <= student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif 81 <= student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"

print(student_grades)

