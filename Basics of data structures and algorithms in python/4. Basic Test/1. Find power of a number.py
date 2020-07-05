'''
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Note : For this question, you can assume that 0 raised to the power of 0 is 1
'''
l = input().split(' ')
x = int(l[0])
n = int(l[1])

if n==0:
    print(1)
else:
    print(x**n)