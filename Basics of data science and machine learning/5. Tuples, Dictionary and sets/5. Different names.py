'''
In Little Flowers Public School, there are many students with same first names. You are given a task to find the students with same names. You will be given a string comprising of all the names of students and you have to tell the name and count of those students having same. If all the names are unique, print -1 instead.
Note: We don't have to mention names whose frequency is 1.
'''
def differentNames(List):
    # Please add your code here
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
    d={}
    for i in dict:
        if dict[i]>1:
            d[i]=dict[i]
    return d

# Main
names=input().strip().split()
m=differentNames(names)
if m:
    for name in m:
        print(name, m[name])
else:
    print(-1)
