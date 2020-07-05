'''Given an integer array A of size n. Find and print all the leaders present in the input array. An array element A[i] is called Leader, if all the elements following it (i.e. present at its right) are less than or equal to A[i].
Print all the leader elements separated by space and in the same order they are present in the input array.'''

n = int(input())
l = input().strip().split(' ')
for i in range(len(l)):
    l[i] = int(l[i])

for i in range(len(l)):
    valid = True
    for j in range(i+1, len(l)):
        if l[i]>=l[j]:
            pass
        else:
            valid = False
            break
    if valid:
        print(l[i],end=' ')