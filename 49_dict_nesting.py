dict_student = {
    "name":["Om","Ravi","Shyam"],
    "roll_no":[1,2,3]
}
print(dict_student["name"][1])
roll = [i for i in dict_student["roll_no"]]
for i in roll:
    print(i)
dict_student = {
    "name":["Om","Ravi","Shyam"],
    "roll_no":[1,2,3],
    "marks":[[10,20,30],[70,60,90],[40,50,90]]
}
for i in dict_student["marks"]:
    for j in i:
        print(j)
dict_school = {
    "class1":{
        "boys":{
            "roll_1":{
                "name":"Aman",
                "age":15
            },
            "roll_2":{
                "name":"Naman",
                "age":17
            },
        "girls":{
            "roll_3":{
                "name":"shurti",
                "age":16
            },
            "roll_4":{
                "name":"Riya",
                "age":16
            }
        }
        }
    }
}
