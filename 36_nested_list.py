l = [[1,2,3],[4,5,6],[7,8,9]]
print(l[0][2])
def nested_element(l):
 for i in range(0,len(l)):
    for j in range(0, len(l[i])):
        print(l[i][j])
nested_element(l)