'''
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
input ->
0
100
20
output ->
0   -17
20  -6
40  4
60  15
80  26
100 37
'''

s = int(input())
e = int(input())
w = int(input())

while s<=e:
    c = (s-32) * 5/9
    print(str(s)+" "+str(int(c)))
    s = s+w