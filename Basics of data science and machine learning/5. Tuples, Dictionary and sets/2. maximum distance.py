def maxFreq(l):
    # Please add your code here
    dict = {}
    count, itm = 0, ''
    for item in reversed(l):
        dict[item] = dict.get(item, 0) + 1
    d={}
    for i in dict:
        if dict[i]>=2:
            d[i]=dict[i]
    if d=={}:
        return 0
    max = 0
    for key in d:
        index1 = l.index(key)
        index2 = list(reversed(l)).index(key)
        index2 = len(l) - index2 - 1
        if abs(index2-index1)>max:
            max = abs(index2-index1)
    return max

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))