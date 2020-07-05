'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
4444
4444
4444
4444
'''
n = int(input())
for row in range(n):
    for col in range(n):
        print(n,end='')
    print()