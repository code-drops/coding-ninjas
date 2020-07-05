'''
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
'''
def checkPalindrome(num):
    n = str(num)
    if str(num) == n[-1::-1]:
        return True
    return False

num = int(input())
isPalindrome = checkPalindrome(num)
if (isPalindrome):
    print('true')
else:
    print('false')
