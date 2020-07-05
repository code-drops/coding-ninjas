'''Given a string S, reverse each word of a string individually. For eg. if a string is "abc def", reversed string should be "cba fed".
'''

s = input()
s = s.split(' ')
for i in range(len(s)):
    s[i]=s[i][-1::-1]
print(' '.join(s))