'''Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum sum and return the maximum sum.
That is, we can switch from one array to another array only at common elements.
If no intersection element is present, we need to take sum of all elements from the array with greater sum.
input ->
6
1 5 10 15 20 25
5
2 4 5 9 15

output -> 81'''

def maximise(a1,a2,m,n):
    maxsum = s1 = s2 = 0
    i = j = 0
    while (i<m) and (j<n):
        if a1[i]<a2[j]:
            s1 = s1+a1[i]
            i = i + 1
        elif a1[i]>a2[j]:
            s2 = s2 + a2[j]
            j = j + 1
        else:
            s1 = s1 + a1[i]
            s2 = s2 + a2[j]
            i = i + 1
            j = j + 1
            maxsum = maxsum + max(s1,s2)
            s1 = s2 = 0
    if maxsum==0:
        print(sum(a1) if sum(a1)>sum(a2) else sum(a2))
        return
    if i<m:
        while i<m:
            maxsum = maxsum + a1[i]
            i = i + 1
    elif j<n:
        while j<n:
            maxsum = maxsum + a2[j]
            j = j + 1
    print(maxsum)



if __name__=='__main__':
    m = int(input())
    a1 = input().strip().split(' ')
    for i in range(m):
        a1[i] = int(a1[i])
    n = int(input())
    a2 = input().strip().split(' ')
    for i in range(n):
        a2[i] = int(a2[i])
    maximise(a1,a2,m,n)