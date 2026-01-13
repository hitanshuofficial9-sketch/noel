dict_student = {
    "name":"Om",
    "roll_no":12
}
print(dict_student.get("name"))
print(dict_student.keys())
print(dict_student.values())
dict_student.update({"name":"Ravi"})
print(dict_student)
dict_student.pop("name") # removes the item with given key
dict_student.popitem() # remove last item
print(dict_student)

dict_student = {
    "name":"Om",
    "roll_no":12
}
del dict_student
try:
    print(dict_student)
except:
    print("dict_student doesn't exist")
# a = [1,2,3,4]
# del a
# try:
#     print(a)
# except:
#     print("a doesn't exist")
# del deletes any variable from memory

dict_student = {
    "name":"Om",
    "roll_no":12
}
dict_student.clear()
print(dict_student)

dict_student = {
    "name":"Om",
    "roll_no":12
}


