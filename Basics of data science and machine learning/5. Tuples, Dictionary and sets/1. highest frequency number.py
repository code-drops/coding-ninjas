def maxFreq(List):
    # Please add your code here
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return (itm)

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))