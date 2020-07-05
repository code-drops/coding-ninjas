'''
Write a program that asks the user for a number N and a choice C. And then give them the possibility to choose between computing the sum and computing the product of all integers in the range 1 to N (both inclusive).
If C is equal to -
 1, then print the sum
 2, then print the product
 Any other number, then print '-1' (without the quotes)
'''
n = int(input())
c = int(input())
if c==1:
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    print(sum)
elif c==2:
    multiple = 1
    for i in range(1, n + 1):
        multiple = multiple * i
    print(multiple)
else:
    print(-1)