def fibonacci(n):
    # input validation
    if (n < 0):
        return "Input must be a positive integer"
    # base cases
    elif (n == 0):
        return 0
    elif (n == 1):
        return 1
    # recursive call
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

# test cases
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(10))
# print(fibonacci(-2))
