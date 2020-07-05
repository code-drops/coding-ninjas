'''Given a String s, check it its palindrome. Return true if string is palindrome, else return false.
Palindrome strings are those, where string s and its reverse is exactly same.'''
s = input()
if s==s[-1::-1]:
    print('true')
else:
    print('false')