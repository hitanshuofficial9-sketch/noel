def undo(n, l):
    index = l.index(n)
    l.pop(index)
    return l

l = ["Hello", 4, 7, "World"]
print(undo(4, l))