str=input("Entre your string")
a=""
b=0
c=1
for i in str:
    a=a+(str[b:c])*2
    b=b+1
    c=c+1
print(a)    