'''
You are provided with an integer array where each number is present either odd number of times or even number of times. You have to find and return the number which is present even number of times.
If multiple numbers are present even number of times, then return that number which occurs first among these numbers in the given array. If no such number exists, then return -1
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