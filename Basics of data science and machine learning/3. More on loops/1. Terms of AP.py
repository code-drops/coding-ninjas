'''
Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
'''
n = int(input())
count = 0
i = 1
while count!=n:
    k = 3*i + 2
    if k%4!=0:
        print(k,end=' ')
        count = count + 1
    i = i + 1