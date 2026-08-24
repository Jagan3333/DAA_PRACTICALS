def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


n = 5

print("Number:", n)
print("Factorial (Recursive):", factorial_recursive(n))