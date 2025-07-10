# code to calculate factorial using recursion
def gamma(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers"
    elif n > 0 and n < 1:
        return n
    else:
        return n * gamma(n - 1)

print(gamma(5))
print(gamma(5.5))
print(gamma(0))
print(gamma(-5))
