'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
21
321
4321
'''
n = int(input())
for row in range(1,n+1):
    for col in range(row,0,-1):
        print(str(col),end='')
    print()