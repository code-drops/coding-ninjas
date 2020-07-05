'''Find and return the equilibrium index of an array. Equilibrium index of an array is an index i such that the sum of elements at indices less than i is equal to the sum of elements at indices greater than i.
Element at index i is not included in either part.
If more than one equilibrium index is present, you need to return the first one. And return -1 if no equilibrium index is present.
'''

def equilibriumIndex(a):
    left_count = 0
    right_count = sum(a[1:])
    for i in range(1, len(a) - 1):

        left_count = left_count + a[i - 1]
        right_count = right_count - a[i]

        if left_count == right_count:
            return i
    return -1


# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))
