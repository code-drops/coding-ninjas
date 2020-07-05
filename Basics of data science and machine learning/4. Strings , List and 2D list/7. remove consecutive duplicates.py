'''Given a string, S, remove all the consecutive duplicates that are present in the given string. That means, if 'aaa' is present in the string then it should become 'a' in the output string.
input -> aabccbaa
output ->abcba '''

s = list(input())
k=0
for i in range(len(s)):
    if s[i]!=s[k]:
        k += 1
        s[k]=s[i]
k +=1
s = s[:k]
print(''.join(s))