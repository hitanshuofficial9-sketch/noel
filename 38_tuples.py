print((1,2,3))
x = (1,2,3,4,5)
# Tuples are are immutable
print(x)
print(x[2])
# tuple[0] = 0 - doesnt work Traceback (most recent call last):
#  File "c:\Users\student\Desktop\noel\38_tuples.py", line 6, in <module>
#    tuple[0] = 0
 #   ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
a = list(x)
a[0] = 0 
x = tuple(a)
print(x)

