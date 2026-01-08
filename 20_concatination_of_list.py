n = [1,2,1]
def concatination(n):
    return n*2
print(concatination(n))

l = [1,2,1]
r = []
for i in range(0,len(l)-1):
    for j in range(0,len(l)):
        r.append(l[j])

print(r)