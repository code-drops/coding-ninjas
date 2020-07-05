'''
Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
'''
n = int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        print(chr(64+n-row+col),end='')
    print()