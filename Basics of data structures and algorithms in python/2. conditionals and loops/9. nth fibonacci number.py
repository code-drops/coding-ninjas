'''
Nth term of fibonacci series F(n) is calculated using following formula -
    F(n) = F(n-1) + F(n-2),
    Where, F(1) = F(2) = 1
'''
def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return f(n-1)+f(n-2)

print(f(int(input())))