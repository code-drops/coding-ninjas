'''
Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.
'''

def reverse(n):
	n = str(n)
	return n[-1::-1]

n=int(input())
result = int(reverse(n))
print(result)