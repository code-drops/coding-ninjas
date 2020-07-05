'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
'''
n = int(input())
print(1)
n = n-1
for i in range(1,n+1):
    for j in range(1,i+2):
        if j == 1 or j==i+1:
            print(i,end='')
        else:
            print(0,end='')
    print()