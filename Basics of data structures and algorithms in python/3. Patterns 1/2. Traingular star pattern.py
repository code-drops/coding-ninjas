'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
*
**
***
****
'''
n = int(input())
for row in range(n):
    for col in range(row+1):
        print('*',end='')
    print()