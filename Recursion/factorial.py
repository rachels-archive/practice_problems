def factorial(n):
    # input validation
    if (n < 0):
        return "Input must be a positive integer"
    # base cases
    elif (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
   
# test cases
# print(factorial(0))
# print(factorial(1))
# print(factorial(5))
# print(factorial(-2))
