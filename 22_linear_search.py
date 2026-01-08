def linearsearch(target, n):
   left=0
   right=len(n)-1
   while left<=right:
      mid=(left+right)//2
      if n[mid]==target:
         return mid
      elif n[mid]<target:
         left=mid+1
      else:
         right=mid-1
   return -1
    
n = [1,2,3,4,5,6,7,8]
target = 11
print(linearsearch(target, n))