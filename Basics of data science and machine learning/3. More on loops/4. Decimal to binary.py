'''
Given a decimal number (integer N), convert it into binary and print.
The binary number should be in the form of an integer.
'''
n = int(input())

if n==0:
    print(0)
elif n==1:
    print(1)
else:
    binary =''
    while n!=1:
        binary = binary + str(n%2)
        n = n//2
    binary = binary+str(1)
    print(binary[-1::-1])