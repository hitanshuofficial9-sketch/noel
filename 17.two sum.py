nums=[1,7,6,1,2,0]
target=8
i=0
while i< len(nums):
    j=i
while j< len(nums):
    if nums[i]+ nums[j]== target:
        print(i,j)
        j=j+1
        i=i+1