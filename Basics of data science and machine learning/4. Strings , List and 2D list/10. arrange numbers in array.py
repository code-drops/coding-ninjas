'''You have been given an empty array(ARR) and its size N. The only input taken from the user will be N and you need not worry about the array.
Your task is to populate the array using the integer values in the range 1 to N(both inclusive) in the order - 1,3,.......4,2.'''

from sys import stdin

def arrange(a, n) :
    count = 0
    for i in range(1,n+1,2):
        a[count] = i
        count = count + 1
    if n%2==0:
        for i in range(n, 1, -2):
            a[count] = i
            count = count + 1
    else:
        for i in range(n-1, 1, -2):
            a[count] = i
            count = count + 1

#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()



#main
t = int(stdin.readline().strip())

while t > 0 :
    n = int(stdin.readline().strip())
    arr = n * [0]
    arrange(arr, n)
    printList(arr, n)
    t -= 1