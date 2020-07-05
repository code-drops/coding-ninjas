'''Given a String S of length n, print all its substrings.
Substring of a String S is a part of S (of any length from 1 to n), which contains all consecutive characters from S.'''

string = input()
length = len(string)
for i in range(1,length+1):
    for k in range(0, len(string)-i+1):
        print(string[k:k+i])