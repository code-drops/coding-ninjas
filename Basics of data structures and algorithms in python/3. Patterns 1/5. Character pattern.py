'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG
'''
n = int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        print(chr(row+col+63),end='')
    print()