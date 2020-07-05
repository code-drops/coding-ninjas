'''
Print the following pattern for the given number of rows.
Pattern for N = 3
1
23
4567
'''
n = int(input())
count = 0
for i in range(0,n):
    for j in range(1,2**i+1):
        count = count + 1
        if(count==10):
            count = 1
        print(count,end='')
    print()