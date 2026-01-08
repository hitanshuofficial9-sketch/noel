l=[3,2,2,1]
n=len(l)
for i in range(n-1):
    swap=False
    for j in range(0,n-i-1):
        if l[j]> l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
            swap=True
        if swap==False:
                print("list is sorted")
        print(l)