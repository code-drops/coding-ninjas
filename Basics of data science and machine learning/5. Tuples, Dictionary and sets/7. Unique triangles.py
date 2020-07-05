'''
You are given n triangles. You are required to find how many triangles are unique out of given triangles. For each triangle you are given three integers a, b and c (the sides of a triangle).
A triangle is said to be unique if there is no other triangle with same set of sides.
'''
def differentNames(List):
    # Please add your code here
    dict = {}
    count, itm = 0, ''
    for item in List:
        dict[item] = dict.get(item, 0) + 1
    d={}
    for i in dict:
        if dict[i]%2==0:
            d[i]=dict[i]
    # print(d)
    for i in List:
        if i in d.keys():
            print(int(i))
            break
    else:
        print(-1)

# Main
n = int(input())
names=input().strip().split()
differentNames(names)