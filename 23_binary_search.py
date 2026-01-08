l = [1,2,3,4,5,6,7,8]
target = 5
left = 0 
right = len(l)-1
while left <= right:
    mid = (left+right)//2
    if l[mid] == mid:
        