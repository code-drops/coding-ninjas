'''
Given an integer N, print all the prime numbers that lie in the range 2 to N (both inclusive).
Print the prime numbers in different lines.
'''
n = int(input())

def prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True

for i in range(2,n+1):
    if(prime(i)):
        print(i)
