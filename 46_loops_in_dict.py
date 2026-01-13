dict_student = {
    "name":"Om",
    "roll_no":12
}
for i in dict_student:
    print(f"{i}:{dict_student[i]}")
# for values
for i in dict_student.values():
    print(f"{i}")

for i,j in dict_student.items():
    print(i,j)