'''
You are given with an array of integers and an integer K. Write a program to find and print all pairs which have difference K.
Take difference as absolute.
'''
def printPairDiffK(List, k):
    # Please add your code here
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
    # print(dict)
    for i in dict:
        # print(i)
        if i+k in dict:
            for m in range(dict[i]):
                for n in range(dict[i+k]):
                    print(i,i+k)
        if i-k in dict:
            for m in range(dict[i]):
                for n in range(dict[i-k]):
                    print(i-k,i)
        dict[i] = 0


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)