'''
Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
'''
n = input()
even = 0
odd = 0
for i in n:
    if int(i)%2==0:
        even = even + int(i)
    else:
        odd = odd + int(i)
print(str(even)+" "+str(odd))
