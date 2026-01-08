# write a python program to insert squares of a numbers in a list upto the given range
n = int(input("Enter the range: "))
sol = [x**2 for x in range(n)]
print(sol)
def square():
    n = int(input("Enter the range: "))
    sol = [x**2 for x in range(n)]
    print(sol)
    return sol
square()