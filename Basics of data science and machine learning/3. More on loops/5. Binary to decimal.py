'''
Given a binary number as an integer N, convert it into decimal and print.
'''
binary = input()
binary = binary[-1::-1]
sum = 0
for i in range(len(binary)):
    sum = sum + int(binary[i]) * (2**i)
print(sum)