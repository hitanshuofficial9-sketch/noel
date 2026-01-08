n = [1,0,2,-1] 
def index(i, n):
    return n.index(i)
sum1 = 0
sum2 = 0
temp = 0

for i in range(0, len(n)):
    # for left sum
    for j in range(0, i):
        sum1 = sum1+n[j]
    # for right sum
    for k in range(i+1, len(n)):
        sum2 = sum2+n[k]
    if sum1 == sum2:
        print(index(i, n)+1)
        temp = 1
        break
    sum1 = 0
    sum2 = 0

if temp == 0:
   print("null")