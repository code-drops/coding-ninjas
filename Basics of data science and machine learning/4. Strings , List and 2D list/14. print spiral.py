'''For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:
a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)
 Mind that every element will be printed only once.

input->
1
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
output -> 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 '''

testcases = int(input())

def printSpiral(a,m,n):
    count = firstrow = firstcol = 0
    lastrow = m - 1
    lastcol = n - 1

    while count <= (m * n):
        for i in range(firstcol, lastcol + 1):
            count += 1
            print(a[firstrow][i], end=' ')
        firstrow = firstrow + 1
        for i in range(firstrow, lastrow + 1):
            count += 1
            print(a[i][lastcol], end=' ')
        lastcol = lastcol - 1
        for i in range(lastcol, firstcol - 1, -1):
            count += 1
            print(a[lastrow][i], end=' ')
        lastrow = lastrow - 1
        for i in range(lastrow, firstrow - 1, -1):
            count += 1
            print(a[i][firstcol], end=' ')
        firstcol = firstcol + 1

if __name__=='__main__':
    for t in range(testcases):
        a = []
        l = input().strip().split(' ')
        for i in range(len(l)):
            l[i] = int(l[i])
        m, n = l

        for i in range(m):
            l = input().strip().split(' ')
            l = [int(i) for i in l]
            a.append(l)

        printSpiral(a, m, n)