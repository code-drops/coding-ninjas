'''
Print the following pattern for the given N number of rows.
Pattern for N = 3
 A
 BB
 CCC
'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end='')
    print()