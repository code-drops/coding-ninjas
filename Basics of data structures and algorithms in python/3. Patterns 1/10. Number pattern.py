'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1
'''

n = int(input())
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end='')
    print()