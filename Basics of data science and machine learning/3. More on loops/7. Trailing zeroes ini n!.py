'''
Find and return number of trailing 0s in n factorial without calculating n factorial.
'''
n = int(input())
count = 0
while True:
    k = n//5
    count = count + k
    if k<1:
        break
    n = n//5
print(count)