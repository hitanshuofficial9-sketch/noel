# Dictionary are mutable datatypes
marks = {
    "Maths":88,
    "English":97,
    "Physics":79,
    "Chemistry":92,
    "CS":99
}
print(marks)
marks["Maths"] = 89
print(marks)
if marks["Maths"] == 88:
    print("Marks in Maths is 88")
elif marks["Maths"] == 89:
    print("Marks in Maths is 89")
