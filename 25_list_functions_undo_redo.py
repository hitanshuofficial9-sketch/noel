n = int(input("Enter the Number of elements: "))
l = []
undo_l = []
for i in range(n):
    element = input("Enter element: ")
    l.append(element)
copy_l = l.copy()
no_undo = int(input("Enter the number of elements you want to undo: "))
for i in range(no_undo):
    undo = input("Enter the element to undo: ")
    undo_l.append(undo)
    l.pop(l.index(undo))
redo = input("Do you want to redo? (y/n): ")
redo = redo.lower()
if redo == "y" or redo == "yes":
    redo = True
else:
    redo = False
if redo == True:
    no_redo = int(input("Enter the number of elements to redo: "))
    l = copy_l.copy()
    for i in range(no_redo):
        redo = input("Enter the element to redo: ")
        if redo in undo_l:
            undo_l.pop(undo_l.index(redo))
        else:
            print(f"{redo} was not in original list.\nFailed to redo")
            break
    for i in undo_l:
        l.pop(copy_l.index(i))
print(f"The Final list is: {l}")