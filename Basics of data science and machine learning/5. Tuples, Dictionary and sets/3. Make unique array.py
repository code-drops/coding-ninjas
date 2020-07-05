'''
Find number of elements to be removed to make an array of all distinct elements.
Example:
Ar = {2,1,4,2,1}
output = 2 (remove 2 and 1).
'''
def duplicateCount(List):
    # Please add your code here
    s = set(List)
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
    return sum(dict.values()) - len(s)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(duplicateCount(arr))
