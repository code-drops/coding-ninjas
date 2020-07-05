'''
Given a number N find the sum of all the even valued terms in the fibonacci sequence less than or equal to N. Try generating only even fibonacci numbers instead of iterating over all Fibonacci numbers.
'''
n = int(input())
fn1 = 2
fn2 = 0
s = fn1 + fn2
while True:
    fn = 4*fn1 + fn2
    if fn>n:
        break
    s = s + fn
    fn2 = fn1
    fn1 = fn
print(s)