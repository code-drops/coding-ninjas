'''For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.
Note :
If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.'''

from sys import stdin


def findLargest(arr, nRows, mCols):
    if nRows == 0 or mCols == 0:
        print('row 0 -2147483648')
        return
    row_sum = []
    for i in range(nRows):
        row_sum.append(sum(arr[i]))
    col_sum = []
    for i in range(mCols):
        count = 0
        for j in range(nRows):
            count = count + arr[j][i]
        col_sum.append(count)
    r = max(row_sum)
    c = max(col_sum)
    if r >= c:
        print('row ' + str(row_sum.index(r)) + ' ' + str(r))
    else:
        print('column ' + str(col_sum.index(c)) + ' ' + str(c))


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1