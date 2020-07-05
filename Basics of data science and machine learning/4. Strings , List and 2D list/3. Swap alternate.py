'''You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.
Input -> 9 3 6 12 4 32
Output -> 3 9 12 6 32 4'''

from sys import stdin

def swapAlternate(arr, n) :
    #Your code goes here
    for i in range(0,n-1,2):
    	arr[i],arr[i+1] = arr[i+1],arr[i]

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#Printing the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1