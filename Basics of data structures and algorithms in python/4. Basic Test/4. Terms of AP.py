'''
Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
'''
n = int(input())
l=[]
count = 0
while len(l)!=n:
    count = count + 1
    x = 3*count+2
    if x%4!=0:
        l.append(x)
        print(x,end=' ')
