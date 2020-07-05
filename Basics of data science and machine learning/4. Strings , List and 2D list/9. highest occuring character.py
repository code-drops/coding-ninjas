'''Given a string, S, find and return the highest occurring character present in the given string.
If there are 2 characters in the input string with same frequency, return the character which comes first.
Note : Assume all the characters in the given string are lowercase.'''

s = input()
d = {}
for i in s:
    k = s.count(i)
    d[i]=k
values = list(d.values())
char = list(d.keys())


print(char[values.index(max(values))])