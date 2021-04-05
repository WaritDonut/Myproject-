"""
def factorial(n):
    fact = 1
    while n >= 1:
        fact = fact * n
        n = n-1
    return fact
print (factorial(10))

"""

def factorial(num):
    fact = 1
    for x in range(1, num + 1):
        fact = fact * x
    return fact

print (factorial(10))
