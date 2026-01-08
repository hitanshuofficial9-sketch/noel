str1=input("enter your string")
str2=""
punchuation="!,@,#,$,%,^,&,*,(,),"
for i in str1:
    if i not in punchuation:
      str2=str2+i.lower()
print(str2)
